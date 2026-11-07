# Demonstração do Resultado do Exercício (DRE)

<!-- Fixação em detalhes. Fontes: aulas de DRE de Igor Cintra e Gilmar Possati, caderno TecConcursos "DRE - 851", Lei 6.404/76 (art. 187) e CPC 26 (R1). Conteúdo reescrito; nada literal dos professores. -->

## Grade

Cada linha alinha as duas estruturas. `~notas`: o CPC leva a linha para as notas explicativas. `~desce`: no CPC a linha aparece mais abaixo. `~sobe`: no CPC a linha se junta a um bloco anterior. `~nao`: a linha não existe naquela estrutura. `—`: vazio.

| Lei 6.404/76 | CPC 26 |
|---|---|
| receita-bruta | ~notas |
| deducoes | ~notas |
| receita-liquida | receita-liquida |
| cmv | cmv |
| resultado-bruto | resultado-bruto |
| despesas-vendas | despesas-vendas |
| despesas-administrativas | despesas-administrativas |
| outras-operacionais | outras-operacionais |
| equivalencia | equivalencia |
| resultado-financeiro | ~desce |
| resultado-operacional | ~nao |
| outras-receitas-despesas | ~sobe |
| — | resultado-antes-financeiro |
| — | resultado-financeiro |
| lair | lair |
| ir-csll | ir-csll |
| — | continuadas |
| — | descontinuadas |
| antes-participacoes | antes-participacoes |
| participacoes | participacoes |
| lucro-liquido | lucro-liquido |
| lucro-por-acao | lucro-por-acao |

## receita-bruta · Receita bruta
- Sinal: +
- Nomes: Receita operacional bruta; Receita bruta de vendas e serviços; Vendas brutas; Receita bruta de vendas de mercadorias; Receita de vendas (quando não há deduções)
- Base: Lei 6.404/76, art. 187, I

É o preço de venda multiplicado pela quantidade vendida (ou o valor dos serviços prestados), reconhecido quando o controle do bem passa ao cliente ou o serviço é prestado (CPC 47), recebido ou não.

**Faturamento bruto × receita bruta.** O IPI é cobrado "por fora": soma-se ao preço na nota fiscal, mas não é receita da empresa. Por isso:

| Linha | Exemplo |
|---|---|
| Faturamento bruto (valor da nota) | 1.100.000 |
| (–) IPI faturado | (100.000) |
| (=) Receita bruta | 1.000.000 |

O faturamento não está no art. 187: é uma adaptação de alguns autores (Possati a usa). Se a questão der "faturamento" e "IPI", tire o IPI **antes** de começar; ele não é dedução.

**Pegadinhas**
- "O IPI é dedução da receita bruta." → **ERRADO** (é retirado antes, porque nem integra a receita bruta).
- "Pelo CPC 26, a DRE começa pela receita bruta." → **ERRADO** (começa pela receita líquida; a conciliação fica nas notas).

## deducoes · Deduções da receita bruta
- Sinal: −
- Nomes: Deduções das vendas; Deduções da receita; Deduções da receita operacional bruta; Descontos, abatimentos e tributos sobre vendas
- Base: Lei 6.404/76, art. 187, I; CPC 47; CPC 12

São cinco deduções (Igor):

1. **Devoluções de vendas** (vendas canceladas ou anuladas). A devolução de uma venda feita em exercício **anterior** é despesa com vendas, porque a DRE daquele ano já fechou. Em prova, só trate assim se o enunciado disser expressamente.
2. **Tributos sobre vendas e serviços**: ICMS, PIS, Cofins e ISS. Só os que incidem sobre a venda. IR, CSLL, IPTU, IPVA e taxas **não** são deduções.
3. **Abatimentos sobre vendas**: redução concedida **depois** da venda, por defeito, avaria, diferença de qualidade ou de quantidade. Não reduz a base dos tributos já destacados.
4. **Descontos incondicionais (comerciais) concedidos**: dados **no ato da venda**, destacados na nota fiscal, sem depender de condição futura.
5. **Ajuste a valor presente (AVP) de vendas a prazo**: os juros embutidos numa venda a prazo saem da receita e vão sendo apropriados como receita financeira (CPC 12).

