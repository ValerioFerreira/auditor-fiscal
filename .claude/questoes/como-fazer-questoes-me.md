# Como fazer as questões de múltipla escolha

Instruções comuns aos agentes `questoes-multipla-<matéria>` (em `.claude/agents/`). Cada agente cuida de uma matéria e usa o guia dela em `.claude/questoes/guias-me/` (estilo da **CEBRASPE** e da **FGV** em múltipla escolha) e, para os assuntos mais cobrados, o guia de Certo ou Errado em `.claude/questoes/guias/`. As questões são feitas só a partir dos **temas** da base (`ESTUDOS/<Matéria>/NN - Assunto/*.md`). O resumo sintético, as pegadinhas, o `_CONTROLE` e as questões de Certo ou Errado não são fonte de conteúdo.

As questões de múltipla escolha ficam numa pasta própria, `ESTUDOS/<Matéria>/Questões Múltipla Escolha/`, separada das de Certo ou Errado (`Questões Turbo/`). O número, a cobertura e o gabarito de uma pasta não têm relação com os da outra.

## 1. Ler só o que é novo (economia de tokens)

Na raiz do projeto, rode:

```bash
python sistema/gerar.py --questoes-pendentes --me "<Matéria>"
```

A saída traz, para cada tema:
- **o arquivo de questões**, com a próxima numeração (`M001`...) e quantas questões já existem de cada banca;
- **só as seções novas ou alteradas** desde a última vez;
- **a lista curta das questões que já citam essas seções.**

Trabalhe **apenas com essa saída**. Não abra os temas nem os arquivos de questões inteiros. A exceção é o fim do arquivo de questões: leia só o fim, com Read (offset), para acrescentar questões nele.

Se a saída disser "Nada pendente", não há o que fazer.

## 2. Formato (exato)

Arquivo: `ESTUDOS/<Matéria>/Questões Múltipla Escolha/<mesmo-nome-do-tema>.md`. Se ainda não existir, crie a pasta e o arquivo assim:

```markdown
# Questões de múltipla escolha — <Título do tema>

## M001 · médio · FGV · <Título da seção do tema>
<Enunciado: um ou mais parágrafos. Afirmativas I, II, III, cada uma em parágrafo próprio (com linha em branco entre elas).>

- A) <alternativa>
- B) <alternativa>
- C) <alternativa>
- D) <alternativa>
- E) <alternativa>
- Gabarito: C
- Comentário: <Por que a alternativa certa está certa e por que as principais erradas estão erradas, de forma direta. Cite a base legal ou o julgado que já estão no tema.>
```

- **Número:** `M` e três dígitos, sequencial a partir da "próxima" indicada. **Nunca renumere** nem reaproveite número: é nele que o site guarda as respostas do estudante.
- **Dificuldade:** exatamente `fácil`, `médio` ou `difícil`.
- **Banca:** exatamente `FGV` ou `CEBRASPE`. É o **estilo** da questão (como o enunciado e as alternativas são redigidos), conforme o guia da matéria.
- **Seção:** o título **mais específico** (`##` a `####`) em que está a informação cobrada, escrito igual ao do tema, sem os `**`. Para o texto que vem antes da primeira seção (aparece como "(início)" na saída), use o título do tema (`# ...`). Se o mesmo subtítulo se repete no tema, cite o título de nível acima, que é único. Ele vira o link "Ver no resumo". Não use "Mapa mental", "Pegadinhas" nem "Relações com outros assuntos".
- **Alternativas:** cada uma em **uma linha só**, no formato `- A) texto`. **FGV: sempre cinco (A a E).** CEBRASPE: cinco (A a E), ou quatro (A a D) se o guia indicar que esse é o padrão do assunto. Em ordem, sem pular letra.
- **Gabarito:** `- Gabarito: C` (só a letra). Exatamente uma alternativa certa.
- **Linha `<!-- cobertura ... -->`:** não escreva à mão. Ela é gravada pelo comando `--cobrir`.
- **Marcação:** só `**negrito**` (por exemplo, em **INCORRETA** ou **EXCETO**), `*itálico*` e texto simples. Nada de tabela, crase, `|`, `<br>` ou lista dentro de alternativa. Fórmulas e contas em texto corrido (ex.: "R$ 120.000 − R$ 45.000 = R$ 75.000").

## 3. Qualidade: o que o estudante pediu

- **Duas bancas por tema.** Faça questões **FGV** e questões **CEBRASPE** em quantidades parecidas (nenhuma das duas abaixo de 40% do total do tema). Cada questão segue o estilo da banca indicada:
  - **FGV:** enunciado mais longo, muitas vezes com caso concreto (personagens, entes, valores, datas); comandos como "De acordo com...", "À luz da jurisprudência do STF...", "Assinale a afirmativa correta"; alternativas longas, homogêneas e plausíveis; afirmativas I, II, III com alternativas combinadas ("somente I e III"); literalidade da lei e jurisprudência.
  - **CEBRASPE:** comando enxuto ("Assinale a opção correta", "Com base no CTN, é correto afirmar que"); alternativas mais curtas e precisas; erro escondido em um termo (absoluto, troca de regra por exceção, de competência, de veículo normativo); item que parece errado e está certo.
  - Os dois estilos, em detalhe (tipos de questão, distratores, exemplos), estão no guia da matéria. Leia-o antes de escrever.
