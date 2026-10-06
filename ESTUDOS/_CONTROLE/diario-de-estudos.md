# Diário de Estudos

> Versão atual da base: **v012** (05/10/2026)

## 26/09/2026 — Carga inicial (v001)

- **Origem:** arquivo "Resumos - Auditor Fiscal.docx" (resumos acumulados; as datas originais de cada sessão não foram informadas).
- **Matérias:** Direito Tributário · Contabilidade Geral e Avançada · Direito Constitucional · Direito Administrativo.

### Direito Tributário
- Fundamentos (receitas originárias x derivadas; status do CTN); conceito de tributo (art. 3º); natureza jurídica e classificação; teorias das espécies; impostos; taxas (serviço e polícia, base de cálculo, taxa x tarifa); contribuição de melhoria; empréstimo compulsório; contribuições especiais (CIDE, corporativas, COSIP); contribuições sociais e previdenciárias (seguridade, RGPS x RPPS, EC 103/2019).
- **Principais enriquecimentos:** jurisprudência atualizada sobre taxas (Tema 1.282 — bombeiros estaduais; ADPFs 512, 1.028 e 1.029; ADI 6.145; Temas 16, 217 e 919); SVs 19, 29 e 41; exceções à legalidade para alíquotas; distinção entre as três "vinculações"; transição da Reforma Tributária (CBS, extinção de PIS/COFINS em 2027); COSIP no CTN (art. 82-A, LC 227/2026).

### Contabilidade Geral e Avançada
- Noções introdutórias (objeto, objetivo, finalidade, funções, técnicas, usuários, CPC 00); patrimônio (ativo, passivo, PL, equação, situações líquidas); capital; contas e partidas dobradas; plano de contas; teorias das contas.
- **Principais enriquecimentos:** definições da CPC 00 (R2); agrupamento de contas (Lei 6.404, art. 176, §2º); capital a integralizar como redutora do PL (art. 182).

### Direito Constitucional
- Concepções da constituição; conceito ideal; estrutura (preâmbulo, parte dogmática, ADCT); elementos; supremacia; classificações (com quadro da CF/88); eficácia e aplicabilidade; regras x princípios; hierarquia das normas; gerações dos direitos fundamentais.
- **Principais enriquecimentos:** exemplos de cada tipo de eficácia; ADI 815 (Bachof), ADI 2.076 (preâmbulo), RE 466.343 (supralegalidade); terceiro tratado com status de EC; decreto autônomo (art. 84, VI).

### Direito Administrativo
- Regime jurídico administrativo; administração direta e indireta (órgãos, entidades); princípios expressos (LIMPE) e implícitos.
- **Principais enriquecimentos:** Lei 9.784/99 (art. 2º, delegação/avocação, motivação, anulação e decadência); SVs 3, 5, 13 e 21; greve de servidor (MIs, RE 693.456, ARE 654.432); encampação x caducidade; devolução de valores recebidos de boa-fé (STJ, Temas 531 e 1.009).

## 27/09/2026 — Respostas às pendências e organização (v002)

- **Sem conteúdo novo de estudo.**
- **Pendências 🔴 resolvidas:** as quatro da carga inicial (duas afirmações desconsideradas, uma reescrita confirmada e uma correção mantida).
- **Reorganização:** três sobreposições consolidadas, sem perda de conteúdo (finalidade das contribuições especiais; tutela; constituição dúctil).
- **Organização:** criado o sistema web de leitura da base (`site/index.html`, com cópia numa página privada), pronto para publicar na Vercel.
- **Fluxo de trabalho:** novos resumos entram pela pasta `ENTRADA/` ou pelo chat; commit ao fim de cada sessão; pendência 🟡 "Persistência da base" resolvida (base em disco, com git).

## 28/09/2026 — Mapas mentais e página de cada disciplina (v003)

- **Sem conteúdo novo de estudo:** a data do último resumo de cada matéria continua a de 26/09/2026.
- **Mapas mentais:** cada tema ganhou a seção "Mapa mental" (25 mapas, 554 ramos), feita só com o conteúdo do próprio tema. O sistema junta os mapas de cada matéria num mapa geral e liga cada ramo ao trecho do resumo.
- **Resumo sintético:** criada a pasta `Resumo Sintético` em cada matéria, para os seus resumos sintéticos numerados (01, 02, 03...), que o sistema junta na ordem, sem alterar o texto.
- **Sistema de leitura:** página própria para cada disciplina (resumo geral dividido em páginas, resumos por tópico, mapa mental geral e por tópico, resumo sintético e marcações), botão Lido, porcentagem de leitura do resumo geral, marca-texto em 4 cores e ordenação das disciplinas pela data do último resumo.
- **Resumo sintético pelo site:** com o site aberto no computador (`python sistema/gerar.py --servir`), a aba "Resumo sintético" recebe cada parte nova, que é salva sem alteração na pasta da matéria. No site, só a numeração dos itens é refeita, em sequência única na matéria inteira.
- **Primeiro resumo sintético:** o arquivo "01 - Sintético.docx", com as quatro matérias misturadas, foi separado pelos títulos de disciplina e salvo como a parte 01 de cada uma (em Markdown, com a mesma formatação e a imagem da pirâmide das normas), sem alteração no conteúdo. Na exibição, os títulos numerados passam a seguir em sequência: Tributário 1 a 24, Contabilidade 1 a 4, Constitucional 1 a 10 (o título repetido "Classificação das Constituições" virou continuação: 7.1 a 7.8); Administrativo já estava em ordem. As próximas partes podem ser enviadas em .docx pela aba "Resumo sintético" do site.

