# Estudos — Auditor Fiscal

Base de conhecimento para o concurso de Auditor Fiscal (banca de referência: CEBRASPE) e o site de leitura gerado a partir dela.

## Organização

| Pasta ou arquivo | O que é |
| --- | --- |
| `ESTUDOS/` | A base: uma pasta por matéria, temas em Markdown (cada um termina com o seu mapa mental) e `_CONTROLE/` (diário, assuntos, pendências e alterações) |
| `ESTUDOS/<matéria>/Resumo Sintético/` | Seus resumos sintéticos, numerados (`01 - ...`, `02 - ...`), em .txt ou .md; o site os junta na ordem, sem alterar o texto |
| `ENTRADA/` | Onde entram os resumos novos (fora do git; ver `ENTRADA/LEIA-ME.txt`) |
| `sistema/` | O gerador do site (`gerar.py`) e a interface (`modelo.html`) |
| `site/` | O site gerado (`index.html`), recriado a cada geração (fora do git) |
| `vercel.json` e `.vercelignore` | Configuração do deploy na Vercel |
| `CLAUDE.md` | As regras que o Claude segue para manter a base |

## Ver no computador

```bash
python sistema/gerar.py --servir
```

Gera o site e o serve em http://localhost:8765/ (Ctrl+C para parar). Sem servidor, dá para abrir `site/index.html` com dois cliques.

## O que o site oferece

- **Início:** as disciplinas lado a lado, cada uma com a data do último resumo, o progresso de leitura e o botão para abrir a página dela. Dá para ordenar pela data do último resumo, para ver o que está há mais tempo sem revisão.
- **Página da disciplina:** resumo geral (todos os tópicos em sequência, dividido em páginas), resumos por tópico, mapa mental geral, mapas por tópico (cada ramo leva ao trecho do resumo), resumo sintético e marcações.
- **Leitura:** botão Lido em cada tópico; no resumo geral, "Marcar lido" pergunta até qual página você leu e mostra a porcentagem. Marca-texto em 4 cores: selecione um trecho e escolha a cor.
- **Onde ficam suas marcações:** no navegador em que você lê. Computador, celular, localhost e Vercel guardam cada um as suas. Para levar de um para outro, use Aa → Exportar e, no outro, Aa → Importar.

## Publicar na Vercel

O deploy já está configurado: a Vercel roda `python3 sistema/gerar.py` e publica só a pasta `site/`. Sobem apenas `ESTUDOS/` e `sistema/`; os resumos brutos de `ENTRADA/` e os arquivos `.zip`/`.docx` ficam no computador.

**Pela linha de comando (sem GitHub)**, na pasta do projeto:

```bash
npx vercel login
```

```bash
npx vercel --prod
```

Na primeira vez, a CLI pergunta como criar o projeto. As respostas padrão servem, porque as configurações vêm do `vercel.json`. Para atualizar o site depois, repita `npx vercel --prod`.

**Pelo GitHub (atualiza sozinho a cada envio):** crie um repositório privado, envie este projeto (`git push`) e importe-o em https://vercel.com/new, sem mudar nenhuma configuração.

**Privacidade:** o endereço de produção fica aberto a quem tiver o link (o site pede aos buscadores para não indexá-lo). Para que só você acesse, ative no projeto da Vercel: Settings → Deployment Protection → Vercel Authentication, com o escopo "All Deployments" (sem custo em nenhum plano). O site passa a pedir login na Vercel.
