#!/usr/bin/env python3
"""Gera o sistema de leitura da base ESTUDOS a partir dos arquivos .md.

Uso (na raiz do projeto):
    python sistema/gerar.py              gera o site (site/index.html) e a cópia da página privada
    python sistema/gerar.py --servir     gera e serve o site em http://localhost:8765/
    python sistema/gerar.py --verificar  só confere a base (referências e formatação)

Não depende de nenhum pacote externo. Mantenha o código compatível com Python 3.9: o build da
Vercel (vercel.json) roda este script com o python3 da imagem de build. A ordem das matérias e
dos temas vem de ESTUDOS/_CONTROLE/assuntos-estudados.md; o que não estiver lá entra em ordem
alfabética.

Além do texto de cada tema, o gerador monta, por matéria:
- o resumo geral (todos os temas em sequência, dividido em páginas de tamanho fixo);
- o mapa mental de cada tema (seção "## Mapa mental", que sai do texto do tema);
- o resumo sintético (arquivos .txt/.md da pasta "Resumo Sintético", na ordem dos números): o
  texto entra como está; só a numeração dos títulos ("1.", "1.1") é refeita na exibição, em
  sequência única na matéria inteira (ver `renumerar`).

A data da última leitura de cada disciplina (o Lido mais recente) é calculada no navegador, a
partir das leituras que o próprio leitor marcou.

Com --servir, o site aberto em http://localhost:8765/ também recebe novas partes do resumo
sintético (formulário da aba "Resumo sintético"): um .docx (convertido em .md com a mesma
formatação) ou texto colado (.txt), salvos sem alteração no conteúdo como a próxima parte da
matéria; em seguida o site é gerado de novo.
"""
from __future__ import annotations

import base64
import functools
import hashlib
import html
import http.server
import json
import math
import posixpath
import re
import sys
import threading
import unicodedata
from datetime import date, datetime
from pathlib import Path

PASTA_SISTEMA = Path(__file__).resolve().parent
RAIZ = PASTA_SISTEMA.parent
BASE = RAIZ / "ESTUDOS"
MODELO = PASTA_SISTEMA / "modelo.html"
PASTA_SITE = RAIZ / "site"
SAIDA_SITE = PASTA_SITE / "index.html"
SAIDA_PAGINA_PRIVADA = PASTA_SISTEMA / "pagina-privada" / "Estudos.html"
PORTA_LOCAL = 8765
MARCADOR_DADOS = "__DADOS_JSON__"

CONTROLE = "_CONTROLE"
ORDEM_CONTROLE = ["diario-de-estudos", "assuntos-estudados", "pendencias", "alteracoes"]
PASTA_SINTETICO = "Resumo Sintético"
ROTA_SINTETICO = "/__estudos/sintetico"
LIMITE_SINTETICO = 40_000_000  # bytes por parte enviada pelo site (.docx vem em base64)
TITULO_MAPA = "mapa mental"
# Tamanho de uma página do resumo geral, em caracteres de texto (cerca de uma folha A4).
CARACTERES_POR_PAGINA = 3000

# Sigla (aba colorida) e cor de cada matéria. Uma matéria nova recebe sigla automática e a
# próxima cor livre; acrescente-a aqui para fixar sigla e cor.
MATERIAS = {
    "Direito Tributário": ("TRIB", "m1"),
    "Contabilidade Geral e Avançada": ("CONT", "m2"),
    "Direito Constitucional": ("CONST", "m3"),
    "Direito Administrativo": ("ADM", "m4"),
}
CORES_LIVRES = ["m5", "m6", "m7", "m8"]
PALAVRAS_POR_MINUTO = 180


# ----------------------------------------------------------------------------- utilidades

def sem_acentos(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c))


def slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", sem_acentos(s).lower()).strip("-") or "secao"


def texto_de_html(h: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", h))).strip()


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def recuo(linha: str) -> int:
    return len(linha) - len(linha.lstrip(" "))


def resumo_hash(texto: str) -> str:
    return hashlib.sha1(texto.encode("utf-8")).hexdigest()[:10]


# ----------------------------------------------------------------------------- blocos

RE_CERCA = re.compile(r"^\s*(`{3,})\s*([\w-]*)\s*$")
RE_TITULO = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
RE_REGUA = re.compile(r"^\s{0,3}([-*_])(?:\s*\1){2,}\s*$")
RE_ITEM = re.compile(r"^(\s*)([-*+]|\d{1,9}[.)])(\s+)(.*)$")
RE_SEPARADOR = re.compile(r"^\s*\|?\s*:?-+:?\s*(?:\|\s*:?-+:?\s*)*\|?\s*$")


def inicia_bloco(linha: str) -> bool:
    s = linha.lstrip()
    return bool(
        RE_CERCA.match(linha) or RE_TITULO.match(s) or RE_REGUA.match(linha)
        or s.startswith(">") or s.startswith("|") or RE_ITEM.match(linha)
    )


def dividir_linha(linha: str) -> list[str]:
    """Divide uma linha de tabela em células, respeitando `código` e \\|."""
    s = linha.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"):
        s = s[:-1]
    celulas, atual, em_codigo, k = [], [], False, 0
    while k < len(s):
        c = s[k]
        if c == "\\" and k + 1 < len(s) and s[k + 1] == "|":
            atual.append("|")
            k += 2
            continue
        if c == "`":
            em_codigo = not em_codigo
        if c == "|" and not em_codigo:
            celulas.append("".join(atual).strip())
            atual = []
        else:
            atual.append(c)
        k += 1
    celulas.append("".join(atual).strip())
    return celulas


def alinhamentos(separador: str, n: int) -> list[str | None]:
    saida = []
    for c in dividir_linha(separador):
        c = c.strip()
        if c.startswith(":") and c.endswith(":"):
            saida.append("center")
        elif c.endswith(":"):
            saida.append("right")
        else:
            saida.append(None)
    return (saida + [None] * n)[:n]


def ler_blocos(linhas: list[str]) -> list[dict]:
    blocos, i, n = [], 0, len(linhas)
    while i < n:
        linha = linhas[i]
        if not linha.strip():
            i += 1
            continue
        m = RE_CERCA.match(linha)
        if m:
            buf, i = [], i + 1
            while i < n and not RE_CERCA.match(linhas[i]):
                buf.append(linhas[i])
                i += 1
            blocos.append({"t": "codigo", "texto": "\n".join(buf)})
            i += 1
            continue
        m = RE_TITULO.match(linha.lstrip())
        if m:
            blocos.append({"t": "h", "nivel": len(m.group(1)), "texto": m.group(2)})
            i += 1
            continue
        if RE_REGUA.match(linha):
            blocos.append({"t": "regua"})
            i += 1
            continue
        if linha.lstrip().startswith(">"):
            buf = []
            while i < n and linhas[i].lstrip().startswith(">"):
                s = linhas[i].lstrip()[1:]
                buf.append(s[1:] if s.startswith(" ") else s)
                i += 1
            blocos.append({"t": "citacao", "blocos": ler_blocos(buf)})
            continue
        if (linha.lstrip().startswith("|") and i + 1 < n
                and RE_SEPARADOR.match(linhas[i + 1]) and "-" in linhas[i + 1]):
            cab = dividir_linha(linha)
            alin = alinhamentos(linhas[i + 1], len(cab))
            corpo, i = [], i + 2
            while i < n and linhas[i].lstrip().startswith("|"):
                corpo.append(dividir_linha(linhas[i]))
                i += 1
            blocos.append({"t": "tabela", "cab": cab, "alin": alin, "linhas": corpo})
            continue
        if RE_ITEM.match(linha):
            bloco, i = ler_lista(linhas, i)
            blocos.append(bloco)
            continue
        buf, i = [linha.strip()], i + 1
        while i < n and linhas[i].strip() and not inicia_bloco(linhas[i]):
            buf.append(linhas[i].strip())
            i += 1
        blocos.append({"t": "p", "texto": " ".join(buf)})
    return blocos


def ler_lista(linhas: list[str], i: int) -> tuple[dict, int]:
    m = RE_ITEM.match(linhas[i])
    base = len(m.group(1))
    ordenada = m.group(2)[0].isdigit()
    inicio = int(m.group(2)[:-1]) if ordenada else None
    itens, n = [], len(linhas)

    def irma(linha: str) -> bool:
        mm = RE_ITEM.match(linha)
        return bool(mm) and len(mm.group(1)) == base and mm.group(2)[0].isdigit() == ordenada

    while i < n:
        if not linhas[i].strip():
            j = i
            while j < n and not linhas[j].strip():
                j += 1
            if j < n and irma(linhas[j]):
                i = j
            else:
                break
        if not irma(linhas[i]):
            break
        m = RE_ITEM.match(linhas[i])
        coluna = len(m.group(1)) + len(m.group(2)) + len(m.group(3))
        buf, i = [m.group(4)], i + 1
        while i < n:
            linha = linhas[i]
            if not linha.strip():
                j = i
                while j < n and not linhas[j].strip():
                    j += 1
                if j < n and recuo(linhas[j]) > base and not irma(linhas[j]):
                    buf.extend([""] * (j - i))
                    i = j
                    continue
                break
            r = recuo(linha)
            if r > base:
                buf.append(linha[min(r, coluna):])
                i += 1
                continue
            break
        itens.append(ler_blocos(buf))
    return {"t": "ol" if ordenada else "ul", "inicio": inicio, "itens": itens}, i


RE_H12 = re.compile(r"^(#{1,2})\s+(.*?)\s*#*\s*$")


def separar_mapa(texto: str) -> tuple[str, str | None]:
    """Tira do tema a seção '## Mapa mental' e a devolve à parte (texto, mapa)."""
    linhas = texto.splitlines()
    ini = None
    for i, linha in enumerate(linhas):
        m = RE_H12.match(linha)
        if m and len(m.group(1)) == 2 and sem_acentos(m.group(2)).strip().lower() == TITULO_MAPA:
            ini = i
            break
    if ini is None:
        return texto, None
    fim = next((j for j in range(ini + 1, len(linhas)) if RE_H12.match(linhas[j])), len(linhas))
    resto = linhas[:ini] + linhas[fim:]
    while resto and not resto[-1].strip():
        resto.pop()
    return "\n".join(resto) + "\n", "\n".join(linhas[ini + 1:fim])


# ----------------------------------------------------------------------------- inline

RE_CODIGO = re.compile(r"(`+)(.+?)\1")
RE_VEREDITO = re.compile(r"\*\*(CERTO|ERRADO)\*\*")
RE_NEGRITO_ITALICO = re.compile(r"\*\*\*(?=\S)(.+?)(?<=\S)\*\*\*")
RE_NEGRITO = re.compile(r"\*\*(?=\S)(.+?)(?<=\S)\*\*")
RE_ITALICO = re.compile(r"(?<![*\w])\*(?=[^\s*])(.+?)(?<=[^\s*])\*(?![*\w])")
RE_A_ESTUDAR = re.compile(r"\(a estudar\)|(?<=— )a estudar\b")
RE_PEGADINHA = re.compile(r"^(?P<s>.*?)\s*→\s*\*\*(?P<v>CERTO|ERRADO)\*\*(?P<x>.*)$")
RE_ROTULO_PEGADINHA = re.compile(r"^(?:⚠️?\s*)?Pegadinha:\s*", re.I)
RE_VAZOU = re.compile(r"\*\*|`|\|\s*-{3,}|\]\(|^#{1,6}\s")
RE_IMAGEM_MD = re.compile(r"!\[([^\]]*)\]\(([^)\n]+)\)")
TIPOS_IMAGEM = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png",
                ".gif": "image/gif", ".webp": "image/webp"}