## 29/09/2026 — Ajustes no site (v004)

- **Sem conteúdo novo de estudo.**
- **Leitura:** o texto dos resumos ficou justificado e ocupa por padrão pelo menos 50% da largura da tela (nunca menos que uma folha A4). O controle "Largura do texto", no rodapé das páginas de leitura, logo acima do contador de páginas, aumenta ou diminui a coluna.
- **Menu da disciplina:** as abas (Visão geral, Resumo geral...) ficam numa faixa fixa logo abaixo da busca, sempre no mesmo lugar; só o conteúdo abaixo muda. A busca fica sempre centralizada no topo.
- **Última leitura:** os cards das disciplinas, a ordenação, o menu lateral e a página da disciplina mostram a data do último Lido marcado (tópico ou resumo geral), no lugar da data do último resumo.
- **Versão da base:** deixou de aparecer no site (fica só aqui e em `assuntos-estudados.md`).
- **Login de administrador e editor:** botão "Entrar" no canto superior direito (não obrigatório). Com o site aberto por `python sistema/gerar.py --servir` e o login feito, os tópicos e as partes do resumo sintético podem ser editados no próprio site (texto, títulos, listas, tabelas com largura de colunas, imagens). Só os blocos alterados são regravados no arquivo; a versão anterior fica em `edicoes-anteriores/` (fora do git).

## 30/09/2026 — Resumos de 29/09/2026 e redesign do site (v005)

- **Origem:** arquivo "29_09_26 - Resumos - Auditor Fiscal.docx" (estudo de 29/09/2026), com Direito Tributário, Contabilidade e Direito Constitucional. A seção de Direito Administrativo veio vazia (ver `pendencias.md`).

### Direito Tributário (estudo de 29/09/2026)
- Contribuições residuais x nominadas; PIS/COFINS não residuais (LC 70/1991 materialmente ordinária); contribuições sociais gerais (salário-educação e Sistema S); FGTS (não é tributo); CIDEs (combustíveis, AFRMM, SEBRAE, CIDE-Royalties, INCRA); contribuições corporativas, OAB e contribuições sindicais; contribuição estadual transitória do art. 136 do ADCT; competência residual de impostos e papel da LC (art. 146, III, "a"); classificações por finalidade, repercussão e alíquotas.
- **Principais enriquecimentos:** EC 132/2023 (CIDE-combustíveis para tarifas de transporte público; art. 136 do ADCT); STF, RE 228.321, RE 396.266, Temas 325, 495, 540, 732 e 935, ADI 3.026, ADI 5.794, ADC 1 e RE 377.457; Súmulas 353 e 516 do STJ; SV 40; CTN, art. 166 (restituição de tributo indireto); ADIs 1.145 e 3.643 (destinação de custas e emolumentos).

### Contabilidade Geral e Avançada (estudo de 29/09/2026)
- Novo tópico com a tabela de 71 contas (classificação, natureza e porquê), com filtros por classificação e natureza no site; dicas pelo nome da conta; atos e fatos administrativos (permutativos, modificativos e mistos, com lançamentos).
- **Principais enriquecimentos:** CMV como custo; PECLD (nome atual da "provisão para perdas"); duplicatas descontadas como passivo; empréstimos a dirigentes no RLP (Lei 6.404, art. 179, II); lucros acumulados nas S.A.; desconto condicional x incondicional.

### Direito Constitucional (estudo de 29/09/2026)
- Poder constituinte: teoria (Sieyès), titularidade e exercício, originário (características, classificações e divergência sobre limites), derivado reformador (limitações do art. 60), decorrente, revisor, difuso (mutação constitucional) e supranacional.
- **Principais enriquecimentos:** ADI 815, ADI 939 (anterioridade tributária como cláusula pétrea), ADI 2.024 (núcleo essencial), ADI 4.277/ADPF 132, SV 25; EC 26/1985; ECR 1 a 6/1994; natureza da Lei Orgânica do DF.