| Desconto | Quando | Onde vai |
|---|---|---|
| Incondicional (comercial) concedido | na venda, na nota fiscal | dedução da receita bruta |
| Condicional (financeiro) concedido | depois, pelo pagamento antecipado | despesa financeira |
| Incondicional obtido (nas compras) | na compra | reduz o custo das compras (CMV) |
| Condicional obtido | pagamento antecipado ao fornecedor | receita financeira |

**Pegadinhas**
- "Descontos concedidos por pagamento antecipado de duplicatas são deduzidos da receita bruta." → **ERRADO** (é desconto financeiro: despesa financeira).
- "O IR e a CSLL são deduções da receita bruta." → **ERRADO** (vêm depois do LAIR).
- "Despesa com impostos sobre vendas" com esse nome → continua sendo **dedução**, não despesa operacional.

## receita-liquida · Receita líquida
- Sinal: =
- Nomes: Receita operacional líquida; Vendas líquidas; Receita líquida de vendas e serviços; Receita (no CPC 26 e no CPC 47)
- Base: Lei 6.404/76, art. 187, II; CPC 26 (R1), item 82

Receita bruta menos as deduções. É a primeira linha da DRE no CPC 26: quando uma questão "pelo CPC" fala só em "receitas", é a receita líquida.

**Pegadinha**
- "A receita líquida é a receita bruta menos o CMV." → **ERRADO** (isso dá o resultado bruto).

## cmv · Custo das mercadorias vendidas (CMV, CPV, CSP)
- Sinal: −
- Nomes: Custo das vendas; Custo das mercadorias vendidas (comércio); Custo dos produtos vendidos (indústria); Custo dos serviços prestados; Custo das mercadorias comercializadas
- Base: Lei 6.404/76, art. 187, II; CPC 16 (Estoques)

Reconhecido junto com a receita da venda (confrontação). No comércio:

**CMV = Estoque inicial + Compras líquidas − Estoque final**

Compras líquidas = compras brutas + fretes e seguros sobre compras + tributos não recuperáveis − devoluções de compras − abatimentos sobre compras − descontos incondicionais obtidos − tributos recuperáveis (ICMS, PIS e Cofins com direito a crédito).

- Frete **da compra** é custo (entra no estoque); frete **da venda** é despesa com vendas.
- Desconto financeiro obtido **não** reduz compras: é receita financeira.
- Na indústria, matéria-prima, mão de obra direta e custos indiretos de fábrica vão para o estoque e só chegam à DRE como CPV quando o produto é vendido.

**Pegadinhas**
- "Compras do período são despesa do período." → **ERRADO** (vão para o estoque; a DRE só vê o CMV).
- "O CMV é subtraído da receita bruta." → **ERRADO** (é subtraído da receita líquida).

## resultado-bruto · Resultado bruto
- Sinal: =
- Nomes: Lucro bruto; Resultado com mercadorias (RCM); Lucro operacional bruto; Resultado operacional bruto; Resultado bruto com vendas; Margem bruta (quando em %); Prejuízo bruto (se negativo)
- Base: Lei 6.404/76, art. 187, II; CPC 26 (R1), item 82 (lucro bruto)

Receita líquida − CMV. É o que **mais cai** em cálculo: muitas questões só pedem o lucro bruto, e todo o resto do enunciado (despesas, juros, IR) é distração.

**Pegadinhas**
- "Lucro operacional bruto" é o lucro **bruto**, não o operacional.
- Resultado bruto ≠ receita bruta − CMV (faltaram as deduções).

## despesas-vendas · Despesas com vendas
- Sinal: −
- Nomes: Despesas comerciais; Despesas de vendas; Despesas com comercialização
- Base: Lei 6.404/76, art. 187, III; CPC 26, itens 99 a 103

Gastos para promover, colocar e distribuir o produto: salários e comissões de vendedores, propaganda e publicidade do produto, fretes e seguros sobre vendas, brindes, embalagens de presente e a **despesa** com perdas estimadas com créditos de liquidação duvidosa (PECLD/PDD). Energia e telefone do setor de vendas também podem vir aqui.

**Marketing:** se promove um produto, é despesa com vendas; se promove a instituição (marketing institucional), é administrativa. A FGV já explorou essa diferença (Igor).

**Pegadinhas**
- "Frete sobre compras é despesa com vendas." → **ERRADO** (é custo da mercadoria).
- O **saldo** da PECLD no balanço é retificadora do ativo; só a constituição do período (a despesa) vai para a DRE.