SELO_A_ESTUDAR = '<span class="est">a estudar</span>'


def envolto_em_parenteses(s: str) -> bool:
    if not (s.startswith("(") and s.endswith(")")):
        return False
    nivel = 0
    for k, c in enumerate(s):
        nivel += c == "("
        nivel -= c == ")"
        if nivel == 0 and k < len(s) - 1:
            return False
    return nivel == 0


def separar_veredito(md: str) -> tuple[str, str, str]:
    """'"Afirmação" → **ERRADO** (explicação)' vira ('E', '"Afirmação"', 'explicação')."""
    m = RE_PEGADINHA.match(md)
    if not m:
        return "", md, ""
    enunciado = m.group("s").strip()
    if len(enunciado) > 1 and enunciado.startswith('"') and enunciado.endswith('"') \
            and enunciado.count('"') == 2:
        enunciado = "“" + enunciado[1:-1] + "”"
    explicacao = m.group("x").strip()
    if explicacao.endswith("."):
        explicacao = explicacao[:-1].rstrip()
    if envolto_em_parenteses(explicacao):
        explicacao = explicacao[1:-1].strip()
    return m.group("v")[0], enunciado, explicacao


def classificar_citacao(texto: str, anterior: dict | None) -> str:
    t = texto.lstrip()
    if RE_ROTULO_PEGADINHA.match(t) or re.match(r"^(⚠️?\s*)?Pegadinha\b", t, re.I):
        return "peg"
    if t.startswith("⚠"):
        return "alerta"
    if t.startswith("\U0001f517"):
        return "ligacao"
    if t.startswith("Divergência"):
        return "div"
    if t[:1] in "\"“":
        return "lei"
    if re.match(r"^(Legenda|Versão)", t):
        return "meta"
    if anterior and anterior["t"] == "h" and re.search(r"\bart\.", anterior["texto"]):
        return "lei"
    return "info"


# ----------------------------------------------------------------------------- renderização