- **Site:** tabela de contas com filtros; a seção "Controle da base" deixou de aparecer; a página inicial perdeu a saudação e o subtítulo; o controle de largura do texto passou para o painel Aa; redesign de todo o site (fonte Manrope, tema escuro neutro, cards reorganizados na página de cada disciplina, novos ícones e transições).

## 30/09/2026 — Questões turbo (v006)

- **Sem conteúdo novo de estudo.**
- **Questões turbo:** 708 questões de Certo ou Errado sobre os 28 temas (Tributário 218, Contabilidade 151, Constitucional 200, Administrativo 139), com selo de dificuldade, comentário e link para a seção do tema; entre 48% e 53% de itens certos em cada matéria. Feitas por um agente por matéria (`.claude/agents/`), com base num guia de como a banca cobra cada disciplina (pesquisa na web, `.claude/questoes/guias/`). O gerador guarda a cobertura de cada seção, para que as próximas questões partam só do texto novo (`--questoes-pendentes`).
- **Base:** ⚠️ no nepotismo em cargos políticos (STF, Tema 1.000, em julgamento); divergência sobre o direito à paz (3ª dimensão x 5ª, Bonavides).
- **Site:** aba e card "Questões turbo" em cada disciplina (ordem por assunto ou aleatória, inéditas primeiro e depois revisão pelas erradas, filtros, favoritas, relatos e desempenho por tópico); o nome da banca não aparece mais no site.

## 30/09/2026 — Login com Google e questões sempre C/E (v007)

- **Sem conteúdo novo de estudo.**
- **Questões turbo:** decidido que continuam só de Certo ou Errado; se os agentes encontrarem questões de múltipla escolha na pesquisa, usam-nas como base para entender como a banca cobra o assunto e as adaptam a C/E (instruções comuns dos agentes de questões).
- **Site:** login com Google para qualquer leitor (leituras, marca-texto, favoritos e respostas das questões ficam na conta e sincronizam entre aparelhos; a edição de textos segue exclusiva do administrador). Precisa ser configurado (Google Cloud + Neon): ver README, "Login com Google", e `sistema/neon.sql`.

## 01/10/2026 — Missão Fiscal: perfil, comentários, downloads e menos texto (v008)

- Sessão de sistema (sem estudo novo). O site passou a se chamar **Missão Fiscal**; "turbo" saiu do que o site mostra.
- Novo modal de login (cartão estreito), menu da conta, página de **Perfil** e **Baixar conteúdo** em DOCX e PDF.
- **Comentários** nos textos (menu Marca-texto / Comentar ao selecionar) e **Marcar lido** por páginas ou tópicos no resumo geral, sem o bloco "Leitura" do topo.
- Topo com **Questões** (página com as disciplinas e as Pegadinhas) e **Aparência** (antes "Aa"); abas da disciplina com menus Resumos e Mapas mentais.
- Textos explicativos trocados por ícone ⓘ com balão.

## 03/10/2026 — Editar no próprio resumo geral e regras do resumo geral (v009)

- Sessão de sistema (sem estudo novo). O botão **Editar** do resumo geral agora abre o editor no lugar do texto do tema, sem levar ao tópico; ao salvar, a página volta ao mesmo ponto, e a mudança vale também em Por tópico.
- Regras registradas no CLAUDE.md: o resumo geral mostra o texto de cada tema por extenso (links são só acréscimo) e o enriquecimento dos resumos é aditivo, sem descaracterizar o que foi marcado como importante.
- Edição sua pelo site em *Conceito e Concepções* (Estado = povo, território e governo; Lassalle; Kelsen) incorporada como está; **6 questões turbo novas** (Q022 a Q027) cobrem o texto novo.
- **Ajustes pedidos por você no mesmo dia:** em *Conceito e Concepções*, o terceiro elemento do Estado passou a "governo soberano" (com as variações *poder* e *soberania*) e a célula de Lassalle foi reescrita (real/efetiva x escrita); mapa mental e questões acompanharam (Q028 e Q029 novas; Q022 a Q024 ajustadas). Pendência 🔴 resolvida.
- **Resumo sintético, parte 02 (enviada em 03/10/2026):** o arquivo "Sintético.docx", com quatro matérias misturadas, foi separado pelos títulos de disciplina e salvo, sem alteração de texto, como a **parte 02** de cada uma (`02 - 2026-10-03`): Direito Constitucional (Princípios Fundamentais), Direito Administrativo (conceito, objeto, critérios e mudanças recentes), Contabilidade Geral e Avançada (escrituração, livros e balancete, com 2 imagens) e Direito Tributário (legalidade, exceções, o que não é majorar, LC x MP). Os títulos "DIREITO ADMINISTRATIVO", "CONTABILIDADE" e "TRIBUTÁRIO" foram associados às matérias já existentes.
- **Resumo sintético, numeração na exibição:** continua a das partes 01 (Constitucional 11; Administrativo 6 a 11; Contabilidade 5 e 6; Tributário 25 a 28). Ajuste no gerador: itens de lista do Word que são títulos entram na sequência e o 3º nível (`5.1.1`) acompanha o subnível.
- **Botão Editar na barra inferior do resumo geral (pedido seu):** abre o tema que está na tela e posiciona o editor no bloco que estava sendo lido; só aparece para o administrador.