## despesas-administrativas · Despesas gerais e administrativas
- Sinal: −
- Nomes: Despesas administrativas; Despesas gerais; Despesas gerais e administrativas
- Base: Lei 6.404/76, art. 187, III

Gastos de direção e gestão: honorários da administração, salários e encargos do pessoal administrativo, FGTS, aluguéis, material de expediente consumido, depreciação de bens de uso administrativo, energia, telefone, seguros, impostos e taxas (IPTU, IPVA), marketing institucional.

**Regime de competência:** só a parte **consumida** no período vai para a DRE. Seguro, aluguel e assinaturas pagos antecipadamente são ativo até serem apropriados; material de consumo em estoque é ativo.

**Pegadinhas**
- "Depreciação acumulada" é retificadora do ativo, e não despesa. A despesa é a "depreciação do período".
- Despesas com vendas e administrativas, juntas, são chamadas de **despesas operacionais** (CEBRASPE, SUFRAMA 2014).

## despesas-operacionais · Despesas operacionais (bloco)
- Sinal: −
- Nomes: Despesas operacionais; Demais despesas operacionais; Despesas "operacionais"
- Base: Lei 6.404/76, art. 187, III

Bloco entre o resultado bruto e o resultado operacional. Na Lei, inclui despesas com vendas, gerais e administrativas, outras despesas operacionais e as despesas financeiras líquidas das receitas financeiras. No CPC 26, o resultado financeiro sai desse bloco.

## outras-operacionais · Outras receitas e despesas operacionais
- Sinal: ±
- Nomes: Outras receitas operacionais; Outras despesas operacionais; Outros resultados operacionais
- Base: Lei 6.404/76, art. 187, III; CPC 26 (R1), item 82

Receitas e despesas das atividades acessórias, que não são de vendas, administrativas nem financeiras:
- dividendos recebidos de investimentos avaliados pelo **custo**;
- receitas de aluguel quando alugar não é a atividade principal;
- venda esporádica de sucatas;
- reversões de provisões;
- perdas por redução ao valor recuperável (*impairment*) ou ao valor realizável líquido dos estoques;
- ganhos de valor justo de propriedade para investimento.

**Divergência entre bancas:** FGV e FCC costumam pôr aqui também os ganhos e perdas na venda de imobilizado, investimentos e intangível. Pelo texto do art. 187, IV, eles são "outras receitas e outras despesas", **depois** do resultado operacional. Veja "Outras receitas e outras despesas".

## equivalencia · Resultado de equivalência patrimonial
- Sinal: ±
- Nomes: Receita (ou despesa) de equivalência patrimonial; Ganho (ou perda) com equivalência patrimonial; Resultado positivo (negativo) de participações societárias; Parcela dos resultados de investidas reconhecida pelo método da equivalência patrimonial
- Base: CPC 26 (R1), item 82; CPC 18

É a parte do lucro (ou prejuízo) das coligadas e controladas que cabe à investidora.
- **Lei:** fica entre as receitas e despesas operacionais (Possati).
- **CPC 26:** é uma linha própria, antes do resultado financeiro.

**Pegadinhas**
- Dividendo recebido de investimento avaliado por equivalência **não** é receita: reduz o valor do investimento. Só é receita o dividendo de investimento avaliado pelo custo.
- A variação de investimento no exterior por conversão cambial vai para outros resultados abrangentes, não para a DRE.

## resultado-financeiro · Resultado financeiro
- Sinal: ±
- Nomes: Receitas e despesas financeiras; Despesas financeiras líquidas; Resultado financeiro líquido; Despesas financeiras, deduzidas das receitas financeiras
- Base: Lei 6.404/76, art. 187, III; CPC 26 (R1), item 82

**Despesas financeiras:** juros passivos, descontos condicionais concedidos, despesas bancárias, IOF, variações monetárias e cambiais passivas, prêmio de resgate de debêntures, apropriação do AVP de compras a prazo.

**Receitas financeiras:** juros ativos (inclusive os cobrados de clientes em atraso), descontos condicionais obtidos, rendimentos de aplicações, variações monetárias ativas, apropriação do AVP de vendas a prazo.

**Onde fica:**
- **Lei:** dentro das despesas operacionais ("as despesas financeiras, deduzidas das receitas"), **antes** do resultado operacional.
- **CPC 26:** **depois** do "resultado antes do resultado financeiro" e antes do LAIR.