class Renderizador:
    """Converte os blocos de um documento em HTML, índice de busca e pegadinhas.

    Os arquivos do resumo sintético são do estudante e entram como estão: não geram avisos,
    ligações "Citado em" nem itens na página de pegadinhas.
    """

    def __init__(self, base: "Base", doc: dict):
        self.base = base
        self.doc = doc
        self.bruto = doc.get("tipo") == "sint"
        self.n = 0
        self.toc: list[dict] = []
        self.ids: set[str] = set()
        self.indice: list[list] = []
        self.pegadinhas: list[dict] = []
        self.ns_titulo: set[int] = set()
        self.ns_peg: set[int] = set()
        self.h2 = self.h3 = None
        self.peg_h2 = self.peg_h3 = False
        self.titulo: str | None = None
        self.palavras = 0

    def aviso(self, msg: str) -> None:
        if not self.bruto:
            self.base.aviso(self.doc, msg)

    # -- inline
    def inline(self, md: str, registrar: bool = True) -> str:
        guardados: list[str] = []

        def guardar(h: str) -> str:
            guardados.append(h)
            return f"\x00{len(guardados) - 1}\x00"

        if self.bruto:  # resumo sintético: imagens, "\*" literal e quebras de linha do .docx
            md = RE_IMAGEM_MD.sub(lambda m: guardar(self.imagem(m.group(1), m.group(2))), md)
            md = re.sub(r"\\([\\`*_{}\[\]()#+\-.!|>])",
                        lambda m: guardar(html.escape(m.group(1), quote=False)), md)
            md = md.replace("<br>", guardar("<br>"))
        s = RE_CODIGO.sub(lambda m: guardar(self.codigo(m.group(2), registrar)), md)
        s = html.escape(s, quote=False)
        s = RE_VEREDITO.sub(
            lambda m: guardar(f'<span class="vd vd-{m.group(1)[0]}">{m.group(1)}</span>'), s)
        s = RE_NEGRITO_ITALICO.sub(r"<strong><em>\1</em></strong>", s)
        s = RE_NEGRITO.sub(r"<strong>\1</strong>", s)
        s = RE_ITALICO.sub(r"<em>\1</em>", s)
        s = RE_A_ESTUDAR.sub(SELO_A_ESTUDAR, s)
        return re.sub(r"\x00(\d+)\x00", lambda m: guardados[int(m.group(1))], s)

    def imagem(self, alt: str, arquivo: str) -> str:
        """Imagem do resumo sintético, embutida na página (o site é um arquivo só)."""
        pasta = self.doc.get("pasta_abs")
        caminho = (pasta / arquivo).resolve() if pasta else None
        tipo = TIPOS_IMAGEM.get(caminho.suffix.lower()) if caminho else None
        if not tipo or caminho.parent != pasta.resolve() or not caminho.is_file():
            self.base.aviso(self.doc, f"imagem não encontrada: {arquivo}")
            return f"[imagem não encontrada: {html.escape(arquivo, quote=False)}]"
        dados = base64.b64encode(caminho.read_bytes()).decode("ascii")
        return f'<img src="data:{tipo};base64,{dados}" alt="{esc(alt)}">'

    def codigo(self, conteudo: str, registrar: bool) -> str:
        c = conteudo.strip()
        registrar = registrar and not self.bruto
        if c.endswith(".md") or c.endswith("/"):
            alvo = self.base.resolver(c, self.doc)
            if alvo:
                destino, rotulo = alvo
                if registrar:
                    self.base.ligar(self.doc, destino)
                return self.base.link(destino, rotulo, self.doc)
            if c.endswith(".md") and registrar:
                self.aviso(f"referência não encontrada: `{c}`")
        return f"<code>{html.escape(c, quote=False)}</code>"

    # -- índice
    def secao(self) -> str:
        return " › ".join(x for x in (self.h2, self.h3) if x)

    def indexar(self, n: int, texto: str) -> None:
        if texto:
            self.indice.append([self.doc["id"], n, self.secao(), texto])
            self.palavras += len(texto.split())

    def novo(self) -> int:
        self.n += 1
        return self.n

    # -- blocos
    def blocos(self, blocos: list[dict], prof: int = 0, lista: bool = False):
        """HTML dos blocos; com lista=True, uma parte por bloco de primeiro nível."""
        partes, anterior = [], None
        for b in blocos:
            t = b["t"]
            if t == "h":
                partes.append(self.titulo_html(b))
            elif t == "p":
                partes.append(self.paragrafo(b["texto"]))
            elif t in ("ul", "ol"):
                partes.append(self.lista(b, prof))
            elif t == "tabela":
                partes.append(self.tabela(b))
            elif t == "citacao":
                partes.append(self.citacao(b, prof, anterior))
            elif t == "codigo":
                partes.append(self.codigo_bloco(b))
            elif t == "regua":
                partes.append("<hr>")
            anterior = b
        partes = [p for p in partes if p]
        return partes if lista else "\n".join(partes)

    def titulo_html(self, b: dict) -> str:
        conteudo = self.inline(b["texto"])
        texto = texto_de_html(conteudo)
        if b["nivel"] == 1 and self.titulo is None and not self.bruto:
            self.titulo = texto
            return ""
        nivel = max(2, b["nivel"])
        raiz = slug(texto)
        hid, k = raiz, 2
        while hid in self.ids:
            hid, k = f"{raiz}-{k}", k + 1
        self.ids.add(hid)
        eh_peg = bool(re.search(r"pegadinha", texto, re.I))
        if nivel == 2:
            self.h2, self.h3, self.peg_h2, self.peg_h3 = texto, None, eh_peg, False
        elif nivel == 3:
            self.h3, self.peg_h3 = texto, eh_peg
        if nivel <= 3:
            self.toc.append({"id": hid, "n": nivel, "t": texto})
        n = self.novo()
        self.ns_titulo.add(n)
        self.indexar(n, texto)
        return f'<h{nivel} id="{hid}" data-b="{n}">{conteudo}</h{nivel}>'

    def paragrafo(self, md: str) -> str:
        conteudo = self.inline(md)
        n = self.novo()
        self.indexar(n, texto_de_html(conteudo))
        return f'<p data-b="{n}">{conteudo}</p>'

    def lista(self, b: dict, prof: int) -> str:
        tag = b["t"]
        inicio = f' start="{b["inicio"]}"' if tag == "ol" and b["inicio"] not in (None, 1) else ""
        pegadinhas = prof == 0 and (self.peg_h2 or self.peg_h3)
        if pegadinhas:
            itens = "".join(self.item_pegadinha(item) for item in b["itens"])
            return f'<{tag}{inicio} class="peg-lista">{itens}</{tag}>'
        itens = "".join(f"<li>{self.blocos(item, prof + 1)}</li>" for item in b["itens"])
        return f"<{tag}{inicio}>{itens}</{tag}>"

    def corpo_pegadinha(self, md: str, registrar: bool) -> tuple[str, str]:
        v, enunciado, explicacao = separar_veredito(md)
        corpo = f'<span class="peg-s">{self.inline(enunciado, registrar)}</span>'
        if v and explicacao:
            corpo += f' <span class="peg-x">{self.inline(explicacao, registrar)}</span>'
        return v, corpo

    @staticmethod
    def li_pegadinha(v: str, n: int, conteudo: str) -> str:
        rotulo = {"C": "Certo", "E": "Errado"}.get(v, "Observação")
        return (f'<li class="peg peg-{v or "n"}" data-b="{n}">'
                f'<span class="peg-v" role="img" aria-label="{rotulo}"></span>'
                f'<div class="peg-c">{conteudo}</div></li>')

    def item_pegadinha(self, item: list[dict]) -> str:
        n = self.novo()
        self.ns_peg.add(n)
        if item and item[0]["t"] == "p":
            v, corpo = self.corpo_pegadinha(item[0]["texto"], True)
            resto = item[1:]
        else:
            v, corpo, resto = "", "", item
        self.indexar(n, texto_de_html(corpo))
        if resto:
            corpo += self.blocos(resto, 1)
        li = self.li_pegadinha(v, n, corpo)
        if not self.bruto:
            self.pegadinhas.append({"d": self.doc["id"], "b": n, "v": v, "h": li})
        return li

    def citacao(self, b: dict, prof: int, anterior: dict | None) -> str:
        primeiro = next((x["texto"] for x in b["blocos"] if x["t"] == "p"), "")
        tipo = classificar_citacao(texto_de_html(self.inline(primeiro, False)), anterior)
        n_inicio = self.n + 1
        interno = self.blocos(b["blocos"], prof + 1)
        if tipo == "peg" and prof == 0 and primeiro:
            self.ns_peg.add(n_inicio)
            v, corpo = self.corpo_pegadinha(RE_ROTULO_PEGADINHA.sub("", primeiro), False)
            if not self.bruto:
                self.pegadinhas.append({"d": self.doc["id"], "b": n_inicio, "v": v,
                                        "h": self.li_pegadinha(v, n_inicio, corpo)})
        return f'<blockquote class="nota nota-{tipo}">{interno}</blockquote>'

    def tabela(self, b: dict) -> str:
        ncol = len(b["cab"])

        def celula(tag: str, md: str, k: int) -> str:
            estilo = f' style="text-align:{b["alin"][k]}"' if b["alin"][k] else ""
            return f"<{tag}{estilo}>{self.inline(md)}</{tag}>"

        def linha_html(cels: list[str]) -> str:
            n = self.novo()
            self.indexar(n, " | ".join(t for t in map(texto_de_html, cels) if t))
            return f'<tr data-b="{n}">' + "".join(cels) + "</tr>"

        cab = linha_html([celula("th", c, k) for k, c in enumerate(b["cab"])])
        corpo = []
        for linha in b["linhas"]:
            if len(linha) != ncol:
                self.aviso(f"linha de tabela com {len(linha)} colunas (esperadas {ncol}): "
                           f"{linha[0][:50]}")
            linha = (linha + [""] * ncol)[:ncol]
            corpo.append(linha_html([celula("td", c, k) for k, c in enumerate(linha)]))
        return (f'<div class="tabela"><table><thead>{cab}</thead>'
                f'<tbody>{"".join(corpo)}</tbody></table></div>')

    def codigo_bloco(self, b: dict) -> str:
        n = self.novo()
        self.indexar(n, re.sub(r"\s+", " ", b["texto"]).strip())
        return (f'<div class="codigo"><pre data-b="{n}"><code>'
                f'{html.escape(b["texto"], quote=False)}</code></pre></div>')

    def texto_simples(self, texto: str) -> list[str]:
        """Arquivo .txt: um parágrafo por bloco separado por linha em branco, quebras mantidas."""
        partes = []
        for par in re.split(r"\n[ \t]*\n", texto.strip("\n")):
            if not par.strip():
                continue
            n = self.novo()
            self.indexar(n, re.sub(r"\s+", " ", par).strip())
            partes.append(f'<p class="txt" data-b="{n}">{html.escape(par.rstrip(), quote=False)}</p>')
        return partes


# ----------------------------------------------------------------------------- mapa mental

PALAVRAS_VAZIAS = set(
    "a o e as os um uma uns umas de da do das dos em no na nos nas ao aos por pelo pela pelos "
    "pelas para pra com sem sob sobre que se ou nem mas como mais menos ja nao sim ser so sua "
    "seu suas seus lhe isso esta este essa esse entre ate apos quando onde qual quais cada toda "
    "todo todas todos outro outra outros outras ha ex etc".split())


def tokens(texto: str) -> set[str]:
    saida = set()
    for t in re.findall(r"[a-z0-9]+", sem_acentos(texto).lower()):
        if len(t) < 2 or t in PALAVRAS_VAZIAS:
            continue
        if len(t) > 4 and t.endswith("s"):
            t = t[:-1]
        saida.add(t[:6])
    return saida


