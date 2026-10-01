# Missão Fiscal

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
- **Questões:** em cada disciplina (aba própria e card na Visão geral; o link **Questões** do topo reúne as disciplinas e as Pegadinhas), questões de Certo ou Errado feitas a partir dos tópicos, com selo de dificuldade. Escolha a ordem (por assunto, na ordem do material, ou aleatória) e filtre por tópico, dificuldade, erradas ou favoritas. Primeiro aparecem só as inéditas; depois de fazer todas, elas voltam para revisão, começando pelas que você errou, e cada resposta atualiza o "Acertou/Errou". Depois de responder, aparecem o comentário e o botão "Ver no resumo", que abre o trecho do tópico. O placar mostra respostas, acertos, fixação (acertou na última vez) e o desempenho por tópico. "Reportar" guarda a sua dúvida sobre a questão; com o `--servir`, ela também vai para `ENTRADA/questoes-relatadas.md`, para ser conferida na sessão seguinte.
- **Resumo sintético:** com o site aberto pelo `python sistema/gerar.py --servir`, a aba "Resumo sintético" de cada disciplina recebe uma parte nova: um arquivo .docx (mantém negrito, tabelas e imagens) ou texto colado. "Salvar e juntar" grava a parte, sem alterar o conteúdo, e atualiza o site; na exibição, só a numeração dos títulos é refeita em sequência. Na Vercel e na página privada o site é só leitura.
- **Leitura:** texto justificado, em Manrope (em Aparência dá para trocar pela serifada Literata), ocupando por padrão metade da largura da tela (nunca menos que uma folha A4). O controle "Largura do texto", no painel Aparência do topo, aumenta ou diminui a coluna; "Padrão" (ou dois cliques no controle) volta ao início. Tabelas marcadas com filtros (como a de 71 contas de Contabilidade) ganham filtros por coluna e uma busca. Botão Lido em cada tópico; no resumo geral, "Marcar lido" (barra do canto inferior esquerdo) marca páginas de uma a outra ou tópicos inteiros e mostra a porcentagem. Ao selecionar um trecho, escolha **Marca-texto** (4 cores) ou **Comentar** (uma nota presa ao trecho, privada e sincronizada com a conta). Marcações e comentários ficam na aba Marcações.
- **Edição (administrador):** o botão **Entrar**, no canto superior direito, abre o login de administrador. Ele não é obrigatório: a leitura continua aberta para todos. Com o site aberto pelo `python sistema/gerar.py --servir` e o login feito, aparecem os botões **Editar** nos tópicos, no resumo geral e em cada parte do resumo sintético. O editor tem desfazer e refazer, estilos de parágrafo (títulos, nota, bloco de código), negrito, itálico, sublinhado, código, listas com recuo, tabelas (linhas, colunas, alinhamento e largura das colunas, arrastando a borda) e imagens (botão, colar ou arrastar; clique na imagem para mudar a largura). "Salvar" grava no arquivo `.md` só os blocos alterados, confere que nenhuma palavra se perdeu, guarda a versão anterior em `edicoes-anteriores/` (fora do git) e atualiza o site. Na Vercel, na página privada e no duplo clique o site continua só leitura.
- **Onde ficam suas marcações:** no navegador em que você lê (inclusive as respostas das questões e os comentários). Computador, celular, localhost e Vercel guardam cada um as suas. Para levar de um para outro, use Aparência → Exportar e, no outro, Aparência → Importar (quem está logado tem a cópia em Perfil → Dados); ou entre com o Google (ver "Login com Google"), e elas acompanham a sua conta.
- **Perfil e downloads:** logado, o menu do topo leva ao **Perfil** (ritmo de estudo, progresso por disciplina, questões, marcações e dados). Em **Baixar conteúdo** (início, Visão geral, menu e Perfil), o material sai em **DOCX** (gerado no navegador) ou **PDF** (impressão do navegador, "Salvar como PDF"), com resumos, sintético, mapas mentais, questões e comentários à escolha. Na página privada o navegador bloqueia downloads e impressão.
- **Login com Google (qualquer leitor):** o botão **Entrar** oferece o login com a conta Google. Não é obrigatório. Quem entra tem leituras, marca-texto, favoritos e respostas das questões guardados na própria conta e sincronizados entre aparelhos; só a edição de textos continua exclusiva do administrador (login ADM, acima). Precisa da configuração da seção "Login com Google"; sem ela, o botão só oferece o login de administrador.

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

