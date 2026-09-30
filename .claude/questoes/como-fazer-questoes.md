# Como fazer as questões turbo

Instruções comuns aos agentes `questoes-<matéria>` (em `.claude/agents/`). Cada agente cuida de uma matéria e usa o guia da banca dela, em `.claude/questoes/guias/`. As questões são de **Certo ou Errado** e são feitas só a partir dos **temas** da base (`ESTUDOS/<Matéria>/NN - Assunto/*.md`). O resumo sintético, as pegadinhas e o `_CONTROLE` não são fonte.

## 1. Ler só o que é novo (economia de tokens)

Na raiz do projeto, rode:

```bash
python sistema/gerar.py --questoes-pendentes "<Matéria>"
```

A saída traz, para cada tema:
- **o arquivo de questões**, com a próxima numeração;
- **só as seções novas ou alteradas** desde a última vez;
- **a lista curta das questões que já citam essas seções.**

Trabalhe **apenas com essa saída**. Não abra os temas nem os arquivos de questões inteiros. A exceção é o fim do arquivo de questões: leia só o fim, com Read (offset), para acrescentar questões nele.

Se a saída disser "Nada pendente", não há o que fazer.

## 2. Formato (exato)

Arquivo: `ESTUDOS/<Matéria>/Questões Turbo/<mesmo-nome-do-tema>.md`. Se ainda não existir, crie-o assim:

```markdown
# Questões turbo — <Título do tema>

## Q001 · médio · <Título da seção do tema>
<Enunciado: um parágrafo; pode ter **negrito** e situação hipotética.>
- Gabarito: ERRADO
- Comentário: <Por que está certo ou errado, de forma direta. Cite a base legal ou o julgado que já estão no tema (ex.: CTN, art. 77; SV 41).>
```

- **Número:** três dígitos, sequencial a partir da "próxima" indicada. **Nunca renumere** nem reaproveite número: é nele que o site guarda as respostas do estudante.
- **Dificuldade:** exatamente `fácil`, `médio` ou `difícil`.
- **Seção:** o título **mais específico** (`##` a `####`) em que está a informação cobrada, escrito igual ao do tema, sem os `**`. Para o texto que vem antes da primeira seção (aparece como "(início)" na saída), use o título do tema (`# ...`). Se o mesmo subtítulo se repete no tema, cite o título de nível acima, que é único. Ele vira o link "Ver no resumo". Não use "Mapa mental", "Pegadinhas" nem "Relações com outros assuntos".
- **Gabarito:** `CERTO` ou `ERRADO`.
- **Linha `<!-- cobertura ... -->`:** não escreva à mão. Ela é gravada pelo comando `--cobrir`.

## 3. Qualidade: o que o estudante pediu

- **Nada de frase recortada do tema com uma palavra trocada:** isso é o que as pegadinhas já fazem. Reescreva a ideia como a banca faria. Use estes recursos:
  - paráfrase;
  - termos menos comuns, mas corretos: "exação", "tributo não vinculado", "prescinde", "situação líquida", "tutela administrativa", "poder constituinte de segundo grau" e outros do guia;
  - troca sutil de regra por exceção;
  - troca de competência ou de veículo normativo;
  - absolutos: "sempre", "exclusivamente", "somente";
  - justificativa falsa depois de "porque" ou "pois";
  - caso hipotético com personagens ou valores;
  - combinação de duas informações do tema.
- **O objetivo é fazer lembrar o conceito em profundidade.** Cada questão testa uma ideia central, e o comentário ensina essa ideia em 1 a 3 frases.
- **Conteúdo só do tema:**
  - o guia da banca dá o **estilo**, nunca o conteúdo;
  - não use lei, julgado, número ou exceção que não esteja no texto pendente;
  - se o tema marca ⚠️ ou divergência, só pergunte o que o tema afirma com segurança, ou use "segundo o STF" ou "para a doutrina majoritária" exatamente como o tema registra.
- **Equilíbrio:**
  - entre **40% e 60% de CERTO** em cada tema;
  - dificuldade em torno de 30% fácil, 45% médio e 25% difícil;
  - "difícil" é o item que exige um passo a mais: exceção da exceção, sinônimo raro, caso concreto, jurisprudência específica do tema ou combinação de conceitos.
- **Quantidade: o máximo que o texto sustenta sem repetir a mesma ideia.** Em geral, uma questão por fato, distinção, exceção ou exemplo relevante. Seções com tabela comparativa costumam render várias. Não faça duas questões que testem a mesma coisa com o mesmo gabarito.
- **Nunca** diga que a questão é de prova real ou de um concurso específico, e não copie questões reais.
- **Português formal, como o da banca.** O enunciado não menciona "o resumo" nem "o tema".
- **Tabela com filtros** (ex.: as 71 contas de Contabilidade): varie. Cobre classificação, natureza, a conta redutora e os cuidados listados.

## 4. Seções alteradas que já têm questões

Para cada questão listada como "já existe nessas seções":
- confira se ela continua correta diante do texto novo;
- se ficou errada, corrija no próprio lugar o enunciado, o gabarito ou o comentário, mantendo o número;
- se perdeu o sentido, apague a questão; o número fica vago;
- não repita o que ela já cobra.

Seção que saiu do tema: as questões que a citam precisam ir para a seção nova correspondente, ou sair.

## 5. Fechar

1. Para cada tema trabalhado, grave a cobertura:
   ```bash
   python sistema/gerar.py --cobrir "<Matéria>/Questões Turbo/<arquivo>.md"
   ```
2. Rode `python sistema/gerar.py --verificar`. Corrija só os avisos dos seus arquivos de questões (seção que não existe, formato). Não mexa em nenhum outro arquivo: temas, `_CONTROLE`, resumo sintético, `sistema/`, site.
3. Rode de novo `--questoes-pendentes "<Matéria>"`. A resposta deve ser "Nada pendente".
4. Responda com um relatório curto. Não repita as questões. Traga:
   - por tema, quantas questões novas, a divisão entre C e E e a divisão por dificuldade;
   - questões antigas corrigidas ou apagadas;
   - **dúvidas de conteúdo:** algo no tema que pareceu errado ou ambíguo. Não corrija o tema: relate.