def ligar_mapa(nos: list[dict], r: Renderizador) -> None:
    """Liga cada nó do mapa ao trecho do tema que mais se parece com ele (campo "b")."""
    entradas = [(n, secao, tokens(texto)) for _, n, secao, texto in r.indice]
    if not entradas:
        return
    df: dict[str, int] = {}
    for _, _, ts in entradas:
        for t in ts:
            df[t] = df.get(t, 0) + 1
    idf = {t: math.log(1 + len(entradas) / c) for t, c in df.items()}
    fracas = re.compile(r"^(base legal|relac|pegadinha)")

    def melhor(proprios: set[str], contexto: set[str], ramo: bool) -> int | None:
        nota_max, escolhido = 0.0, None
        for n, secao, ts in entradas:
            nota = sum(idf[t] for t in proprios & ts)
            if not nota:
                continue
            nota += 0.3 * sum(idf[t] for t in (contexto - proprios) & ts)
            nota /= 1 + len(ts) / 30  # trecho curto e certeiro vence trecho longo e genérico
            if n in r.ns_titulo:
                nota *= 1.5 if ramo else 1.1
            if n in r.ns_peg:
                nota *= 0.6
            if fracas.match(sem_acentos(secao).lower()):
                nota *= 0.4
            if nota > nota_max:
                nota_max, escolhido = nota, n
        return escolhido if nota_max >= 0.8 else None

    def visitar(no: dict, contexto: set[str]) -> None:
        proprios = tokens(texto_de_html(no["t"]))
        b = melhor(proprios, contexto, bool(no.get("c")))
        if b:
            no["b"] = b
        for filho in no.get("c", []):
            visitar(filho, contexto | proprios)

    for no in nos:
        visitar(no, set())


# ----------------------------------------------------------------------------- base

def ler_assuntos(caminho: Path) -> tuple[list[str], dict]:
    """Lê a ordem pedagógica (matérias e arquivos), o resumo e o status de cada tema."""
    ordem, tabela, materia, k = [], {}, None, 0
    if not caminho.exists():
        return ordem, tabela
    for linha in caminho.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^##\s+(.+?)\s*$", linha)
        if m:
            materia = m.group(1).strip()
            ordem.append(materia)
            continue
        if materia and linha.lstrip().startswith("|"):
            cels = dividir_linha(linha)
            if len(cels) >= 4 and cels[1].startswith("`") and cels[1].endswith("`"):
                tabela[(materia, cels[0], cels[1].strip("`"))] = (k, cels[2], cels[3])
                k += 1
    return ordem, tabela


def chave_materia(nome: str) -> str:
    return re.sub(r"\s+", " ", sem_acentos(nome).lower()).strip()


def titulo_do_md(texto: str) -> str | None:
    for linha in texto.splitlines():
        m = re.match(r"^#\s+(.*?)\s*#*\s*$", linha)
        if m:
            return re.sub(r"[*`]", "", m.group(1)).strip()
    return None


def sigla_automatica(nome: str) -> str:
    vazias = {"direito", "de", "da", "do", "das", "dos", "e", "geral", "avançada"}
    palavras = [p for p in nome.split() if p.lower() not in vazias] or [nome]
    p = sem_acentos(palavras[0]).upper()
    return p if len(p) <= 6 else p[:4]


def chave_sintetico(p: Path) -> tuple:
    m = re.match(r"^\s*(\d+)", p.stem)
    return (0, int(m.group(1)), p.name.lower()) if m else (1, 0, p.name.lower())


# Título numerado no começo da linha, com um ou dois níveis: "1. Taxas", "**1. Taxas**",
# "### 1.2. Base de cálculo", "1.1– Regime", "1.Atos". Não pega "1.1.1", "10.000", "1ª" nem "10%".
RE_NUM_TITULO = re.compile(
    r"^(?P<pre>#{1,6}[ \t]+(?:\*\*)?|\*\*)?(?P<a>\d{1,3})(?:\.(?P<b>[1-9]\d?))?(?![\d.]*\d)"
    r"(?![/,%ºª°])")


def renumerar(texto: str, estado: dict, markdown: bool) -> str:
    """Refaz a numeração dos títulos em sequência única, na ordem em que aparecem.

    O resumo sintético é uma colagem de resumos soltos, e a numeração recomeça no meio
    ("1, 2, 3, 1..."). O nível principal segue em sequência na matéria inteira; o subnível
    (1.1, 1.2...) acompanha o título principal em que está e recomeça em cada um. O mesmo título
    com o mesmo número repetido logo em seguida é continuação (mantém o número; os subtítulos
    seguem). Só os números mudam; o resto da linha fica igual. `estado` guarda os contadores entre os arquivos da
    matéria. Em Markdown, "1. item" sem negrito é item de lista (fica como está); título é o que
    vem em negrito, em "#" ou escapado ("1\\.").
    """
    linhas = texto.split("\n")
    em_codigo = False
    for i, linha in enumerate(linhas):
        if RE_CERCA.match(linha):
            em_codigo = not em_codigo
            continue
        m = None if em_codigo else RE_NUM_TITULO.match(linha)
        if not m:
            continue
        resto = linha[m.end():]
        if m.group("b") is None:
            separador = re.match(r"(\\?\.|\))\s*\S|\s*[-–—]\s", resto)
            if not separador or (markdown and not m.group("pre") and not resto.startswith("\\")):
                continue
            nome = (m.group("a"), nucleo_titulo(resto))
            if nome[1] and nome == estado.get("titulo"):
                # O mesmo título, com o mesmo número, repetido logo em seguida (colagem feita em
                # duas vezes): é continuação dele; os subtítulos seguem de onde pararam.
                linhas[i] = linha[:m.start("a")] + str(estado["a"]) + resto
                continue
            estado["a"] = estado.get("a", 0) + 1
            estado["b"] = 0
            estado["titulo"] = nome
            linhas[i] = linha[:m.start("a")] + str(estado["a"]) + resto
        else:
            if not re.match(r"\.?\s*[-–—]?\s*\S", resto):
                continue
            estado["a"] = max(estado.get("a", 0), 1)
            estado["b"] = estado.get("b", 0) + 1
            linhas[i] = linha[:m.start("a")] + f"{estado['a']}.{estado['b']}" + resto
    return "\n".join(linhas)


def nucleo_titulo(resto: str) -> str:
    """Nome do título sem número, marcas e complementos, para reconhecer um título repetido."""
    texto = re.sub(r"^\\?[.)]?\s*[-–—]?\s*", "", resto)
    texto = re.split(r"<br>|\(", texto)[0]
    texto = re.sub(r"[*_\\#`]", "", texto)
    return re.sub(r"\s+", " ", sem_acentos(texto).lower()).strip(" .:-–—")


def pastas_das_materias() -> dict[str, Path]:
    return {slug(p.name): p for p in sorted(BASE.iterdir()) if p.is_dir() and p.name != CONTROLE}


def proxima_parte(pasta: Path) -> str:
    """Nome-base da próxima parte do resumo sintético: "NN - AAAA-MM-DD"."""
    numeros = [int(m.group(1)) for p in pasta.iterdir() if p.is_file()
               for m in [re.match(r"^\s*(\d+)", p.stem)] if m]
    return f"{max(numeros, default=0) + 1:02d} - {date.today().isoformat()}"


def salvar_sintetico(pasta_materia: Path, texto: str = "", docx: bytes = b"") -> Path:
    """Grava a próxima parte do resumo sintético, sem alterar o conteúdo.

    Texto colado vira .txt exatamente como veio. Um .docx vira .md com a mesma formatação
    (negrito, títulos, listas, tabelas), e as imagens dele ficam ao lado, como arquivos.
    """
    pasta = pasta_materia / PASTA_SINTETICO
    pasta.mkdir(exist_ok=True)
    nome = proxima_parte(pasta)
    if not docx:
        caminho = pasta / f"{nome}.txt"
        with open(caminho, "x", encoding="utf-8", newline="") as f:
            f.write(texto)
        return caminho
    blocos, midias = docx_para_blocos(docx)
    md = gravar_midias("\n\n".join(b for b, _ in blocos), midias, pasta, nome)
    caminho = pasta / f"{nome}.md"
    with open(caminho, "x", encoding="utf-8", newline="\n") as f:
        f.write(md + "\n")
    return caminho


def gravar_midias(md: str, midias: dict, pasta: Path, nome: str) -> str:
    """Salva as imagens usadas no texto ao lado dele e troca as marcas pelos nomes dos arquivos."""
    usadas = [rid for rid in midias if f"](§{rid}§)" in md]
    for k, rid in enumerate(usadas, 1):
        extensao, dados = midias[rid]
        arquivo = f"{nome} - imagem {k}{extensao}"
        (pasta / arquivo).write_bytes(dados)
        md = md.replace(f"](§{rid}§)", f"]({arquivo})")
    return md


# ----------------------------------------------------------------------------- .docx → Markdown

W_NS = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
R_NS = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
A_NS = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
EXTENSOES_IMAGEM = {".jpg", ".jpeg", ".png", ".gif", ".webp"}


def _md_escapar(texto: str) -> str:
    return texto.replace("\\", "\\\\").replace("*", "\\*").replace("`", "\\`").replace("|", "\\|")