A FGV já cobrou pelo CPC (TCE-PI 2021): "o resultado financeiro compõe o resultado antes do IR/CSLL" foi a resposta, e não "integra o resultado operacional".

**Como saber qual estrutura a questão usa (Igor):** se fala em "lucro operacional", é a Lei; se fala em "resultado financeiro" ou em "resultado antes do resultado financeiro", é o CPC.

**JCP (juros sobre o capital próprio) — divergência:** para o fisco, é despesa financeira dedutível (Lei 9.249/95, art. 9º), e Possati o lista entre as despesas financeiras. Pela ICPC 08 (R1), contabilmente o JCP é distribuição do resultado e vai direto ao patrimônio líquido. Leia o comando da questão.

## resultado-operacional · Resultado operacional
- Sinal: =
- Nomes: Lucro operacional; Lucro operacional líquido; Resultado operacional líquido; Lucro (prejuízo) operacional
- Base: Lei 6.404/76, art. 187, IV

Resultado bruto − despesas operacionais (incluídas as financeiras líquidas). Está no art. 187, IV, mas não é apresentado pelas normas do CPC, que não separam operacional de não operacional.

**Pegadinhas**
- "Lucro operacional bruto" ≠ "lucro operacional": o primeiro é o resultado bruto.
- Pela Lei, o resultado operacional **inclui** o resultado financeiro.

## outras-receitas-despesas · Outras receitas e outras despesas
- Sinal: ±
- Nomes: Outras receitas; Outras despesas; Ganhos e perdas de capital; Resultado não operacional (nome antigo); Receitas e despesas não operacionais (nome antigo)
- Base: Lei 6.404/76, art. 187, IV (redação da Lei 11.941/2009)

Ganhos e perdas na venda, baixa ou alienação de bens do **investimento, imobilizado e intangível**. Na DRE entra o **resultado** da venda (preço de venda − valor contábil líquido), não o preço inteiro.

- **Lei:** depois do resultado operacional e antes do LAIR.
- **CPC 26:** dentro do bloco operacional ("outras receitas e despesas operacionais"). FGV e FCC seguem essa linha.

**Pegadinhas**
- "O ganho na venda de imobilizado é resultado não operacional." → **ERRADO** (a expressão foi extinta; hoje são "outras receitas").
- Operações **descontinuadas** não são "outras receitas": têm linha própria, depois dos tributos (CPC 31).

## resultado-antes-financeiro · Resultado antes do resultado financeiro
- Sinal: =
- Nomes: Resultado antes das receitas e despesas financeiras; Lucro antes do resultado financeiro; Resultado operacional (no sentido do CPC)
- Base: CPC 26 (R1), item 82

Subtotal só do CPC 26: resultado bruto − despesas com vendas e administrativas ± outras receitas e despesas ± equivalência patrimonial.

## lair · Resultado antes do IR e da CSLL (LAIR)
- Sinal: =
- Nomes: Lucro antes do imposto de renda (LAIR); Resultado antes dos tributos sobre o lucro; Lucro antes do IR e da CSLL; Resultado do exercício antes do IR e da provisão para o imposto; Lucro antes dos impostos
- Base: Lei 6.404/76, art. 187, V; CPC 26 (R1), item 82

Último resultado comum às duas estruturas antes dos tributos. É a base que a maioria das questões usa para calcular o IR e a CSLL ("alíquota × LAIR").

## ir-csll · Imposto de renda e CSLL
- Sinal: −
- Nomes: Provisão para o imposto de renda e a contribuição social; Despesa com tributos sobre o lucro; IR e CSLL correntes e diferidos; Imposto sobre o lucro
- Base: Lei 6.404/76, art. 187, V; CPC 26 (R1), item 82; CPC 32

Em prova, quase sempre: **IR/CSLL = alíquota × LAIR**. A alíquota normal é de 15% de IR, mais 10% de adicional sobre o que passar de R$ 20 mil por mês, e 9% de CSLL.

Quando a questão traz ajustes, a base é o lucro real: LAIR + adições − exclusões − compensação de prejuízo fiscal (até 30% do lucro ajustado).
- **Adições:** multas indedutíveis, brindes, despesa com PECLD, despesa de equivalência patrimonial.
- **Exclusões:** receita de equivalência patrimonial, reversões de provisões não dedutíveis.

**Pegadinhas**
- IR e CSLL a **pagar** são passivo; a DRE mostra a **despesa**.
- O IR vem **antes** das participações (art. 189).

