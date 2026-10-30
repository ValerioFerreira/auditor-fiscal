# Diário de Estudos

> Versão atual da base: **v015** (30/10/2026)

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

## 07/10/2026 — Resumos de 06/10/2026, ajustes pedidos nos temas e questões de múltipla escolha (v013)

- **Origem:** arquivo "06_10_26 - Resumos - Auditor Fiscal.docx", com quatro títulos de matéria: Direito Tributário, Contabilidade Geral e Avançada, Direito Constitucional (sem conteúdo abaixo; pendência 🔴) e Direito Administrativo.
- **Organização:** nova pasta `04 - Limitações ao Poder de Tributar` em Tributário (dois temas); em Contabilidade, dois temas novos em `05 - Escrituração`; em Administrativo, dois temas novos em `01 - Introdução ao Direito Administrativo`.
- **Ajustes pedidos por você:** quadro-resumo da CF/88 refeito em tabela; visão geral da hierarquia das normas transformada em **imagem da pirâmide de Kelsen** (modelo de três níveis mais difundido nos materiais, com os tratados de direitos humanos, os supralegais e a norma fundamental hipotética); Art. 4º com **quadro dos dez princípios** e mnemônico (IPA · NI · DS · RCA); **critérios para definição do Direito Administrativo** unidos numa tabela única (as duas escolas do resumo de 04/10 reescritas no mesmo padrão dos seis critérios novos, sem perda), com **imagem em balões** (critério, ideia central e crítica).

### Direito Tributário (estudo de 06/10/2026)
- Limitações ao poder de tributar (visão geral: lei complementar x emenda, cláusulas pétreas) e princípio da legalidade tributária (reserva de lei, lei delegada, medida provisória, exceções, jurisprudência).
- **Principais enriquecimentos:** CTN, art. 97 completo (com o inciso VI) e §§1º e 2º; CF, arts. 62, §§1º, III, e 2º, e 68, §1º; rol atual das matérias reservadas à LC (IBS, CBS e imposto seletivo, após a EC 132/2023); fundamentos das exceções (CF, arts. 153, §1º, 177, §4º, I, "b", e 155, §§4º e 5º); Súmula 160 do STJ; SV 50; Tema 829 do STF (RE 838.284); ADI 939 como paradigma das cláusulas pétreas tributárias.

### Contabilidade Geral e Avançada (estudo de 06/10/2026)
- Exemplos de escrituração (dezessete fatos, com lançamentos e classificação) e balancete de verificação (conceito, elementos mínimos, tipos por colunas, sintético e analítico).
- **Principais enriquecimentos:** valores calculados a partir dos dados (juros, descontos, custo da venda); lançamentos das três hipóteses de vencimento no desconto de duplicatas; o que o balancete não prova. **Correção:** na venda à vista, a receita é lançada a **crédito** (o resumo indicava débito).

### Direito Administrativo (estudo de 06/10/2026)
- Critérios para definição do Direito Administrativo (oito); direito administrativo brasileiro (formação, influências e tendências); fontes do direito administrativo.
- **Principais enriquecimentos:** leis de referência das tendências (Lei 13.848/2019, EC 19/1998 e Lei 13.140/2015); súmula vinculante e controle concentrado como fontes que vinculam a Administração (CF, arts. 102, §2º, e 103-A); papel dos costumes (suprem lacunas e não contrariam a lei).

### Direito Constitucional
- O título veio sem conteúdo abaixo (pendência 🔴); os ajustes pedidos foram feitos nos temas já existentes.

- **Questões turbo (Certo ou Errado):** 161 novas (Tributário 50, Contabilidade 52, Constitucional 19 e Administrativo 40), no total de 1.043 na base.
- **Questões de múltipla escolha (pedido seu):** nova funcionalidade. Quatro agentes, um por matéria (`questoes-multipla-<matéria>`), seguem as instruções comuns (instruções comuns em .claude/questoes) e o guia de estilo da CEBRASPE e da FGV de cada disciplina (pasta guias-me, pesquisa de 06/10/2026). **469 questões**: Tributário 124, Contabilidade 140, Constitucional 105 e Administrativo 100, metade em cada estilo de banca, com alternativas de A a E.
- **Site:** a aba **Questões** passou a montar um **caderno**: formato (Certo ou Errado, múltipla escolha ou ambas), estilo da banca (CEBRASPE, FGV ou ambas), quantidade (10, 20, 30, 50, 100, outro número ou todas) e tempo (sem tempo, cronômetro ou tempo limite). No fim, o resultado mostra o percentual de acerto, de erro e em branco, o tempo, os tópicos com mais acertos e mais erros, o desempenho por tipo de questão e as questões a rever, com a opção de refazer as erradas.

## 21/10/2026 — Resumos de 21/10/2026 e resumo sintético (v014)

- **Origem:** quatro arquivos de matéria (Tributário, Contabilidade, Constitucional e Administrativo) e o "Sintético (1).docx", com quatro disciplinas misturadas.
- **Resumo sintético:** o arquivo foi separado pelos títulos de disciplina ("Direito Constitucional", "DIREITO ADMINISTRATIVO", "CONTABILIDADE" e "TRIBUTÁRIO"), sem mudar o texto, e cada trecho virou a **parte 03** do sintético da matéria correspondente (`03 - 2026-10-21`; as cinco imagens de Contabilidade ficaram ao lado). "Contabilidade" e "Tributário" foram associados a Contabilidade Geral e Avançada e a Direito Tributário.
- **Organização:** nova pasta `06 - Demonstrações Contábeis` em Contabilidade (três temas); em Tributário, oito temas novos em `04 - Limitações ao Poder de Tributar`; em Constitucional, dois temas novos em `01 - Teoria da Constituição`, a teoria geral dos direitos fundamentais ampliada e um tema novo na mesma pasta; em Administrativo, `sistemas-administrativos` em `01` e dois temas novos em `03 - Organização Administrativa` (um deles com a sua imagem). Todos os temas foram ligados entre si, dentro e fora da matéria.

