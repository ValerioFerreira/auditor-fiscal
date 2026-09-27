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
"""
from __future__ import annotations

import functools
import html
import http.server
import json
import posixpath
import re
import sys
import unicodedata
from datetime import datetime
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


# ----------------------------------------------------------------------------- inline

RE_CODIGO = re.compile(r"(`+)(.+?)\1")
RE_VEREDITO = re.compile(r"\*\*(CERTO|ERRADO)\*\*")
RE_NEGRITO_ITALICO = re.compile(r"\*\*\*(?=\S)(.+?)(?<=\S)\*\*\*")
RE_NEGRITO = re.compile(r"\*\*(?=\S)(.+?)(?<=\S)\*\*")
RE_ITALICO = re.compile(r"(?<![*\w])\*(?=[^\s*])(.+?)(?<=[^\s*])\*(?![*\w])")
RE_A_ESTUDAR = re.compile(r"\(a estudar\)|(?<=— )a estudar\b")
RE_PEGADINHA = re.compile(r"^(?P<s>.*?)\s*→\s*\*\*(?P<v>CERTO|ERRADO)\*\*(?P<x>.*)$")
RE_ROTULO_PEGADINHA = re.compile(r"^(?:⚠️?\s*)?Pegadinha:\s*", re.I)
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
    """Converte os blocos de um documento em HTML, índice de busca e pegadinhas."""

    def __init__(self, base: "Base", doc: dict):
        self.base = base
        self.doc = doc
        self.n = 0
        self.toc: list[dict] = []
        self.ids: set[str] = set()
        self.indice: list[list] = []
        self.pegadinhas: list[dict] = []
        self.h2 = self.h3 = None
        self.peg_h2 = self.peg_h3 = False
        self.titulo: str | None = None
        self.palavras = 0

    # -- inline
    def inline(self, md: str, registrar: bool = True) -> str:
        guardados: list[str] = []

        def guardar(h: str) -> str:
            guardados.append(h)
            return f"\x00{len(guardados) - 1}\x00"

        s = RE_CODIGO.sub(lambda m: guardar(self.codigo(m.group(2), registrar)), md)
        s = html.escape(s, quote=False)
        s = RE_VEREDITO.sub(
            lambda m: guardar(f'<span class="vd vd-{m.group(1)[0]}">{m.group(1)}</span>'), s)
        s = RE_NEGRITO_ITALICO.sub(r"<strong><em>\1</em></strong>", s)
        s = RE_NEGRITO.sub(r"<strong>\1</strong>", s)
        s = RE_ITALICO.sub(r"<em>\1</em>", s)
        s = RE_A_ESTUDAR.sub(SELO_A_ESTUDAR, s)
        return re.sub(r"\x00(\d+)\x00", lambda m: guardados[int(m.group(1))], s)

    def codigo(self, conteudo: str, registrar: bool) -> str:
        c = conteudo.strip()
        if c.endswith(".md") or c.endswith("/"):
            alvo = self.base.resolver(c, self.doc)
            if alvo:
                destino, rotulo = alvo
                if registrar:
                    self.base.ligar(self.doc, destino)
                return self.base.link(destino, rotulo, self.doc)
            if c.endswith(".md") and registrar:
                self.base.aviso(self.doc, f"referência não encontrada: `{c}`")
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
    def blocos(self, blocos: list[dict], prof: int = 0) -> str:
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
        return "\n".join(p for p in partes if p)

    def titulo_html(self, b: dict) -> str:
        conteudo = self.inline(b["texto"])
        texto = texto_de_html(conteudo)
        if b["nivel"] == 1 and self.titulo is None:
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
        if item and item[0]["t"] == "p":
            v, corpo = self.corpo_pegadinha(item[0]["texto"], True)
            resto = item[1:]
        else:
            v, corpo, resto = "", "", item
        self.indexar(n, texto_de_html(corpo))
        if resto:
            corpo += self.blocos(resto, 1)
        li = self.li_pegadinha(v, n, corpo)
        self.pegadinhas.append({"d": self.doc["id"], "b": n, "v": v, "h": li})
        return li

    def citacao(self, b: dict, prof: int, anterior: dict | None) -> str:
        primeiro = next((x["texto"] for x in b["blocos"] if x["t"] == "p"), "")
        tipo = classificar_citacao(texto_de_html(self.inline(primeiro, False)), anterior)
        n_inicio = self.n + 1
        interno = self.blocos(b["blocos"], prof + 1)
        if tipo == "peg" and prof == 0 and primeiro:
            v, corpo = self.corpo_pegadinha(RE_ROTULO_PEGADINHA.sub("", primeiro), False)
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
                self.base.aviso(self.doc, f"linha de tabela com {len(linha)} colunas "
                                          f"(esperadas {ncol}): {linha[0][:50]}")
            linha = (linha + [""] * ncol)[:ncol]
            corpo.append(linha_html([celula("td", c, k) for k, c in enumerate(linha)]))
        return (f'<div class="tabela"><table><thead>{cab}</thead>'
                f'<tbody>{"".join(corpo)}</tbody></table></div>')

    def codigo_bloco(self, b: dict) -> str:
        n = self.novo()
        self.indexar(n, re.sub(r"\s+", " ", b["texto"]).strip())
        return (f'<div class="codigo"><pre data-b="{n}"><code>'
                f'{html.escape(b["texto"], quote=False)}</code></pre></div>')


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


class Base:
    def __init__(self):
        self.avisos: list[str] = []
        self.docs: list[dict] = []
        self.controle: list[dict] = []
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
            m = re.search(r"Versão atual da base:\s*\*\*(v\d+)\*\*\s*\((\d{2}/\d{2}/\d{4})\)",
                          diario.read_text(encoding="utf-8"))
            if m:
                self.versao, self.data = m.group(1), m.group(2)

        cores_livres = list(CORES_LIVRES)
        materias: dict[str, dict] = {}
        brutos = []
        for p in sorted(BASE.rglob("*.md")):
            rel = p.relative_to(BASE).as_posix()
            partes = rel.split("/")
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
            if materia_nome not in materias and partes[0] != CONTROLE:
                sigla, cor = MATERIAS.get(materia_nome, (None, None))
                if cor is None:
                    sigla = sigla_automatica(materia_nome)
                    cor = cores_livres.pop(0) if cores_livres else "ctrl"
                materias[materia_nome] = {"id": slug(materia_nome), "nome": materia_nome,
                                          "sigla": sigla, "cor": cor}
            mid = "controle" if partes[0] == CONTROLE else slug(materia_nome)
            num = re.match(r"^(\d+)\s*-\s*(.+)$", posixpath.basename(pasta)) if pasta else None
            chave = tabela.get((materia_nome, pasta, arquivo))
            doc = {
                "id": f"{mid}.{slug(nome)}",
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
            }
            if not titulo_do_md(texto):
                self.aviso(doc, "arquivo sem título (# ...) na primeira seção")
            if not texto.strip():
                self.aviso(doc, "arquivo vazio")
            ordem_arquivo = chave[0] if chave else 10 ** 6
            if mid == "controle":
                pos = ORDEM_CONTROLE.index(nome) if nome in ORDEM_CONTROLE else len(ORDEM_CONTROLE)
                doc["_ordem"] = (pos, nome)
            else:
                pos_m = (ordem_materias.index(materia_nome) if materia_nome in ordem_materias
                         else 1000)
                n_pasta = int(num.group(1)) if num else 999
                doc["_ordem"] = (pos_m, materia_nome, n_pasta, pasta, ordem_arquivo, nome)
            brutos.append(doc)

        self.materia_por_id = {m["id"]: m for m in materias.values()}
        self.materia_por_id["controle"] = {"id": "controle", "nome": "Controle da base",
                                           "sigla": "CTRL", "cor": "ctrl"}
        brutos.sort(key=lambda d: d["_ordem"])
        for d in brutos:
            (self.controle if d["materia"] == "controle" else self.docs).append(d)
            self.por_caminho[d["caminho"]] = d
            self.por_nome.setdefault(posixpath.basename(d["caminho"]), []).append(d)
            self.por_pasta.setdefault(d["pasta"], []).append(d)

        vistas = []
        for d in self.docs:
            if d["materia"] not in vistas:
                vistas.append(d["materia"])
        for mid in vistas:
            m = dict(self.materia_por_id[mid])
            assuntos: list[dict] = []
            for d in (x for x in self.docs if x["materia"] == mid):
                if not assuntos or assuntos[-1]["pasta"] != d["pasta"]:
                    assuntos.append({"pasta": d["pasta"], "num": d["assuntoNum"],
                                     "nome": d["assuntoNome"], "temas": []})
                assuntos[-1]["temas"].append(d["id"])
            m["assuntos"] = [{k: a[k] for k in ("num", "nome", "temas")} for a in assuntos]
            self.materias.append(m)

    # -- renderização e checagens
    def renderizar(self) -> dict:
        indice, pegadinhas, saida = [], [], {}
        todos = self.docs + self.controle
        for d in todos:
            r = Renderizador(self, d)
            corpo = r.blocos(ler_blocos(d["md"].splitlines()))
            resumo = Renderizador(self, d).inline(d["resumo_md"], False) if d["resumo_md"] else ""
            d.update(html=corpo, toc=r.toc, palavras=r.palavras, resumo=resumo,
                     titulo=r.titulo or d["titulo"])
            indice.extend(r.indice)
            if d["materia"] != "controle":
                pegadinhas.extend(r.pegadinhas)
        for e in indice:
            vazou = re.search(r"\*\*|`|\|\s*-{3,}|\]\(|^#{1,6}\s", e[3])
            if vazou:
                d = next(x for x in todos if x["id"] == e[0])
                self.aviso(d, f"marcação markdown não convertida ({vazou.group(0)!r}): "
                              f"{e[3][:70]}")
        ordem = [d["id"] for d in self.docs]
        for d in todos:
            citantes = self.citado_em.get(d["id"], set())
            saida[d["id"]] = {
                "titulo": d["titulo"], "materia": d["materia"], "assunto": d["assuntoNome"],
                "num": d["assuntoNum"], "resumo": d["resumo"], "status": d["status"],
                "caminho": d["caminho"], "palavras": d["palavras"], "toc": d["toc"],
                "citadoEm": [x for x in ordem if x in citantes], "html": d["html"],
            }
        return {
            "meta": {"versao": self.versao, "data": self.data,
                     "gerado": datetime.now().strftime("%d/%m/%Y %H:%M")},
            "materias": self.materias,
            "controle": dict(self.materia_por_id["controle"],
                             temas=[d["id"] for d in self.controle]),
            "ordem": ordem,
            "docs": saida,
            "indice": indice,
            "pegadinhas": pegadinhas,
        }


# ----------------------------------------------------------------------------- saída

DESCRICAO = ("Base de estudos para Auditor Fiscal: matérias, temas, busca em todo o material "
             "e pegadinhas CEBRASPE.")
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


class Manipulador(http.server.SimpleHTTPRequestHandler):
    """Serve a pasta site/ sem cache: a página regenerada aparece ao recarregar."""

    def end_headers(self) -> None:
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()


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
    base = Base()
    base.carregar()
    dados = base.renderizar()
    n_temas, n_ctrl = len(base.docs), len(base.controle)
    tipos = {}
    for p in dados["pegadinhas"]:
        tipos[p["v"] or "obs"] = tipos.get(p["v"] or "obs", 0) + 1
    print(f"Base {base.versao} ({base.data}): {len(base.materias)} matérias, {n_temas} temas "
          f"e {n_ctrl} arquivos de controle")
    print(f"Índice de busca: {len(dados['indice'])} trechos · Pegadinhas: "
          f"{len(dados['pegadinhas'])} (E {tipos.get('E', 0)}, C {tipos.get('C', 0)}, "
          f"observações {tipos.get('obs', 0)})")
    verificar = "--verificar" in argv
    if not verificar:
        site, pagina_privada = montar_paginas(dados)
        escrever(SAIDA_SITE, site)
        escrever(SAIDA_PAGINA_PRIVADA, pagina_privada)
        print(f"Gerado: {SAIDA_SITE.relative_to(RAIZ).as_posix()} "
              f"({len(site.encode('utf-8')) // 1024} KB) e "
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