## continuadas · Resultado líquido das operações continuadas
- Sinal: =
- Nomes: Resultado das operações continuadas
- Base: CPC 26 (R1), item 82; CPC 31

Subtotal do CPC: resultado depois dos tributos sobre o lucro, antes do resultado das operações descontinuadas.

## descontinuadas · Resultado das operações descontinuadas
- Sinal: ±
- Nomes: Resultado líquido após tributos das operações descontinuadas
- Base: CPC 26 (R1), item 82; CPC 31, item 32

Resultado de um componente baixado ou mantido para venda que é uma linha de negócio ou área geográfica importante (ou uma controlada comprada só para revenda). Aparece **depois** dos tributos, em valor líquido, numa linha única.

**Pegadinha**
- Não confunda com a venda de um imobilizado isolado, que é "outras receitas/despesas".

## antes-participacoes · Resultado antes das participações
- Sinal: =
- Nomes: Lucro após o IR e a CSLL; Resultado do exercício antes das participações
- Base: Lei 6.404/76, arts. 187, VI, e 189

LAIR − IR e CSLL. É o ponto de partida da base das participações. O **prejuízo acumulado** reduz a base das participações (art. 189), mas **não aparece** na DRE.

## participacoes · Participações no resultado
- Sinal: −
- Nomes: Participações estatutárias; Participações de debêntures, empregados, administradores e partes beneficiárias; Contribuições para fundos de assistência ou previdência de empregados
- Base: Lei 6.404/76, arts. 187, VI, 189 e 190

**Ordem (mnemônico DEAPI, ou DEAPF no Possati):** **D**ebêntures → **E**mpregados → **A**dministradores → **P**artes beneficiárias → **I**nstituições (fundos) de assistência ou previdência de empregados.

**Base:** resultado após IR e CSLL − prejuízos acumulados. Cada participação é calculada sobre o que **sobra** depois de deduzida a anterior (art. 190).

| Etapa (exemplo do Possati, 10% cada) | Valor |
|---|---|
| Resultado antes das participações | 600.000 |
| (–) prejuízos acumulados (só para a base) | (100.000) |
| Base das debêntures | 500.000 → 50.000 |
| Base dos empregados | 450.000 → 45.000 |
| Base dos administradores | 405.000 → 40.500 |
| Base das partes beneficiárias | 364.500 → 36.450 |
| Base dos fundos | 328.050 → 32.805 |
| **Lucro líquido** (600.000 − todas) | **395.245** |

**Pegadinhas**
- O prejuízo acumulado reduz a base, mas o lucro líquido parte do valor **antes** dessa redução.
- Pelo art. 187, VI, entram as participações "que não se caracterizem como despesa". A participação dos empregados (PLR), pelo CPC 33, costuma ser despesa operacional; em prova de Lei, siga a ordem DEAPI depois do IR.
- O limite da participação dos administradores (art. 152) não se confunde com a ordem do cálculo.

## lucro-liquido · Lucro (prejuízo) líquido do exercício
- Sinal: =
- Nomes: Resultado líquido do exercício; Lucro líquido do período; Resultado do período
- Base: Lei 6.404/76, art. 187, VII; CPC 26 (R1), item 82

Resultado final, que vai para o patrimônio líquido. A destinação (reservas e dividendos) **não** passa pela DRE: está na DLPA ou na DMPL.

## lucro-por-acao · Lucro líquido por ação
- Sinal: ÷
- Nomes: Montante do lucro por ação do capital social; Resultado por ação
- Base: Lei 6.404/76, art. 187, VII; CPC 41

Lucro líquido ÷ número de ações. A Lei exige, e o CPC 41 detalha (básico e diluído).

## calculo-cmv · Entra no cálculo do CMV
- Sinal: ·
- Nomes: Estoques, compras e gastos com compras
- Base: CPC 16

Não são linhas da DRE: compõem o CMV pela fórmula EI + compras líquidas − EF. Veja o grupo CMV.

## fora-ativo · Fora da DRE: ativo
- Sinal: ·
- Nomes: Contas do balanço (ativo)

Disponível, clientes, estoques, despesas pagas antecipadamente, investimentos, imobilizado, intangível e as retificadoras (depreciação e amortização acumuladas, saldo da PECLD, provisões para perdas). **Ignore na DRE**, salvo para calcular CMV ou depreciação.