## 04/10/2026 — Editar no menu do trecho selecionado (v010)

- Sessão de sistema (sem estudo novo). O menu que aparece ao selecionar um trecho (Marca-texto, Comentar) ganhou **Editar**, só para o administrador: abre o editor do tema (no resumo geral, no tópico) ou da parte do resumo sintético, com o cursor no começo do trecho selecionado.

## 04/10/2026 — Resumos de 04/10/2026 (v011)

- **Origem:** arquivo "04_10_26 - Resumos - Auditor Fiscal.docx", com quatro títulos de matéria: Direito Tributário (sem conteúdo), Contabilidade Geral e Avançada, Direito Constitucional e Direito Administrativo.
- **Organização:** nova pasta `05 - Escrituração` em Contabilidade; em Constitucional, `02 - Princípios Fundamentais` (a antiga 02 passou a `03 - Direitos e Garantias Fundamentais`); em Administrativo, `00 - Introdução ao Direito Administrativo`, sem renumerar as demais, para não alterar temas já lidos.

### Contabilidade Geral e Avançada
- Escrituração contábil e livros (Diário, Razão, Caixa, razonete; livros da S.A.; formalidades intrínsecas e extrínsecas); lançamentos (elementos, processo manual x mecanizado, fórmulas) e retificação (estorno, transferência e complementação).
- **Principais enriquecimentos:** obrigatoriedade e dispensa (CC, arts. 1.179 e 1.180; ITG 2000 (R1), item 2; MEI até R$ 81.000); Razão conforme o referencial (comercial, IR e ITG); art. 100 da Lei 6.404/1976 conferido (o "se houver" é só do Conselho de Administração; substituição por registros eletrônicos, §§2º e 3º); escrituração resumida (CC, art. 1.184); Livro Caixa no lucro presumido (Lei 8.981/1995, art. 45); conteúdo mínimo do registro e retificação conforme a ITG 2000 (R1); quadro de erros e retificações típicas.

### Direito Constitucional
- Princípios Fundamentais (Título I): fundamentos (art. 1º), forma de Estado (federação), forma de governo (república), regime político (democracia), Estado Democrático de Direito, separação dos Poderes (art. 2º), objetivos (art. 3º) e princípios nas relações internacionais (art. 4º).
- **Principais enriquecimentos:** oito princípios do Estado Democrático de Direito (José Afonso da Silva) e sua divergência com a visão de simples soma; soberania x autonomia (arts. 18, 21, I, e 52, V); federalismo (terceiro grau, centrífugo, cooperativo); forma x sistema de governo (ADCT, art. 2º); instrumentos da democracia semidireta (art. 14, art. 61, §2º, Lei 9.709/1998); funções típicas e atípicas dos Poderes, com exemplos.

### Direito Administrativo
- Conceito, escolas e objeto do Direito Administrativo: origem francesa, conceito, função administrativa, escolas das prerrogativas públicas e do serviço público.
- **Principais enriquecimentos:** contencioso administrativo (França) x jurisdição una (CF, art. 5º, XXXV); função administrativa como aplicação da lei de ofício; os demais critérios para conceituar o Direito Administrativo; autores das escolas.

### Direito Tributário
- O título veio sem conteúdo abaixo (pendência 🔴).

- **Questões turbo:** 166 novas (Contabilidade 68, Constitucional 74, Administrativo 24), no total de 882 na base.

## 05/10/2026 — Decisões sobre os resumos de 04/10/2026 e novos recursos do site (v012)

- **Decisões suas:** as pastas de Direito Administrativo foram renumeradas (`01 - Introdução ao Direito Administrativo`, `02 - Regime Jurídico Administrativo`, `03 - Organização Administrativa`, `04 - Princípios da Administração Pública`), com as referências cruzadas ajustadas (os quatro temas que tinham referência a pastas aparecem como "mudou" nas leituras); os adendos ao Livro Razão (três referenciais) foram aprovados; o teto do MEI ficou em R$ 81.000, com ressalva entre parênteses sobre os projetos de lei complementar em tramitação.
- **Modo E-book (pedido seu):** novo modo em Aparência, com papel de tom quente (Papel, Sépia e Noite), letra serifada, coluna estreita centralizada, margens largas, contraste e brilho baixos.