def _md_trechos(trechos: list) -> str:
    """Junta trechos (texto, negrito, itálico) em Markdown, com as marcas fora dos espaços."""
    unidos: list = []
    for texto, negrito, italico in trechos:
        if unidos and unidos[-1][1:] == (negrito, italico):
            unidos[-1] = (unidos[-1][0] + texto, negrito, italico)
        else:
            unidos.append((texto, negrito, italico))
    saida = []
    for texto, negrito, italico in unidos:
        for k, pedaco in enumerate(texto.split("\n")):
            if k:
                saida.append("<br>")
            miolo = pedaco.strip()
            if not miolo or not (negrito or italico):
                saida.append(_md_escapar(pedaco))
                continue
            marca = ("**" if negrito else "") + ("*" if italico else "")
            ini = pedaco[:len(pedaco) - len(pedaco.lstrip())]
            fim = pedaco[len(pedaco.rstrip()):]
            saida.append(f"{ini}{marca}{_md_escapar(miolo)}{marca[::-1]}{fim}")
    return "".join(saida)


def docx_para_blocos(dados: bytes) -> tuple[list, dict]:
    """Converte um .docx em blocos Markdown [(markdown, texto puro)] e imagens {id: (ext, bytes)}.

    Só usa a biblioteca padrão. Mantém negrito, itálico, títulos, listas (com a numeração que o
    Word mostra), tabelas, quebras de linha e imagens; cores e fontes não são levadas.
    """
    import xml.etree.ElementTree as ET
    import zipfile
    from io import BytesIO

    W = W_NS
    pacote = zipfile.ZipFile(BytesIO(dados))
    nomes = set(pacote.namelist())
    documento = ET.fromstring(pacote.read("word/document.xml"))
    estilos = {}
    if "word/styles.xml" in nomes:
        for s in ET.fromstring(pacote.read("word/styles.xml")).iter(W + "style"):
            n = s.find(W + "name")
            estilos[s.get(W + "styleId")] = n.get(W + "val") if n is not None else ""
    niveis_de, abstrato_de = {}, {}
    if "word/numbering.xml" in nomes:
        numeracao = ET.fromstring(pacote.read("word/numbering.xml"))
        for a in numeracao.iter(W + "abstractNum"):
            niveis = {}
            for lvl in a.iter(W + "lvl"):
                ini, fmt = lvl.find(W + "start"), lvl.find(W + "numFmt")
                niveis[int(lvl.get(W + "ilvl"))] = (
                    int(ini.get(W + "val")) if ini is not None else 1,
                    fmt.get(W + "val") if fmt is not None else "bullet")
            niveis_de[a.get(W + "abstractNumId")] = niveis
        for n in numeracao.iter(W + "num"):
            abstrato_de[n.get(W + "numId")] = n.find(W + "abstractNumId").get(W + "val")
    relacoes = {}
    if "word/_rels/document.xml.rels" in nomes:
        for r in ET.fromstring(pacote.read("word/_rels/document.xml.rels")):
            relacoes[r.get("Id")] = r.get("Target")
    midias, contadores = {}, {}

    def trechos_do(elemento) -> list:
        trechos = []
        for r in elemento.iter(W + "r"):
            rpr = r.find(W + "rPr")

            def ligado(tag: str) -> bool:
                e = rpr.find(W + tag) if rpr is not None else None
                return e is not None and e.get(W + "val") not in ("0", "false")

            negrito, italico = ligado("b"), ligado("i")
            for filho in r:
                if filho.tag == W + "t":
                    trechos.append((filho.text or "", negrito, italico))
                elif filho.tag == W + "tab":
                    trechos.append(("\t", negrito, italico))
                elif filho.tag in (W + "br", W + "cr"):
                    trechos.append(("\n", False, False))
            for blip in r.iter(A_NS + "blip"):
                rid = blip.get(R_NS + "embed")
                alvo = relacoes.get(rid, "")
                if alvo and "word/" + alvo in nomes:
                    midias[rid] = (Path(alvo).suffix.lower() or ".png", pacote.read("word/" + alvo))
                    trechos.append((f"\x02{rid}\x02", False, False))
        return trechos

    def em_markdown(trechos: list) -> str:
        md = _md_trechos(trechos)
        md = re.sub(r"\x02([^\x02]+)\x02", lambda m: f"![imagem](§{m.group(1)}§)", md)
        while md.endswith("<br>"):
            md = md[:-4].rstrip()
        return md

    def rotulo_lista(num_id: str, nivel: int) -> str:
        niveis = niveis_de.get(abstrato_de.get(num_id, ""), {})
        inicio, formato = niveis.get(nivel, (1, "bullet"))
        c = contadores.setdefault(num_id, {})
        c[nivel] = c.get(nivel, inicio - 1) + 1
        for k in [k for k in c if k > nivel]:
            del c[k]
        v = c[nivel]
        if formato == "decimal":
            return f"{v}."
        if formato in ("lowerLetter", "upperLetter"):
            letra = chr(96 + v) if formato == "lowerLetter" else chr(64 + v)
            return f"- {letra})"
        return "-"

    blocos = []
    for el in documento.find(W + "body"):
        if el.tag == W + "p":
            ppr = el.find(W + "pPr")
            estilo, lista = "", None
            if ppr is not None:
                ps = ppr.find(W + "pStyle")
                if ps is not None:
                    estilo = estilos.get(ps.get(W + "val"), ps.get(W + "val") or "").lower()
                npr = ppr.find(W + "numPr")
                if npr is not None and npr.find(W + "numId") is not None:
                    num_id = npr.find(W + "numId").get(W + "val")
                    ilvl = npr.find(W + "ilvl")
                    if num_id != "0":
                        lista = (num_id, int(ilvl.get(W + "val")) if ilvl is not None else 0)
            trechos = trechos_do(el)
            puro = "".join(t for t, _, _ in trechos).replace("\n", " ").strip()
            titulo = re.match(r"(?:heading|título|titulo)\s*(\d)", estilo)
            if titulo and puro:
                nivel = min(6, max(2, int(titulo.group(1))))
                blocos.append(("#" * nivel + " " + em_markdown([(t, False, i) for t, _, i in trechos]),
                               puro))
            elif lista and puro:
                recuo = "    " * lista[1]
                blocos.append((f"{recuo}{rotulo_lista(*lista)} {em_markdown(trechos)}", puro))
            elif puro or "\x02" in "".join(t for t, _, _ in trechos):
                md = em_markdown(trechos)
                if re.match(r"(\d{1,9}[.)]|[-+>#]|\|)\s", md):  # não virar lista ou título por acaso
                    md = re.sub(r"^(\d{1,9})([.)])", r"\1\\\2", md) if md[0].isdigit() else "\\" + md
                blocos.append((md, puro))
            else:
                blocos.append(("", ""))
        elif el.tag == W + "tbl":
            linhas = []
            for tr in el.findall(W + "tr"):
                celulas = []
                for tc in tr.findall(W + "tc"):
                    partes = [em_markdown(trechos_do(p)) for p in tc.findall(W + "p")]
                    celulas.append("<br>".join(x for x in partes if x.strip()).replace("\n", " "))
                linhas.append(celulas)
            puro = " ".join(re.sub(r"<br>|\\", " ", c) for ln in linhas for c in ln)
            if len(linhas) == 1 and len(linhas[0]) == 1:  # tabela de uma célula é um quadro de destaque
                blocos.append(("> " + linhas[0][0].replace("<br>", "\n> "), puro))
            elif linhas:
                n = max(len(ln) for ln in linhas)
                md = ["| " + " | ".join((ln + [""] * n)[:n]) + " |" for ln in linhas]
                md.insert(1, "|" + "---|" * n)
                blocos.append(("\n".join(md), puro))
    # Uma linha em branco entre blocos, nenhuma entre itens seguidos da mesma lista.
    juntos, anterior_lista = [], False
    for md, puro in blocos:
        if not md.strip():
            anterior_lista = False
            if juntos and juntos[-1][0] != "":
                juntos.append(("", ""))
            continue
        eh_lista = bool(re.match(r"\s*(-|\d+\.)\s", md)) and not md.startswith("\\")
        if juntos and juntos[-1][0] != "" and not (eh_lista and anterior_lista):
            juntos.append(("", ""))
        juntos.append((md, puro))
        anterior_lista = eh_lista
    while juntos and juntos[-1][0] == "":
        juntos.pop()
    saida, atual = [], []
    for md, puro in juntos:  # itens de lista seguidos ficam num bloco só
        if md == "":
            if atual:
                saida.append(("\n".join(m for m, _ in atual), " ".join(p for _, p in atual)))
                atual = []
        else:
            atual.append((md, puro))
    if atual:
        saida.append(("\n".join(m for m, _ in atual), " ".join(p for _, p in atual)))
    return saida, midias