- **Conteúdo só do tema:**
  - o guia dá o **estilo**, nunca o conteúdo;
  - não use lei, julgado, número, prazo ou exceção que não esteja no texto pendente;
  - se o tema marca ⚠️ ou divergência, só pergunte o que o tema afirma com segurança, ou use "segundo o STF" ou "para a doutrina majoritária" exatamente como o tema registra.
- **Uma única alternativa certa.** Antes de fechar a questão, confira cada alternativa errada contra o texto do tema: ela precisa estar claramente errada, e a certa claramente certa. Nada de duas respostas defensáveis. Se o tema não sustenta com segurança, não faça a questão.
- **Distratores bons:** cada alternativa errada nasce de um erro **plausível** (troca de competência, de exceção por regra, de prazo, de órgão, de conceito vizinho, absoluto "sempre/somente", justificativa falsa depois de "porque"). Alternativas com extensão e estrutura parecidas; a certa **não** pode ser a mais longa nem a mais detalhada por padrão.
- **Proibido:** "todas as anteriores", "nenhuma das anteriores", "nenhuma das alternativas" e alternativas do tipo "A e B estão corretas" (exceto nas questões de afirmativas I, II, III, em que as alternativas combinam as afirmativas).
- **Afirmativas I, II, III:** no máximo 3 ou 4 afirmativas por questão, cada uma em parágrafo próprio, sem alternativa repetida.
- **Comando "INCORRETA/EXCETO":** no máximo 20% das questões do tema; destaque a palavra com `**INCORRETA**`.
- **Letra do gabarito:** distribua entre A e E de forma parecida em cada tema (cerca de 20% em cada uma; nunca mais de duas questões seguidas com a mesma letra). Alternativas numéricas, em ordem crescente.
- **Equilíbrio de dificuldade:** em torno de 30% fácil, 45% médio e 25% difícil. "Difícil" exige um passo a mais: exceção da exceção, caso concreto, combinação de conceitos, jurisprudência específica, cálculo em duas etapas.
- **Quantidade:** o que o texto sustenta **sem repetir a mesma ideia**. Como referência, de 4 a 10 questões de cada banca por tema; seções com tabela comparativa ou muitas exceções rendem mais. Não faça duas questões que cobrem o mesmo fato com o mesmo gabarito, nem repita o que já existe nas questões listadas.
- **Variedade de tipo:** misture afirmativa única correta, afirmativa incorreta, I-II-III, completar lacuna, caso concreto e (em Contabilidade) cálculo e lançamento, conforme o guia.
- **Comentário:** de 2 a 4 frases. Diga por que a certa está certa (com o dispositivo ou julgado do tema) e por que cada distrator principal está errado. Em questões de cálculo, mostre a conta.
- **Nunca** diga que a questão é de prova real ou de um concurso específico, e não copie questões reais (nem enunciado, nem alternativas). Nomes de personagens e entes são fictícios e neutros ("Ana", "Município Alfa", "Empresa Beta S.A.").
- **Português formal, como o da banca.** O enunciado não menciona "o resumo" nem "o tema".
- **Tabela com filtros** (ex.: as 71 contas de Contabilidade): varie. Cobre classificação, natureza, conta redutora e os cuidados listados.

## 4. Seções alteradas que já têm questões

Para cada questão listada como "já existe nessas seções":
- confira se ela continua correta diante do texto novo;
- se ficou errada, corrija no próprio lugar o enunciado, as alternativas, o gabarito ou o comentário, mantendo o número;
- se perdeu o sentido, apague a questão; o número fica vago;
- não repita o que ela já cobra.

Seção que saiu do tema: as questões que a citam precisam ir para a seção nova correspondente, ou sair.

## 5. Fechar

1. Para cada tema trabalhado, grave a cobertura:
   ```bash
   python sistema/gerar.py --cobrir "<Matéria>/Questões Múltipla Escolha/<arquivo>.md"
   ```
2. Rode `python sistema/gerar.py --verificar`. Corrija só os avisos dos seus arquivos de questões (seção que não existe, formato, alternativa fora do padrão). Não mexa em nenhum outro arquivo: temas, `_CONTROLE`, resumo sintético, questões de Certo ou Errado, `sistema/`, site.
3. Rode de novo `--questoes-pendentes --me "<Matéria>"`. A resposta deve ser "Nada pendente".
4. Responda com um relatório curto. Não repita as questões. Traga:
   - por tema, quantas questões novas, a divisão por banca (FGV e CEBRASPE), por dificuldade e por letra do gabarito;
   - questões antigas corrigidas ou apagadas;
   - **dúvidas de conteúdo:** algo no tema que pareceu errado ou ambíguo. Não corrija o tema: relate.