### Direito Tributário (estudo de 21/10/2026)
- Isonomia; capacidade contributiva (progressividade, Súmulas 656 e 668, EC 132, sigilo bancário); vedação ao confisco e multas; irretroatividade e hipótese de incidência; anterioridade e noventena (com medidas provisórias e o quadro-resumo com a legalidade); liberdade de tráfego e princípios federativos; transparência, segurança jurídica e princípios da EC 132; imunidades (conceito e classificações).
- **Principais enriquecimentos:** CF, art. 145 (§§1º, 3º e 4º), 150 (II, III, IV, V, §5º), 151, 152, 153 (§4º), 155 (§1º, VI, e §6º, II), 156 (§1º), 182 (§4º), 195 (§§6º e 9º) e 237; CTN, arts. 104, 106, 113-A, 175 e 206; **LC 236/2026** (novo art. 113-A do CTN: multas de 75%, 100% e 150%) conferida no Planalto; LC 105/2001 e a constitucionalidade do acesso do Fisco a dados bancários; Súmula 584 (superada); lista do art. 150, VI.

### Contabilidade Geral e Avançada (estudo de 21/10/2026)
- Demonstrações contábeis (Lei 6.404/1976 e NBC TG 26), balanço patrimonial (estrutura, ativo, passivo) e patrimônio líquido (contas, reservas, ações em tesouraria, absorção de prejuízos, exemplo numérico). A primeira parte do resumo (atos e fatos, livros, contas, razonete e fórmulas) já estava na base; acrescentei só a limitação do razonete.
- **Principais enriquecimentos e correções:** a fonte das contas do PL é a Lei 6.404/1976 (o resumo dizia "CTN"); coligadas (influência significativa, presumida a partir de 20% do capital votante) e controladas (art. 243); ARLP (vendas, adiantamentos ou empréstimos: art. 179, II); art. 176 da Lei 6.404 (DFC e DVA); aviso sobre o CPC 06 (R1 x R2) no arrendamento; correção do termo "montante subscrito" no capital social.

### Direito Constitucional (estudo de 21/10/2026)
- Direito constitucional intertemporal; interpretação constitucional (correntes, mutação, métodos, princípios, interpretação conforme); direitos fundamentais (terminologia, direitos e garantias, gerações, status de Jellinek, catalogados) e, em tema próprio, características, dimensões, limites, eficácia e eficácia horizontal.
- **Principais enriquecimentos:** LINDB, art. 2º, §3º (repristinação); Lei 9.868/1999, art. 28, parágrafo único; Häberle e Hesse; STF, RE 201.819 (eficácia horizontal direta).

### Direito Administrativo (estudo de 21/10/2026)
- Fontes (agora com os entendimentos judiciais vinculantes como fonte primária), sistemas administrativos, Estado e governo (conceitos, funções, federação, sistemas e formas de governo) e Administração Pública (sentidos, atividades e atividades-meio e fim, com a sua imagem).
- **Principais enriquecimentos:** artigos da Constituição para os pontos comuns da federação; CF, art. 52, I (impeachment) e art. 5º, XXXV.

- **Questões turbo (Certo ou Errado):** 365 novas, no total de 1.408 (Tributário 406, Contabilidade 352, Constitucional 377 e Administrativo 273).
- **Questões de múltipla escolha:** 203 novas, no total de 672 (Tributário 209, Contabilidade 171, Constitucional 150 e Administrativo 142).

## 30/10/2026 — Resumo sintético e nova disciplina Língua Portuguesa (v015)

- **Origem:** o arquivo "Sintético.md", com quatro disciplinas misturadas ("Direito Constitucional", "CONTABILIDADE", "TRIBUTÁRIO" e "PORTUGUÊS").
- **Resumo sintético:** separado pelos títulos de disciplina, sem mudar o texto, e salvo como a **parte 04** de Constitucional, Contabilidade e Tributário (`04 - 2026-10-30`) e como a **parte 01** da nova disciplina (`01 - 2026-10-30`). Na parte de Português, a imagem que vinha embutida no arquivo foi gravada ao lado (`01 - 2026-10-30 - imagem 1.png`), como nas outras partes. Na exibição, os títulos numerados seguem em sequência.
- **Nova disciplina: Língua Portuguesa** (sigla PORT, cor m5): criadas a pasta da matéria, o `Resumo Sintético/` (com `LEIA-ME.txt`), a entrada em `MATERIAS` de `gerar.py` e os agentes e guias de banca de questões (Certo ou Errado e múltipla escolha). Ainda não há temas próprios nem questões; as abas de resumos, mapas e questões aparecem vazias até a chegada dos primeiros resumos. As pastas `Questões Turbo/` e `Questões Múltipla Escolha/` serão criadas junto com o primeiro tema.
- Os guias de banca de Português foram escritos de conhecimento geral, sem pesquisa na web; vale complementá-los quando os primeiros temas entrarem.