def peso_parte(parte: str) -> int:
    """Espaço aproximado que um bloco ocupa na página, em caracteres de texto."""
    peso = len(texto_de_html(parte)) + 60
    peso += 45 * parte.count("<tr") + 25 * parte.count("<li")
    if re.match(r"<h[2-6]", parte):
        peso += 120
    if parte.startswith('<div class="codigo"'):
        peso += 30 * parte.count("\n")
    return peso


class Base:
    def __init__(self):
        self.avisos: list[str] = []
        self.docs: list[dict] = []
        self.controle: list[dict] = []
        self.sinteticos: list[dict] = []
        self.por_caminho: dict[str, dict] = {}
        self.por_nome: dict[str, list[dict]] = {}
        self.por_pasta: dict[str, list[dict]] = {}
        self.materias: list[dict] = []
        self.materia_por_id: dict[str, dict] = {}
        self.citado_em: dict[str, set[str]] = {}
        self.versao, self.data = "v???", ""

    def aviso(self, doc: dict, msg: str) -> None:
        linha = f"{doc['caminho']}: {msg}"
        if linha not in self.avisos:
            self.avisos.append(linha)

    # -- referências cruzadas
    def resolver(self, ref: str, origem: dict) -> tuple[dict, str] | None:
        pasta = posixpath.dirname(origem["caminho"])
        da_raiz = ref[len("ESTUDOS/"):] if ref.startswith("ESTUDOS/") else ref
        candidatos = [posixpath.normpath(posixpath.join(pasta, ref)), posixpath.normpath(da_raiz)]
        if ref.endswith(".md"):
            for c in candidatos:
                if c in self.por_caminho:
                    d = self.por_caminho[c]
                    return d, d["titulo"]
            iguais = self.por_nome.get(posixpath.basename(ref), [])
            if len(iguais) == 1:
                return iguais[0], iguais[0]["titulo"]
            return None
        candidatos.append(posixpath.normpath(posixpath.join(posixpath.dirname(pasta), ref)))
        for c in candidatos:
            c = c.rstrip("/")
            if c in self.por_pasta:
                primeiro = self.por_pasta[c][0]
                return primeiro, primeiro["assuntoNome"] or posixpath.basename(c)
        return None

    def ligar(self, origem: dict, destino: dict) -> None:
        if origem["materia"] != "controle" and destino["id"] != origem["id"]:
            self.citado_em.setdefault(destino["id"], set()).add(origem["id"])

    def link(self, destino: dict, rotulo: str, origem: dict) -> str:
        m = self.materia_por_id[destino["materia"]]
        sigla = f' data-sig="{m["sigla"]}"' if destino["materia"] != origem["materia"] else ""
        dica = " › ".join(x for x in (m["nome"], destino["assuntoNome"], destino["titulo"]) if x)
        return (f'<a class="xref c-{m["cor"]}" href="#{destino["id"]}"{sigla} '
                f'title="{esc(dica)}">{esc(rotulo)}</a>')

    # -- carga
    def carregar(self) -> None:
        ordem_materias, tabela = ler_assuntos(BASE / CONTROLE / "assuntos-estudados.md")
        diario = BASE / CONTROLE / "diario-de-estudos.md"
        if diario.exists():
            texto_diario = diario.read_text(encoding="utf-8")
            m = re.search(r"Versão atual da base:\s*\*\*(v\d+)\*\*\s*\((\d{2}/\d{2}/\d{4})\)",
                          texto_diario)
            if m:
                self.versao, self.data = m.group(1), m.group(2)

        cores_livres = list(CORES_LIVRES)
        materias: dict[str, dict] = {}

        def materia(nome: str) -> dict:
            if nome not in materias:
                sigla, cor = MATERIAS.get(nome, (None, None))
                if cor is None:
                    sigla = sigla_automatica(nome)
                    cor = cores_livres.pop(0) if cores_livres else "ctrl"
                pos = ordem_materias.index(nome) if nome in ordem_materias else 1000
                materias[nome] = {"id": slug(nome), "nome": nome, "sigla": sigla, "cor": cor,
                                  "_ordem": (pos, nome)}
            return materias[nome]

        brutos = []
        for p in sorted(BASE.rglob("*.md")):
            rel = p.relative_to(BASE).as_posix()
            partes = rel.split("/")
            if len(partes) > 2 and partes[1] == PASTA_SINTETICO:
                continue
            texto = p.read_text(encoding="utf-8")
            arquivo = partes[-1]
            nome = arquivo[:-3]
            if partes[0] == CONTROLE:
                materia_nome, pasta = "Controle", ""
            else:
                materia_nome = partes[0]
                pasta = "/".join(partes[1:-1])
                if len(partes) > 3:
                    self.avisos.append(f"{rel}: pasta aninhada demais; exibida como '{pasta}'")
                materia(materia_nome)
            mid = "controle" if partes[0] == CONTROLE else slug(materia_nome)
            num = re.match(r"^(\d+)\s*-\s*(.+)$", posixpath.basename(pasta)) if pasta else None
            chave = tabela.get((materia_nome, pasta, arquivo))
            md_mapa = None
            if mid != "controle":
                texto, md_mapa = separar_mapa(texto)
            doc = {
                "id": f"{mid}.{slug(nome)}",
                "tipo": "ctrl" if mid == "controle" else "tema",
                "caminho": rel,
                "materia": mid,
                "materiaNome": materia_nome,
                "pasta": posixpath.join(partes[0], pasta) if pasta else partes[0],
                "assuntoNum": num.group(1) if num else "",
                "assuntoNome": (num.group(2) if num else posixpath.basename(pasta)) if pasta else "",
                "titulo": titulo_do_md(texto) or nome.replace("-", " ").capitalize(),
                "resumo_md": chave[1] if chave else "",
                "status": chave[2] if chave else "",
                "md": texto,
                "md_mapa": md_mapa,
                "hash": resumo_hash(texto),
            }
            if not titulo_do_md(texto):
                self.aviso(doc, "arquivo sem título (# ...) na primeira seção")
            if not texto.strip():
                self.aviso(doc, "arquivo vazio")
            if mid != "controle" and md_mapa is None:
                self.aviso(doc, "tema sem mapa mental (seção '## Mapa mental')")
            ordem_arquivo = chave[0] if chave else 10 ** 6
            if mid == "controle":
                pos = ORDEM_CONTROLE.index(nome) if nome in ORDEM_CONTROLE else len(ORDEM_CONTROLE)
                doc["_ordem"] = (pos, nome)
            else:
                n_pasta = int(num.group(1)) if num else 999
                doc["_ordem"] = materias[materia_nome]["_ordem"] + (n_pasta, pasta, ordem_arquivo,
                                                                     nome)
            brutos.append(doc)

        for pasta in sorted(BASE.iterdir()):
            if pasta.is_dir() and pasta.name != CONTROLE and (pasta / PASTA_SINTETICO).is_dir():
                self.carregar_sintetico(materia(pasta.name), pasta / PASTA_SINTETICO)

        self.materia_por_id = {m["id"]: m for m in materias.values()}
        self.materia_por_id["controle"] = {"id": "controle", "nome": "Controle da base",
                                           "sigla": "CTRL", "cor": "ctrl"}
        brutos.sort(key=lambda d: d["_ordem"])
        for d in brutos:
            (self.controle if d["materia"] == "controle" else self.docs).append(d)
            self.por_caminho[d["caminho"]] = d
            self.por_nome.setdefault(posixpath.basename(d["caminho"]), []).append(d)
            self.por_pasta.setdefault(d["pasta"], []).append(d)

        for mb in sorted(materias.values(), key=lambda x: x["_ordem"]):
            m = {k: v for k, v in mb.items() if k != "_ordem"}
            assuntos: list[dict] = []
            for d in (x for x in self.docs if x["materia"] == m["id"]):
                if not assuntos or assuntos[-1]["pasta"] != d["pasta"]:
                    assuntos.append({"pasta": d["pasta"], "num": d["assuntoNum"],
                                     "nome": d["assuntoNome"], "temas": []})
                assuntos[-1]["temas"].append(d["id"])
            m["assuntos"] = [{k: a[k] for k in ("num", "nome", "temas")} for a in assuntos]
            m["sintetico"] = [d["id"] for d in self.sinteticos if d["materia"] == m["id"]]
            self.materias.append(m)

    def carregar_sintetico(self, materia: dict, pasta: Path) -> None:
        """Arquivos do resumo sintético: .txt e .md, na ordem do número no início do nome."""
        rel_pasta = pasta.relative_to(BASE).as_posix()
        numeracao: dict = {}
        for p in sorted(pasta.iterdir(), key=chave_sintetico):
            if not p.is_file() or p.name.upper().startswith("LEIA-ME"):
                continue
            if p.suffix.lower() in EXTENSOES_IMAGEM:  # imagens usadas pelas partes .md
                continue
            doc = {"caminho": f"{rel_pasta}/{p.name}"}
            if p.suffix.lower() not in (".txt", ".md"):
                self.aviso(doc, "formato não lido no resumo sintético (use .txt ou .md)")
                continue
            dados = p.read_bytes()
            try:
                texto = dados.decode("utf-8-sig")
            except UnicodeDecodeError:
                texto = dados.decode("cp1252", errors="replace")
                self.aviso(doc, "arquivo não está em UTF-8; lido como Windows-1252 (confira os "
                                "acentos e salve em UTF-8)")
            texto = texto.replace("\r\n", "\n").replace("\r", "\n")
            if not texto.strip():
                self.aviso(doc, "arquivo vazio")
                continue
            m = re.match(r"^\s*(\d+)", p.stem)
            if not m:
                self.aviso(doc, "nome sem número no início: entra depois dos numerados")
            nome = re.sub(r"^\s*\d+\s*[-–—._)]*\s*", "", p.stem).strip()
            data = nome if re.fullmatch(r"\d{4}-\d{2}-\d{2}", nome) else ""
            parte = f"Parte {m.group(1)}" if m else "Parte sem número"
            rotulo = " · ".join(x for x in (parte, "" if data else nome,
                                            f"adicionada em {'/'.join(reversed(data.split('-')))}"
                                            if data else "") if x)
            exibido = renumerar(texto, numeracao, p.suffix.lower() == ".md")
            mid = materia["id"]
            doc.update({
                "pasta_abs": pasta,
                "id": f"{mid}.sint.{slug(p.stem)}",
                "tipo": "sint",
                "materia": mid,
                "materiaNome": materia["nome"],
                "pasta": rel_pasta,
                "assuntoNum": m.group(1) if m else "",
                "assuntoNome": PASTA_SINTETICO,
                "titulo": parte if data or not nome else nome,
                "rotulo": rotulo,
                "resumo_md": "",
                "status": "",
                "formato": p.suffix.lower()[1:],
                "md": exibido,
                "md_mapa": None,
                "hash": resumo_hash(texto),
            })
            self.sinteticos.append(doc)

    # -- renderização e checagens
    def renderizar(self) -> dict:
        indice, pegadinhas, saida = [], [], {}
        todos = self.docs + self.controle + self.sinteticos
        n_nos = 0
        for d in todos:
            r = Renderizador(self, d)
            if d["tipo"] == "sint" and d["formato"] == "txt":
                partes = r.texto_simples(d["md"])
            else:
                partes = r.blocos(ler_blocos(d["md"].splitlines()), lista=True)
            resumo = Renderizador(self, d).inline(d["resumo_md"], False) if d["resumo_md"] else ""
            titulo = d["titulo"] if d["tipo"] == "sint" else (r.titulo or d["titulo"])
            d.update(partes=partes, toc=r.toc, palavras=r.palavras, resumo=resumo, titulo=titulo)
            if d["md_mapa"] is not None:
                d["mapa"] = self.arvore_mapa(d, d["md_mapa"])
                ligar_mapa(d["mapa"], r)
                n_nos += contar_nos(d["mapa"])
            indice.extend(r.indice)
            if d["tipo"] == "tema":
                pegadinhas.extend(r.pegadinhas)
        self.n_nos = n_nos
        brutos = {d["id"] for d in self.sinteticos}
        for e in indice:
            vazou = RE_VAZOU.search(e[3])
            if vazou and e[0] not in brutos:
                d = next(x for x in todos if x["id"] == e[0])
                self.aviso(d, f"marcação markdown não convertida ({vazou.group(0)!r}): "
                              f"{e[3][:70]}")
        ordem = [d["id"] for d in self.docs]
        for m in self.materias:
            m["geral"] = self.paginar([d for d in self.docs if d["materia"] == m["id"]])
        for d in todos:
            citantes = self.citado_em.get(d["id"], set())
            item = {
                "titulo": d["titulo"], "tipo": d["tipo"], "materia": d["materia"],
                "assunto": d["assuntoNome"], "num": d["assuntoNum"], "resumo": d["resumo"],
                "status": d["status"], "caminho": d["caminho"], "palavras": d["palavras"],
                "toc": d["toc"], "citadoEm": [x for x in ordem if x in citantes],
                "hash": d["hash"], "partes": d["partes"],
            }
            if "mapa" in d:
                item["mapa"] = d["mapa"]
            if "pag" in d:
                item["pag"] = d["pag"]
            if d["tipo"] == "sint":
                item["rotulo"] = d["rotulo"]
                item["texto"] = d["md"]  # para copiar/baixar o resumo sintético completo
            saida[d["id"]] = item
        return {
            "meta": {"gerado": datetime.now().strftime("%d/%m/%Y %H:%M")},
            "materias": self.materias,
            "controle": dict(self.materia_por_id["controle"],
                             temas=[d["id"] for d in self.controle]),
            "ordem": ordem,
            "docs": saida,
            "indice": indice,
            "pegadinhas": pegadinhas,
        }

    def arvore_mapa(self, doc: dict, md: str) -> list[dict]:
        r = Renderizador(self, doc)

        def nos_da_lista(bloco: dict) -> list[dict]:
            nos = []
            for item in bloco["itens"]:
                rotulo = " ".join(b["texto"] for b in item if b["t"] == "p")
                no = {"t": r.inline(rotulo, False)}
                if RE_VAZOU.search(texto_de_html(no["t"])):
                    self.aviso(doc, f"mapa mental: marcação não convertida em '{rotulo[:60]}'")
                filhos = [f for b in item if b["t"] in ("ul", "ol") for f in nos_da_lista(b)]
                if filhos:
                    no["c"] = filhos
                nos.append(no)
            return nos

        nos = []
        for b in ler_blocos(md.splitlines()):
            if b["t"] in ("ul", "ol"):
                nos.extend(nos_da_lista(b))
            else:
                self.aviso(doc, "mapa mental: só listas com '-' são lidas; o resto foi ignorado")
        if not nos:
            self.aviso(doc, "mapa mental vazio")
        return nos

    @staticmethod
    def paginar(temas: list[dict]) -> dict:
        """Divide o resumo geral da matéria em páginas, sem quebrar blocos.

        Cada página começa num bloco; um título nunca fica sozinho no fim da página, e um tema
        que começaria no último quinto de uma página passa para a seguinte.
        """
        itens = []  # (tema, k, peso, prende_ao_proximo); k = -1 é o cabeçalho do tema
        for d in temas:
            itens.append((d["id"], -1, 200, True))
            for k, parte in enumerate(d["partes"]):
                itens.append((d["id"], k, peso_parte(parte), bool(re.match(r"<h[2-6]", parte))))
        if not itens:
            return {"paginas": 0, "quebras": [], "hash": ""}
        inicios, atual = [0], 0
        for i, (_, k, peso, _) in enumerate(itens):
            cheia = atual + peso > CARACTERES_POR_PAGINA
            tema_no_fim = k == -1 and atual > 0.8 * CARACTERES_POR_PAGINA
            if atual > 0 and (cheia or tema_no_fim):
                j = i
                while j - 1 > inicios[-1] and itens[j - 1][3]:
                    j -= 1
                inicios.append(j)
                atual = sum(x[2] for x in itens[j:i])
            atual += peso
        pagina_de = []
        p = 0
        for i in range(len(itens)):
            if p < len(inicios) and i == inicios[p]:
                p += 1
            pagina_de.append(p)
        faixa: dict[str, list[int]] = {}
        for (tid, _, _, _), pg in zip(itens, pagina_de):
            faixa.setdefault(tid, [pg, pg])[1] = pg
        for d in temas:
            d["pag"] = faixa[d["id"]]
        return {
            "paginas": len(inicios),
            "quebras": [[itens[i][0], itens[i][1]] for i in inicios],
            "hash": resumo_hash("".join(d["hash"] for d in temas)),
        }


