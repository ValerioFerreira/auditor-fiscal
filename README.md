# Estudos — Auditor Fiscal

Base de conhecimento para o concurso de Auditor Fiscal (banca de referência: CEBRASPE) e o site de leitura gerado a partir dela.

## Organização

| Pasta ou arquivo | O que é |
| --- | --- |
| `ESTUDOS/` | A base: uma pasta por matéria, temas em Markdown e `_CONTROLE/` (diário, assuntos, pendências e alterações) |
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
