# Estudos — Auditor Fiscal

Base de conhecimento para o concurso de Auditor Fiscal e o site de leitura gerado a partir dela.

## Organização

| Pasta ou arquivo | O que é |
| --- | --- |
| `ESTUDOS/` | A base: uma pasta por matéria, temas em Markdown (cada um termina com o seu mapa mental) e `_CONTROLE/` (diário, assuntos, pendências e alterações) |
| `ESTUDOS/<matéria>/Questões Turbo/` | As questões de Certo ou Errado de cada tema (um arquivo por tema, com o mesmo nome) |
| `ESTUDOS/<matéria>/Resumo Sintético/` | As partes do seu resumo sintético (`01 - AAAA-MM-DD.md` ou `.txt`, `02 - ...`); o site as junta na ordem, sem alterar o texto, e só refaz a numeração dos títulos em sequência |
| `ENTRADA/` | Onde entram os resumos novos (fora do git; ver `ENTRADA/LEIA-ME.txt`) |
| `sistema/` | O gerador do site (`gerar.py`) e a interface (`modelo.html`) |
| `site/` | O site gerado (`index.html`), recriado a cada geração (fora do git) |
| `edicoes-anteriores/` | Cópia de cada arquivo antes de uma edição feita pelo site, com data e hora no nome (fora do git) |
| `vercel.json` e `.vercelignore` | Configuração do deploy na Vercel |
| `CLAUDE.md` | As regras que o Claude segue para manter a base |
| `.claude/agents/` e `.claude/questoes/` | Os agentes que fazem as questões turbo de cada matéria, as instruções comuns e o guia de como a banca cobra cada disciplina |

## Ver no computador

```bash
python sistema/gerar.py --servir
```

Gera o site e o serve em http://localhost:8765/ (Ctrl+C para parar). Sem servidor, dá para abrir `site/index.html` com dois cliques.

## O que o site oferece

- **Início:** um card por disciplina (o card inteiro abre a página dela), com a data da última leitura (o último Lido que você marcou) e o progresso de leitura. Dá para ordenar pela última leitura, para ver o que está há mais tempo sem revisão.
- **Página da disciplina:** a Visão geral destaca o resumo geral (com a porcentagem lida e o botão para continuar), ao lado dos resumos por tópico e do resumo sintético, com os mapas mentais e as marcações embaixo. As abas ficam numa faixa fixa logo abaixo da busca, e só o conteúdo muda: resumo geral (todos os tópicos em sequência, dividido em páginas), resumos por tópico, mapa mental geral, mapas por tópico (cada ramo leva ao trecho do resumo), resumo sintético e marcações.
- **Questões turbo:** em cada disciplina (aba própria e card na Visão geral), questões de Certo ou Errado feitas a partir dos tópicos, com selo de dificuldade. Escolha a ordem (por assunto, na ordem do material, ou aleatória) e filtre por tópico, dificuldade, erradas ou favoritas. Primeiro aparecem só as inéditas; depois de fazer todas, elas voltam para revisão, começando pelas que você errou, e cada resposta atualiza o "Acertou/Errou". Depois de responder, aparecem o comentário e o botão "Ver no resumo", que abre o trecho do tópico. O placar mostra respostas, acertos, fixação (acertou na última vez) e o desempenho por tópico. "Reportar" guarda a sua dúvida sobre a questão; com o `--servir`, ela também vai para `ENTRADA/questoes-relatadas.md`, para ser conferida na sessão seguinte.
- **Resumo sintético:** com o site aberto pelo `python sistema/gerar.py --servir`, a aba "Resumo sintético" de cada disciplina recebe uma parte nova: um arquivo .docx (mantém negrito, tabelas e imagens) ou texto colado. "Salvar e juntar" grava a parte, sem alterar o conteúdo, e atualiza o site; na exibição, só a numeração dos títulos é refeita em sequência. Na Vercel e na página privada o site é só leitura.
- **Leitura:** texto justificado, em Manrope (em Aa dá para trocar pela serifada Literata), ocupando por padrão metade da largura da tela (nunca menos que uma folha A4). O controle "Largura do texto", no painel Aa do topo, aumenta ou diminui a coluna; "Padrão" (ou dois cliques no controle) volta ao início. Tabelas marcadas com filtros (como a de 71 contas de Contabilidade) ganham filtros por coluna e uma busca. Botão Lido em cada tópico; no resumo geral, "Marcar lido" pergunta até qual página você leu e mostra a porcentagem. Marca-texto em 4 cores: selecione um trecho e escolha a cor.
- **Edição (administrador):** o botão **Entrar**, no canto superior direito, abre o login de administrador. Ele não é obrigatório: a leitura continua aberta para todos. Com o site aberto pelo `python sistema/gerar.py --servir` e o login feito, aparecem os botões **Editar** nos tópicos, no resumo geral e em cada parte do resumo sintético. O editor tem desfazer e refazer, estilos de parágrafo (títulos, nota, bloco de código), negrito, itálico, sublinhado, código, listas com recuo, tabelas (linhas, colunas, alinhamento e largura das colunas, arrastando a borda) e imagens (botão, colar ou arrastar; clique na imagem para mudar a largura). "Salvar" grava no arquivo `.md` só os blocos alterados, confere que nenhuma palavra se perdeu, guarda a versão anterior em `edicoes-anteriores/` (fora do git) e atualiza o site. Na Vercel, na página privada e no duplo clique o site continua só leitura.
- **Onde ficam suas marcações:** no navegador em que você lê (inclusive as respostas das questões turbo). Computador, celular, localhost e Vercel guardam cada um as suas. Para levar de um para outro, use Aa → Exportar e, no outro, Aa → Importar.

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