def contar_nos(nos: list[dict]) -> int:
    return sum(1 + contar_nos(n.get("c", [])) for n in nos)


# ----------------------------------------------------------------------------- saída

DESCRICAO = ("Base de estudos para Auditor Fiscal: resumos por matéria e por tópico, mapas "
             "mentais, busca em todo o material e pegadinhas CEBRASPE.")
# Ícone da aba: um livro com as abas coloridas das quatro primeiras matérias.
ICONE_SVG = (
    "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'>"
    "<rect x='20' y='4' width='10' height='5' rx='1.5' fill='#0b7285'/>"
    "<rect x='20' y='10' width='10' height='5' rx='1.5' fill='#b45309'/>"
    "<rect x='20' y='16' width='10' height='5' rx='1.5' fill='#3f4fc4'/>"
    "<rect x='20' y='22' width='10' height='5' rx='1.5' fill='#a3174f'/>"
    "<rect x='2' y='2' width='22' height='28' rx='3.5' fill='#2b3f7a'/>"
    "<rect x='7' y='9' width='12' height='2.5' rx='1.25' fill='#fff'/>"
    "<rect x='7' y='14.5' width='9' height='2.5' rx='1.25' fill='#fff' fill-opacity='.65'/>"
    "</svg>"
)


def montar_paginas(dados: dict) -> tuple[str, str]:
    """Devolve (página completa do site, página sem esqueleto HTML para a página privada)."""
    modelo = MODELO.read_text(encoding="utf-8")
    if MARCADOR_DADOS not in modelo:
        raise SystemExit(f"O modelo {MODELO.name} não contém o marcador {MARCADOR_DADOS}.")
    bruto = json.dumps(dados, ensure_ascii=False, separators=(",", ":"))
    bruto = bruto.replace("</", "<\\/").replace("<!--", "<\\!--")
    pagina = modelo.replace(MARCADOR_DADOS, bruto)
    icone = "data:image/svg+xml," + (ICONE_SVG.replace("#", "%23")
                                     .replace("<", "%3C").replace(">", "%3E"))
    site = ('<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, '
            'viewport-fit=cover">\n'
            f'<meta name="description" content="{esc(DESCRICAO)}">\n'
            '<meta name="robots" content="noindex, nofollow">\n'
            f'<link rel="icon" href="{icone}">\n' + pagina + "\n</html>\n")
    return site, pagina