## Login com Google (outros usuários)

O site é estático, então os dados de cada pessoa ficam num banco **Neon** (Postgres da Vercel), acessado direto do navegador pela Data API do Neon com o token do login do Google. O banco só deixa cada pessoa ler e gravar as próprias linhas (`sistema/neon.sql`). Não há servidor novo: nenhum segredo vai para o site. Só o **ID do cliente** do Google e o **endereço da Data API** entram no site, e os dois são públicos.

Passo a passo (feito uma vez, por você, porque exige as suas contas):

1. **Google Cloud Console** (https://console.cloud.google.com/apis/credentials): crie um projeto, configure a *tela de consentimento OAuth* (tipo Externo, nome do app, seu e-mail; os escopos padrão `openid`, `email` e `profile` não exigem verificação) e **publique** o app (em "Testando", só entram os usuários de teste). Em *Credenciais → Criar credenciais → ID do cliente OAuth → Aplicativo da Web*, acrescente em **Origens JavaScript autorizadas** o endereço do site na Vercel (ex.: `https://seu-projeto.vercel.app`) e `http://localhost:8765`. Não precisa de URI de redirecionamento. Copie o **ID do cliente** (termina em `.apps.googleusercontent.com`).
2. **Neon pela Vercel:** no projeto da Vercel, *Storage → Create Database → Neon*. No console do Neon, abra *Data API → Enable*. Em autenticação, escolha **Other provider** e preencha: JWKS URL `https://www.googleapis.com/oauth2/v3/certs` e JWT Audience = o ID do cliente do passo 1. Marque "Grant public schema access".
3. No *SQL Editor* do Neon, rode o conteúdo de `sistema/neon.sql` e, na página da Data API, clique em *Refresh schema cache*.
4. Na Data API, em *Settings*, libere o CORS para o endereço do site na Vercel e para `http://localhost:8765` (se a opção existir).
5. Copie o **API URL** da Data API (termina em `/rest/v1`) e crie `sistema/conta.json`:

   ```json
   {
     "cliente": "SEU-ID.apps.googleusercontent.com",
     "api": "https://ep-...apirest.....neon.tech/neondb/rest/v1"
   }
   ```

   (Alternativa: as variáveis `ESTUDOS_GOOGLE_CLIENT_ID` e `ESTUDOS_NEON_API` na Vercel.) Faça o commit e o `git push`.
6. **Vercel → Settings → Deployment Protection:** desligue a *Vercel Authentication* da produção; com ela ligada, só você (logado na Vercel) abre o site, e nenhum outro usuário chega até o login do Google.

Como funciona:

- O login só aparece onde o endereço está autorizado (Vercel e localhost); na página privada e no duplo clique ele avisa que não funciona.
- Ao entrar, o que já estava no navegador é somado ao que a conta tem. Depois, cada marcação, resposta ou favorito é enviado em poucos segundos. Uma mudança feita num aparelho (inclusive desmarcar uma leitura) chega aos outros na próxima abertura ou quando a aba volta ao primeiro plano.
- O token do Google vale cerca de 1 hora e é renovado sozinho; se não der, o botão do topo fica com um ponto vermelho e nada se perde (as alterações ficam no navegador e seguem no próximo login).
- **Sair** limpa as leituras e marcações daquele navegador (continuam na conta), para que o próximo usuário do mesmo computador não as veja.
- Dados guardados por pessoa: leituras, marca-texto, favoritos, respostas e relatos das questões, filtros e a última posição de leitura. Nome, e-mail e foto do Google ficam só no navegador.