## fora-passivo · Fora da DRE: passivo
- Sinal: ·
- Nomes: Contas do balanço (passivo)

Fornecedores, salários, impostos e IR a pagar ou a recolher, empréstimos, debêntures emitidas, receitas recebidas antecipadamente (ainda não ganhas), provisões passivas (o saldo). **Ignore na DRE.**

## fora-pl · Fora da DRE: patrimônio líquido
- Sinal: ·
- Nomes: Contas do patrimônio líquido

Capital, reservas, ações em tesouraria, ajustes de avaliação patrimonial e lucros ou prejuízos acumulados. O prejuízo acumulado só serve para a base das participações.

## fora-destinacao · Fora da DRE: destinação do lucro
- Sinal: ·
- Nomes: Distribuição do resultado

Dividendos, constituição de reservas, JCP (pela ICPC 08) e ajustes de exercícios anteriores (art. 186, § 1º) aparecem na DLPA ou na DMPL. A DRE **termina** no lucro líquido.

## fora-outros · Fora da DRE: fluxo de caixa
- Sinal: ·
- Nomes: Recebimentos e pagamentos

Recebimentos e pagamentos são caixa (DFC). A DRE segue o regime de competência: receita entra quando ganha, despesa quando incorrida, independentemente de pagamento ou recebimento (art. 187, § 1º).

## Diferenças entre a Lei e o CPC

| Ponto | Lei 6.404/76 (art. 187) | CPC 26 (item 82) |
|---|---|---|
| Primeira linha | Receita bruta | Receita (líquida); a conciliação fica nas notas |
| Resultado financeiro | Dentro das operacionais, antes do resultado operacional | Separado, depois do "resultado antes do resultado financeiro" |
| Resultado operacional | Existe (art. 187, IV) | Não é apresentado |
| Outras receitas e despesas | Depois do resultado operacional | Dentro do bloco operacional |
| Equivalência patrimonial | Entre as receitas e despesas operacionais | Linha própria antes do resultado financeiro |
| Operações descontinuadas | Não trata | Linha própria, líquida de tributos (CPC 31) |
| Participações | Depois do IR, ordem DEAPI | Silencioso (PLR de empregado tende a ser despesa pelo CPC 33) |

## Fora da DRE

Ponto de partida de toda questão com balancete: **separe o que é patrimonial**. Fica fora:
- **Ativo**, inclusive estoques, despesas antecipadas e retificadoras.
- **Passivo**, inclusive "a pagar", "a recolher" e receitas antecipadas.
- **Patrimônio líquido.**
- **Destinação do lucro.**
- **Movimentos de caixa.**

Entram só as contas de resultado (receitas e despesas), e as de estoque e compras só por meio do CMV.

## Mudanças à vista ⚠️

- ⚠️ **CPC 51 (IFRS 18)** substitui o CPC 26 (R1) nos exercícios iniciados a partir de **1º/1/2027** (Resoluções CVM 237 e 238). A DRE passa a ter categorias (operacional, investimento, financiamento) e dois subtotais obrigatórios: **lucro operacional** e **lucro antes do financiamento e dos tributos sobre o lucro**. Há discussão sobre a harmonização com o art. 187 da Lei 6.404/76. As provas atuais ainda cobram o CPC 26 e a Lei.
- ⚠️ **IBS e CBS (Reforma Tributária, LC 214/2025):** são cobrados "por fora". A Orientação Técnica CFC nº 1/2026, que não é vinculante, entende que **não compõem a receita bruta**, de forma parecida com o IPI. A prática ainda não é uniforme.

## Mapa mental
- Estrutura
  - Lei: começa na receita bruta
  - CPC 26: começa na receita líquida
- Receita
  - Receita bruta
  - Deduções: devoluções, tributos, abatimentos, descontos incondicionais, AVP
  - Receita líquida
- Custo e resultado bruto
  - CMV = EI + compras líquidas − EF
  - Resultado bruto = receita líquida − CMV
- Despesas operacionais
  - Vendas
  - Administrativas
  - Outras operacionais e equivalência
- Financeiro e outras
  - Resultado financeiro: Lei dentro, CPC depois
  - Outras receitas e despesas
- Tributos e participações
  - LAIR
  - IR e CSLL
  - Participações DEAPI
- Fora da DRE
  - Ativo, passivo, PL
  - Destinação do lucro