def escrever(caminho: Path, texto: str) -> None:
    caminho.parent.mkdir(parents=True, exist_ok=True)
    # open() em vez de write_text(newline=...), que só existe a partir do Python 3.10
    with open(caminho, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)


def gerar(escrever_saida: bool = True) -> tuple["Base", dict, int]:
    """Carrega a base, monta os dados e, se pedido, grava as duas saídas (devolve o tamanho)."""
    base = Base()
    base.carregar()
    dados = base.renderizar()
    tamanho = 0
    if escrever_saida:
        site, pagina_privada = montar_paginas(dados)
        escrever(SAIDA_SITE, site)
        escrever(SAIDA_PAGINA_PRIVADA, pagina_privada)
        tamanho = len(site.encode("utf-8"))
    return base, dados, tamanho


TRAVA_GERACAO = threading.Lock()


class Manipulador(http.server.SimpleHTTPRequestHandler):
    """Serve a pasta site/ sem cache e recebe as novas partes do resumo sintético.

    O envio só é aceito da própria página em localhost (Host e Origin conferidos, cabeçalho
    X-Estudos obrigatório): outro site aberto no navegador não consegue gravar nada.
    """

    def end_headers(self) -> None:
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()

    def responder(self, codigo: int, dados: dict) -> None:
        corpo = json.dumps(dados, ensure_ascii=False).encode("utf-8")
        self.send_response(codigo)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(corpo)))
        self.end_headers()
        self.wfile.write(corpo)

    def da_propria_pagina(self) -> bool:
        porta = self.server.server_address[1]
        hosts = {f"localhost:{porta}", f"127.0.0.1:{porta}"}
        origem = self.headers.get("Origin")
        return (self.headers.get("Host") in hosts and self.headers.get("X-Estudos") == "1"
                and (origem is None or origem in {f"http://{h}" for h in hosts}))

    def do_GET(self) -> None:
        if self.path.split("?")[0] == ROTA_SINTETICO:
            if not self.da_propria_pagina():
                self.responder(403, {"ok": False, "erro": "pedido recusado"})
            else:
                self.responder(200, {"ok": True})
            return
        super().do_GET()

    def do_POST(self) -> None:
        if self.path.split("?")[0] != ROTA_SINTETICO:
            self.responder(404, {"ok": False, "erro": "endereço desconhecido"})
            return
        if not self.da_propria_pagina():
            self.responder(403, {"ok": False, "erro": "pedido recusado"})
            return
        tamanho = int(self.headers.get("Content-Length") or 0)
        if not 0 < tamanho <= LIMITE_SINTETICO:
            self.responder(413, {"ok": False, "erro": "texto vazio ou grande demais"})
            return
        try:
            pedido = json.loads(self.rfile.read(tamanho).decode("utf-8"))
            materia, texto = pedido["materia"], pedido.get("texto", "")
            docx = base64.b64decode(pedido["docx"]) if pedido.get("docx") else b""
        except (ValueError, KeyError, TypeError, AttributeError):
            self.responder(400, {"ok": False, "erro": "pedido inválido"})
            return
        pasta = pastas_das_materias().get(materia) if isinstance(materia, str) else None
        if pasta is None or not isinstance(texto, str) or not (texto.strip() or docx):
            self.responder(400, {"ok": False, "erro": "disciplina desconhecida ou texto vazio"})
            return
        if docx:
            try:
                blocos, _ = docx_para_blocos(docx)
            except Exception:
                blocos = []
            if not any(md.strip() for md, _ in blocos):
                self.responder(400, {"ok": False, "erro": "não consegui ler o arquivo .docx"})
                return
        with TRAVA_GERACAO:
            caminho = salvar_sintetico(pasta, texto, docx)
            rel = caminho.relative_to(BASE).as_posix()
            print(f"Resumo sintético: parte salva em ESTUDOS/{rel}", flush=True)
            try:
                base, _, _ = gerar()
            except Exception as erro:  # o arquivo já está salvo; só a geração falhou
                self.responder(500, {"ok": False, "arquivo": rel,
                                     "erro": f"parte salva, mas o site não foi gerado: {erro}"})
                return
        avisos = [a for a in base.avisos if a.startswith(f"{pasta.name}/{PASTA_SINTETICO}/")]
        self.responder(200, {"ok": True, "arquivo": rel, "id": f"{materia}.sint.{slug(caminho.stem)}",
                             "avisos": avisos})


def servir(porta: int) -> int:
    manipulador = functools.partial(Manipulador, directory=str(PASTA_SITE))
    try:
        servidor = http.server.ThreadingHTTPServer(("127.0.0.1", porta), manipulador)
    except OSError:
        print(f"\nA porta {porta} já está em uso: o site pode já estar no ar em "
              f"http://localhost:{porta}/")
        return 1
    print(f"\nSite no ar em http://localhost:{porta}/ (Ctrl+C para parar)", flush=True)
    with servidor:
        try:
            servidor.serve_forever()
        except KeyboardInterrupt:
            print("\nServidor parado.")
    return 0


def main(argv: list[str]) -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    if not BASE.is_dir():
        print(f"Pasta não encontrada: {BASE}")
        return 1
    verificar = "--verificar" in argv
    base, dados, tamanho = gerar(escrever_saida=not verificar)
    n_temas, n_ctrl = len(base.docs), len(base.controle)
    tipos = {}
    for p in dados["pegadinhas"]:
        tipos[p["v"] or "obs"] = tipos.get(p["v"] or "obs", 0) + 1
    print(f"Base {base.versao} ({base.data}): {len(base.materias)} matérias, {n_temas} temas "
          f"e {n_ctrl} arquivos de controle")
    print(f"Índice de busca: {len(dados['indice'])} trechos · Pegadinhas: "
          f"{len(dados['pegadinhas'])} (E {tipos.get('E', 0)}, C {tipos.get('C', 0)}, "
          f"observações {tipos.get('obs', 0)})")
    com_mapa = sum(1 for d in base.docs if d.get("mapa"))
    print(f"Mapas mentais: {com_mapa} de {n_temas} temas ({base.n_nos} ramos) · "
          f"Resumo sintético: {len(base.sinteticos)} arquivo(s)")
    print("Resumo geral: " + " · ".join(
        f"{m['sigla']} {m['geral']['paginas']} págs." for m in base.materias))
    if not verificar:
        print(f"Gerado: {SAIDA_SITE.relative_to(RAIZ).as_posix()} ({tamanho // 1024} KB) e "
              f"{SAIDA_PAGINA_PRIVADA.relative_to(RAIZ).as_posix()}")
    if base.avisos:
        print(f"\n{len(base.avisos)} aviso(s):")
        for a in base.avisos:
            print("  -", a)
    else:
        print("Nenhum aviso: todas as referências resolvem e não sobrou markdown sem conversão.")
    if "--servir" in argv and not verificar:
        return servir(PORTA_LOCAL)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
