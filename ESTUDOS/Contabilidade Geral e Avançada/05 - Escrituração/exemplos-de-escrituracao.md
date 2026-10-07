# Exemplos de Escrituração

## Como ler

- **A** = ativo · **P** = passivo exigível · **PL** = patrimônio líquido · **D** = débito · **C** = crédito. O sinal indica o efeito: **+** aumenta, **−** diminui. Receita **aumenta** o PL; despesa **diminui** o PL.
- **Apropriação**: reconhecimento de uma despesa **já incorrida** (o fato gerador já ocorreu), mas **ainda não paga**. O **regime de competência** manda reconhecer receitas e despesas **no momento do fato gerador**, independentemente de recebimento ou pagamento.
- Classificação dos fatos: **permutativo** (PL não muda), **modificativo** (aumentativo ou diminutivo) e **misto** (permuta + modificação) → `../04 - Atos e Fatos Administrativos/atos-e-fatos-administrativos.md`.

## Fatos permutativos (o PL não muda)

| Fato | Lançamento | Observações |
|---|---|---|
| **Depósito bancário** de R$ 40.000 | D Bancos 40.000 (+A) · C Caixa 40.000 (−A) | Saída de caixa e aumento em bancos |
| **Compra de mercadorias a prazo** por R$ 20.000, aceitando duplicatas | D Estoque 20.000 (+A) · C Duplicatas a pagar 20.000 (+P) | Entrada em estoque e surgimento de obrigação |
| **Aplicação financeira** de R$ 10.000 | D Aplicação financeira 10.000 (+A) · C Bancos 10.000 (−A) | Diminui banco e aumenta aplicação financeira. **Momento 1**: aplicação (troca entre componentes, +A/−A). **Momento 2**: apropriação dos rendimentos → **receita** (+A/+PL). **Momento 3**: resgate, com os rendimentos apropriados, se houver (+A/−A) |
| **Empréstimo bancário** obtido, R$ 3.000 | D Bancos 3.000 (+A) · C Empréstimos bancários 3.000 (+P) | **Momento 1**: obtenção (+A/+P). **Momento 2**: apropriação dos juros (provisão dos encargos financeiros) → **despesa** (+P/−PL). **Momento 3**: pagamento/quitação (−A/−P) |
| **Pagamento dos salários provisionados**, em dinheiro | D Salários a pagar (−P) · C Caixa (−A) | Reduz caixa e reduz salários a pagar |
| **Compra de veículo para uso** por R$ 20.000: 10% à vista, em dinheiro, e o restante a prazo | D Veículos 20.000 (+A) · C Caixa 2.000 (−A) · C Financiamentos a pagar 18.000 (+P) | Aumenta veículos, reduz caixa e aumenta financiamentos |
| **Desconto de duplicatas** de R$ 5.000 a vencer em 30 dias, com juros de 10% ao mês | D Bancos 4.500 (+A) · D Encargos financeiros a transcorrer 500 (−P) · C Duplicatas descontadas 5.000 (+P) | A empresa entrega ao banco as duplicatas (direitos de recebimento das vendas a prazo) para receber hoje, e o banco cobra juros: **na prática, um empréstimo**. Os **encargos financeiros a transcorrer (a vencer)** são o valor cobrado para adiantar o pagamento. Os R$ 4.500 e os R$ 500 são calculados a partir dos dados (10% de R$ 5.000) |

- **Desconto de duplicatas — no vencimento** (três hipóteses):
  1. **o cliente paga** a duplicata: D Duplicatas descontadas · C Duplicatas a receber;
  2. **o cliente não paga** (a empresa assume o encargo): D Duplicatas descontadas · C Bancos;
  3. **o cliente paga parcialmente**: D Duplicatas descontadas · C Duplicatas a receber · C Bancos.

## Fatos modificativos

| Fato | Lançamento | Classificação |
|---|---|---|
| **Subscrição de capital** com integralização em dinheiro, R$ 100.000 | D Caixa 100.000 (+A) · C Capital social 100.000 (+PL) | **Aumentativo** (+A/+PL) |
| **Apropriação de rendimentos financeiros**, R$ 1.000 | D Aplicação financeira 1.000 (+A) · C Rendimentos financeiros — receita 1.000 (+PL) | **Aumentativo** |
| **Apropriação da folha de pagamento**, R$ 2.000 | D Despesa com salários 2.000 (−PL) · C Salários a pagar 2.000 (+P) | **Diminutivo** (+P/−PL): reconhece a despesa, diminuindo o PL |
| **Pagamento, em dinheiro, de despesas administrativas**, R$ 5.000 | D Despesas administrativas 5.000 (−PL) · C Caixa 5.000 (−A) | **Diminutivo** (−A/−PL) |

## Fatos mistos

| Fato | Lançamento | Classificação |
|---|---|---|
| **Venda de mercadorias à vista** por R$ 10.000, com **lucro de 20% sobre o preço de venda** (custo = 80% = R$ 8.000) | **Reconhecimento da venda**: D Caixa 10.000 (+A) · C Receita de vendas 10.000 (+PL). **Reconhecimento do custo** (o que saiu do estoque): D Custo das mercadorias vendidas 8.000 (−PL) · C Estoque 8.000 (−A) | **Misto aumentativo**: o PL aumenta no lucro (R$ 2.000) |
| **Pagamento de duplicata** de R$ 4.000, em dinheiro, **com juros de 10%** | D Duplicatas a pagar 4.000 (−P) · D Juros passivos 400 (−PL) · C Caixa 4.400 (−A) | **Misto diminutivo**: reduz a dívida e o caixa e reconhece despesa de juros |
| **Pagamento, em cheque, de duplicata** de R$ 6.000, **com desconto de 10%** | D Duplicatas a pagar 6.000 (−P) · C Bancos 5.400 (−A) · C Descontos obtidos 600 (+PL) | **Misto aumentativo**: o desconto obtido é **receita** |

## Resumo da classificação

| Classificação | Exemplos |
|---|---|
| **Permutativo** | Depósito bancário; compra de mercadorias a prazo; aplicação financeira; empréstimo bancário; pagamento de salários provisionados; compra de veículo; desconto de duplicatas |
| **Modificativo aumentativo** | Subscrição de capital; rendimentos financeiros |
| **Modificativo diminutivo** | Folha de pagamento apropriada; despesas administrativas pagas |
| **Misto aumentativo** | Venda de mercadorias à vista; pagamento de duplicata com desconto |
| **Misto diminutivo** | Pagamento de duplicata com juros |

## Pegadinhas

- "A subscrição de capital com integralização em dinheiro é fato permutativo" → **ERRADO** (modificativo aumentativo: aumentam o caixa e o capital social, e o PL cresce).
- "A obtenção de empréstimo bancário é fato modificativo, pois cria uma obrigação" → **ERRADO** (permutativo: +A/+P; o PL só muda com a apropriação dos juros, que é despesa).
- "Na venda à vista, a receita é lançada a débito" → **ERRADO** (receita é lançada a crédito; o débito é o do caixa, e o custo da mercadoria vendida também é débito).
- "O pagamento dos salários já provisionados diminui o patrimônio líquido" → **ERRADO** (permutativo: a despesa foi reconhecida na apropriação; o pagamento reduz o caixa e o passivo).
- "O pagamento de duplicata com juros é fato permutativo" → **ERRADO** (misto diminutivo).
- "O desconto de duplicatas em banco é uma operação que, na prática, equivale a um empréstimo" → **CERTO**.

## Relações com outros assuntos

- Tipos de fatos contábeis → `../04 - Atos e Fatos Administrativos/atos-e-fatos-administrativos.md`
- Elementos do lançamento e fórmulas → `lancamentos-e-retificacao.md`
- Natureza das contas usadas → `../03 - Contas/classificacao-e-natureza-das-contas.md`
- Partidas dobradas → `../03 - Contas/contas-e-partidas-dobradas.md`
- Balancete de verificação → `balancete-de-verificacao.md`

## Mapa mental

- Como ler
  - A, P, PL, débito e crédito; + aumenta e − diminui
  - Apropriação e regime de competência
- Permutativos (PL não muda)
  - Depósito, compra a prazo, aplicação, empréstimo, pagamento de salários provisionados, compra de veículo
  - Desconto de duplicatas: na prática, um empréstimo; três hipóteses no vencimento
- Modificativos
  - Aumentativos: subscrição de capital, rendimentos financeiros
  - Diminutivos: folha apropriada, despesas administrativas pagas
- Mistos
  - Aumentativos: venda à vista (receita e custo), pagamento com desconto
  - Diminutivo: pagamento com juros
