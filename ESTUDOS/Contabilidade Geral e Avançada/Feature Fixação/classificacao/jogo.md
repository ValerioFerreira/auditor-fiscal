# Classificação de contas

<!-- Jogo da Fixação. Formato e validações no comentário de carregar_jogo_classificacao (sistema/gerar.py). Fontes: caderno TecConcursos "Contabilidade" (F0001 a F4000), caderno de DRE (DRE:F0001...), aulas de Gilmar Possati e Igor Cintra, catálogos de bp/ e dre/ e o tema 03 - Contas. Histórias e explicações reescritas. -->

<!-- ===== Ativo circulante ===== -->

## caixa · Caixa
- Classe: patrimonial · ativo · devedora · normal · circulante · -
- Nomes: Caixa
- Por quê: Dinheiro em espécie (e cheques recebidos ainda não depositados) é disponibilidade, o item mais líquido do ativo circulante (Lei 6.404/76, art. 179, I). Como todo ativo, aumenta por débito e diminui por crédito.
- Liga: bp:ativo-circulante
- Questões: F0399, F0526, F1060, F1813, F2893, F2950, F2955, F3259, DRE:F0454, DRE:F0479, DRE:F0637, DRE:F0761
### Histórias
- Caixa | Uma loja vendeu quadros de madeira e recebeu metade do valor em dinheiro, no próprio balcão. (F0399)

## bancos · Bancos conta movimento
- Classe: patrimonial · ativo · devedora · normal · circulante · -
- Nomes: Banco conta movimento; Banco; Bancos; Bancos c/movimento; Conta corrente; Depósitos bancários
- Por quê: Depósitos à vista, que a empresa movimenta a qualquer momento, são disponibilidades do ativo circulante (Lei 6.404/76, art. 179, I). Se a conta ficar com saldo credor (cheque especial), o valor deixa de ser ativo e passa a ser obrigação no passivo circulante.
- Liga: bp:ativo-circulante
- Questões: F0399, F1056, F2887, DRE:F0454, DRE:F0465, DRE:F0479, DRE:F0489, DRE:F0591
### Histórias
- Banco conta movimento | Na mesma venda de quadros, um quarto do valor entrou por transferência na conta corrente que a empresa mantém no banco. (F0399)

## caixa-equivalentes · Caixa e equivalentes de caixa
- Classe: patrimonial · ativo · devedora · normal · circulante · -
- Nomes: Caixa e equivalentes de caixa; Caixa e equivalente de caixa; Caixa e equivalentes; Disponibilidades; Caixa e bancos; Caixa/Bancos
- Por quê: Linha que soma o dinheiro em espécie, os depósitos à vista e as aplicações de liquidez imediata; é o primeiro item do ativo circulante (Lei 6.404/76, art. 179, I; CPC 03, item 6). "Disponível" e "disponibilidades" são os nomes tradicionais do mesmo grupo.
- Liga: bp:ativo-circulante
- Questões: F0420, F0471, F1390, F2345, F2949, F3265, F3675, DRE:F0234, DRE:F0300, DRE:F0305, DRE:F0577, DRE:F0788
### Histórias
- Disponibilidades | No balanço, a empresa soma o dinheiro do cofre, o saldo da conta movimento e uma aplicação resgatável em 30 dias, feita há poucos dias. (F3265)

## equivalentes-caixa · Equivalentes de caixa
- Classe: patrimonial · ativo · devedora · normal · circulante · -
- Nomes: Equivalentes de caixa
- Por quê: Aplicações de curto prazo e alta liquidez, conversíveis em montante conhecido de caixa e com risco insignificante de mudança de valor; em regra, com vencimento de até 3 meses contados da aquisição (CPC 03, itens 6 e 7). Ficam no ativo circulante, somadas ao caixa; instrumentos patrimoniais (ações), em regra, não são equivalentes de caixa.
- Liga: bp:ativo-circulante
- Questões: F3257, F3265, F3428, F3467
### Histórias
- Equivalentes de caixa | A empresa aplicou a sobra do mês num título de altíssima liquidez, com risco quase nulo de oscilação e vencimento 60 dias depois da compra. (F3265, F3467)

## aplicacoes-financeiras · Aplicações financeiras
- Classe: patrimonial · ativo · devedora · normal · circulante · -
- Nomes: Aplicações financeiras; Aplicação financeira; Títulos públicos
- Depende: prazo
- Por quê: Recursos aplicados em títulos e fundos. Resgatáveis em até 3 meses da compra e com risco insignificante, são equivalentes de caixa; com vencimento até o fim do exercício seguinte, ativo circulante; depois disso, realizável a longo prazo (Lei 6.404/76, art. 179, I e II). Sem prazo informado, a banca as lê no ativo circulante.
- Liga: bp:ativo-circulante
- Questões: F0484, F2281, F2887, F3257, F3795, DRE:F0454, DRE:F0489, DRE:F0577
### Histórias
- Aplicações financeiras | No balanço de 31/12, a empresa tem um CDB comprado em dezembro, com vencimento em agosto do ano seguinte; o prazo passa de 3 meses, então não é equivalente de caixa. (F3257, F3265)

## clientes · Clientes
- Classe: patrimonial · ativo · devedora · normal · circulante · -
- Nomes: Clientes; Duplicatas a receber; Contas a receber; Contas a receber de clientes; Valores a receber de clientes; Créditos a receber; Títulos a receber
- Depende: prazo
- Por quê: Direito de receber por vendas ou serviços a prazo (Lei 6.404/76, art. 179, I). Sem prazo informado, a banca o lê no ativo circulante; com recebimento depois do fim do exercício seguinte, vai para o realizável a longo prazo, assim como, em qualquer prazo, os créditos fora do negócio usual com coligadas, controladas, diretores ou acionistas (art. 179, II). É ajustado pela PECLD e, quando relevante, pelo ajuste a valor presente.
- Liga: bp:ativo-circulante
- Questões: F0399, F0420, F0526, F1056, F1058, F1060, F2761, F2950, F2955, F3390, DRE:F0234, DRE:F0479
### Histórias
- Duplicatas a receber | A loja vendeu quadros de madeira e deixou um quarto do valor para receber em 30 dias. (F0399)
- Clientes | Uma consultoria prestou serviços em janeiro, com pagamento combinado para 31 de março; o cliente ganharia desconto se pagasse em fevereiro. (F0526)
- Valores a receber de clientes | Um supermercado vendeu em abril, recebeu 60% na hora e vai receber o restante em maio. (F2955)
- Duplicatas a receber | A empresa descontou no banco uma duplicata de serviço com vencimento em 90 dias: o título continua sendo direito dela, e a dívida com o banco vai para o passivo. (F2950)

## clientes-curto-prazo · Clientes (curto prazo)
- Classe: patrimonial · ativo · devedora · normal · circulante · -
- Nomes: Clientes (vencimento em 100 dias); Clientes (para receber em até 120 dias); Duplicatas a receber de clientes (recebimento em até 180 dias); Duplicatas a receber (vencimento em até 60 dias)
- Por quê: Com recebimento dentro do exercício seguinte, contado da data do balanço, o crédito é ativo circulante (Lei 6.404/76, art. 179, I; CPC 26, item 66). Só o recebimento depois do fim do exercício seguinte levaria ao realizável a longo prazo.
- Liga: bp:ativo-circulante
- Questões: F3675, DRE:F0300, DRE:F0301, DRE:F0305, DRE:F0309
### Histórias
- Clientes | No balanço de 31/12/X2, as duplicatas das vendas a prazo vencem em 100 dias. (DRE:F0300)

## outros-creditos · Outras contas a receber
- Classe: patrimonial · ativo · devedora · normal · circulante · -
- Nomes: Outras contas a receber
- Depende: prazo
- Por quê: Créditos que não vêm das vendas usuais (venda de um bem usado, aluguéis, juros ou dividendos a receber, cheques em cobrança). Com realização até o fim do exercício seguinte, ativo circulante (Lei 6.404/76, art. 179, I); depois disso, realizável a longo prazo (art. 179, II).
- Liga: bp:ativo-circulante
- Questões: DRE:F0577, DRE:F0580
### Histórias
- Outras contas a receber | A empresa vendeu um computador usado a um terceiro e vai receber o valor em 60 dias.

## pecld · (–) Perdas estimadas em créditos de liquidação duvidosa
- Classe: patrimonial · ativo · credora · retificadora · circulante · -
- Nomes: PECLD; PCLD; Perdas estimadas com crédito de liquidação duvidosa; Perdas estimadas com créditos de liquidação duvidosa; Perdas estimadas em créditos de liquidação duvidosa; Estimativa de perdas com créditos de liquidação duvidosa; Estimativa para perdas com créditos de liquidação duvidosa; Provisão para devedores duvidosos; Provisão para créditos de liquidação duvidosa; Prov. para crédito de liquidação duvidosa
- Por quê: Redutora de clientes: guarda a parte dos recebíveis que provavelmente não será recebida, sem baixar os títulos (Lei 6.404/76, art. 183, I, b; CPC 48); por retificar um ativo, tem natureza credora, e a contrapartida é a despesa com PECLD. Os nomes antigos "provisão para devedores duvidosos" (PDD) e "provisão para créditos de liquidação duvidosa" (PCLD) caíram em desuso porque, desde a convergência às normas internacionais, "provisão" designa só passivo (CPC 25).
- Liga: bp:ativo-circulante
- Questões: F0420, F0484, F0485, F1056, F1058, F1060, F2762, F2893, F3675, DRE:F0305, DRE:F0454, DRE:F0637
### Histórias
- PECLD | Em 31/12, a empresa estimou que não receberá R$ 28.000 de duplicatas de dois clientes em dificuldade, que vencem nos meses seguintes, e registrou a estimativa sem baixar os títulos. (F1056)
- Perdas estimadas em créditos de liquidação duvidosa | Uma duplicata de curto prazo julgada incobrável é baixada contra a conta que já guardava a estimativa dessa perda. (F1058)

## avp-clientes · (–) Ajuste a valor presente de clientes
- Classe: patrimonial · ativo · credora · retificadora · circulante · -
- Nomes: AVP – Receita financeira comercial a apropriar
- Depende: prazo
- Por quê: Juros embutidos numa venda a prazo e ainda não apropriados: reduzem o valor a receber até virarem receita financeira com o passar do tempo (Lei 6.404/76, art. 183, VIII; CPC 12). Por retificar um ativo, é credora, e segue o prazo do crédito que ajusta: circulante se o recebimento vence até o fim do exercício seguinte.
- Liga: bp:ativo-circulante
- Questões: F0485
### Histórias
- AVP – Receita financeira comercial a apropriar | A empresa vendeu por R$ 100.000 para receber em 8 meses; os R$ 24.000 de juros embutidos ficam numa conta que reduz o recebível até serem apropriados como receita financeira. (F0485)

## estoques · Estoques
- Classe: patrimonial · ativo · devedora · normal · circulante · -
- Nomes: Estoques; Estoque; Estoque de mercadorias; Estoques de mercadorias; Estoque de mercadorias (prazo médio de renovação de 80 dias); Estoque de mercadorias para revenda; Estoques de mercadorias para revenda; Mercadorias; Mercadorias para revenda; Mercadorias estoque; Estoque de produtos acabados; Matéria-prima
- Por quê: Bens mantidos para venda no curso normal dos negócios, em produção ou para consumo na produção (CPC 16, item 6) são ativo circulante (Lei 6.404/76, art. 179, I), avaliados pelo custo ou pelo valor realizável líquido, se menor (art. 183, II; CPC 16, item 9). O custo inclui frete, seguro e tributos não recuperáveis da compra e exclui os recuperáveis; só a venda prevista para depois do exercício seguinte levaria o estoque ao realizável a longo prazo.
- Liga: bp:ativo-circulante
- Questões: F0616, F0865, F0903, F0936, F1813, F2848, F2893, F2949, F3675, DRE:F0010, DRE:F0163, DRE:F0305
### Histórias
- Estoques | Depois de vender 80% do lote comprado em novembro, a empresa ainda guarda o restante para revender nos primeiros meses do ano seguinte. (F0903)
- Estoque de mercadorias | O frete e o seguro pagos para trazer um lote até o depósito somam-se ao custo das mercadorias, que ainda não foram vendidas. (DRE:F0163, F0890)
- Matéria-prima | Uma indústria comprou a prazo um lote de matéria-prima que será consumido na produção nos próximos meses. (F2893)
- Estoque de produtos acabados | Uma indústria terminou a fabricação de um lote, que aguarda venda nos próximos meses. (F2848)

## estoque-inicial-final · Estoque inicial e estoque final de mercadorias
- Classe: patrimonial · ativo · devedora · normal · circulante · -
- Nomes: Estoque inicial; Estoque inicial de mercadorias; Estoque inicial de mercadorias para revenda; Estoque final de mercadorias; Estoque final de mercadorias para revenda
- Por quê: No inventário periódico, a conta de mercadorias guarda o saldo do início do exercício até a apuração do resultado; o estoque final é o que a contagem física encontra no encerramento e é o que vai para o balanço. Os dois são o saldo do mesmo ativo circulante em datas diferentes e entram no cálculo do CMV (CMV = EI + compras líquidas − EF); nenhum deles é despesa.
- Liga: dre:calculo-cmv
- Questões: F3116, F3121, DRE:F0452, DRE:F0479, DRE:F0480, DRE:F0577, DRE:F0580, DRE:F0637, DRE:F0761, DRE:F0764
### Histórias
- Estoque inicial de mercadorias | Empresa com inventário periódico: no balancete de fim de ano, a conta de mercadorias ainda mostra o saldo contado no início do exercício. (DRE:F0761)
- Estoque final de mercadorias | Na contagem física de 31/12, sobraram mercadorias que serão revendidas no ano seguinte, e o valor delas vai para o balanço. (DRE:F0479)

## perdas-estoques · (–) Perdas estimadas em estoques
- Classe: patrimonial · ativo · credora · retificadora · circulante · -
- Nomes: Provisão para perda de estoques
- Por quê: Redutora que leva o estoque ao valor realizável líquido (preço de venda estimado menos os gastos para vender) quando ele fica abaixo do custo (Lei 6.404/76, art. 183, II; CPC 16, itens 9 e 28 a 34); a contrapartida é despesa do período em que a redução ocorre. "Provisão" é o nome antigo: depois da convergência, a palavra ficou reservada ao passivo (CPC 25), e o ajuste passou a se chamar perda estimada.
- Liga: bp:ativo-circulante
- Questões: F0767, F0874, F0876, F0899, DRE:F0479, DRE:F0480
### Histórias
- Provisão para perda de estoques | Um produto que custou R$ 250.000 só será vendido por R$ 220.000, com mais R$ 10.000 de gastos para vender, por causa de uma tecnologia nova; a diferença fica numa conta que reduz o estoque. (F0876)

## material-consumo · Material de consumo
- Classe: patrimonial · ativo · devedora · normal · circulante · -
- Nomes: Material de consumo; Material de expediente; Material de limpeza e conservação
- Por quê: Materiais comprados para uso próprio e ainda não usados são bens do ativo circulante (Lei 6.404/76, art. 179, I). À medida que são consumidos, saem do ativo e viram despesa (despesa de material).
- Liga: bp:ativo-circulante
- Questões: F2887, DRE:F0465, DRE:F0466, DRE:F0577, DRE:F0591
### Histórias
- Material de limpeza e conservação | No balancete, ao lado da despesa com o material de limpeza já usado, aparece o saldo dos produtos de limpeza ainda guardados no almoxarifado. (DRE:F0465)

## tributos-recuperar · Tributos a recuperar
- Classe: patrimonial · ativo · devedora · normal · circulante · -
- Nomes: ICMS a recuperar; Impostos a recuperar; Tributos recuperáveis; Impostos recuperáveis
- Por quê: Tributo pago na compra que a lei permite compensar com o devido nas vendas (ICMS, IPI, PIS e Cofins não cumulativos) não entra no custo do estoque (CPC 16, item 11): vira um direito no ativo circulante, compensado nos meses seguintes (Lei 6.404/76, art. 179, I).
- Liga: bp:ativo-circulante
- Questões: F0865, F0890, F0902, F0903, F0905, F0932, F2887, F2956, F3121, DRE:F0010
### Histórias
- ICMS a recuperar | Na compra à vista de mercadorias para revenda por R$ 50.000, R$ 9.000 de ICMS poderão ser abatidos do ICMS das próximas vendas. (F0865)
- Tributos recuperáveis | Na importação de mercadorias, a empresa pagou impostos locais que vai compensar com os impostos devidos quando as vender, nos meses seguintes. (DRE:F0010, F0932)

## adiantamento-fornecedores · Adiantamento a fornecedores
- Classe: patrimonial · ativo · devedora · normal · circulante · -
- Nomes: Adiantamento a fornecedores; Adiantamentos a fornecedores; Adiantamento a fornecedores (recebimento em 110 dias); Adiantamento a fornecedor de curto prazo
- Por quê: Pagamento feito antes de receber o bem ou o serviço é um direito (receber a mercadoria), não despesa nem estoque: fica no ativo circulante até a entrega, quando vira estoque (Lei 6.404/76, art. 179, I). Adiantamento para comprar imobilizado acompanha o imobilizado; e não confunda com adiantamento de clientes, que é passivo.
- Liga: bp:ativo-circulante
- Questões: F2887, F2949, F3675, DRE:F0234, DRE:F0305
### Histórias
- Adiantamento a fornecedores | A empresa pagou R$ 64.000 a um fornecedor para que ele entregue as mercadorias até o fim do mês. (F2949)
- Adiantamento a fornecedores | Em 31/12, a companhia já tinha pago ao fornecedor por mercadorias que só chegaram em 12 de janeiro. (DRE:F0234)

## adiantamento-empregados · Adiantamento a empregados
- Classe: patrimonial · ativo · devedora · normal · circulante · -
- Nomes: Adiantamento de salários
- Por quê: Parte do salário paga antes do vencimento da folha é um direito da empresa, que será descontado do salário a pagar; fica no ativo circulante (Lei 6.404/76, art. 179, I) e não é despesa antes da competência do salário.
- Liga: bp:ativo-circulante
- Questões: DRE:F0591
### Histórias
- Adiantamento de salários | No dia 20, a empresa entregou aos empregados parte do salário do mês, que será descontada quando a folha for paga.

## despesas-antecipadas · Despesas antecipadas
- Classe: patrimonial · ativo · devedora · normal · circulante · -
- Nomes: Despesas antecipadas; Despesa antecipada; Despesas antecipadas de seguros; Despesas antecipadas de aluguel; Despesas antecipadas de aluguéis; Seguros pagos antecipadamente; Seguros pagos antecipadamente (vencimento em 7 meses); Despesas pagas antecipadamente (utilização até 220 dias); Seguros antecipados; Seguro antecipado; Aluguel antecipado; Assinaturas antecipadas
- Por quê: Gasto já pago cujo benefício será usado depois (seguro, aluguel, assinatura): pelo regime de competência, fica no ativo e vira despesa à medida que o período passa. Usado até o fim do exercício seguinte, é ativo circulante (Lei 6.404/76, art. 179, I: "aplicações de recursos em despesas do exercício seguinte"); a parte de exercícios posteriores vai para o realizável a longo prazo.
- Liga: bp:ativo-circulante
- Questões: F2345, F2887, F2950, DRE:F0163, DRE:F0300, DRE:F0305, DRE:F0452, DRE:F0465, DRE:F0479, DRE:F0489, DRE:F0591, DRE:F0637
### Histórias
- Seguros antecipados | Em 1º de janeiro, a empresa pagou à vista o seguro de um ano do prédio administrativo; a cada mês, um doze avos vira despesa. (F2345)
- Despesas pagas antecipadamente | No balanço, há gastos já pagos que serão consumidos ao longo dos próximos 220 dias. (DRE:F0305)

<!-- ===== Ativo não circulante ===== -->

## clientes-lp · Clientes (longo prazo)
- Classe: patrimonial · ativo · devedora · normal · nao-circulante · rlp
- Nomes: Duplicatas a receber — longo prazo
- Por quê: Direito de receber por vendas a prazo que vence depois do fim do exercício seguinte ao do balanço: realizável a longo prazo (Lei 6.404/76, art. 179, II). As parcelas que vencem nos 12 meses seguintes continuam no circulante.
- Liga: bp:rlp
- Questões: DRE:F0522
### Histórias
- Duplicatas a receber | A loja vendeu mercadorias em 30 parcelas mensais; pergunta-se pelas parcelas que só vencem depois do fim do exercício seguinte ao do balanço.

## creditos-lp · Títulos e empréstimos a receber de longo prazo
- Classe: patrimonial · ativo · devedora · normal · nao-circulante · rlp
- Nomes: Títulos a receber de longo prazo; Empréstimos a receber de longo prazo
- Por quê: Créditos realizáveis depois do término do exercício social seguinte vão para o realizável a longo prazo (Lei 6.404/76, art. 179, II). O prazo se conta da data do balanço, e não da data em que o crédito nasceu.
- Liga: bp:rlp
- Questões: DRE:F0578, DRE:F0803, DRE:F0804, DRE:F0805
### Histórias
- Títulos a receber | Ao vender um carro velho da frota a um comprador sem vínculo com a empresa, ela aceitou uma nota promissória que vence daqui a dois anos e meio.

## creditos-ligadas · Créditos com sociedades ligadas e administradores (negócios não usuais)
- Classe: patrimonial · ativo · devedora · normal · nao-circulante · rlp
- Por quê: Empréstimos e adiantamentos a coligadas, controladas, diretores, acionistas ou participantes no lucro, fora dos negócios usuais da empresa, vão para o realizável a longo prazo qualquer que seja o vencimento (Lei 6.404/76, art. 179, II). A banca costuma dar um vencimento curto para induzir o circulante.
- Liga: bp:rlp
- Questões: F2792
### Histórias
- Empréstimo à coligada | A consultoria, que tem participação permanente numa coligada, emprestou-lhe dinheiro no fim de dezembro para receber em outubro do ano seguinte. (F2792)
- Empréstimo a diretor | A loja de roupas emprestou dinheiro a um dos seus diretores, para devolução em três meses.

## despesas-antecipadas-lp · Despesas antecipadas (longo prazo)
- Classe: patrimonial · ativo · devedora · normal · nao-circulante · rlp
- Por quê: Despesa paga antes de o serviço ser usado é um direito: a parte que será apropriada nos 12 meses seguintes fica no circulante e a parte posterior vai para o realizável a longo prazo (Lei 6.404/76, art. 179, I e II). A banca separa os valores ano a ano.
- Liga: bp:rlp
- Questões: F1445, F2890
### Histórias
- Seguro antecipado | Em 1º de janeiro, a pizzaria comprou uma moto e pagou à vista o seguro dela para dois anos; pergunta-se, na data da compra, pela parte que cobre o segundo ano. (F2890)
- Manutenção paga antecipadamente | A firma de auditoria pagou de uma vez a manutenção anual dos computadores pelos cinco anos de vida útil; pergunta-se, na data do pagamento, pela parte que cobre do segundo ao quinto ano. (F1445)

## ativo-fiscal-diferido · Ativo fiscal diferido
- Classe: patrimonial · ativo · devedora · normal · nao-circulante · rlp
- Nomes: Ativos fiscais diferidos; Ativo fiscal diferido
- Por quê: IR e CSLL a recuperar no futuro por prejuízos fiscais, bases negativas e diferenças temporárias dedutíveis, reconhecidos só quando for provável haver lucro tributável suficiente (CPC 32). Nunca vai para o circulante (CPC 26, item 56) e costuma ficar no realizável a longo prazo. Depreciação fiscal acelerada gera o contrário: passivo fiscal diferido (F2090).
- Liga: bp:rlp
- Questões: F2272, F2090
### Histórias
- Ativo fiscal diferido | A S.A. acumulou prejuízos fiscais e bases negativas de CSLL e tem projeções de lucro tributável que sustentam a compensação deles nos próximos anos. (F2272)

## participacoes-societarias · Participações permanentes em outras sociedades
- Classe: patrimonial · ativo · devedora · normal · nao-circulante · investimentos
- Nomes: Participações em Outras Companhias; Participações permanentes em outras empresas; Ações de controladas; Ações de coligadas; Investimentos permanentes; Participação permanente em outra sociedade; Investimentos na Sociedade B; Participações Societárias
- Por quê: Participações que a empresa pretende manter, e não negociar, ficam em investimentos (Lei 6.404/76, art. 179, III). Coligadas, controladas e controladas em conjunto são avaliadas pela equivalência patrimonial (art. 248; CPC 18); ações compradas para vender no curto prazo vão para o circulante.
- Liga: bp:investimentos
- Questões: F0478, F1241, F1305, F1347, F2792, F3378, F3434, DRE:F0494, DRE:F0522, DRE:F0578, DRE:F0583, DRE:F0803
### Histórias
- Participação permanente em outra sociedade | A livraria, além de comprar livros para vender até janeiro, adquiriu uma participação que pretende manter de forma permanente em outra sociedade. (F0478)
- Investimentos na Sociedade B | A Sociedade A tem 65% das ações com voto da Sociedade B e a controla; no fim do ano, registrou a sua parte no lucro de B. (F1305)
- Ações de coligadas | A fabricante de móveis comprou 40% das ações de uma fábrica de colchões e passou a ter influência significativa sobre ela. (F1241)
- Participações Societárias | A Cia. A divide com a Cia. X o controle da Cia. B e avalia essa participação pela equivalência patrimonial. (F1347)

## propriedades-investimento · Propriedades para investimento
- Classe: patrimonial · ativo · devedora · normal · nao-circulante · investimentos
- Nomes: Propriedade para investimento; Propriedades para investimento; Propriedade Para Investimento (PPI); Imóvel para valorização futura; Imóvel destinado exclusivamente à valorização
- Por quê: Terreno ou edificação (ou parte dela) mantido para renda de aluguel ou valorização, e não para uso próprio nem para venda no curso normal dos negócios, é propriedade para investimento (CPC 28, item 5); no balanço da Lei fica em investimentos (art. 179, III), em linha própria (CPC 26, item 54). Decide o uso que a dona faz: alugado a terceiros é propriedade para investimento, mesmo que o locatário o use na atividade dele; ocupado pela própria entidade ou alugado a empregados é imobilizado (CPC 28, item 9).
- Liga: bp:propriedade-investimento
- Questões: F1183, F1186, F1190, F1193, F1199, F1209, F1214, F1222, F1226, F1409, F2852, F3057
### Histórias
- Prédio | A empresa, cujo negócio é arrendar imóveis, alugou um prédio inteiro a uma escola por dois anos, num arrendamento operacional; a escola usa um andar para a secretaria e os outros para as aulas. (F1409)
- Casas | A administradora de imóveis tem casas num condomínio que estão alugadas a terceiros ou em reforma para futura locação; pergunta-se por essas casas. (F1214)
- Imóvel | A consultoria aluga um imóvel a terceiros; a diretoria decidiu ocupá-lo quando o contrato acabar, daqui a 18 meses, mas a ocupação ainda não começou. (F1199)
- Prédio em construção | Perto de onde vão erguer um shopping, a firma de contabilidade comprou um terreno e começou a construir um prédio para alugar a terceiros quando ficar pronto. (F1193)
- Andares | No prédio de uma escola, dois andares são alugados a outras empresas e dois a pessoas de fora, que moram ali. (F1222)
- Terreno | A S.A. comprou um terreno a prazo para obter renda alugando-o. (F1209)

## terrenos-valorizacao · Terrenos para valorização
- Classe: patrimonial · ativo · devedora · normal · nao-circulante · investimentos
- Nomes: Terreno mantido para valorização do capital a longo prazo
- Por quê: Terreno mantido para valorização de longo prazo, ou comprado sem uso definido, é propriedade para investimento (CPC 28, item 8, a e b), no subgrupo investimentos. Se a entidade começar obras para usá-lo, passa ao imobilizado; se o puser à venda com plano firme, passa a mantido para venda (CPC 31).
- Liga: bp:propriedade-investimento
- Questões: F1178, F1180, F1187, F1189, F1194, F1207, F1367, F1380
### Histórias
- Terreno | O escritório de advocacia comprou um terreno vizinho apenas para ganhar com a valorização no longo prazo. (F1194)
- Terreno | A sociedade comprou um terreno e, na data da compra, ainda não tinha decidido o que faria com ele. (F1180)
- Terrenos | A loteadora tirou dois terrenos do estoque à venda e decidiu mantê-los por anos, esperando a valorização da região. (F1207)
- Terreno | Até o fim de 2024, a consultoria tributária mantinha um terreno só pela valorização, sem nenhuma obra começada. (F1189)

## mais-valia · Mais-valia de ativos líquidos (balanço individual)
- Classe: patrimonial · ativo · devedora · normal · nao-circulante · investimentos
- Nomes: Mais-valia; Mais-valia do terreno
- Por quê: Na compra de participação avaliada pela equivalência, a parte do preço que corresponde à diferença entre o valor justo e o valor contábil dos ativos líquidos da investida fica destacada dentro de investimentos, no balanço individual da investidora (CPC 18, item 32; ICPC 09). Realiza-se à medida que o ativo que a originou é depreciado, baixado ou vendido; no consolidado não aparece, porque os ativos da controlada já entram pelo valor justo.
- Liga: bp:investimentos
- Questões: F1279, F1290, F1333, F1334, F1335, F1336, F1344
### Histórias
- Mais-valia | A Compra Tudo pagou por 80% da Perspectiva exatamente a sua parte no valor justo dos ativos líquidos; a diferença para o patrimônio líquido contábil vinha de um imóvel registrado pelo custo. Pergunta-se, no balanço individual, por essa parcela do investimento. (F1335)
- Mais-valia do terreno | Parte do que a investidora pagou pelo controle, acima do valor contábil, se explica por um terreno da investida que vale mais que o registrado; pergunta-se, no balanço individual, por essa parte. (F1344)

## goodwill-investimentos · Goodwill na compra de participação (balanço individual)
- Classe: patrimonial · ativo · devedora · normal · nao-circulante · investimentos
- Nomes: Ágio na aquisição
- Depende: subgrupo
- Por quê: Na compra de participação em controlada ou coligada, o que se paga acima da parte no valor justo dos ativos líquidos é ágio por rentabilidade futura; no balanço individual da investidora ele integra a conta de investimentos (CPC 18, item 32; ICPC 09), e no consolidado aparece no intangível. Não é amortizado.
- Liga: bp:investimentos
- Questões: F1333, F1335, F1344, F1925, F1926
### Histórias
- Ágio na aquisição | A Todas as Bebidas pagou R$ 42 milhões por 80% de uma empresa cujos ativos líquidos valiam R$ 45 milhões a valor justo; pergunta-se, no balanço individual da compradora, pela parcela paga acima dos R$ 36 milhões. (F1333)
- Goodwill | A Cia X comprou 100% da Cia Y por um preço que se explica pelo bom posicionamento da Y no mercado; pergunta-se pelo goodwill no balanço individual da Cia X. (F1925)

## provisao-perdas-investimentos · (–) Provisão para perdas em investimentos
- Classe: patrimonial · ativo · credora · retificadora · nao-circulante · investimentos
- Nomes: Provisão para perda de investimentos
- Por quê: Reduz o valor de participações permanentes pela perda provável na sua realização (Lei 6.404/76, art. 183, III); retifica ativo, logo tem saldo credor. "Provisão" é o nome antigo: hoje se fala em perda por redução ao valor recuperável (CPC 01; CPC 18).
- Liga: bp:investimentos
- Questões: DRE:F0583
### Histórias
- Provisão para perda de investimentos | A investidora concluiu que parte do valor de uma participação permanente não será recuperada e registrou a perda sem baixar o investimento.

## terrenos-uso · Terrenos (uso)
- Classe: patrimonial · ativo · devedora · normal · nao-circulante · imobilizado
- Nomes: Terrenos; Terreno
- Depende: prazo; subgrupo
- Por quê: Terreno usado nas atividades (sede, fábrica, estacionamento dos empregados) é imobilizado (Lei 6.404/76, art. 179, IV; CPC 27) e não se deprecia, porque a vida útil é ilimitada. Mantido para renda ou valorização é propriedade para investimento; o de uma loteadora, à venda no curso normal dos negócios, é estoque.
- Liga: bp:imobilizado
- Questões: F1189, F1194, F1306, F1628, F3221, F3378, F3434, F3470, DRE:F0522, DRE:F0583
### Histórias
- Terreno | A consultoria jurídica comprou um terreno ao lado do escritório para construir o estacionamento dos funcionários. (F1194, F1628)
- Terreno | A partir de janeiro de 2025, a consultoria tributária começou obras no terreno que mantinha para valorização, para ali instalar a sua futura sede. (F1189)
- Terreno | A consultoria jurídica comprou um terreno onde vai construir a sua nova sede. (F1194)

## imoveis-uso · Imóveis de uso
- Classe: patrimonial · ativo · devedora · normal · nao-circulante · imobilizado
- Nomes: Imóveis; Prédio
- Depende: prazo; subgrupo
- Por quê: Imóvel ocupado pela própria entidade na sua atividade é imobilizado (Lei 6.404/76, art. 179, IV; CPC 27), inclusive o alugado a empregados (CPC 28, item 9, c). Alugado a terceiros ou mantido para valorização é propriedade para investimento; o de uma incorporadora, construído para vender, é estoque.
- Liga: bp:imobilizado
- Questões: F1199, F1214, F1222, F1409, DRE:F0494
### Histórias
- Casas | A administradora de imóveis usa duas casas do condomínio na própria operação e aluga outras três, por valor reduzido, aos seus funcionários e às famílias deles. (F1214)
- Andares | A escola presta os seus serviços nos cinco primeiros andares do prédio e aluga outro andar para funcionários vindos de outras cidades morarem. (F1222)

## benfeitorias-terceiros · Benfeitorias em propriedades de terceiros
- Classe: patrimonial · ativo · devedora · normal · nao-circulante · imobilizado
- Nomes: Benfeitorias em Propriedades de Terceiros
- Por quê: Reformas e instalações feitas num imóvel alugado são imobilizado de quem aluga para usar, que controla os benefícios durante o contrato (Lei 6.404/76, art. 179, IV; CPC 27). São amortizadas pelo prazo do contrato ou pela vida útil, o que for menor; por isso a retificadora delas se chama amortização acumulada, embora fique no imobilizado.
- Liga: bp:imobilizado
- Questões: DRE:F0494
### Histórias
- Benfeitorias em propriedades de terceiros | A loja alugou um imóvel por cinco anos e pagou a instalação de divisórias, piso e iluminação para funcionar ali.

## maquinas-equipamentos · Máquinas e equipamentos
- Classe: patrimonial · ativo · devedora · normal · nao-circulante · imobilizado
- Nomes: Máquinas e equipamentos; Máquina industrial; Equipamento industrial
- Por quê: Bens corpóreos usados na produção ou nos serviços por mais de um exercício são imobilizado (Lei 6.404/76, art. 179, IV; CPC 27). O custo inclui frete, tributos não recuperáveis, preparação do local, instalação, montagem e a estimativa de desmontagem; propaganda do novo produto é despesa. Software sem o qual a máquina não funciona faz parte dela (CPC 04, item 4).
- Liga: bp:imobilizado
- Questões: F1441, F1804, F1872, F1900, F3221, F3434, F3470, DRE:F0522
### Histórias
- Máquina injetora | A fábrica de plásticos importou uma máquina injetora para uma nova linha de produtos e pagou a preparação do local, a instalação e a montagem. (F1872)
- Software | A empresa comprou uma máquina-ferramenta que só funciona controlada por um software específico, adquirido junto com ela. (F1441)

## veiculos · Veículos
- Classe: patrimonial · ativo · devedora · normal · nao-circulante · imobilizado
- Nomes: Veículos
- Depende: prazo; subgrupo
- Por quê: Veículos usados na atividade (frota, entregas, uso da diretoria) são imobilizado (Lei 6.404/76, art. 179, IV). Na concessionária, os veículos à venda são estoque; os que ela usa (test-drive, diretores) continuam no imobilizado e são depreciados.
- Liga: bp:imobilizado
- Questões: F1622, F3378, DRE:F0494, DRE:F0578, DRE:F0583
### Histórias
- Veículos | A concessionária separa alguns carros para os clientes fazerem test-drive e outros para uso dos diretores; pergunta-se por esses carros. (F1622)
- Veículos | A empresa renovou toda a frota, comprando veículos adequados às suas necessidades dos próximos cinco anos. (DRE:F0494)

## moveis-utensilios · Móveis e utensílios
- Classe: patrimonial · ativo · devedora · normal · nao-circulante · imobilizado
- Nomes: Móveis e utensílios
- Por quê: Móveis usados no escritório ou na loja são imobilizado (Lei 6.404/76, art. 179, IV). Comprados usados, são depreciados pelo tempo que a própria empresa espera usá-los, descontado o valor residual (CPC 27).
- Liga: bp:imobilizado
- Questões: F1629, DRE:F0583
### Histórias
- Móveis | A Cia X comprou de outra empresa móveis com dois anos de uso para mobiliar o seu escritório e pretende usá-los por cinco anos. (F1629)

## computadores · Computadores
- Classe: patrimonial · ativo · devedora · normal · nao-circulante · imobilizado
- Nomes: Computadores
- Por quê: Computadores usados pelos empregados são imobilizado (Lei 6.404/76, art. 179, IV; CPC 27). Manutenção paga adiantada não entra no custo: é despesa antecipada.
- Liga: bp:imobilizado
- Questões: F1445, F1502
### Histórias
- Computadores | A firma de auditoria comprou a prazo computadores para os seus funcionários, com vida útil estimada em cinco anos. (F1445)
- Computadores | A sociedade ZZ comprou computadores para os colaboradores usarem por três anos. (F1502)

## pecas-reposicao-imobilizado · Peças de reposição usadas por mais de um período
- Classe: patrimonial · ativo · devedora · normal · nao-circulante · imobilizado
- Por quê: Peças sobressalentes que se espera usar por mais de um período, ou só com um item do imobilizado, são imobilizado (CPC 27, item 8); as de consumo rápido ficam em estoque.
- Liga: bp:imobilizado
- Questões: F1502
### Histórias
- Peças de reposição | Junto com os computadores, a sociedade ZZ comprou peças de reposição para usar ao longo dos três anos de vida útil das máquinas. (F1502)

## direito-uso · Direito de uso (arrendamento)
- Classe: patrimonial · ativo · devedora · normal · nao-circulante · imobilizado
- Nomes: Ativo de direito de uso
- Por quê: O arrendatário reconhece como ativo o direito de usar o bem arrendado, em contrapartida do passivo de arrendamento (CPC 06 (R2)). Sendo o bem tangível, o ativo vai para o imobilizado (Lei 6.404/76, art. 179, IV, que inclui bens cujos benefícios, riscos e controle foram transferidos), podendo aparecer em linha separada (CPC 06, item 47).
- Liga: bp:imobilizado
- Questões: F1518
### Histórias
- Direito de uso | A transportadora arrendou um caminhão por quatro anos, com pagamentos mensais, e o usa com exclusividade nas suas entregas.

## depreciacao-acumulada · (–) Depreciação acumulada
- Classe: patrimonial · ativo · credora · retificadora · nao-circulante · imobilizado
- Nomes: Depreciação acumulada; Depreciação acumulada — máquinas e equipamentos; Depreciação e amortização acumulada do imobilizado
- Por quê: Soma o desgaste já registrado dos bens do imobilizado e reduz o seu valor, sem baixá-los (Lei 6.404/76, art. 183, § 2º, a); retifica ativo, logo tem saldo credor. A depreciação do período é despesa, conta de resultado; terreno não se deprecia.
- Liga: bp:imobilizado
- Questões: F1719, F1798, F3057, DRE:F0494, DRE:F0522, DRE:F0578, DRE:F0583, DRE:F0803
### Histórias
- Depreciação acumulada | A usina que entrou em operação em janeiro teve registrado, no fim do ano, o desgaste do primeiro dos seus 20 anos de vida útil, sem baixa do bem. (F1719)
- Depreciação acumulada | No balanço da Tank, o imobilizado aparece pelo custo de aquisição menos o desgaste já apropriado e menos a perda por impairment; pergunta-se pela conta do desgaste. (F1798)

## perdas-impairment-imobilizado · (–) Perdas por redução ao valor recuperável (imobilizado)
- Classe: patrimonial · ativo · credora · retificadora · nao-circulante · imobilizado
- Nomes: Provisão para perda de valor recuperável
- Depende: subgrupo
- Por quê: Quando o valor contábil passa do valor recuperável (o maior entre o valor em uso e o valor justo menos as despesas de venda), a perda vai para o resultado e o saldo acumulado reduz o ativo (CPC 01; Lei 6.404/76, art. 183, § 3º). Pode ser revertida depois, até o valor que o bem teria sem a perda; "provisão" é o nome antigo.
- Liga: bp:imobilizado
- Questões: F1798, F1804, F1872, F1878, F1900
### Histórias
- Perda por desvalorização (impairment) | No balanço da Tank, o custo de um bem do imobilizado aparece reduzido pela depreciação acumulada e pelo saldo de uma perda por desvalorização reconhecida em teste anterior. (F1798)
- Provisão para perda de valor recuperável | O equipamento industrial vale menos, em uso e na venda, do que o seu valor contábil líquido, e a empresa registra a diferença sem baixar o bem. (F1900)

## patentes · Patentes
- Classe: patrimonial · ativo · devedora · normal · nao-circulante · intangivel
- Nomes: Patentes; Patentes registradas
- Por quê: Direitos sobre invenções, sem substância física, usados na atividade: intangível (Lei 6.404/76, art. 179, VI; CPC 04). Amortizam-se pelo prazo de proteção ou de uso, o que for menor.
- Liga: bp:intangivel
- Questões: DRE:F0522, DRE:F0583
### Histórias
- Patentes | A indústria comprou de um inventor o direito exclusivo de explorar, por 15 anos, o processo patenteado que usa na fábrica.

## marcas · Marcas
- Classe: patrimonial · ativo · devedora · normal · nao-circulante · intangivel
- Nomes: Marcas; Marca
- Por quê: Marca adquirida, ou identificada numa combinação de negócios, é intangível (Lei 6.404/76, art. 179, VI; CPC 04). Com vida útil indefinida, não se amortiza e passa por teste de impairment todo ano (CPC 01); marca gerada internamente não se reconhece como ativo (CPC 04, item 63).
- Liga: bp:intangivel
- Questões: F1306, F1826, F1899, F1926, DRE:F0578, DRE:F0583
### Histórias
- Marca | A Cia. Lira tem no balanço uma marca sem prazo previsível para deixar de gerar benefícios e a testa todos os anos para impairment. (F1899)

## softwares · Softwares
- Classe: patrimonial · ativo · devedora · normal · nao-circulante · intangivel
- Nomes: Softwares
- Depende: subgrupo
- Por quê: Software que funciona separado de um equipamento é intangível (CPC 04); se for parte integrante do hardware, sem o qual a máquina não funciona, é imobilizado (CPC 04, item 4). Customizações próprias que a empresa controla e que geram benefícios futuros também se ativam no intangível.
- Liga: bp:intangivel
- Questões: F1441, F1518, F1522
### Histórias
- Softwares | O radar de controle aéreo veio com softwares que não são parte integrante do equipamento e servem a outras finalidades; é possível atribuir valor a cada componente. (F1522)
- Customizações do software | A companhia contratou software em nuvem e desenvolveu módulos próprios, exclusivos e transferíveis para outro fornecedor, que atendem aos critérios de identificação, controle e benefícios futuros. (F1518)

## licencas-software · Licenças de uso de software
- Classe: patrimonial · ativo · devedora · normal · nao-circulante · intangivel
- Nomes: Licença de uso de software; Licença de software; Licença exclusiva para uso de um software
- Por quê: Licença de uso de software independente do hardware é intangível, mesmo com prazo de poucos anos: não se divide entre circulante e longo prazo, apenas se amortiza (CPC 04). O custo é o preço menos descontos, mais tributos de importação e a preparação para o uso; treinamento é despesa.
- Liga: bp:intangivel
- Questões: F1514, F1535, F1570, F1643, F1871
### Histórias
- Licença de software | A entidade pagou uma licença para usar, por três anos, um software não vinculado a nenhum equipamento. (F1514)
- Licença de uso de software | A Batucada comprou por oito anos a licença do software de controle da produção e pagou imposto de importação e a integração com os seus sistemas. (F1570)

## goodwill · Goodwill (combinação de negócios)
- Classe: patrimonial · ativo · devedora · normal · nao-circulante · intangivel
- Nomes: Goodwill; Ágio por expectativa de rentabilidade futura (goodwill); Ágio derivado da expectativa de rentabilidade futura (goodwill); Ágio por expectativa de resultados futuros; Ágio pago por expectativa de resultados futuros
- Depende: subgrupo
- Por quê: É o que se paga, numa combinação de negócios, acima do valor justo dos ativos líquidos identificáveis (CPC 15). No consolidado e na incorporadora fica no intangível (Lei 6.404/76, art. 179, VI, "fundo de comércio adquirido"); no balanço individual da controladora, dentro de investimentos (ICPC 09). Não é amortizado, é testado todo ano e a perda não se reverte (CPC 01); o gerado internamente não se reconhece.
- Liga: bp:intangivel
- Questões: F1233, F1545, F1583, F1603, F1826, F1849, F1873, F1880, F1896
### Histórias
- Goodwill | A Cia. Gama incorporou a Cia. Beta pagando mais que o valor justo dos ativos líquidos recebidos; a diferença ficou no balanço da própria Gama, que absorveu a Beta.
- Ágio por expectativa de rentabilidade futura (goodwill) | No balanço consolidado do grupo, a controladora apresenta o ágio que pagou, acima do valor justo dos ativos líquidos, na compra da controlada.

## amortizacao-acumulada · (–) Amortização acumulada
- Classe: patrimonial · ativo · credora · retificadora · nao-circulante · intangivel
- Nomes: Amortização acumulada; Amortização acumulada — patentes
- Por quê: Soma a amortização já registrada dos intangíveis de vida útil definida e reduz o seu valor (Lei 6.404/76, art. 183, § 2º, b); retifica ativo, logo tem saldo credor. Intangível de vida útil indefinida e goodwill não se amortizam; benfeitorias em imóvel de terceiros também se amortizam, mas dentro do imobilizado.
- Liga: bp:intangivel
- Questões: F1641, F1643, F1808, F1832, F3057, DRE:F0522
### Histórias
- Amortização acumulada | A Dedalus comprou em julho uma licença de software para cinco exercícios e registrou em dezembro a parte já consumida, sem baixar a licença. (F1643)
- Amortização acumulada | No balanço, o ativo intangível de vida útil definida em 20 anos aparece pelo custo de aquisição menos a parte já apropriada ao resultado. (F1832)

## perdas-impairment-intangivel · (–) Perdas por redução ao valor recuperável (intangível)
- Classe: patrimonial · ativo · credora · retificadora · nao-circulante · intangivel
- Nomes: (-) Perda por desvalorização (impairment)
- Depende: subgrupo
- Por quê: Saldo das perdas por impairment reconhecidas sobre um intangível, que reduz o seu valor contábil (CPC 01; Lei 6.404/76, art. 183, § 3º); retifica ativo, logo tem saldo credor. Pode ser revertido até o valor que o ativo teria sem a perda, salvo no goodwill, cuja perda nunca se reverte.
- Liga: bp:intangivel
- Questões: F1603, F1641, F1808, F1849, F1873, F1896, F1899
### Histórias
- Perda por desvalorização (impairment) | O intangível de vida útil indefinida da Só Inventores aparece no balanço pelo custo de aquisição, reduzido pelo saldo de uma perda reconhecida em teste anterior. (F1873)
- (-) Perda por desvalorização (impairment) | O ativo intangível amortizável, de vida útil de 20 anos, aparece no balanço pelo custo, menos a amortização acumulada e menos uma perda por desvalorização reconhecida antes. (F1808)

## gastos-pre-operacionais · Gastos pré-operacionais (antigo ativo diferido)
- Classe: resultado · despesa · devedora · normal · - · despesas-administrativas
- Nomes: Gastos pré-operacionais
- Depende: subgrupo
- Por quê: Pela regra atual, gastos de implantação e pré-operacionais vão para o resultado como despesa quando incorridos (CPC 04, item 69, a), salvo os que façam parte do custo de um imobilizado ou de um intangível; a linha da DRE segue a natureza do gasto. Até 2008 iam para o ativo diferido (art. 179, V), extinto pela Lei 11.941/2009; o saldo de 31/12/2008 pôde ficar no ativo até ser amortizado (art. 299-A).
- Liga: bp:diferido
- Questões: F2940, DRE:F0578, DRE:F0583
### Histórias
- Gastos pré-operacionais | Hoje, antes de começar a operar, a nova empresa pagou o aluguel do escritório e os salários da equipe administrativa durante os meses de implantação.

<!-- ===== Passivo ===== -->

## fornecedores · Fornecedores
- Classe: patrimonial · passivo · credora · normal · circulante · -
- Nomes: Fornecedores; Contas a pagar - fornecedores; Contas a pagar a fornecedores; Fornecedores de estoque a pagar; Fornecedores de serviços; Duplicatas a pagar; Materiais a pagar
- Depende: prazo
- Por quê: Obrigação por compras a prazo de mercadorias, materiais e serviços. Sem prazo informado, a leitura padrão é o circulante; vencendo depois do término do exercício seguinte, vai para o não circulante (Lei 6.404/76, art. 180). Se de longo prazo, ou de curto prazo com efeito relevante, é ajustada a valor presente (art. 184, III; CPC 12).
- Liga: bp:passivo-circulante
- Questões: DRE:F0102, DRE:F0105, DRE:F0263, DRE:F0525, DRE:F0645, DRE:F0664, F0500, F2473, F2842, F3244, F3322, F3951
### Histórias
- Fornecedores | Uma loja comprou mercadorias para revender e combinou pagar o fornecedor daqui a três meses. (F0500)
- Materiais a pagar | Para consertar produtos na garantia, a empresa comprou peças a prazo, com pagamento no mês seguinte. (F2473)
- Duplicatas a pagar | A empresa aceitou a duplicata emitida pelo fornecedor de matéria-prima, com vencimento em 45 dias.

## contas-a-pagar · Contas a pagar
- Classe: patrimonial · passivo · credora · normal · circulante · -
- Nomes: Contas a pagar; Outras contas a pagar; Outros valores a pagar
- Depende: prazo
- Por quê: Obrigações diversas com terceiros, ainda não pagas. Sem prazo, a leitura padrão é o circulante; com vencimento após o exercício seguinte, não circulante (Lei 6.404/76, art. 180). Pequenos saldos semelhantes podem ser agrupados, indicada a natureza, se não passarem de 10% do grupo; "diversas contas" é vedado (art. 176, §2º).
- Liga: bp:passivo-circulante
- Questões: DRE:F0263, DRE:F0346, DRE:F0449, DRE:F0493, DRE:F0566, DRE:F0624, DRE:F0629, DRE:F0762, F2681, F3951
### Histórias
- Outras contas a pagar | No passivo circulante, a companhia reúne numa só linha vários saldos pequenos que vencem nos próximos meses, informando a natureza deles. (F2681)
- Contas a pagar | O escritório de consultoria já entregou o relatório contratado e a fatura vence em 30 dias.

## contas-a-pagar-cp · Contas a pagar (curto prazo)
- Classe: patrimonial · passivo · credora · normal · circulante · -
- Nomes: Contas a pagar em 3 meses
- Por quê: Obrigação que vence dentro do exercício seguinte: passivo circulante (Lei 6.404/76, art. 180).
- Liga: bp:passivo-circulante
- Questões: F2757
### Histórias
- Contas a pagar | Obrigação que vence três meses depois da data do balanço. (F2757)

## contas-a-pagar-lp · Contas e títulos a pagar (longo prazo)
- Classe: patrimonial · passivo · credora · normal · nao-circulante · -
- Nomes: Contas a pagar de longo prazo; Duplicatas a pagar em longo prazo; Promissórias a pagar a longo prazo; Títulos a pagar de longo prazo
- Por quê: Obrigações com vencimento após o término do exercício seguinte ficam no passivo não circulante (Lei 6.404/76, arts. 178, §2º, II, e 180) e são ajustadas a valor presente (art. 184, III). A parte que passar a vencer em até 12 meses é reclassificada para o circulante a cada balanço.
- Liga: bp:passivo-nao-circulante
- Questões: DRE:F0449, DRE:F0525, DRE:F0624, DRE:F0645, DRE:F0717, F2878
### Histórias
- Fornecedores | A indústria comprou um equipamento do fabricante e vai pagá-lo numa parcela única daqui a dois anos.
- Promissórias a pagar a longo prazo | A empresa assinou notas promissórias a favor de um credor, com vencimento em 30 meses.

## cartao-credito-a-pagar · Cartão de crédito a pagar
- Classe: patrimonial · passivo · credora · normal · circulante · -
- Nomes: Cartões de crédito a pagar; Cartão de crédito a pagar
- Por quê: Fatura do cartão da empresa por gastos já feitos e ainda não pagos: obrigação de curto prazo (Lei 6.404/76, art. 180).
- Liga: bp:passivo-circulante
- Questões: DRE:F0449, DRE:F0699
### Histórias
- Cartão de crédito a pagar | As passagens da viagem do diretor foram compradas no cartão corporativo; a fatura vence no mês seguinte.

## aluguel-a-pagar · Aluguéis a pagar
- Classe: patrimonial · passivo · credora · normal · circulante · -
- Nomes: Aluguel a pagar; Aluguéis a pagar
- Por quê: Aluguel do período já usado (despesa incorrida, regime de competência) e ainda não pago: obrigação do passivo circulante. Não confundir com aluguel pago antecipadamente, que é ativo.
- Liga: bp:passivo-circulante
- Questões: DRE:F0573, DRE:F0587, DRE:F0624, DRE:F0645, DRE:F0664, DRE:F0757, DRE:F0759, DRE:F0760, F3444, F3460, F3464
### Histórias
- Aluguéis a pagar | A loja ocupou o imóvel durante todo o mês de dezembro, mas o aluguel desse mês só vence em 5 de janeiro.

## condominio-a-pagar · Condomínio a pagar
- Classe: patrimonial · passivo · credora · normal · circulante · -
- Nomes: Condomínio a pagar; Taxa de condomínio a pagar
- Por quê: Taxa de condomínio do período já transcorrido e não paga: despesa incorrida com obrigação de curto prazo (passivo circulante).
- Liga: bp:passivo-circulante
- Questões: DRE:F0449, DRE:F0463, DRE:F0525, DRE:F0624
### Histórias
- Condomínio a pagar | O boleto do condomínio das salas do escritório, referente a novembro, vence em 10 de dezembro e ainda não foi pago.

## energia-a-pagar · Energia a pagar
- Classe: patrimonial · passivo · credora · normal · circulante · -
- Nomes: Energia a pagar; Energia elétrica a pagar
- Por quê: Energia já consumida e ainda não paga: a despesa é do período (competência) e a obrigação vai para o passivo circulante. "Energia antecipada" é o contrário: ativo.
- Liga: bp:passivo-circulante
- Questões: DRE:F0449, DRE:F0566, DRE:F0573, DRE:F0587, DRE:F0624, DRE:F0645, DRE:F0664, DRE:F0757, F2942, F3460, F3471
### Histórias
- Energia elétrica a pagar | A conta de luz de dezembro chegou no fim do mês, com vencimento para meados de janeiro.

## telefone-internet-a-pagar · Telefone e internet a pagar
- Classe: patrimonial · passivo · credora · normal · circulante · -
- Nomes: Telefone a pagar; Telefone e Internet a pagar; Serviços de Internet a pagar; Telecomunicações a pagar
- Por quê: Serviços de comunicação já usados e não pagos: obrigação de curto prazo (passivo circulante), com a despesa reconhecida no período em que o serviço foi usado.
- Liga: bp:passivo-circulante
- Questões: DRE:F0525, DRE:F0573, DRE:F0587, DRE:F0624, DRE:F0645, DRE:F0664
### Histórias
- Telefone e Internet a pagar | A operadora faturou o pacote de telefonia e internet de dezembro, com vencimento em janeiro.

## manutencao-a-pagar · Manutenção a pagar
- Classe: patrimonial · passivo · credora · normal · circulante · -
- Nomes: Manutenção a pagar; Manutenção de veículos a pagar
- Por quê: Serviço de manutenção já executado e ainda não pago: passivo circulante. Se a manutenção tivesse sido paga antes de executada, seria ativo (despesa antecipada).
- Liga: bp:passivo-circulante
- Questões: DRE:F0525, DRE:F0527, DRE:F0573, DRE:F0587, DRE:F0645, DRE:F0664
### Histórias
- Manutenção de veículos a pagar | A oficina revisou os caminhões da frota em dezembro e cobrará o serviço em 30 dias.

## combustiveis-a-pagar · Combustíveis a pagar
- Classe: patrimonial · passivo · credora · normal · circulante · -
- Nomes: Combustíveis a pagar; Combustíveis e lubrificantes a pagar
- Por quê: Valor devido ao posto por combustível já abastecido: obrigação de curto prazo (passivo circulante). A conta "Combustíveis", sem o "a pagar", é estoque (ativo).
- Liga: bp:passivo-circulante
- Questões: DRE:F0587, DRE:F0624, DRE:F0664
### Histórias
- Combustíveis a pagar | Os veículos de entrega abastecem no posto conveniado, que cobra o total do mês no dia 10 do mês seguinte.

## seguros-a-pagar · Seguros a pagar
- Classe: patrimonial · passivo · credora · normal · circulante · -
- Nomes: Seguros a pagar
- Por quê: Prêmio de seguro contratado e ainda devido à seguradora: passivo circulante. A cobertura ainda não usada (seguros antecipados, seguros a vencer, prêmios a apropriar) é outra conta, do ativo.
- Liga: bp:passivo-circulante
- Questões: DRE:F0263, DRE:F0527, DRE:F0624, DRE:F0664, F3460, F3471
### Histórias
- Seguros a pagar | A empresa contratou o seguro anual da frota e vai quitar o prêmio em três parcelas mensais a partir de janeiro.

## assinaturas-a-pagar · Assinaturas a pagar
- Classe: patrimonial · passivo · credora · normal · circulante · -
- Nomes: Assinaturas a pagar
- Por quê: Valor devido por assinaturas (revistas, sistemas, jornais) contratadas e ainda não pagas: obrigação de curto prazo. "Assinaturas antecipadas" é o contrário: ativo.
- Liga: bp:passivo-circulante
- Questões: DRE:F0624, DRE:F0664
### Histórias
- Assinaturas a pagar | A empresa assinou um jornal de economia e combinou pagar o valor anual em 60 dias.

## honorarios-a-pagar · Honorários a pagar
- Classe: patrimonial · passivo · credora · normal · circulante · -
- Nomes: Honorários a pagar
- Por quê: Remuneração devida a profissionais (advogados, contadores, auditores) por serviços já prestados: passivo circulante.
- Liga: bp:passivo-circulante
- Questões: DRE:F0645
### Histórias
- Honorários a pagar | O escritório de advocacia concluiu o parecer em dezembro e emitiu a nota para pagamento em janeiro.

## salarios-a-pagar · Salários e encargos a pagar
- Classe: patrimonial · passivo · credora · normal · circulante · -
- Nomes: Salários a pagar; Salários e encargos a pagar; Encargos e salários a pagar; Pró-labore a pagar; Mão de obra a pagar
- Por quê: Remuneração do mês (de empregados, de administradores no pró-labore, da mão de obra usada) reconhecida como despesa pela competência e paga no mês seguinte: passivo circulante. O valor a pagar ao empregado é o líquido; o que a empresa retém (INSS, IRRF) vira obrigação própria com o fisco.
- Liga: bp:passivo-circulante
- Questões: DRE:F0102, DRE:F0263, DRE:F0493, DRE:F0699, F0402, F0543, F2325, F2473, F2789, F2842, F3322, F3462
### Histórias
- Salários a pagar | A folha de agosto, de 100.000 brutos, será paga em setembro; do bruto, a empresa reteve 11.000 de INSS e 4.000 de IRRF e deve aos empregados só o líquido. (F0402)
- Mão de obra a pagar | Os reparos feitos no mês seguinte à venda, cobertos pela garantia, usaram mão de obra que ainda não foi paga. (F2473)
- Pró-labore a pagar | A retirada mensal dos sócios administradores, relativa a dezembro, será paga no quinto dia útil de janeiro.

## ferias-a-pagar · Férias a pagar (provisão para férias)
- Classe: patrimonial · passivo · credora · normal · circulante · -
- Nomes: Provisões para férias
- Por quê: Apesar do nome, não é provisão do CPC 25: valor e prazo são conhecidos, é passivo por competência (CPC 25, item 11; CPC 33, ausências remuneradas acumuláveis). A cada mês trabalhado, reconhece-se a parte das férias já adquirida, devida no curto prazo.
- Liga: bp:passivo-circulante
- Questões: F2406
### Histórias
- Provisões para férias | A cada mês de trabalho, a empresa registra a fração das férias que o empregado já conquistou e que ele vai gozar e receber dentro do próximo ano. (F2406)

## retencoes-a-recolher · Tributos retidos a recolher
- Classe: patrimonial · passivo · credora · normal · circulante · -
- Nomes: INSS a recolher; IRRF a recolher; IR na fonte a recolher
- Por quê: Valores descontados do empregado (ou do prestador) que a empresa, como responsável, deve repassar ao fisco no mês seguinte: passivo circulante. Não é despesa da empresa: a despesa é o salário bruto.
- Liga: bp:passivo-circulante
- Questões: DRE:F0699, F0402, F2325
### Histórias
- IR na fonte a recolher | Ao apropriar a folha de janeiro, de 400.000, a empresa reteve 12,5% de imposto de renda dos empregados, a recolher em fevereiro. (F2325)
- INSS a recolher | A contribuição previdenciária de 11.000 descontada dos salários de agosto será repassada à Previdência em setembro. (F0402)

## tributos-a-recolher · Tributos a recolher
- Classe: patrimonial · passivo · credora · normal · circulante · -
- Nomes: Impostos a pagar; Impostos a recolher; Tributos a recolher; Contribuições a recolher; Taxas e contribuições a pagar; Impostos e contribuições a pagar; Obrigações fiscais
- Depende: prazo
- Por quê: Tributos já devidos e ainda não pagos: passivo circulante, no prazo normal de recolhimento. Em parcelamento, as parcelas que vencem após o exercício seguinte vão para o não circulante (Lei 6.404/76, art. 180). Não confundir com tributos a recuperar ou antecipados (ativo).
- Liga: bp:passivo-circulante
- Questões: DRE:F0102, DRE:F0105, DRE:F0346, DRE:F0391, DRE:F0463, DRE:F0525, DRE:F0587, DRE:F0664, F2681, F2789, F2842, F3244
### Histórias
- Impostos a recolher | O ICMS apurado sobre as vendas de dezembro será recolhido no dia 20 de janeiro.

## ir-csll-a-pagar · IR e CSLL a pagar
- Classe: patrimonial · passivo · credora · normal · circulante · -
- Nomes: CSLL a pagar; Imposto de renda a pagar; Imposto de renda e contribuição social a pagar; IR a pagar
- Por quê: Tributos correntes sobre o lucro do exercício, ainda não pagos: passivo circulante (CPC 32). O tributo diferido passivo é outra conta e fica sempre no não circulante (CPC 26, item 56).
- Liga: bp:passivo-circulante
- Questões: DRE:F0391, DRE:F0573, F3444
### Histórias
- IR a pagar | Parte do imposto de renda sobre o lucro de 20X8 ainda não foi paga e vence ao longo de 20X9. (F3444)

## emprestimos-financiamentos · Empréstimos e financiamentos
- Classe: patrimonial · passivo · credora · normal · circulante · -
- Nomes: Empréstimos; Empréstimos a pagar; Empréstimos bancários; Empréstimos bancários a pagar; Empréstimos e financiamentos; Financiamentos; Financiamentos a pagar; Financiamento
- Depende: prazo
- Por quê: Recursos obtidos de terceiros, com obrigação de devolver com juros. Classificam-se pelo vencimento de cada parcela: as do exercício seguinte no circulante, mesmo que o dinheiro tenha financiado o imobilizado; as demais no não circulante (Lei 6.404/76, art. 180; CPC 26, item 69).
- Liga: bp:passivo-circulante
- Questões: DRE:F0102, DRE:F0105, DRE:F0463, DRE:F0493, DRE:F0527, DRE:F0717, F0498, F0500, F0543, F2789, F2828, F3244
### Histórias
- Empréstimos a pagar | Empréstimo de 180.000 amortizado em 30.000 por semestre; em 31/12/2022, restam 150.000, e esta é a parte das duas parcelas que vencem em 2023. (F2828)
- Empréstimos | Depois de comprar mercadorias a prazo, a empresa e o fornecedor fecharam com um banco uma operação de risco sacado, e a dívida, a vencer em três meses, passou a ser tratada como empréstimo. (F0500)

## emprestimos-financiamentos-cp · Empréstimos e financiamentos (curto prazo)
- Classe: patrimonial · passivo · credora · normal · circulante · -
- Nomes: Empréstimos a pagar de curto prazo; Financiamentos a pagar de curto prazo; Empréstimo a pagar com vencimento para 180 dias
- Por quê: Dívida com vencimento dentro do exercício seguinte: passivo circulante (Lei 6.404/76, art. 180).
- Liga: bp:passivo-circulante
- Questões: DRE:F0629, DRE:F0645, F2756
### Histórias
- Empréstimos a pagar | Ao revisar o balancete, o contador encontrou um empréstimo bancário que não tinha sido lançado, com vencimento em 180 dias. (DRE:F0629)

## emprestimos-financiamentos-lp · Empréstimos e financiamentos (longo prazo)
- Classe: patrimonial · passivo · credora · normal · nao-circulante · -
- Nomes: Empréstimos e financiamentos de longo prazo a pagar; Empréstimos a pagar a longo prazo; Empréstimos a longo prazo; Empréstimos a pagar em longo prazo; Empréstimos a pagar de longo prazo; Empréstimos a pagar após 12 meses; Financiamentos a pagar em longo prazo; Financiamentos a pagar de longo prazo; Financiamentos a pagar após 36 meses; Financiamentos de longo prazo
- Por quê: Parcelas que vencem após o término do exercício seguinte: passivo não circulante (Lei 6.404/76, arts. 178, §2º, II, e 180), ajustadas a valor presente (art. 184, III; CPC 12). A cada balanço, a parte que passa a vencer em até 12 meses é transferida para o circulante, sem ser paga.
- Liga: bp:passivo-nao-circulante
- Questões: DRE:F0263, DRE:F0346, DRE:F0391, DRE:F0493, DRE:F0525, DRE:F0624, DRE:F0629, DRE:F0717, F1980, F2756, F2757, F2828
### Histórias
- Empréstimos a pagar | Em março de 2024, uma consultoria tomou empréstimo bancário cujo principal e juros só serão pagos em março de 2027. (F1980)
- Empréstimos a pagar | Do empréstimo de 180.000 amortizado em 30.000 por semestre, em 31/12/2022, esta é a parte das parcelas que vencem de 2024 em diante. (F2828)
- Empréstimos a pagar | Em 2008, a empresa quitou a dívida antiga e contratou outra, com quitação prevista para o fim de 2012. (DRE:F0493)

## juros-a-pagar · Juros a pagar
- Classe: patrimonial · passivo · credora · normal · circulante · -
- Nomes: Juros a pagar
- Depende: prazo
- Por quê: Juros já incorridos (despesa financeira pela competência) e ainda não pagos: passivo circulante quando vencem no exercício seguinte; se forem pagos só com o principal de longo prazo, acompanham o não circulante (Lei 6.404/76, art. 180).
- Liga: bp:passivo-circulante
- Questões: DRE:F0102, DRE:F0493, DRE:F0587, F3244, F3436, F3471
### Histórias
- Juros a pagar | As despesas financeiras de 20X5 foram reconhecidas no resultado, mas a empresa só vai pagá-las ao longo de 20X6. (F3244)

## debentures · Debêntures a pagar
- Classe: patrimonial · passivo · credora · normal · circulante · -
- Nomes: Debêntures a pagar
- Depende: prazo
- Por quê: Título de dívida emitido pela companhia, que dá ao debenturista direito de crédito contra ela (Lei 6.404/76, art. 52). Classifica-se pelo prazo de resgate: no exercício seguinte, circulante; depois, não circulante (art. 180).
- Liga: bp:passivo-circulante
- Questões: DRE:F0699, DRE:F0757, F2014
### Histórias
- Debêntures a pagar | A série de debêntures emitida há quatro anos será resgatada em parcela única daqui a sete meses.

## debentures-cp · Debêntures (curto prazo)
- Classe: patrimonial · passivo · credora · normal · circulante · -
- Nomes: Debêntures emitidas com resgate em curto prazo; Debêntures a pagar em curto prazo; Debêntures emitidas para resgate em curto prazo; Debêntures de curto prazo
- Por quê: Debêntures com resgate dentro do exercício seguinte: passivo circulante (Lei 6.404/76, art. 180). Debêntures que a empresa comprou de outra são outra conta: ativo.
- Liga: bp:passivo-circulante
- Questões: DRE:F0449, DRE:F0624, DRE:F0645, DRE:F0762
### Histórias
- Debêntures | A companhia captou recursos com debêntures que vencem no fim do exercício seguinte ao do balanço.

## debentures-lp · Debêntures (longo prazo)
- Classe: patrimonial · passivo · credora · normal · nao-circulante · -
- Nomes: Debêntures exigíveis a longo prazo; Debêntures emitidas com resgate em longo prazo; Debêntures de longo prazo
- Por quê: Debêntures com resgate após o término do exercício seguinte: passivo não circulante (Lei 6.404/76, arts. 178, §2º, II, e 180). A parte que passa a vencer em 12 meses é reclassificada para o circulante.
- Liga: bp:passivo-nao-circulante
- Questões: DRE:F0346, DRE:F0624, DRE:F0645, DRE:F0762
### Histórias
- Debêntures a pagar | Para financiar a expansão, a companhia emitiu debêntures com resgate em cinco anos.

## desagio-debentures · (–) Deságio na emissão de debêntures
- Classe: patrimonial · passivo · devedora · retificadora · circulante · -
- Nomes: Deságio na emissão de debêntures
- Depende: prazo
- Por quê: Desconto dado ao investidor quando a debênture é colocada abaixo do valor nominal. Pelo CPC 08 (R1), é encargo financeiro a apropriar: reduz o saldo das debêntures (natureza devedora) e vira despesa financeira pela taxa efetiva até o resgate. Segue o prazo das debêntures que retifica.
- Liga: bp:passivo-circulante
- Questões: DRE:F0699, DRE:F0757
### Histórias
- Deságio na emissão de debêntures | Debêntures de valor nominal 50.000, com resgate em oito meses, foram vendidas aos investidores por 48.000; a diferença será levada a despesa financeira até o resgate.

## desagio-debentures-cp · (–) Deságio na emissão de debêntures de curto prazo
- Classe: patrimonial · passivo · devedora · retificadora · circulante · -
- Nomes: Deságio na emissão de debêntures de curto prazo
- Por quê: Redutora das debêntures que vencem no exercício seguinte: fica no passivo circulante, com natureza devedora, e é apropriada como despesa financeira até o resgate (CPC 08 (R1)).
- Liga: bp:passivo-circulante
- Questões: DRE:F0624
### Histórias
- Deságio na emissão de debêntures | A companhia colocou abaixo do valor nominal uma série de debêntures que vence dentro do exercício seguinte, e o desconto ainda não foi todo apropriado ao resultado.

## premio-emissao-debentures · Prêmio na emissão de debêntures
- Classe: patrimonial · passivo · credora · normal · circulante · -
- Nomes: Prêmio na emissão de debêntures; Ágio na emissão de debêntures
- Depende: prazo
- Por quê: Valor pago pelo investidor acima do nominal da debênture. Até a Lei 11.638/2007 era reserva de capital (Lei 6.404/76, art. 182, §1º, "c", revogado); hoje, pelo CPC 08 (R1), fica no passivo junto das debêntures e é apropriado ao resultado, reduzindo o custo da dívida, até o resgate. Segue o prazo das debêntures.
- Liga: bp:passivo-circulante
- Questões: DRE:F0699, DRE:F0757, F2014
### Histórias
- Prêmio na emissão de debêntures | Investidores pagaram 12.000 por debêntures de valor nominal 10.000, com resgate previsto para daqui a dez meses; o excedente será apropriado ao resultado até lá.

## custos-transacao-a-apropriar · (–) Custos de transação a apropriar
- Classe: patrimonial · passivo · devedora · retificadora · circulante · -
- Nomes: Custos de transação a apropriar
- Depende: prazo
- Por quê: Gastos para captar a dívida (comissões, assessoria, registro) não vão direto para a despesa: reduzem o passivo captado e são apropriados ao resultado pela taxa efetiva ao longo do prazo (CPC 08 (R1)). Como retifica o passivo, tem natureza devedora e segue o prazo da dívida.
- Liga: bp:passivo-circulante
- Questões: F2014
### Histórias
- Custos de transação a apropriar | Para emitir debêntures de 10.000 com resgate em dez meses, a companhia pagou 1.000 a bancos coordenadores e ao registro da emissão.

## duplicatas-descontadas · Duplicatas descontadas
- Classe: patrimonial · passivo · credora · normal · circulante · -
- Nomes: Duplicatas descontadas; Títulos descontados
- Por quê: No desconto com direito de regresso, a empresa continua com o risco de não receber: mantém as duplicatas a receber e registra no passivo a dívida com o banco (CPC 48, baixa de ativos financeiros). A apresentação antiga, que ainda aparece em bancas e autores, era como redutora de duplicatas a receber no ativo (com a mesma natureza credora); pela regra atual, é passivo.
- Liga: bp:passivo-circulante
- Questões: DRE:F0263, DRE:F0391, DRE:F0449, DRE:F0493, DRE:F0757, DRE:F0762
### Histórias
- Duplicatas descontadas | A empresa levou ao banco duplicatas de clientes que vencem em 60 dias e recebeu o dinheiro antes; se o cliente não pagar, ela terá de devolver o valor ao banco.

## adiantamento-clientes · Adiantamentos de clientes
- Classe: patrimonial · passivo · credora · normal · circulante · -
- Nomes: Adiantamentos de clientes; Adiantamentos recebidos de clientes
- Depende: prazo
- Por quê: Quem recebe antes de entregar o bem ou prestar o serviço tem obrigação de cumprir (passivo de contrato, CPC 47), e não receita. Classifica-se pelo prazo de cumprimento: dentro do exercício seguinte ou do ciclo operacional, circulante (Lei 6.404/76, art. 180).
- Liga: bp:passivo-circulante
- Questões: F2091, F3436, F3444
### Histórias
- Adiantamentos de clientes | Uma consultoria recebeu adiantado por serviços que serão prestados até setembro do ano seguinte; o ciclo operacional dela é menor que 12 meses. (F2091)

## receita-antecipada · Receita antecipada
- Classe: patrimonial · passivo · credora · normal · circulante · -
- Nomes: Receita antecipada; Receitas antecipadas; Receita antecipada de vendas; Receita de serviços antecipada
- Depende: prazo
- Por quê: Valor recebido antes de entregar ou prestar: obrigação (passivo), que vira receita quando cumprida (competência; CPC 47). Antes de 2009, a receita recebida sem obrigação de devolver ia para o grupo resultados de exercícios futuros, extinto pela Lei 11.941/2009 (art. 181 revogado; saldo levado ao passivo não circulante pelo art. 299-B). Hoje se classifica pelo prazo.
- Liga: bp:passivo-circulante
- Questões: DRE:F0346, DRE:F0463, DRE:F0527, DRE:F0573, DRE:F0664, DRE:F0699, DRE:F0759, DRE:F0762, F2331, F2942, F3436, F3471
### Histórias
- Receitas antecipadas | São valores que os clientes pagaram adiantado por produtos que a empresa vai entregar nos próximos meses. (F3436)
- Receita antecipada | Em junho de 2024, a empresa recebeu adiantado o aluguel de dois anos de uma sala, com contrato iniciado em julho; em 31/12/2024, esta é a parte que corresponde aos aluguéis de 2025. (F2331)

## dividendos-a-pagar · Dividendos a pagar
- Classe: patrimonial · passivo · credora · normal · circulante · -
- Nomes: Dividendos a pagar
- Por quê: Dividendo declarado, inclusive o mínimo obrigatório, é obrigação com os acionistas: passivo circulante (Lei 6.404/76, art. 202). O que exceder o mínimo e ainda depender de aprovação da assembleia fica no PL como dividendo adicional proposto (ICPC 08).
- Liga: bp:passivo-circulante
- Questões: DRE:F0102, DRE:F0105, DRE:F0664, DRE:F0721, F0498, F2842, F3244, F3322, F3436
### Histórias
- Dividendos a pagar | Em dezembro, a companhia distribuiu 10.000 de dividendos, que serão pagos aos acionistas em março do ano seguinte. (DRE:F0105)

## passivo-arrendamento · Passivo de arrendamento
- Classe: patrimonial · passivo · credora · normal · circulante · -
- Nomes: Arrendamentos a pagar; Passivo de arrendamento
- Depende: prazo
- Por quê: O arrendatário reconhece o direito de uso (ativo) e o passivo de arrendamento pelo valor presente dos pagamentos ainda não feitos (CPC 06 (R2), item 26), salvo a isenção para contratos de curto prazo ou de baixo valor. O passivo se divide pelo vencimento das prestações: as do exercício seguinte no circulante, as demais no não circulante.
- Liga: bp:passivo-circulante
- Questões: F2681, F3863, F3868, F3870
### Histórias
- Arrendamentos a pagar | No passivo circulante, a companhia apresenta as prestações de arrendamento que vencem nos 12 meses seguintes ao balanço. (F2681)
- Passivo de arrendamento | A empresa arrendou um galpão por cinco anos; esta é a parte do passivo correspondente às prestações do próximo ano.

## provisao-contingencias · Provisão para contingências
- Classe: patrimonial · passivo · credora · normal · circulante · -
- Nomes: Provisão para contingências; Provisões para contingências; Provisão para contingências judiciais; Provisão para contingências diversas; Provisão para contingências trabalhistas; Provisões para contingências trabalhistas; Provisões para riscos trabalhistas; Provisão para riscos cíveis, fiscais e trabalhistas
- Depende: prazo
- Por quê: Passivo de prazo ou valor incertos, reconhecido quando há obrigação presente, saída de recursos provável e estimativa confiável (CPC 25, item 14); com saída só possível, é passivo contingente e vai apenas para nota (item 28). Classifica-se pela data esperada de saída, a valor presente quando relevante. Não confundir com a reserva para contingências (PL, destinação do lucro) nem com as "provisões" redutoras de ativo.
- Liga: bp:passivo-circulante
- Questões: DRE:F0449, DRE:F0463, DRE:F0525, DRE:F0527, DRE:F0566, DRE:F0717, F2361, F2403, F2406, F2542, F2789, F2878
### Histórias
- Provisões para riscos trabalhistas | Um ex-empregado cobra horas extras na Justiça; o jurídico considera a perda provável, estima o valor com segurança e espera pagar o acordo em quatro meses.
- Provisão para contingências | Numa ação contra duas companhias solidárias, a perda é provável; cada uma reconhece só a metade que lhe cabe, e a sentença deve ser paga ainda no exercício seguinte.

## provisao-garantias · Provisão para garantias
- Classe: patrimonial · passivo · credora · normal · circulante · -
- Nomes: Provisão para garantias; Provisão para garantias de produtos
- Depende: prazo
- Por quê: A venda com garantia cria obrigação presente de reparar defeitos; a provisão é reconhecida na venda pelo valor esperado dos reparos (CPC 25). Se a responsabilidade é dividida com outro, só a parte própria vira provisão, e a parte esperada do outro é passivo contingente (item 29). Garantia de até 12 meses: circulante.
- Liga: bp:passivo-circulante
- Questões: F2427, F2473, F2789
### Histórias
- Provisão para garantias | Uma loja vende computadores com garantia de 12 meses e responde por 40% dos reparos; registra na venda essa parte do custo esperado com defeitos. (F2427)
- Provisão para garantias | Uma empresa estimou em 2% das vendas do mês os reparos em garantia das máquinas vendidas e, já no mês seguinte, usou parte desse valor em consertos. (F2473)

## provisao-reestruturacao · Provisão para reestruturação
- Classe: patrimonial · passivo · credora · normal · circulante · -
- Nomes: Provisão para reestruturação; Provisão para gastos com reestruturação; Provisão para custos de reestruturação
- Depende: prazo
- Por quê: Reconhecida quando há plano formal e expectativa válida criada nos afetados (CPC 25, itens 70 a 83). Inclui só gastos diretos da reestruturação, e o ganho esperado com a venda de ativos não reduz o valor (itens 51 e 83). Classifica-se pelo prazo de execução.
- Liga: bp:passivo-circulante
- Questões: F2462, F2496
### Histórias
- Provisão para reestruturação | Um hotel decidiu fechar o restaurante e cumpre os requisitos para reconhecer os gastos de reestruturação, a executar nos próximos meses; o ganho com a venda dos equipamentos não reduz o valor. (F2462, F2496)

## provisao-desmontagem · Provisão para desmontagem e retirada de ativos
- Classe: patrimonial · passivo · credora · normal · nao-circulante · -
- Nomes: Provisões para retirada de ativos de longo prazo
- Por quê: Obrigação de desmontar e remover um ativo ao fim da vida útil: provisão do CPC 25, reconhecida a valor presente, cujo valor também entra no custo do imobilizado (CPC 27, item 16, "c"). Como a saída ocorre só no fim da vida útil, fica no não circulante.
- Liga: bp:passivo-nao-circulante
- Questões: F2406
### Histórias
- Provisões para retirada de ativos de longo prazo | A empresa instalou um equipamento num terreno cedido pelo governo e, ao fim da vida útil dele, daqui a muitos anos, terá de desmontá-lo e removê-lo. (F2406)

<!-- ===== Patrimônio líquido ===== -->

## capital-social · Capital social
- Classe: patrimonial · pl · credora · normal · - · capital-social
- Nomes: Capital social; Capital; Capital social subscrito
- Por quê: É o primeiro subgrupo do PL e registra o que os sócios entregaram ou se comprometeram a entregar, em dinheiro ou em bens avaliáveis (Lei 6.404/76, arts. 7º, 178, §2º, III, e 182, caput). A conta mostra o capital subscrito; a parte ainda não entregue aparece por dedução, em capital a integralizar.
- Liga: bp:capital-social
- Questões: F0083, F2099, F2118, F2123, F2149, F2183, F2186, F2266, F2785, F2791, F2896, DRE:F0314
### Histórias
- Capital social | Os sócios aumentaram a sua participação na empresa entregando a ela um terreno avaliado em R$ 50.000, sem nenhuma dívida em troca. (F2785, F2791)
- Capital social | A companhia vendeu 50.000 ações novas de valor nominal R$ 1,00 por R$ 1,30 cada; a conta que recebe a parte equivalente ao valor nominal das ações. (F2123, F2118)
- Capital social | Em 2025, a assembleia passou para esta conta todo o saldo da reserva de capital, que subiu de R$ 8.000.000 para R$ 9.000.000 sem entrada de dinheiro. (F2099)

## capital-a-integralizar · Capital a integralizar
- Classe: patrimonial · pl · devedora · retificadora · - · capital-social
- Nomes: Capital a integralizar; Capital a realizar; Capital social a integralizar
- Por quê: É a parte do capital subscrito que os sócios ainda não entregaram; aparece deduzida do capital social, dentro do PL (Lei 6.404/76, art. 182, caput). Não é ativo: a promessa dos sócios não é recurso controlado pela entidade enquanto não for paga.
- Liga: bp:capital-social
- Questões: F0480, F2186, F2237, DRE:F0314
### Histórias
- Capital social a integralizar | Do capital de R$ 2.000.000 assinado pelos acionistas, R$ 300.000 ainda não tinham sido pagos no fim de 2020; em 2021, eles entregaram R$ 100.000 dessa parte. (F2186)
- Capital a realizar | Os sócios subscreveram o capital e prometeram pagar R$ 5.000 mais tarde; a conta que mostra esse valor prometido e ainda não pago, que só zerou quando eles o quitaram no ano seguinte. (DRE:F0314)

## gastos-emissao-acoes · Gastos com emissão de ações
- Classe: patrimonial · pl · devedora · retificadora · - · capital-social
- Nomes: Gastos na emissão de ações
- Por quê: Os custos de transação de uma captação por emissão de ações (bancos coordenadores, advogados, registros) não são despesa: ficam em conta redutora do PL, junto do capital (CPC 08 (R1)). Só iriam ao resultado se a emissão não se concretizasse.
- Liga: bp:capital-social
- Questões: F3210, F2125
### Histórias
- Gastos na emissão de ações | Para lançar R$ 50 milhões em ações novas no mercado, a companhia pagou R$ 1,5 milhão a coordenadores, advogados e taxas de registro; a conta em que ficam esses custos. (F2125)
- Gastos na emissão de ações | A companhia concluiu com sucesso um aumento de capital por oferta de ações e pagou a comissão do banco que coordenou a venda; o valor reduz diretamente o patrimônio, sem passar pela DRE.

## reservas-capital · Reservas de capital
- Classe: patrimonial · pl · credora · normal · - · reservas-capital
- Nomes: Reservas de capital; Reserva de capital
- Por quê: Recebem valores vindos de sócios ou de terceiros que não são receita e não passam pelo resultado: o ágio na emissão de ações e o produto da alienação de partes beneficiárias e de bônus de subscrição (Lei 6.404/76, art. 182, §1º). O ganho na revenda de ações em tesouraria também vai para cá. Desde a Lei 11.638/2007, o prêmio na emissão de debêntures e as doações e subvenções para investimento deixaram de ser reserva de capital.
- Liga: bp:reservas-capital
- Questões: F0083, F2099, F2117, F2168, F2190, F2193, F2198, F2205, F2208, F2264, F2874, F3181
### Histórias
- Reserva de capital | A companhia revendeu por R$ 25.000 ações próprias que havia recomprado por R$ 22.000; a conta que recebe os R$ 3.000 de diferença. (F2193, F2264)
- Reserva de capital | A companhia vendeu partes beneficiárias a investidores e recebeu o dinheiro; a conta do PL que registra esse valor, que não passa pela DRE. (F3181)
- Reservas de capital | Valores recebidos em transações de capital com os sócios, que nunca vão transitar pelo resultado como receita. (F2208)
- Reserva de capital | O prejuízo de R$ 18.000 do ano superou os R$ 12.000 de reservas de lucros; os R$ 6.000 restantes foram absorvidos por esta conta, que tinha saldo de R$ 16.000. (F2168)

## agio-emissao-acoes · Ágio na emissão de ações
- Classe: patrimonial · pl · credora · normal · - · reservas-capital
- Nomes: Ágio na emissão de ações; Reserva de ágio na emissão de ações; Reserva de ágio
- Por quê: É a parte do preço pago pelo subscritor que ultrapassa o valor nominal da ação; vai para reserva de capital, não para o capital nem para o resultado (Lei 6.404/76, art. 182, §1º, "a"). Pode absorver prejuízos que superem os lucros acumulados e as reservas de lucros (art. 200, I).
- Liga: bp:reservas-capital
- Questões: F2117, F2118, F2123, F2175, F2181, F2188, F2205
### Histórias
- Ágio na emissão de ações | A companhia emitiu 100.000 ações novas de valor nominal R$ 1,00 e as vendeu à vista por R$ 1,50 cada; a conta que recebe os R$ 50.000 acima do valor nominal. (F2118)
- Reserva de ágio na emissão de ações | A sociedade tinha R$ 20.000 recebidos acima do valor nominal em emissões passadas; esgotadas a reserva estatutária e a reserva legal, usou R$ 15.000 desse saldo para absorver o prejuízo de dezembro. (F2175)
- Ágio na emissão de ações | Mesmo com prejuízo no ano, o PL da sociedade cresceu porque ela vendeu ações novas acima do valor nominal, sem que o excesso passasse pela DRE. (F2117)

## opcoes-outorgadas · Opções outorgadas reconhecidas
- Classe: patrimonial · pl · credora · normal · - · reservas-capital
- Nomes: Instrumentos patrimoniais outorgados
- Por quê: No pagamento baseado em ações liquidado com as próprias ações, a despesa de remuneração tem contrapartida no PL (CPC 10 (R1)); o Manual de Contabilidade Societária (FIPECAFI) apresenta essa conta junto das reservas de capital, porque o valor vem dos serviços dos empregados, e não do lucro. Se o plano fosse liquidado em dinheiro, a contrapartida seria passivo.
- Liga: bp:reservas-capital
- Questões: F3913
### Histórias
- Instrumentos patrimoniais outorgados | A S.A. deu 20 opções de ações a cada empregado, exercíveis após dois anos de serviço e liquidadas com ações da própria empresa; a conta que recebe, a cada ano, a contrapartida da despesa de remuneração. (F3913)

## ajustes-avaliacao-patrimonial · Ajustes de avaliação patrimonial
- Classe: patrimonial · pl · credora · normal · - · ajustes-avaliacao
- Nomes: Ajustes de avaliação patrimonial; Ajuste de avaliação patrimonial; Ajuste de avaliação patrimonial (saldo credor); Outros resultados abrangentes
- Depende: natureza; retificadora
- Por quê: Recebem as contrapartidas de aumentos e diminuições de valor justo de ativos e passivos enquanto não forem levadas ao resultado (Lei 6.404/76, art. 182, §3º, redação das Leis 11.638/2007 e 11.941/2009; CPC 26 (R1); CPC 48). Não é reserva e pode ter saldo credor (ganhos) ou devedor (perdas), por isso o nome sozinho não decide a natureza. Criado em 2007 com a expressão "a preço de mercado", trocada por "a valor justo" em 2009.
- Liga: bp:ajustes-avaliacao
- Questões: F0480, F1130, F1157, F1197, F2151, F2175, F2222, F2223, F2234, F2235, F2237, DRE:F0328
### Histórias
- Ajustes de avaliação patrimonial | A empresa tem 1% das ações de um fornecedor só para facilitar a compra de matéria-prima e mede essas ações a valor justo por outros resultados abrangentes; neste ano elas se valorizaram. (F1130)
- Ajustes de avaliação patrimonial | Um título comprado por R$ 50.000 rendeu R$ 5.000 de juros e passou a valer R$ 58.000 no mercado; a entidade leva as variações de valor justo ao PL. A conta que recebe os R$ 3.000 que excedem os juros. (F1157)
- Ajuste de avaliação patrimonial | O prédio usado pela própria empresa, com valor contábil de R$ 540.000, passou a ser propriedade para investimento medida a valor justo de R$ 610.000; a conta que recebe o aumento de R$ 70.000 na transferência. (F1197)

## reservas-lucros · Reservas de lucros
- Classe: patrimonial · pl · credora · normal · - · reservas-lucros
- Nomes: Reservas de lucros; Reserva de lucros; Reserva de lucro
- Por quê: São parcelas do lucro líquido que a companhia retém em vez de distribuir, cada uma com uma finalidade (Lei 6.404/76, arts. 182, §4º, e 193 a 197). O saldo delas, exceto contingências, incentivos fiscais e lucros a realizar, não pode passar do capital social (art. 199).
- Liga: bp:reservas-lucros
- Questões: F0083, F2140, F2143, F2168, F2174, F2185, F2190, F2249, F3211, DRE:F0314, DRE:F0554, DRE:F0641
### Histórias
- Reservas de lucros | Parte do lucro do ano que a companhia separou e manteve no patrimônio, para reinvestir ou distribuir mais tarde. (F2143)
- Reserva de lucros | Do lucro líquido de 2010, 5% foram para a reserva legal, 50% para dividendos e todo o restante ficou retido na empresa nesta conta. (DRE:F0314)
- Reservas de lucros | O saldo destas reservas da companhia passou do valor do capital social, e a assembleia teve de decidir entre aumentar o capital ou distribuir dividendos com o excesso. (F2190, F2174)

## reserva-legal · Reserva legal
- Classe: patrimonial · pl · credora · normal · - · reservas-lucros
- Nomes: Reserva legal; Reservas legais
- Por quê: Reserva de lucros obrigatória: 5% do lucro líquido, antes de qualquer outra destinação, até 20% do capital social; pode deixar de ser constituída quando, somada às reservas de capital, passar de 30% do capital (Lei 6.404/76, art. 193). Só serve para compensar prejuízos ou aumentar o capital (art. 193, §2º), e é a última reserva de lucros a absorver prejuízo (art. 189, parágrafo único).
- Liga: bp:reservas-lucros
- Questões: F2127, F2132, F2134, F2148, F2151, F2165, F2172, F2183, F2188, F2927, DRE:F0314, DRE:F0822
### Histórias
- Reserva legal | A companhia, de capital de R$ 50.000, já tinha R$ 9.200 nesta reserva obrigatória por lei; do lucro de R$ 23.000, só separou R$ 800, o que faltava para chegar a 20% do capital. (F2127)
- Reserva legal | Com capital de R$ 17.500.000, a companhia somava R$ 2.800.000 nesta reserva e R$ 2.625.000 em reservas de capital, mais de 30% do capital, e por isso pôde deixar de reforçá-la no ano. (F2132)
- Reservas legais | No início de 2010, a empresa usou todo o saldo desta reserva, formada com 5% dos lucros de cada ano, para aumentar o capital social. (DRE:F0314)

## reserva-estatutaria · Reserva estatutária
- Classe: patrimonial · pl · credora · normal · - · reservas-lucros
- Nomes: Reserva estatutária; Reservas estatutárias
- Por quê: Reserva de lucros prevista no estatuto, que deve indicar a finalidade, a parcela do lucro destinada e o limite (Lei 6.404/76, art. 194). Absorve prejuízo antes da reserva legal (art. 189, parágrafo único).
- Liga: bp:reservas-lucros
- Questões: F2105, F2126, F2134, F2137, F2148, F2149, F2175, F2183, F2184, F2186, F2927, F3211
### Histórias
- Reserva estatutária | O estatuto manda separar 10% do lucro líquido, depois da reserva legal, numa reserva com finalidade definida nele mesmo. (F2134, F2149)
- Reserva estatutária | No prejuízo de R$ 75.000, esta reserva, de R$ 50.000, foi a primeira a ser consumida, antes da reserva legal e do ágio na emissão de ações. (F2175)

## reserva-contingencias · Reserva para contingências
- Classe: patrimonial · pl · credora · normal · - · reservas-lucros
- Nomes: Reserva para contingências; Reservas para contingências; Reserva de contingências; Reserva de contingência
- Por quê: Parcela do lucro retida para compensar, em exercício futuro, a diminuição do lucro por perda julgada provável e estimável; é revertida quando a razão deixa de existir ou a perda ocorre (Lei 6.404/76, art. 195). É reserva de lucros (PL), e não provisão: a provisão para contingências é passivo.
- Liga: bp:reservas-lucros
- Questões: F2129, F2157, F2171, F2174, F2180, F2185, F2223, F2874, F3179, F3191, DRE:F0822
### Histórias
- Reserva para contingências | A companhia previu, com boa segurança, que o lucro do ano seguinte cairia 80% e separou parte do lucro deste ano para compensar a queda. (F2171)
- Reserva de contingência | A empresa reverteu R$ 150.000 desta parcela de lucros retida, porque deixaram de existir os motivos que justificaram a sua formação. (F3179, F2129)

## reserva-incentivos-fiscais · Reserva de incentivos fiscais
- Classe: patrimonial · pl · credora · normal · - · reservas-lucros
- Nomes: Reserva de incentivos fiscais
- Por quê: Por proposta da administração e decisão da assembleia, recebe a parte do lucro que veio de doações ou subvenções governamentais para investimento, que pode ficar fora da base do dividendo obrigatório (Lei 6.404/76, art. 195-A; CPC 07 (R1)). A subvenção passa antes pelo resultado; até 2007, as subvenções para investimento iam direto para reserva de capital.
- Liga: bp:reservas-lucros
- Questões: F2130, F2140, F2174, F2180, F2185, F2190, F3888
### Histórias
- Reserva de incentivos fiscais | A empresa teve redução de ICMS concedida como subvenção para investimento; o valor passou pelo resultado e, depois, por proposta da administração aprovada em assembleia, parte do lucro foi separada nesta conta, fora da base do dividendo obrigatório. (F3888)
- Reserva de incentivos fiscais | Dos R$ 300.000 de lucro, R$ 50.000 vieram de incentivos fiscais, e a empresa os reteve no PL para não ter de distribuí-los nem tributá-los. (F2130)

## reserva-lucros-a-realizar · Reserva de lucros a realizar
- Classe: patrimonial · pl · credora · normal · - · reservas-lucros
- Nomes: Reserva de lucros a realizar; Reservas de lucros a realizar
- Por quê: Quando o dividendo obrigatório passa da parcela do lucro já realizada financeiramente, a assembleia pode reter a diferença nesta reserva (Lei 6.404/76, art. 197); é uma faculdade, não obrigação. Quando o lucro se realiza, a reserva é revertida para lucros acumulados e o valor entra no dividendo.
- Liga: bp:reservas-lucros
- Questões: F0427, F2105, F2117, F2126, F2157, F2174, F2180, F2181, F2185, DRE:F0267
### Histórias
- Reserva de lucros a realizar | Em 2024, parte do lucro da companhia aberta ainda não tinha virado dinheiro, e ela reteve R$ 20.000 para não pagar dividendo sobre essa parte; em 2025, com o lucro realizado, o valor foi revertido para lucros acumulados. (F2126, F2181)

## reserva-retencao-lucros · Reserva de retenção de lucros
- Classe: patrimonial · pl · credora · normal · - · reservas-lucros
- Nomes: Retenção de lucros; Reserva para expansão; Reserva de lucros para expansão; Reservas de lucros para expansão
- Por quê: Lucros retidos para financiar investimentos previstos em orçamento de capital aprovado pela assembleia (Lei 6.404/76, art. 196); a doutrina chama essa reserva também de reserva de lucros para expansão. Entra no limite das reservas de lucros em relação ao capital (art. 199).
- Liga: bp:reservas-lucros
- Questões: F2099, F2130, F2134, F2171, F2172, F2174, F2184, F2186, F2874, F3179, F3211
### Histórias
- Reserva para expansão | Depois da reserva legal, da reserva estatutária e do dividendo obrigatório, todo o saldo do lucro ficou retido na empresa para financiar o crescimento das atividades. (F2134, F2172)
- Retenção de lucros | O estatuto mandou reter na companhia o saldo do lucro que sobrou depois da reserva legal, da reserva de incentivos fiscais e dos dividendos obrigatórios. (F2130)

## dividendo-adicional-proposto · Dividendo adicional proposto
- Classe: patrimonial · pl · credora · normal · - · reservas-lucros
- Nomes: Dividendo adicional; Dividendos adicionais propostos; Dividendos adicionais
- Por quê: O dividendo acima do mínimo obrigatório, enquanto a assembleia não o aprova, não é obrigação presente: fica no PL, em conta específica, e só vai para o passivo quando declarado (ICPC 08 (R1)). A Lei não lhe dá subgrupo próprio: tecnicamente, ele é uma conta específica do PL, e **não** uma reserva de lucros (não está entre as reservas dos arts. 193 a 197 da Lei 6.404/76). O jogo o coloca em reservas de lucros só porque não tem a opção "outras contas do PL" e porque é a linha ao lado da qual ele costuma aparecer no balanço: ambos são lucro retido à espera de destinação. Em questão, se afirmarem que ele "é uma reserva de lucros", desconfie.
- Liga: bp:reservas-lucros
- Questões: F2183, F2186, F3179, F3211
### Histórias
- Dividendos adicionais propostos | Além do dividendo obrigatório já registrado, a administração propôs pagar mais R$ 97.000 aos acionistas, valor que a assembleia ainda vai votar. (F3211)
- Dividendo adicional | A administração propôs que o saldo que sobrou do lucro do exercício fosse pago aos acionistas além do mínimo obrigatório; no balanço, a assembleia ainda não tinha decidido. (F3179)

## acoes-tesouraria · Ações em tesouraria
- Classe: patrimonial · pl · devedora · retificadora · - · acoes-tesouraria
- Nomes: Ações em tesouraria
- Por quê: Ações da própria companhia que ela recomprou; aparecem como dedução da conta do PL de onde saíram os recursos da compra (Lei 6.404/76, art. 182, §5º), que só pode usar lucros ou reservas, exceto a legal (art. 30, §1º, "b"). Não são ativo, e os custos de transação da recompra entram no custo delas; na revenda, o ganho vai para reserva de capital, sem passar pelo resultado.
- Liga: bp:acoes-tesouraria
- Questões: F0083, F2125, F2193, F2223, F2237, F2261, F2264, F2266, F2803, F2874, F3191, F3211
### Histórias
- Ações em tesouraria | A companhia comprou 10.000 das suas próprias ações por R$ 12.000, para mantê-las guardadas e talvez revendê-las depois. (F2874)
- Ações em tesouraria | A sociedade readquiriu ações de sua emissão por R$ 100.000 e pagou mais R$ 15.000 de custos da operação, registrando os R$ 115.000 na mesma conta. (F2261)
- Ações em tesouraria | Conta que mostra, reduzindo a reserva de lucros usada na compra, as ações da própria empresa que ela recomprou no mercado. (F2223, F2266)

## lucros-acumulados · Lucros acumulados
- Classe: patrimonial · pl · credora · normal · - · lucros-prejuizos
- Nomes: Lucros acumulados; Lucro acumulado
- Por quê: Recebe o lucro do exercício, as reversões de reservas e os ajustes de exercícios anteriores, e dela saem as destinações (reservas e dividendos). Desde a Lei 11.638/2007, nas S.A. é conta transitória: o saldo credor não pode ficar no balanço, porque o lucro não destinado deve ser distribuído (Lei 6.404/76, art. 202, §6º); antes disso, e ainda hoje nas limitadas, o saldo credor podia permanecer.
- Liga: bp:lucros-prejuizos
- Questões: F2105, F2126, F2127, F2129, F2181, F2193, F2278, F2927, F3179, DRE:F0267, DRE:F0641, DRE:F0822
### Histórias
- Lucros acumulados | A companhia levou para esta conta o lucro do exercício e, a partir dela, debitou o valor destinado à reserva legal. (F2127)
- Lucros acumulados | O balanço de uma S.A. trazia R$ 10.000 de lucros sem destinação nesta conta, saldo credor que a lei atual não admite no fim do exercício. (F2278)
- Lucros acumulados | Em 2001, antes da Lei 11.638/2007, a companhia aberta manteve no PL os lucros que sobraram depois da reserva legal, da reserva de contingências e dos dividendos. (DRE:F0822)

## prejuizos-acumulados · Prejuízos acumulados
- Classe: patrimonial · pl · devedora · retificadora · - · lucros-prejuizos
- Nomes: Prejuízos acumulados
- Por quê: Saldo devedor da conta de lucros ou prejuízos acumulados: perdas que não foram absorvidas pelos lucros acumulados e pelas reservas de lucros e legal (Lei 6.404/76, art. 189, parágrafo único). É o subgrupo que fecha o PL (art. 178, §2º, III) e aparece com sinal negativo, reduzindo o patrimônio.
- Liga: bp:prejuizos-acumulados
- Questões: F0427, F1325, F2143, F2237, F2714, F2803, F2927, F3668, DRE:F0118, DRE:F0267, DRE:F0328, DRE:F0554
### Histórias
- Prejuízos acumulados | No balanço da investida, o capital social de R$ 36.000 aparece reduzido por R$ 6.000 de perdas de anos anteriores ainda não cobertas, e o PL total é de R$ 30.000. (F1325)
- Lucros ou prejuízos acumulados | O prejuízo do ano foi maior que todas as reservas de lucros disponíveis, e o saldo devedor que sobrou ficou nesta conta, reduzindo o PL.

## lucros-ou-prejuizos-acumulados · Lucros ou prejuízos acumulados
- Classe: patrimonial · pl · credora · normal · - · lucros-prejuizos
- Nomes: Lucros ou prejuízos acumulados
- Depende: natureza; retificadora
- Por quê: O nome é o da conta mista que acumula os resultados: credora quando guarda lucros, devedora (prejuízos acumulados, redutora do PL) quando guarda perdas (Lei 6.404/76, art. 178, §2º, "d", na redação original). Nas S.A. de hoje, o saldo credor é só transitório, e no balanço sobra apenas o devedor.
- Liga: bp:lucros-prejuizos
- Questões: DRE:F0554
### Histórias
- Lucros ou prejuízos acumulados | Ao encerrar o exercício, a empresa transferiu para esta conta o lucro apurado, antes de destiná-lo às reservas e aos dividendos.

## reserva-reavaliacao · Reserva de reavaliação
- Classe: patrimonial · pl · credora · normal · - · reservas-reavaliacao
- Nomes: Reserva de reavaliação; Reservas de reavaliação; Reservas de reavaliações
- Por quê: Recebia a contrapartida do aumento de valor de bens reavaliados por laudo (Lei 6.404/76, art. 182, §3º, redação original). A Lei 11.638/2007 acabou com a reavaliação espontânea: os saldos de então puderam ser mantidos até a realização dos bens (depreciação, baixa ou venda, com transferência para lucros acumulados) ou estornados até o fim de 2008 (art. 6º). Por isso a conta ainda aparece, só com saldo remanescente.
- Liga: bp:reservas-reavaliacao
- Questões: F1492, F2214, DRE:F0554, DRE:F0641
### Histórias
- Reserva de reavaliação | Em 2024, a companhia fechada ainda tinha no PL o saldo de reavaliações de bens feitas antes de 2008, mantido e baixado aos poucos conforme os bens se realizam. (F2214)

## nao-controladores · Participação de não controladores
- Classe: patrimonial · pl · credora · normal · - · nao-controladores
- Nomes: Participação de não controladores
- Por quê: No balanço consolidado, a parte do patrimônio das controladas que pertence a outros sócios aparece dentro do PL, separada do PL dos controladores (CPC 26 (R1), item 54, "q"; CPC 36 (R3)). Antes, era apresentada entre o passivo e o PL, como "participação minoritária".
- Liga: bp:nao-controladores
- Questões: F2656, F3696
### Histórias
- Participação de não controladores | A Cia. Alfa comprou 70% da Cia. Beta; no balanço consolidado, os 30% do patrimônio da Beta que continuam com outros sócios. (F3696)
- Participação de não controladores | No consolidado da Cia. Y, dona de 90% da Cia. X, a fatia do patrimônio da Cia. X que pertence à Cia. Z, dona dos outros 10%. (F2656)

<!-- ===== Receitas e deduções ===== -->

## receita-vendas · Receita de vendas
- Classe: resultado · receita · credora · normal · - · receita-bruta
- Nomes: Receita de vendas; Receitas de vendas; Receita de vendas de mercadorias; Vendas; Vendas de mercadorias; Vendas de Produtos; Vendas à vista; Venda à vista; Vendas a prazo
- Por quê: É a receita da atividade principal (venda de mercadorias ou produtos), reconhecida quando o controle passa ao cliente, tenha ou não sido recebida (CPC 47; Lei 6.404/76, art. 187, I). Na venda a prazo com juros embutidos relevantes, a receita entra pelo valor presente, e a diferença vira receita financeira ao longo do prazo (Lei 6.404/76, art. 183, VIII; CPC 12). Perdas estimadas com clientes e gastos com garantia são despesas: não reduzem a receita.
- Liga: dre:receita-bruta
- Questões: DRE:F0009, DRE:F0020, DRE:F0045, DRE:F0108, DRE:F0164, DRE:F0176, DRE:F0238, DRE:F0276, DRE:F0434, F0773, F3918, F3956
### Histórias
- Receita de vendas | A empresa vendeu R$ 3 milhões em produtos para receber no ano seguinte e estima, com base confiável, que 3% não serão pagos e que 2% serão gastos com consertos em garantia. (DRE:F0009)
- Vendas a prazo | Uma loja vendeu mercadorias para receber numa parcela única daqui a dois anos, com juros de mercado embutidos no preço; na data da venda, entra no resultado a parte que corresponde ao preço à vista. (DRE:F0045, F3956)
- Receita de vendas | Uma comercial vendeu por R$ 1.020.000, para receber em um ano, mercadorias que à vista sairiam por R$ 850.000, num prazo muito maior que os 90 dias que costuma dar aos clientes. (F0773)

## receita-bruta-vendas · Receita bruta de vendas
- Classe: resultado · receita · credora · normal · - · receita-bruta
- Nomes: Receita bruta de vendas; Receita bruta; Receita Operacional Bruta de Vendas; Vendas brutas
- Por quê: É a primeira linha da DRE da Lei: tudo o que a atividade principal faturou com vendas e serviços, antes de devoluções, abatimentos, descontos incondicionais e tributos sobre vendas (Lei 6.404/76, art. 187, I). Pelo CPC 26 a DRE já começa na receita líquida, e a conciliação vai para as notas (CPC 47). Aluguel só entra aqui quando alugar é o objeto da empresa.
- Liga: dre:receita-bruta
- Questões: DRE:F0044, DRE:F0181, DRE:F0205, DRE:F0237, DRE:F0257, DRE:F0306, DRE:F0341, DRE:F0416, DRE:F0670, DRE:F0735, F3043
### Histórias
- Receita bruta de vendas | Uma loja de roupas não teve devoluções nem perdas no ano, e a questão manda desconsiderar os tributos sobre vendas: o que ela faturou com as vendas abre a DRE e, nesse caso, também é a receita líquida. (F3043)
- Vendas brutas | A companhia faturou R$ 2 milhões com vendas no ano; desse valor ainda saem devoluções, abatimentos e impostos sobre vendas até chegar à receita líquida. (DRE:F0237)
- Receita de aluguel | Uma administradora cujo objeto social é alugar os imóveis que possui registrou os aluguéis do mês.

## receita-servicos · Receita de serviços
- Classe: resultado · receita · credora · normal · - · receita-bruta
- Nomes: Receita de Serviços; Receita de prestação de serviços
- Por quê: É a receita da atividade principal de quem presta serviços e entra na receita bruta ao lado das vendas (Lei 6.404/76, art. 187, I; CPC 47). O ISS que incide sobre ela é dedução; se o recebimento for a prazo longo, a receita também vai a valor presente (CPC 12).
- Liga: dre:receita-bruta
- Questões: DRE:F0410, DRE:F0411, F3925
### Histórias
- Receita de Serviços | Uma concessionária de serviço público emitiu faturas com vencimento em 12 meses e calculou juros embutidos relevantes; o serviço é reconhecido pelo valor sem esses juros. (F3925)
- Receita de prestação de serviços | Além de vender mercadorias, uma empresa comercial presta serviços aos clientes e somou R$ 800 mil por eles no ano, com o ISS calculado por dentro. (DRE:F0410)

## devolucoes-vendas · Devoluções de vendas
- Classe: resultado · receita · devedora · retificadora · - · deducoes
- Nomes: Devoluções de vendas; Devolução de vendas; Devoluções de venda; Vendas canceladas
- Por quê: Desfaz, no todo ou em parte, uma venda do próprio exercício; por isso reduz a receita bruta como retificadora, de saldo devedor (Lei 6.404/76, art. 187, I; Decreto-Lei 1.598/77, art. 12, § 1º, I). Igor Cintra lembra que a devolução de venda de exercício já encerrado tende a ir para despesa com vendas, mas só trate assim se o enunciado disser.
- Liga: dre:deducoes
- Questões: DRE:F0044, DRE:F0108, DRE:F0192, DRE:F0205, DRE:F0218, DRE:F0238, DRE:F0265, DRE:F0388, DRE:F0434, DRE:F0617, DRE:F0735, F2063
### Histórias
- Devolução de vendas | Parte das mercadorias vendidas no ano voltou porque o cliente desistiu da compra, e a empresa estornou o valor das notas. (DRE:F0108)
- Vendas canceladas | Vendas faturadas no exercício foram canceladas, e a questão dá o lucro bruto, o CMV e as deduções para que se chegue à receita bruta. (DRE:F0735)

## abatimentos-vendas · Abatimentos sobre vendas
- Classe: resultado · receita · devedora · retificadora · - · deducoes
- Nomes: Abatimentos sobre vendas; Abatimento sobre Vendas
- Por quê: É a redução de preço dada depois da venda, por defeito, avaria ou diferença de qualidade, sem que a mercadoria volte; deduz-se da receita bruta, com saldo devedor (Lei 6.404/76, art. 187, I). Não se confunde com o desconto por pagamento antecipado, que é despesa financeira.
- Liga: dre:deducoes
- Questões: DRE:F0044, DRE:F0205, DRE:F0218, DRE:F0237, DRE:F0265, DRE:F0272, DRE:F0306, DRE:F0341, DRE:F0416, DRE:F0434
### Histórias
- Abatimentos sobre vendas | O cliente reclamou de avarias nas mercadorias que recebeu e, para ficar com elas, aceitou pagar a duplicata com uma redução de valor.

## devolucoes-abatimentos-vendas · Devoluções e abatimentos sobre vendas
- Classe: resultado · receita · devedora · retificadora · - · deducoes
- Nomes: Devoluções e abatimentos sobre vendas
- Por quê: Conta que junta as duas deduções (mercadoria devolvida e preço reduzido depois da venda); continua sendo retificadora da receita bruta (Lei 6.404/76, art. 187, I).
- Liga: dre:deducoes
- Questões: DRE:F0276, DRE:F0283
### Histórias
- Devoluções e abatimentos sobre vendas | A indústria reuniu numa conta só as mercadorias que voltaram e os descontos dados depois por defeito; a questão pede as vendas líquidas e traz, de propósito, ICMS a recuperar e contribuição social. (DRE:F0276)

## descontos-incondicionais-concedidos · Descontos incondicionais concedidos
- Classe: resultado · receita · devedora · retificadora · - · deducoes
- Nomes: Descontos Incondicionais Concedidos; Desconto comercial de vendas; Descontos concedidos a grandes clientes
- Por quê: É o desconto dado no ato da venda e destacado na nota, sem depender de nada futuro (volume, cliente especial, promoção); reduz a receita bruta como retificadora (Lei 6.404/76, art. 187, I; Decreto-Lei 1.598/77, art. 12, § 1º, II; CPC 47). O desconto condicional, por pagamento antecipado, é despesa financeira; o incondicional obtido nas compras reduz o custo da mercadoria.
- Liga: dre:deducoes
- Questões: DRE:F0410, DRE:F0621, DRE:F0670, DRE:F0735, DRE:F0776, DRE:F0779, F0838, F2063
### Histórias
- Descontos concedidos a grandes clientes | A empresa deu, já na nota fiscal, um desconto aos clientes que compram em grande volume, sem nenhuma condição posterior; os descontos por pagamento antecipado ficaram em outra conta. (DRE:F0410)
- Desconto comercial | Um supermercado que mede o estoque pelo método do varejo vendeu alguns produtos abaixo do preço básico de etiqueta; a diferença para esse preço reduz a venda. (F0838)
- Descontos Incondicionais Concedidos | A lista traz descontos incondicionais concedidos aos clientes e obtidos dos fornecedores, e a questão parte do lucro bruto para chegar à receita bruta. (DRE:F0735)

## impostos-sobre-vendas · Impostos sobre vendas
- Classe: resultado · receita · devedora · retificadora · - · deducoes
- Nomes: Impostos sobre vendas; Impostos sobre as vendas; Impostos incidentes sobre venda; Demais Impostos Incidentes sobre Vendas; Impostos e contribuições sobre a venda
- Por quê: Os tributos cobrados sobre a receita (ICMS, ISS, PIS e Cofins) não ficam com a empresa: reduzem a receita bruta, mesmo quando o balancete os chama de "despesa" (Lei 6.404/76, art. 187, I; Decreto-Lei 1.598/77, art. 12, § 1º, III). IR e CSLL incidem sobre o lucro e ficam depois do LAIR; o IPI, cobrado por fora, nem chega a integrar a receita bruta.
- Liga: dre:deducoes
- Questões: DRE:F0044, DRE:F0192, DRE:F0205, DRE:F0218, DRE:F0237, DRE:F0257, DRE:F0265, DRE:F0306, DRE:F0341, DRE:F0575, DRE:F0670, DRE:F0735
### Histórias
- Impostos sobre vendas | Os tributos calculados sobre o valor das notas de venda do ano somaram R$ 370 mil, e a questão pede a receita líquida. (DRE:F0237)

## icms-sobre-vendas · ICMS sobre vendas
- Classe: resultado · receita · devedora · retificadora · - · deducoes
- Nomes: ICMS sobre vendas; ICMS sobre venda
- Por quê: Imposto estadual calculado por dentro sobre as vendas de mercadorias: integra a receita bruta e sai dela como dedução (Lei 6.404/76, art. 187, I). O ICMS das compras com direito a crédito é outra conta, "ICMS a recuperar", do ativo circulante.
- Liga: dre:deducoes
- Questões: DRE:F0242, DRE:F0272, DRE:F0276, DRE:F0283, DRE:F0410, DRE:F0621, DRE:F0670
### Histórias
- ICMS sobre vendas | O balancete traz o ICMS calculado sobre as vendas do mês e o ICMS a recuperar das compras, e a questão pede a receita líquida de vendas. (DRE:F0272)

## pis-cofins-sobre-vendas · PIS e Cofins sobre vendas
- Classe: resultado · receita · devedora · retificadora · - · deducoes
- Nomes: PIS sobre faturamento; PIS sobre o faturamento; PIS sobre Vendas; COFINS sobre faturamento; COFINS sobre o faturamento; COFINS sobre vendas
- Por quê: Contribuições calculadas sobre a receita, no regime cumulativo ou no não cumulativo; são dedução da receita bruta (Lei 6.404/76, art. 187, I). Os créditos de PIS e Cofins sobre compras vão para o ativo ("a recuperar"), e a CSLL, apesar do nome de contribuição, é tributo sobre o lucro.
- Liga: dre:deducoes
- Questões: DRE:F0242, DRE:F0272, DRE:F0273, DRE:F0276, DRE:F0283, DRE:F0621
### Histórias
- COFINS sobre o faturamento | A tabela mostra ICMS, PIS e Cofins calculados sobre o faturamento e também a CSLL; só os três primeiros separam a receita bruta das vendas líquidas. (DRE:F0242)
- PIS sobre faturamento | Ao lado do PIS a recuperar das compras, o balancete mostra o PIS calculado sobre a receita das vendas do período. (DRE:F0272)

## iss-sobre-servicos · ISS sobre serviços prestados
- Classe: resultado · receita · devedora · retificadora · - · deducoes
- Nomes: ISS sobre serviços prestados
- Por quê: Imposto municipal sobre a receita de serviços; deduz-se da receita bruta, como o ICMS nas vendas (Lei 6.404/76, art. 187, I; Decreto-Lei 1.598/77, art. 12, § 1º, III).
- Liga: dre:deducoes
- Questões: DRE:F0410, DRE:F0411
### Histórias
- ISS sobre serviços prestados | Uma comercial que também presta serviços calculou o imposto municipal sobre o que cobrou por eles, e a questão pede a receita líquida de vendas e serviços. (DRE:F0410)

## receitas-financeiras · Receitas financeiras
- Classe: resultado · receita · credora · normal · - · resultado-financeiro
- Nomes: Receita financeira; Receitas financeiras
- Por quê: São os rendimentos do dinheiro aplicado ou emprestado: juros ativos, descontos obtidos, rendimentos de aplicações, variações monetárias e cambiais ativas e apropriação do AVP de vendas a prazo (Lei 6.404/76, art. 187, III; CPC 26, item 82). Pela Lei, ficam antes do resultado operacional, deduzindo as despesas financeiras; pelo CPC 26, depois do resultado antes do resultado financeiro.
- Liga: dre:resultado-financeiro
- Questões: DRE:F0108, DRE:F0175, DRE:F0283, DRE:F0326, DRE:F0388, DRE:F0396, DRE:F0434, DRE:F0617, DRE:F0621, F0392, F1142
### Histórias
- Receita financeira | A sociedade fez uma aplicação de longo prazo cujos juros são somados ao principal todo mês, para resgate só no vencimento. (F0392)
- Receita financeira | A empresa mantém uma debênture que rende juros anuais e escolheu levar a variação do valor justo para outros resultados abrangentes; os juros do ano vão para o resultado. (F1142)

## receita-juros · Receitas de juros
- Classe: resultado · receita · credora · normal · - · resultado-financeiro
- Nomes: Receitas de juros
- Por quê: Juros ativos, ganhos sobre valores emprestados, aplicados ou cobrados de clientes em atraso, são receita financeira (Lei 6.404/76, art. 187, III). Não confunda com "juros a receber" (ativo) nem com "juros ativos a transcorrer" (retificadora do ativo).
- Liga: dre:resultado-financeiro
- Questões: DRE:F0272, DRE:F0273
### Histórias
- Receitas de juros | Um cliente pagou a duplicata com 30 dias de atraso, e a empresa cobrou juros de mora sobre o valor devido.
- Receitas de juros | No balancete, ao lado das despesas de juros, aparecem os juros ganhos no período, e a questão pede o lucro do exercício. (DRE:F0273)

## apropriacao-avp-vendas · Receita financeira comercial (apropriação do AVP de vendas)
- Classe: resultado · receita · credora · normal · - · resultado-financeiro
- Nomes: Receita financeira comercial
- Por quê: Na venda a prazo, os juros embutidos saem da receita de vendas (ajuste a valor presente) e são reconhecidos como receita financeira com o passar do prazo, pela taxa da operação (Lei 6.404/76, art. 183, VIII; CPC 12). Exceção do CPC 12 (item 33): se a entidade tem um segmento próprio de financiamento das vendas e o efeito é relevante, a reversão pode ser apresentada como receita operacional.
- Liga: dre:resultado-financeiro
- Questões: DRE:F0020, DRE:F0045, DRE:F0164, DRE:F0176, DRE:F0298, F3918, F3938, F3956, F3961, F3966, F3973, F3975
### Histórias
- Receita financeira comercial | Uma indústria vendeu máquinas para receber em 14 meses, com juros de 2% ao mês embutidos no preço, e, passado o primeiro mês, apropriou a parcela de juros transcorrida. (F3961)
- Receita financeira | Vendas a prazo feitas no início de dezembro, para receber em 18 meses, foram trazidas a valor presente; em 31/12 já transcorreu um mês da taxa da operação. (DRE:F0020)
- Receita financeira | Uma venda a prazo feita no último dia do ano, para receber em 12 meses, foi trazida a valor presente; os juros embutidos só aparecem no resultado do ano seguinte. (F3975, F3977)

## descontos-financeiros-obtidos · Descontos financeiros obtidos
- Classe: resultado · receita · credora · normal · - · resultado-financeiro
- Nomes: Descontos Financeiros Obtidos; Desconto financeiro de compras
- Por quê: É o desconto condicional ganho por pagar o fornecedor antes do vencimento: receita financeira, que não reduz o custo das compras (Lei 6.404/76, art. 187, III; CPC 16). Quem reduz o custo é o desconto incondicional obtido, dado na nota de compra.
- Liga: dre:resultado-financeiro
- Questões: DRE:F0670, DRE:F0776, DRE:F0779, DRE:F0780
### Histórias
- Descontos Financeiros Obtidos | A empresa quitou as duplicatas de um fornecedor dez dias antes do vencimento e, por isso, pagou menos que o valor dos títulos.
- Desconto financeiro de compras | No mês, a empresa ganhou um desconto por pagar antes do prazo mercadorias que comprou, e a questão pede o CMV do período, que esse desconto não reduz. (DRE:F0780)

## variacoes-monetarias-ativas · Variações monetárias ativas
- Classe: resultado · receita · credora · normal · - · resultado-financeiro
- Nomes: Variações Monetárias Ativas
- Por quê: Ganho pela atualização, por índice ou por moeda estrangeira, de direitos (que aumentam) ou de obrigações (que diminuem); é receita financeira (Lei 6.404/76, art. 187, III; CPC 02, na variação cambial).
- Liga: dre:resultado-financeiro
- Questões: DRE:F0670
### Histórias
- Variações Monetárias Ativas | A empresa tem um crédito a receber corrigido por índice de preços e, no ano, o índice subiu, aumentando o valor do direito.

## receita-equivalencia-patrimonial · Receita de equivalência patrimonial
- Classe: resultado · receita · credora · normal · - · equivalencia
- Nomes: Receita de equivalência patrimonial; Ganho na Equivalência Patrimonial; Resultado Positivo em Participações Societárias; Parcela do lucro de empresas investidas reconhecidas por meio do método de equivalência patrimonial
- Aceita: subgrupo=outras-operacionais
- Por quê: É a parte do lucro de coligadas e controladas que cabe à investidora, reconhecida pelo método da equivalência patrimonial (Lei 6.404/76, art. 248; CPC 18). O CPC 26 (item 82) dá a ela linha própria; na estrutura da Lei, muitos autores a apresentam entre as outras receitas operacionais, daí a resposta alternativa. Dividendos recebidos dessas investidas não são receita: reduzem o investimento.
- Liga: dre:equivalencia
- Questões: DRE:F0283, DRE:F0621, DRE:F0622, DRE:F0670, F2150
### Histórias
- Parcela do lucro de empresas investidas reconhecidas por meio do método de equivalência patrimonial | A empresa reconhece pela equivalência a parte que lhe cabe no lucro das suas investidas, e a questão pede o resultado antes do IR e da CSLL. (DRE:F0283)
- Resultado Positivo em Participações Societárias | A empresa avalia suas controladas por equivalência e, no ano, elas tiveram lucro; o valor entra no lucro operacional da estrutura da Lei. (DRE:F0670)

## resultado-equivalencia-patrimonial · Resultado de equivalência patrimonial
- Classe: resultado · receita · credora · normal · - · equivalencia
- Nomes: Resultado de Equivalência Patrimonial; Parcela dos resultados de empresas investidas reconhecidas por meio do método de equivalência patrimonial; Resultado com equivalência patrimonial
- Depende: grupo; natureza
- Aceita: subgrupo=outras-operacionais
- Por quê: O nome sozinho não diz o sinal: se as investidas lucraram, é receita; se tiveram prejuízo, é despesa na mesma linha (CPC 18; CPC 26, item 82). A leitura padrão das questões é o resultado positivo; a alternativa de subgrupo segue a da receita de equivalência.
- Liga: dre:equivalencia
- Questões: DRE:F0326, F2150, F3539
### Histórias
- Resultado de Equivalência Patrimonial | A Cia. X tem 100% da Cia. Y, avaliada por equivalência patrimonial, e a Y apurou lucro líquido de R$ 10 mil no ano. (F2150)
- Parcela dos resultados de empresas investidas reconhecidas por meio do método de equivalência patrimonial | A parte que cabe à empresa nos lucros das suas investidas soma R$ 120 mil e aumenta o lucro antes do IR. (DRE:F0326)
- Resultado com equivalência patrimonial | A investidora tem 80% de uma investida que lucrou R$ 50 mil no ano e avalia essa participação pelo método da equivalência patrimonial. (F3539)

## outras-receitas-operacionais · Outras receitas operacionais
- Classe: resultado · receita · credora · normal · - · outras-operacionais
- Nomes: Outras receitas operacionais
- Por quê: São as receitas de atividades acessórias, que não vêm da venda da atividade principal nem são financeiras: aluguel eventual, venda de sucata, reversões, publicidade num negócio que não é de publicidade (Lei 6.404/76, art. 187, III; CPC 26, item 82). Ficam dentro do resultado operacional.
- Liga: dre:outras-operacionais
- Questões: DRE:F0087, DRE:F0191, F3042, F3146
### Histórias
- Receita com a publicidade | Uma companhia aérea vende anúncios na revista de bordo que distribui de graça aos passageiros; a atividade da empresa é o transporte aéreo. (DRE:F0087, F3042)

## receita-aluguel · Receita de aluguel
- Classe: resultado · receita · credora · normal · - · outras-operacionais
- Nomes: Receita de aluguel
- Depende: subgrupo
- Por quê: Quando alugar não é o objeto da empresa, o aluguel recebido é outra receita operacional, e não receita financeira (Lei 6.404/76, art. 187, III). Se a empresa vive de alugar imóveis, o aluguel é a sua receita bruta (CPC 06).
- Liga: dre:outras-operacionais
- Questões: DRE:F0191, F3146
### Histórias
- Receita de aluguel | Uma loja de calçados alugou a terceiros uma sala que estava sem uso no andar de cima do prédio.

## reversao-pecld · Reversão das perdas estimadas com créditos de liquidação duvidosa
- Classe: resultado · receita · credora · normal · - · outras-operacionais
- Nomes: Reversão para Créditos de Liquidação Duvidosa; Reversão da provisão para créditos de liquidação duvidosa; Reversão das perdas estimadas; Reversão das perdas estimadas com crédito de liquidação duvidosa
- Por quê: Quando a perda estimada com clientes supera a que de fato ocorreu (ou a nova estimativa é menor que o saldo), o excesso volta ao resultado como receita operacional, sem tocar a receita bruta nem o lucro bruto (CPC 48; Lei 6.404/76, art. 187, III). "Provisão para créditos de liquidação duvidosa" é o nome antigo; hoje se fala em perdas estimadas (ou esperadas) com créditos.
- Liga: dre:outras-operacionais
- Questões: DRE:F0326, DRE:F0396, DRE:F0434, F1055, F3061
### Histórias
- Reversão das perdas estimadas | A entidade estimou perda de 4% sobre R$ 120 mil a receber; no mês seguinte recebeu R$ 116 mil e encerrou a carteira, e a parte da estimativa que não se confirmou voltou ao resultado. (F1055)
- Reversão das perdas estimadas com crédito de liquidação duvidosa | A sociedade reverteu R$ 10 mil de perdas estimadas com clientes: o valor mexe no resultado antes do resultado financeiro e no resultado líquido, mas não no resultado bruto. (F3061)

## reversao-provisoes · Reversão de provisões
- Classe: resultado · receita · credora · normal · - · outras-operacionais
- Nomes: Reversão de Provisões; Reversão da provisão
- Por quê: A provisão constituída a mais (contingência, garantia) que deixa de ser necessária volta ao resultado como outra receita operacional (CPC 25, item 59); o mesmo vale para a reversão de perda por desvalorização de ativos (CPC 01, item 119). Fica dentro do resultado operacional.
- Liga: dre:outras-operacionais
- Questões: DRE:F0621, DRE:F0622, DRE:F0670, F1876, F2499
### Histórias
- Reversão da provisão | A companhia aérea provisionou R$ 24 mil para oito processos de passageiros; perdeu cinco, pagando R$ 20 mil no total, e ganhou três, sem possibilidade de recurso, e o excesso provisionado voltou ao resultado. (F2499)
- Reversão de Provisões | Na DRE da companhia, a reversão de provisões entra no lucro operacional, junto com as receitas financeiras e a equivalência patrimonial. (DRE:F0622)
- Reversão de perda por redução ao valor recuperável | Um terreno de uso que tinha acumulado R$ 20 mil de perdas por desvalorização voltou a valer mais que o custo, e a perda foi revertida até esse limite. (F1876)

## recuperacao-creditos-baixados · Recuperação de créditos baixados
- Classe: resultado · receita · credora · normal · - · outras-operacionais
- Nomes: Recuperação de créditos com clientes; Recuperação de perdas com créditos
- Por quê: É o valor recebido de cliente cujo crédito já tinha sido baixado como perda: outra receita operacional, que não é dedução nem entra na receita líquida (Lei 6.404/76, art. 187, III).
- Liga: dre:outras-operacionais
- Questões: DRE:F0237, DRE:F0416
### Histórias
- Recuperação de créditos com clientes | Um cliente cuja duplicata tinha sido baixada como incobrável num exercício anterior acabou pagando a dívida.
- Recuperação de perdas com créditos | Para chegar à receita líquida, a questão mistura devoluções, abatimentos, impostos sobre vendas e a recuperação de perdas com créditos; só esta última fica de fora das deduções. (DRE:F0416)

## outras-receitas · Outras receitas
- Classe: resultado · receita · credora · normal · - · outras-receitas-despesas
- Nomes: Outras receitas
- Depende: subgrupo
- Aceita: subgrupo=outras-operacionais
- Por quê: Pela Lei 6.404/76 (art. 187, IV, redação da Lei 11.941/2009), "outras receitas" são os ganhos fora das operações, sobretudo na venda ou baixa de investimentos, imobilizado e intangível, apresentados depois do resultado operacional. O CPC 26 não separa operacional de não operacional, e FGV e FCC costumam pôr esses ganhos nas outras receitas operacionais, daí a alternativa; já as "outras receitas" de atividade acessória (aluguel eventual, publicidade) são operacionais.
- Liga: dre:outras-receitas-despesas
- Questões: DRE:F0087, F1688, F1816, F3042
### Histórias
- Outras receitas | Uma consultoria contábil comprou um terreno para usar nas suas atividades e, meses depois, vendeu-o por R$ 25 mil acima do custo; o teste de recuperabilidade não tinha apontado perda. (F1816)
- Outras receitas | Um escritório pôs à venda, só para os empregados, computadores que usava e que já estavam em parte depreciados, e vendeu quatro deles acima do valor contábil. (F1688)

## ganho-alienacao-nao-circulante · Ganho na venda de bens do ativo não circulante
- Classe: resultado · receita · credora · normal · - · outras-receitas-despesas
- Nomes: Ganho de Capital na Venda de Bens Permanentes
- Aceita: subgrupo=outras-operacionais
- Por quê: É a diferença positiva entre o preço de venda e o valor contábil líquido de investimento, imobilizado ou intangível; entra pelo líquido, nunca pelo preço inteiro, e não é receita de vendas (CPC 27, itens 68 e 71; Lei 6.404/76, art. 187, IV). "Ativo permanente" era o nome do grupo antes da Lei 11.941/2009; a alternativa de subgrupo segue a das outras receitas.
- Liga: dre:outras-receitas-despesas
- Questões: DRE:F0191, DRE:F0670, F3146
### Histórias
- Ganho de Capital na Venda de Bens Permanentes | A empresa vendeu bens do antigo ativo permanente acima do valor contábil; na estrutura da Lei, o ganho fica fora do lucro operacional e entra antes dos tributos sobre o lucro. (DRE:F0670)

## receita-venda-imobilizado · Receita com venda de ativo imobilizado
- Classe: resultado · receita · credora · normal · - · outras-receitas-despesas
- Nomes: Receita com venda de ativo imobilizado
- Aceita: subgrupo=outras-operacionais
- Por quê: Forma bruta de registrar a venda de um imobilizado: o preço vai para esta conta e o valor contábil baixado vai para "custo do imobilizado vendido"; o que pesa no resultado é a diferença, que é outra receita (ou despesa), nunca receita de vendas nem parte do lucro bruto (Lei 6.404/76, art. 187, IV; CPC 27, item 68).
- Liga: dre:outras-receitas-despesas
- Questões: DRE:F0396
### Histórias
- Receita com venda de ativo imobilizado | A companhia vendeu por R$ 60 mil um bem do imobilizado cujo valor contábil era de R$ 23 mil, e a questão pede só o lucro bruto. (DRE:F0396)

## ganho-nao-operacional · Ganho não operacional (nome antigo)
- Classe: resultado · receita · credora · normal · - · outras-receitas-despesas
- Nomes: Ganho não-operacional; Resultado Não-operacional Positivo; Resultados não-operacionais (positivo)
- Por quê: Era o nome, até a Lei 11.941/2009, dos ganhos fora da atividade, como a venda de bens do ativo permanente; hoje são "outras receitas" (Lei 6.404/76, art. 187, IV). Na estrutura da Lei, ficam depois do resultado operacional e antes do LAIR.
- Liga: dre:outras-receitas-despesas
- Questões: DRE:F0575, DRE:F0621, DRE:F0622, DRE:F0623, DRE:F0776
### Histórias
- Resultado Não-operacional Positivo | Na DRE de 2006 da companhia, o ganho fora das operações não entra no lucro operacional, mas é somado a ele antes das provisões para IR e CSLL. (DRE:F0622, DRE:F0623)
- Ganho não-operacional | A empresa teve no mês um ganho fora da sua atividade comercial, e a questão pede o lucro operacional, tratando as receitas financeiras como operacionais. (DRE:F0776)

<!-- ===== Custos e despesas ===== -->

## cmv · Custo das mercadorias vendidas
- Classe: resultado · despesa · devedora · normal · - · cmv
- Nomes: Custo das mercadorias vendidas; CMV; Custo da mercadoria vendida
- Por quê: Custo das mercadorias que saíram com as vendas do período, reconhecido junto com a receita que elas geraram (confrontação) e deduzido da receita líquida para chegar ao lucro bruto (Lei 6.404/76, art. 187, II; CPC 16). É custo, e não despesa operacional.
- Liga: dre:cmv
- Questões: DRE:F0016, F2971, DRE:F0190, DRE:F0248, DRE:F0440, DRE:F0568, DRE:F0634, DRE:F0635, DRE:F0700, F2005, F3295, F3559
### Histórias
- Custo das mercadorias vendidas | A loja vendeu no ano mercadorias que lhe tinham custado R$ 6 milhões; esse valor sai da receita líquida antes das comissões, da propaganda e dos fretes de entrega. (DRE:F0016, F2971)
- CMV | No fim do ano, a empresa comercial apurou o custo do que vendeu somando o estoque inicial às compras líquidas e tirando o inventário final. (DRE:F0635)
- Custo da mercadoria vendida | Na apuração do resultado, o custo das mercadorias entregues aos clientes é encerrado contra o resultado do exercício, ao lado das despesas do período. (DRE:F0700)

## cpv · Custo dos produtos vendidos
- Classe: resultado · despesa · devedora · normal · - · cmv
- Nomes: Custo dos produtos vendidos; Custos dos produtos vendidos
- Por quê: Na indústria, matéria-prima, mão de obra e custos indiretos ficam no estoque de produtos; quando o produto é vendido, esse custo vai para a DRE como CPV, logo depois da receita líquida (art. 187, II; CPC 16). Na DRE pela natureza da despesa (CPC 26, item 102), o CPV não aparece como linha: os gastos aparecem como materiais consumidos, salários, depreciação.
- Liga: dre:cmv
- Questões: DRE:F0296, DRE:F0297, DRE:F0333, F3216, F3301, F3437, F3490
### Histórias
- Custo dos produtos vendidos | A fábrica vendeu no ano parte dos produtos que tinha em estoque; o custo de fabricação desses itens saiu do ativo e foi para o resultado, logo abaixo da receita líquida.
- Custo dos produtos vendidos | Na DRE da companhia, o custo dos itens vendidos vem logo depois da receita e forma o lucro bruto, antes das despesas com salários, depreciação e vendas. (F3437)

## csp · Custo dos serviços prestados
- Classe: resultado · despesa · devedora · normal · - · cmv
- Nomes: Custo dos serviços prestados; Custo do serviço prestado
- Por quê: Na empresa de serviços, o custo de executar os serviços vendidos (mão de obra, materiais e demais gastos aplicados) ocupa a linha do custo das vendas, abaixo da receita líquida (art. 187, II).
- Liga: dre:cmv
- Questões: DRE:F0700, DRE:F0750, DRE:F0751, DRE:F0752
### Histórias
- Custo dos serviços prestados | Uma operadora de telefonia fixa apresentou, logo abaixo da receita líquida, o custo de operar e manter a rede que gera os serviços que ela vende. (DRE:F0750)
- Custo do serviço prestado | Uma empresa que revende mercadorias e também presta serviços confrontou a receita dos serviços com o custo de executá-los no período. (DRE:F0700)

## compras-mercadorias · Compras de mercadorias
- Classe: resultado · despesa · devedora · normal · - · cmv
- Nomes: Compras de mercadorias; Compra de mercadorias; Compra de mercadorias para revenda; Compra de mercadorias à vista; Compras do período; Compras; Aquisição de mercadorias; Aquisição de mercadorias para revenda
- Por quê: No inventário periódico, a conta Compras acumula as aquisições do período e é encerrada no cálculo do CMV (estoque inicial + compras líquidas − estoque final); por isso o jogo a trata como conta de custo, na linha do CMV (CPC 16). Ela não vai para a DRE pelo saldo: compra não é despesa do período. **Atenção à outra leitura:** no inventário permanente não existe a conta Compras, porque a aquisição é debitada direto em Estoques (ativo circulante); e há autores que chamam Compras de conta patrimonial transitória. Em questão, veja qual sistema de inventário o enunciado adota: se ele mandar debitar Estoques, a classificação é do ativo. O jogo cobra a leitura do inventário periódico, a que as bancas usam no cálculo do CMV. O mesmo vale para fretes e seguros, devoluções, abatimentos e descontos incondicionais sobre compras.
- Liga: dre:calculo-cmv
- Questões: DRE:F0450, DRE:F0524, DRE:F0562, DRE:F0590, DRE:F0635, DRE:F0640, DRE:F0683, DRE:F0691, DRE:F0704, DRE:F0754, DRE:F0763, DRE:F0769
### Histórias
- Compras de mercadorias | A empresa usa inventário periódico: lançou as aquisições do ano numa conta própria e, no fim, somou-as ao estoque inicial e tirou o inventário final para achar o CMV. (DRE:F0635)
- Aquisição de mercadorias | No balancete, as mercadorias adquiridas no período aparecem ao lado do estoque inicial e do estoque final; o saldo só chega ao resultado por meio do custo das vendas. (DRE:F0691, DRE:F0769)

## fretes-seguros-compras · Fretes e seguros sobre compras
- Classe: resultado · despesa · devedora · normal · - · cmv
- Nomes: Fretes sobre compras; Frete sobre compras; Fretes sobre compras de mercadorias; Transporte sobre compras; Transportes sobre Compras; Seguro sobre compras; Seguros sobre compras; Seguro de compras; Seguros sobre compras de mercadorias; Carga e descarga de mercadorias adquiridas
- Por quê: O gasto para trazer a mercadoria até o estabelecimento integra o custo de aquisição do estoque (CPC 16, item 11) e, por isso, entra no CMV, nunca nas despesas com vendas. Frete da compra é custo; frete da venda é despesa. No inventário permanente, esse gasto vai direto para Estoques (ativo); o jogo cobra a leitura do inventário periódico (ver Compras de mercadorias).
- Liga: dre:calculo-cmv
- Questões: DRE:F0450, DRE:F0524, DRE:F0562, DRE:F0584, DRE:F0616, DRE:F0640, DRE:F0683, DRE:F0687, DRE:F0704, DRE:F0756, DRE:F0763, DRE:F0769
### Histórias
- Fretes sobre compras | A transportadora cobrou para levar as mercadorias do fornecedor até o depósito da loja, que vai revendê-las. (DRE:F0616)
- Seguro sobre compras | A empresa contratou seguro para o transporte das mercadorias compradas, do fornecedor até o seu armazém. (DRE:F0704)
- Carga e descarga de mercadorias adquiridas | Ao receber um lote comprado para revenda, a empresa pagou a equipe que descarregou as mercadorias no estoque. (DRE:F0584)

## devolucoes-compras · (–) Devoluções de compras
- Classe: resultado · despesa · credora · retificadora · - · cmv
- Nomes: Devolução de compras; Devolução de compras de mercadorias; Devolução de mercadorias adquiridas; Anulações de compras
- Por quê: A mercadoria devolvida ao fornecedor desfaz parte da compra: reduz as compras brutas e, com elas, o CMV (CPC 16). Como retifica uma conta de custo, que é devedora, tem natureza credora. No inventário permanente, a devolução é creditada direto em Estoques (ativo); o jogo cobra a leitura do inventário periódico (ver Compras de mercadorias).
- Liga: dre:calculo-cmv
- Questões: DRE:F0524, DRE:F0571, DRE:F0590, DRE:F0600, DRE:F0616, DRE:F0640, DRE:F0687, DRE:F0691, DRE:F0704, DRE:F0754, DRE:F0769
### Histórias
- Devolução de mercadorias adquiridas | A empresa mandou de volta ao fornecedor parte de um lote comprado para revenda, que chegou fora da especificação do pedido. (DRE:F0590)
- Anulações de compras | Uma compra a prazo foi cancelada depois de registrada, e as mercadorias voltaram ao fornecedor. (DRE:F0754)

## abatimentos-compras · (–) Abatimentos sobre compras
- Classe: resultado · despesa · credora · retificadora · - · cmv
- Nomes: Abatimento sobre compras; Abatimentos sobre compras; Abatimento de compras; Abatimento de compras de mercadorias; Abatimentos s/Compras
- Por quê: Redução de preço obtida depois da compra, por avaria, defeito ou atraso: diminui o custo de aquisição e, portanto, o CMV. Retifica uma conta de custo, por isso é credora. No inventário permanente, o abatimento é creditado direto em Estoques (ativo); o jogo cobra a leitura do inventário periódico (ver Compras de mercadorias).
- Liga: dre:calculo-cmv
- Questões: DRE:F0524, DRE:F0571, DRE:F0584, DRE:F0600, DRE:F0616, DRE:F0640, DRE:F0683, DRE:F0687, DRE:F0691, DRE:F0754
### Histórias
- Abatimento sobre compras | Parte das mercadorias compradas chegou com a embalagem danificada, e o fornecedor reduziu o valor da fatura em vez de recebê-las de volta. (DRE:F0683)

## descontos-incondicionais-obtidos · (–) Descontos incondicionais obtidos
- Classe: resultado · despesa · credora · retificadora · - · cmv
- Nomes: Descontos Comerciais sobre Compras; Descontos sobre compras; Desconto de compras; Deduções sobre compras
- Depende: grupo; retificadora; subgrupo
- Por quê: Desconto comercial dado pelo fornecedor na própria nota fiscal, sem nenhuma condição: reduz o custo da compra e o CMV (CPC 16, item 11). Se o desconto depender do pagamento antecipado (condicional), é receita financeira e não mexe nas compras. No inventário permanente, o desconto incondicional reduz direto o valor de Estoques (ativo); o jogo cobra a leitura do inventário periódico (ver Compras de mercadorias).
- Liga: dre:calculo-cmv
- Questões: DRE:F0640, DRE:F0683, DRE:F0691, DRE:F0756
### Histórias
- Descontos Comerciais sobre Compras | Na nota fiscal de compra das mercadorias, o fornecedor já destacou um desconto pelo volume do pedido, sem nenhuma condição de pagamento. (DRE:F0640)

## despesas-vendas · Despesas com vendas
- Classe: resultado · despesa · devedora · normal · - · despesas-vendas
- Nomes: Despesas com vendas; Despesas de vendas; Despesa de vendas; Despesas comerciais; Despesas de comercialização
- Por quê: Gastos para vender e entregar: salários e comissões de vendedores, propaganda de produtos, fretes de entrega e a despesa com PECLD (Lei 6.404/76, art. 187, III; CPC 26, item 103). Somadas às administrativas, formam as despesas operacionais.
- Liga: dre:despesas-vendas
- Questões: DRE:F0081, DRE:F0248, DRE:F0296, DRE:F0297, DRE:F0333, DRE:F0440, DRE:F0634, DRE:F0635, DRE:F0704, DRE:F0750, DRE:F0801, F3437
### Histórias
- Despesas comerciais | Na DRE, depois do lucro bruto, a empresa reuniu numa linha os gastos da sua área comercial com a equipe de vendas e as campanhas dos seus produtos. (DRE:F0801)

## despesa-pecld · Despesa com perdas estimadas em créditos de liquidação duvidosa
- Classe: resultado · despesa · devedora · normal · - · despesas-vendas
- Nomes: Despesa com perdas estimadas com créditos de liquidação duvidosa; Despesa com perdas estimadas com crédito de liquidação duvidosa; Despesa de perdas estimadas com crédito de liquidação duvidosa; Despesas com devedores duvidosos
- Por quê: É a constituição, no período, da estimativa dos clientes que não vão pagar (CPC 48): entra na DRE como despesa com vendas. O saldo acumulado (PECLD) é retificadora de clientes no ativo; "provisão para devedores duvidosos" é o nome antigo dessa estimativa.
- Liga: dre:despesas-vendas
- Questões: DRE:F0016, F2971, DRE:F0083, DRE:F0190, F3145, DRE:F0634, F3216, F3490, F3559, F3612
### Histórias
- Despesa com perdas estimadas com créditos de liquidação duvidosa | A loja estimou quanto das vendas a prazo do ano não vai receber e lançou esse valor no resultado; ele não mexe no lucro bruto, só no resultado operacional. (DRE:F0016, F2971)
- Despesas com devedores duvidosos | No balancete, o valor lançado como despesa do período é igual ao saldo da conta redutora de clientes, porque a estimativa foi constituída neste ano. (DRE:F0634)

## perdas-clientes · Perdas com clientes
- Classe: resultado · despesa · devedora · normal · - · despesas-vendas
- Nomes: Perdas c/ Clientes
- Por quê: Registra a baixa de duplicatas que se tornaram incobráveis sem estimativa suficiente para cobri-las; como a despesa com PECLD, é perda ligada às vendas a prazo e vai para as despesas com vendas. Se a PECLD já cobria o título, a baixa é feita contra ela, sem nova despesa.
- Liga: dre:despesas-vendas
- Questões: DRE:F0635, DRE:F0636
### Histórias
- Perdas c/ Clientes | Um cliente faliu, e a empresa baixou a duplicata dele, que a estimativa de perdas já constituída não cobria.

## fretes-vendas · Fretes e seguros sobre vendas
- Classe: resultado · despesa · devedora · normal · - · despesas-vendas
- Nomes: Despesa com fretes sobre vendas; Fretes sobre vendas; Fretes sobre vendas de mercadorias; Frete de vendas; Transporte de vendas; Transportes sobre Vendas
- Por quê: Gasto para entregar ao cliente a mercadoria vendida: despesa com vendas (art. 187, III). Não entra no custo do estoque, ao contrário do frete da compra (CPC 16, item 11).
- Liga: dre:despesas-vendas
- Questões: DRE:F0016, F2971, DRE:F0562, DRE:F0584, DRE:F0640, DRE:F0648, DRE:F0683, DRE:F0687, DRE:F0704, DRE:F0756, DRE:F0763
### Histórias
- Fretes sobre vendas | No mesmo mês, a empresa pagou um frete para receber mercadorias do fornecedor e outro para entregar pedidos aos clientes; esta conta registra o segundo. (DRE:F0704)

## comissoes-vendas · Comissões sobre vendas
- Classe: resultado · despesa · devedora · normal · - · despesas-vendas
- Nomes: Comissões sobre vendas; Comissão de vendas; Comissões s/Vendas; Despesas de comissões; Despesas com comissões de vendedores; Despesas de comissões de vendedores
- Por quê: Remuneração do vendedor proporcional ao que ele vende: despesa com vendas (art. 187, III), nunca dedução da receita bruta nem despesa administrativa.
- Liga: dre:despesas-vendas
- Questões: DRE:F0016, F2971, DRE:F0083, DRE:F0394, DRE:F0640, DRE:F0754, DRE:F0835, F3156
### Histórias
- Despesas de comissões de vendedores | Os vendedores recebem um percentual sobre cada venda que fecham; a banca considerou errado lançar esse gasto como despesa geral e administrativa. (DRE:F0835)
- Comissões sobre vendas | A loja pagou aos vendedores um percentual sobre as vendas do ano; o gasto não altera a receita líquida nem o lucro bruto. (DRE:F0016, F2971)

## propaganda · Propaganda e publicidade
- Classe: resultado · despesa · devedora · normal · - · despesas-vendas
- Nomes: Despesas com propaganda; Propaganda e publicidade; Despesas de propaganda; Despesas de publicidade
- Depende: subgrupo
- Por quê: A propaganda que promove a venda de produtos é despesa com vendas; a institucional, que divulga a imagem da empresa, é despesa administrativa (CEBRASPE, DATAPREV 2023). Sem essa informação, a banca a lê como despesa com vendas (art. 187, III).
- Liga: dre:despesas-vendas
- Questões: DRE:F0016, F2971, DRE:F0083, DRE:F0127, F3082, DRE:F0333, DRE:F0640, DRE:F0691, F3156
### Histórias
- Despesas com propaganda | A franquia de artigos esportivos pagou anúncios para promover os tênis da nova coleção que tem à venda. (DRE:F0127, F3082, F3156)

## propaganda-institucional · Propaganda institucional
- Classe: resultado · despesa · devedora · normal · - · despesas-administrativas
- Nomes: Propaganda institucional
- Por quê: Divulga a marca e a imagem da empresa, sem ligação com a venda de um produto: por isso a banca a classifica entre as despesas administrativas, e não nas despesas com vendas (CEBRASPE, DATAPREV 2023).
- Liga: dre:despesas-administrativas
- Questões: DRE:F0127, F3082
### Histórias
- Despesas com propaganda | A companhia patrocinou uma campanha sobre seus 50 anos de história e seus valores, sem anunciar nenhum produto. (DRE:F0127, F3082)

## salarios-vendedores · Salários dos vendedores
- Classe: resultado · despesa · devedora · normal · - · despesas-vendas
- Nomes: Salários dos vendedores
- Por quê: A remuneração do pessoal de vendas é despesa com vendas (art. 187, III). O que decide a linha é a função de quem trabalha, e não o vínculo: vendedor próprio ou terceirizado fica no mesmo grupo (FGV, ALEP 2024).
- Liga: dre:despesas-vendas
- Questões: DRE:F0081, DRE:F0825, F3156
### Histórias
- Salários dos vendedores terceirizados | Para reforçar o atendimento em dezembro, a loja de roupas contratou vendedores por meio de uma empresa terceirizada. (DRE:F0081)
- Salários dos vendedores | A franquia de artigos esportivos paga salário fixo à equipe que atende os clientes no balcão da loja. (F3156)

## despesa-salarios · Despesa de salários
- Classe: resultado · despesa · devedora · normal · - · despesas-administrativas
- Nomes: Despesa de salários; Despesas de salários; Despesa com salários; Despesas com salários; Despesas de salários e encargos; Despesa com salários e encargos; Despesa com salários e ordenados; Salários; Despesas com pessoal; Despesa com benefícios para os empregados; Salário do gerente da loja; Despesa de salários de empregados próprios
- Depende: subgrupo
- Por quê: Remuneração do período, reconhecida por competência quando o trabalho é prestado, paga ou não; o IR retido na fonte do empregado continua dentro da despesa bruta de salários. A linha segue a função: pessoal administrativo vai para despesas administrativas, vendedores para despesas com vendas e operários da fábrica para o custo de produção (CEBRASPE, PARANAPREVIDÊNCIA 2002).
- Liga: dre:despesas-administrativas
- Questões: DRE:F0190, DRE:F0634, DRE:F0825, DRE:F0834, F0499, F0501, F0503, F0527, F2317, F2321, F3495, F3518
### Histórias
- Despesa com salários | Em 31 de março, a empresa registrou o salário do mês do novo gerente de recursos humanos, que só começou a trabalhar em março e será pago no 5º dia útil de abril. (F0527)
- Despesa de salários | A folha do escritório central somou R$ 500 mil no mês, dos quais R$ 120 mil foram retidos dos empregados como IR na fonte; a despesa de salários é o valor bruto. (F0499, F2321)
- Despesas com salários | O salário dos advogados do departamento jurídico, que assessoram a diretoria, foi lançado no resultado do mês. (DRE:F0834)

## encargos-sociais · Encargos sociais da empresa sobre a folha
- Classe: resultado · despesa · devedora · normal · - · despesas-administrativas
- Nomes: INSS sobre salários (parcela da empresa); FGTS sobre salários
- Depende: subgrupo
- Por quê: As contribuições que o empregador paga sobre a folha (INSS patronal, FGTS) são despesa da empresa e acompanham a função dos empregados; sem informação, despesas administrativas. O INSS descontado do empregado não é despesa da empresa: é parte do salário bruto retida para repasse.
- Liga: dre:despesas-administrativas
- Questões: F3216, F3490, F3495, F3518, F3542, F3566
### Histórias
- FGTS sobre salários | Entre as despesas gerais da companhia estavam o FGTS e o INSS patronal calculados sobre a folha do período, com o FGTS ainda a recolher. (F3216, F3490)

## honorarios-administracao · Honorários da administração
- Classe: resultado · despesa · devedora · normal · - · despesas-administrativas
- Nomes: Honorários da administração
- Por quê: Remuneração fixa dos diretores e conselheiros (pró-labore) é gasto de gestão: despesa administrativa (FGV, ALETO 2024). Não se confunde com a participação dos administradores no lucro, que vem depois do IR e da CSLL (Lei 6.404/76, arts. 152 e 187, VI).
- Liga: dre:despesas-administrativas
- Questões: DRE:F0083
### Histórias
- Honorários da administração | A companhia pagou a remuneração mensal fixa dos seus diretores, aprovada em assembleia. (DRE:F0083)

## servicos-terceiros · Despesa com serviços de terceiros
- Classe: resultado · despesa · devedora · normal · - · despesas-administrativas
- Nomes: Despesa com serviço de terceiros; Despesa de salários de empregados terceirizados
- Depende: subgrupo
- Por quê: Serviço contratado de outra empresa (limpeza, vigilância, mão de obra terceirizada) é despesa operacional, na linha da área atendida; sem informação, administrativa. Na DVA, é insumo adquirido de terceiros, e não remuneração de pessoal (CPC 09).
- Liga: dre:despesas-administrativas
- Questões: DRE:F0749, F3216, F3490, F3495, F3612
### Histórias
- Serviço de terceiros | A companhia contratou uma empresa de limpeza e vigilância para a sua sede administrativa e lançou no resultado a fatura do mês.

## despesa-aluguel · Despesa de aluguel
- Classe: resultado · despesa · devedora · normal · - · despesas-administrativas
- Nomes: Despesa de aluguel; Despesas de aluguel; Despesa com aluguel; Despesas com aluguel; Despesa com aluguéis; Despesas com aluguéis; Despesas de aluguéis; Despesa de aluguel do período; Despesa com aluguel da loja
- Depende: subgrupo
- Por quê: Aluguel do período de uso do imóvel, por competência: o que foi pago e ainda não venceu é aluguel antecipado, no ativo. Sem outra informação, despesa administrativa; o aluguel ligado à área de vendas pode ir para despesas com vendas. Pelo CPC 06 (R2), o arrendatário reconhece direito de uso e passivo, e só mantém a despesa de aluguel nos contratos de curto prazo ou de baixo valor.
- Liga: dre:despesas-administrativas
- Questões: DRE:F0190, DRE:F0568, DRE:F0589, DRE:F0597, DRE:F0635, DRE:F0640, DRE:F0756, DRE:F0769, F3156, F3295, F3301, F3461
### Histórias
- Despesa de aluguel | A empresa pagou adiantado o aluguel do escritório; no fim do ano, só os meses já ocupados foram lançados no resultado, e o restante ficou como aluguel antecipado. (F3295)

## despesa-condominio · Despesa de condomínio
- Classe: resultado · despesa · devedora · normal · - · despesas-administrativas
- Nomes: Despesa de condomínio
- Por quê: Rateio mensal dos gastos do prédio ocupado pela empresa: despesa administrativa do período, por competência; a parte ainda não paga é condomínio a pagar, no passivo.
- Liga: dre:despesas-administrativas
- Questões: DRE:F0628, DRE:F0648
### Histórias
- Despesa de condomínio | O condomínio do andar ocupado pela administração venceu no mês e ainda não foi pago; o valor entra no resultado e, ao mesmo tempo, num passivo. (DRE:F0628)

## utilidades · Energia, água, telefone e internet
- Classe: resultado · despesa · devedora · normal · - · despesas-administrativas
- Nomes: Despesa de energia; Despesa de energia elétrica; Despesas de energia elétrica; Despesa com energia elétrica; Despesas com energia elétrica; Despesa com energia; Despesa de água; Despesa com água; Despesa de telefone; Despesa de Internet; Despesa de telefonia e Internet; Despesas de telecomunicações; Utilidades e serviços
- Depende: subgrupo
- Por quê: Consumo do período, por competência: o que venceu e não foi pago é passivo (energia a pagar). Sem indicação do setor, a banca as trata como despesas administrativas; o consumo da área de vendas pode ir para despesas com vendas, e o da fábrica, para o custo de produção.
- Liga: dre:despesas-administrativas
- Questões: DRE:F0083, DRE:F0394, DRE:F0556, DRE:F0568, DRE:F0628, DRE:F0644, DRE:F0648, DRE:F0756, DRE:F0769, F2005, F3156, F3461
### Histórias
- Despesa com energia elétrica | A conta de luz do escritório referente a dezembro só chegou em janeiro e será paga no mês seguinte; mesmo assim, entra no resultado de dezembro. (F3461)
- Utilidades e serviços | O gasto do mês com água, luz e telefone da sede da empresa foi reconhecido no resultado. (DRE:F0083)

## despesa-seguros · Despesa de seguros
- Classe: resultado · despesa · devedora · normal · - · despesas-administrativas
- Nomes: Despesa de seguros; Despesas de seguros; Despesa com seguros; Despesas com seguros; Despesas de seguros do período
- Por quê: Parte do prêmio que corresponde à cobertura já decorrida (competência); o prêmio pago adiantado fica no ativo como seguros antecipados e vai sendo apropriado. Sem outra informação, despesa administrativa; o seguro do transporte das compras é custo, e o das entregas, despesa com vendas.
- Liga: dre:despesas-administrativas
- Questões: DRE:F0524, DRE:F0571, DRE:F0589, DRE:F0590, DRE:F0597, DRE:F0616, DRE:F0628, DRE:F0634, DRE:F0644, DRE:F0687, DRE:F0763, F3461
### Histórias
- Despesa de seguros | Em julho, a empresa pagou à vista um ano de seguro do prédio da sede; em dezembro, lançou no resultado os seis meses de cobertura já transcorridos. (DRE:F0589)

## despesa-depreciacao · Despesa de depreciação
- Classe: resultado · despesa · devedora · normal · - · despesas-administrativas
- Nomes: Despesa de depreciação; Despesas de depreciação; Despesa com depreciação; Despesas com depreciação; Depreciação do período; Depreciações do Período; Despesa de depreciação e amortização
- Depende: subgrupo
- Por quê: Parcela do custo do imobilizado consumida no período (CPC 27): debita o resultado e credita a depreciação acumulada, retificadora do ativo. Bem de uso administrativo gera despesa administrativa; bem da área de vendas, despesa com vendas; máquina da fábrica, custo de produção, que só chega à DRE pelo CPV.
- Liga: dre:despesas-administrativas
- Questões: DRE:F0450, DRE:F0562, DRE:F0590, DRE:F0628, DRE:F0634, DRE:F0635, DRE:F0683, DRE:F0763, F3295, F3437, F3559, F3566
### Histórias
- Despesa de depreciação | Os computadores do escritório, que custaram R$ 300 mil, aparecem por R$ 240 mil no balanço seguinte, sem baixa nem venda; a diferença foi lançada no resultado do ano. (F3295)
- Depreciações do Período | No balancete, o desgaste do ano dos veículos e imóveis usados pela administração aparece ao lado da depreciação acumulada, mas só ele entra no resultado. (DRE:F0635)

## despesa-amortizacao · Despesa de amortização
- Classe: resultado · despesa · devedora · normal · - · despesas-administrativas
- Nomes: Despesa de amortização; Despesa com amortização de direito de uso de marca; Amortização do período
- Depende: subgrupo
- Por quê: Consumo, no período, do custo de um intangível de vida útil definida, como marcas, licenças e softwares (CPC 04, item 97); a contrapartida é a amortização acumulada. Intangível de vida útil indefinida não se amortiza: só passa pelo teste de impairment. Sem outra informação, despesa administrativa.
- Liga: dre:despesas-administrativas
- Questões: DRE:F0450, DRE:F0590, DRE:F0628, DRE:F0644, DRE:F0679, DRE:F0687, F1521, F3156
### Histórias
- Despesa de amortização | A empresa comprou por R$ 5 milhões um ativo intangível com vida útil definida de 20 anos e lança no resultado, a cada ano, a parcela do custo consumida. (F1521)
- Despesa com amortização de direito de uso de marca | A franqueada paga pelo direito de usar a marca da rede por prazo determinado e apropria, todo ano, a parte desse custo que corresponde ao período. (F3156)

## despesa-exaustao · Despesa de exaustão
- Classe: resultado · despesa · devedora · normal · - · despesas-administrativas
- Nomes: Despesa de exaustão; Despesas de exaustão
- Depende: subgrupo
- Por quê: Parcela do custo de um recurso natural (mina, jazida, floresta) consumida pela exploração do período; a contrapartida é a exaustão acumulada. Nos balancetes de prova sem outra informação, entra como despesa operacional, fora do lucro bruto; na empresa extrativa, compõe o custo da produção.
- Liga: dre:despesas-administrativas
- Questões: DRE:F0562, DRE:F0644, DRE:F0679, DRE:F0683
### Histórias
- Despesa de exaustão | Numa empresa comercial, a exaustão do período aparece no balancete ao lado da depreciação e da manutenção, sem ligação com a área de vendas, e fica fora do cálculo do lucro bruto. (DRE:F0562)

## despesa-material-consumo · Despesa de material de consumo
- Classe: resultado · despesa · devedora · normal · - · despesas-administrativas
- Nomes: Despesa de material de consumo; Despesas de material de consumo; Despesas com material de consumo; Materiais consumidos
- Depende: subgrupo
- Por quê: Só o material de expediente e de consumo efetivamente usado no período vai ao resultado; o que continua guardado é ativo circulante (material de consumo). Sem outra informação, despesa administrativa.
- Liga: dre:despesas-administrativas
- Questões: DRE:F0333, DRE:F0524, DRE:F0700, DRE:F0731, DRE:F0756, DRE:F0769
### Histórias
- Despesa de material de consumo | A empresa comprou papel e toner para o escritório; o que foi usado no mês foi para o resultado, e o restante continuou no almoxarifado como material de consumo. (DRE:F0731)

## despesa-manutencao · Despesa de manutenção e conservação
- Classe: resultado · despesa · devedora · normal · - · despesas-administrativas
- Nomes: Despesa de manutenção; Despesas de manutenção; Despesa de manutenção e conservação; Despesas de manutenção e conservação
- Depende: subgrupo
- Por quê: Reparos e conservação que só mantêm o bem funcionando, sem aumentar a sua vida útil ou capacidade, são despesa do período (CPC 27, item 12); sem outra informação, administrativa. O gasto que aumenta a vida útil ou a capacidade é somado ao imobilizado.
- Liga: dre:despesas-administrativas
- Questões: DRE:F0450, DRE:F0524, DRE:F0562, DRE:F0590, DRE:F0644, DRE:F0648, DRE:F0679, DRE:F0691, DRE:F0756
### Histórias
- Despesa de manutenção e conservação | A empresa pagou a pintura e pequenos reparos no prédio da sede, sem ampliar a área nem prolongar a vida útil do imóvel.

## despesa-combustiveis · Despesa de combustíveis
- Classe: resultado · despesa · devedora · normal · - · despesas-administrativas
- Nomes: Despesa de combustíveis; Despesas de combustíveis; Despesas com combustíveis; Despesa de combustíveis e lubrificantes
- Depende: subgrupo
- Por quê: Combustível consumido no período pelos veículos e máquinas da empresa; sem outra informação, despesa administrativa. O dos veículos de entrega pode ir para despesas com vendas, e o das máquinas da fábrica, para o custo de produção.
- Liga: dre:despesas-administrativas
- Questões: DRE:F0524, DRE:F0568, DRE:F0590, DRE:F0628, DRE:F0648, DRE:F0691
### Histórias
- Despesa de combustíveis | A empresa abasteceu o carro usado pela diretoria nas visitas às filiais e lançou no resultado o gasto do mês.

## despesa-assinaturas · Despesa de assinaturas
- Classe: resultado · despesa · devedora · normal · - · despesas-administrativas
- Nomes: Despesa de assinaturas; Despesa de assinatura de revistas
- Por quê: Parte da assinatura de jornais e revistas que corresponde ao período já decorrido; o valor pago adiantado fica no ativo (assinaturas antecipadas) até ser apropriado. É despesa administrativa.
- Liga: dre:despesas-administrativas
- Questões: DRE:F0571, DRE:F0600, DRE:F0628, DRE:F0648, DRE:F0700
### Histórias
- Despesa de assinaturas | A empresa pagou adiantado um ano de assinatura de revistas técnicas para o escritório; no balancete, a parte já decorrida está no resultado e o restante em assinaturas antecipadas. (DRE:F0628)

## despesas-tributarias · Despesas com impostos e taxas
- Classe: resultado · despesa · devedora · normal · - · despesas-administrativas
- Nomes: Despesas com impostos e taxas; Despesas de impostos e taxas; Despesa de impostos e taxas; Despesa de impostos e taxas diversas; Impostos prediais e territoriais urbanos
- Por quê: Tributos que não incidem sobre a venda nem sobre o lucro (IPTU, IPVA, taxas) são despesa operacional, em regra administrativa: não são dedução da receita bruta nem entram na linha de IR e CSLL.
- Liga: dre:despesas-administrativas
- Questões: DRE:F0524, DRE:F0571, DRE:F0600, DRE:F0628, DRE:F0648, DRE:F0836
### Histórias
- Impostos prediais e territoriais urbanos | A companhia pagou o IPTU do prédio da sua sede social; a banca considerou correto tratá-lo como despesa operacional, e não como dedução da receita bruta. (DRE:F0836)

## outras-despesas-gerais · Outras despesas gerais (cartórios, viagens, gráficas, transporte)
- Classe: resultado · despesa · devedora · normal · - · despesas-administrativas
- Nomes: Despesas com cartórios; Despesas legais e judiciais; Despesas com viagens; Despesas gráficas; Despesa de transporte
- Depende: subgrupo
- Por quê: Gastos de apoio à gestão, como cartórios, custas judiciais, viagens, serviços gráficos e transporte, são despesas operacionais; sem indicação de que servem à área de vendas (ou ao transporte das compras, que é custo), a banca os põe nas despesas gerais e administrativas.
- Liga: dre:despesas-administrativas
- Questões: DRE:F0083, DRE:F0333, DRE:F0648, DRE:F0691
### Histórias
- Despesas com cartórios | A empresa pagou o cartório para reconhecer firmas e registrar a ata da reunião da diretoria.
- Despesas legais e judiciais | O departamento jurídico da companhia pagou as custas de um processo em que ela discute uma cobrança de tributo.

## despesas-administrativas · Despesas gerais e administrativas
- Classe: resultado · despesa · devedora · normal · - · despesas-administrativas
- Nomes: Despesas gerais e administrativas; Despesas administrativas; Despesas gerais
- Por quê: Gastos de direção e gestão da empresa: pessoal do escritório, aluguel e utilidades da sede, honorários, material de expediente, tributos que não incidem sobre vendas nem sobre o lucro (art. 187, III). Somadas às despesas com vendas, formam as despesas operacionais.
- Liga: dre:despesas-administrativas
- Questões: DRE:F0248, DRE:F0296, DRE:F0297, DRE:F0394, DRE:F0440, DRE:F0562, DRE:F0640, DRE:F0704, DRE:F0750, DRE:F0801, F3295, F3437
### Histórias
- Despesas gerais e administrativas | A companhia reuniu numa só linha da DRE os gastos da diretoria, da contabilidade e do jurídico, que não estão ligados à venda dos produtos. (DRE:F0834)

## despesa-provisoes · Despesas com provisões
- Classe: resultado · despesa · devedora · normal · - · outras-operacionais
- Nomes: Despesas com provisões para contingências; Despesas com provisões; Despesas com Provisão para Riscos Ambientais
- Depende: subgrupo
- Aceita: subgrupo=despesas-administrativas
- Por quê: Constituir uma provisão (obrigação de prazo ou valor incertos, com saída de recursos provável e estimável, CPC 25) debita o resultado e credita o passivo. A Lei não fixa a linha: muitos autores a levam para outras despesas operacionais, e a FGV já a pôs entre as despesas administrativas (ALETO 2024), por isso as duas respostas valem.
- Liga: dre:outras-operacionais
- Questões: DRE:F0083, DRE:F0763, F3216, F3490
### Histórias
- Despesas com Provisão para Riscos Ambientais | A companhia estimou com confiabilidade uma saída provável de recursos para reparar um dano ambiental, com prazo superior a um ano, e reconheceu a obrigação no passivo não circulante contra o resultado. (F3216)
- Despesas com provisões para contingências | Os advogados avaliaram como provável a perda de uma ação movida por clientes por quebra de contrato e conseguiram estimar o valor; a empresa reconheceu a obrigação contra o resultado. (F2574)

## outras-despesas-operacionais · Outras despesas operacionais
- Classe: resultado · despesa · devedora · normal · - · outras-operacionais
- Nomes: Outras despesas operacionais
- Por quê: Despesas operacionais que não são de vendas, administrativas nem financeiras, como perdas por impairment, perdas de estoque ao valor realizável líquido e algumas provisões (CPC 26, itens 82 e 98). Ficam antes do resultado financeiro no CPC e antes do lucro operacional na Lei.
- Liga: dre:outras-operacionais
- Questões: DRE:F0750, DRE:F0751, DRE:F0752, DRE:F0753
### Histórias
- Outras despesas operacionais | Na DRE de uma operadora de telefonia, gastos que não são do serviço, das vendas, da administração nem financeiros aparecem numa linha própria dentro do resultado operacional. (DRE:F0750)

## perda-impairment · Perda por redução ao valor recuperável (impairment)
- Classe: resultado · despesa · devedora · normal · - · outras-operacionais
- Nomes: Despesa de perda de recuperabilidade de ativos
- Por quê: Quando o valor contábil de um ativo supera o valor recuperável (o maior entre o valor justo líquido de despesas de venda e o valor em uso), a diferença é perda no resultado (CPC 01, item 59), em outras despesas operacionais; a contrapartida reduz o ativo. A perda pode ser revertida depois, salvo a do goodwill.
- Liga: dre:outras-operacionais
- Questões: F1521, F3559
### Histórias
- Perda por desvalorização (impairment) | No teste de recuperabilidade, um intangível registrado por R$ 4,75 milhões, já líquido da amortização, mostrou valor recuperável de R$ 4,56 milhões, e a empresa lançou a diferença no resultado do ano. (F1521)
- Despesa de perda de recuperabilidade de ativos | A sociedade reconheceu no ano uma perda porque o valor recuperável de ativos seus ficou abaixo do valor contábil; na DVA, esse valor aparece junto com os insumos adquiridos de terceiros. (F3559)

## reversao-perdas-estoques · (–) Reversão de perdas estimadas nos estoques
- Classe: resultado · despesa · credora · retificadora · - · cmv
- Nomes: Reversão de perdas estimadas nos estoques
- Aceita: grupo=receita; retificadora=normal; subgrupo=outras-operacionais
- Por quê: Se o valor realizável líquido do estoque volta a subir, a perda reconhecida antes é revertida, até o limite dela; o CPC 16 (item 34) manda registrar a reversão como redução do valor do estoque reconhecido como despesa no período, por isso o jogo a trata como retificadora de custo, credora. Como muitos autores apresentam reversões de provisões e perdas como outras receitas operacionais, essa leitura também vale.
- Liga: dre:cmv
- Questões: DRE:F0394
### Histórias
- Reversão de perdas estimadas nos estoques | Um lote de mercadorias tinha sido ajustado ao valor realizável líquido no ano anterior; neste ano o preço de venda se recuperou, e a empresa desfez parte desse ajuste no resultado. (DRE:F0394)

## juros-passivos · Despesa de juros
- Classe: resultado · despesa · devedora · normal · - · resultado-financeiro
- Nomes: Despesa de juros; Despesas de juros
- Por quê: Custo do dinheiro de terceiros, apropriado pelo tempo decorrido (competência), pago ou não: despesa financeira (art. 187, III; CPC 26, item 82). Os juros que ainda não decorreram de um empréstimo ficam como encargos a transcorrer, redutores do passivo.
- Liga: dre:resultado-financeiro
- Questões: DRE:F0571, DRE:F0600, DRE:F0731, DRE:F0756, F3156, F3437
### Histórias
- Despesa de juros | A empresa tem um financiamento bancário e, no fim do ano, reconheceu os juros do período, que só serão pagos junto com o principal. (F3437)

## despesas-financeiras · Despesas financeiras
- Classe: resultado · despesa · devedora · normal · - · resultado-financeiro
- Nomes: Despesas financeiras; Despesa financeira; Despesas Financeiras de Juros; Despesas Financeiras (juros)
- Por quê: Juros passivos, descontos condicionais concedidos, tarifas bancárias, IOF e variações monetárias e cambiais passivas. Pela Lei, entram nas despesas operacionais, deduzidas das receitas financeiras (art. 187, III); pelo CPC 26, ficam depois do resultado antes do resultado financeiro.
- Liga: dre:resultado-financeiro
- Questões: DRE:F0296, DRE:F0440, DRE:F0450, DRE:F0584, DRE:F0628, DRE:F0634, DRE:F0640, DRE:F0704, DRE:F0753, DRE:F0801, F3301, F3437
### Histórias
- Despesas financeiras | Uma operadora pagou no ano os juros dos empréstimos que contratou; na DRE, eles aparecem ao lado das receitas financeiras, e não entre as despesas administrativas. (DRE:F0753)

## despesa-ir-csll · Despesa com IR e CSLL
- Classe: resultado · despesa · devedora · normal · - · ir-csll
- Nomes: Despesa com Imposto de Renda e Contribuição Social; Despesa com Imposto de Renda; Despesa com Imposto de Renda e CSLL; Despesa com IR e CSLL; Despesa de IR; Despesas de imposto de renda; Despesas com Imposto sobre Lucro; Imposto de renda; Contribuição social sobre o lucro; Imposto de renda e contribuição social; Imposto de renda e contribuição social sobre o lucro; Imposto sobre o lucro; Imposto sobre lucro; Impostos sobre lucro; Imposto e contribuição sobre lucro; IR e CSLL
- Por quê: Tributos sobre o lucro do período, correntes e diferidos (CPC 32), calculados sobre o LAIR ajustado; vêm depois do LAIR e antes das participações (Lei 6.404/76, arts. 187, V, e 189). O IR e a CSLL a pagar são passivo, e o IR retido na fonte dos salários não é despesa de IR da empresa: continua dentro da despesa de salários.
- Liga: dre:ir-csll
- Questões: DRE:F0190, F3145, DRE:F0248, DRE:F0524, DRE:F0562, DRE:F0590, DRE:F0628, DRE:F0801, F0499, F2321, F3216, F3437
### Histórias
- Provisão para IR | Na DRE da empresa, o imposto de renda do exercício foi calculado sobre o lucro antes do IR e lançado logo abaixo desse subtotal, antes das participações dos empregados e administradores. (DRE:F0440)
- Imposto sobre lucro | A empresa calculou o imposto sobre o lucro do mês à alíquota de 20% e o reconheceu no próprio período, embora só vá pagá-lo depois. (DRE:F0590)

## participacoes · Participações no lucro
- Classe: resultado · despesa · devedora · normal · - · participacoes
- Nomes: Participações dos empregados e administradores; Participação de empregados; Participações da Diretoria nos Lucros
- Por quê: Parcelas do lucro atribuídas a debêntures, empregados, administradores, partes beneficiárias e fundos de assistência, calculadas depois do IR e da CSLL, cada uma sobre o que resta da anterior (Lei 6.404/76, arts. 187, VI, 189 e 190). Pelo CPC 33, a participação dos empregados tende a ser despesa operacional; em questão pela Lei, siga a ordem do art. 190.
- Liga: dre:participacoes
- Questões: DRE:F0248, DRE:F0438, DRE:F0440, DRE:F0441, DRE:F0634, DRE:F0750, DRE:F0801
### Histórias
- Participações da Diretoria nos Lucros | Depois de apurar o IR e as contribuições, a companhia atribuiu aos diretores uma parte do lucro do exercício, antes de calcular a reserva legal e os dividendos. (DRE:F0634)
- Participação de empregados | A companhia destinou aos empregados uma fatia do lucro, calculada sobre o resultado já líquido do IR e da CSLL. (DRE:F0801)

## custo-imobilizado-vendido · Custo do ativo imobilizado vendido
- Classe: resultado · despesa · devedora · normal · - · outras-receitas-despesas
- Nomes: Custo do ativo imobilizado vendido
- Aceita: subgrupo=outras-operacionais
- Por quê: Baixa do valor contábil (custo menos depreciação) do bem vendido, confrontado com a receita da venda; o que afeta o resultado é o ganho ou a perda líquida, em outras receitas e despesas (art. 187, IV). Pelo CPC 26, FGV e FCC põem esse resultado dentro das outras receitas e despesas operacionais, e essa resposta também vale.
- Liga: dre:outras-receitas-despesas
- Questões: DRE:F0190, F3145, F3612
### Histórias
- Custo do ativo imobilizado vendido | A empresa vendeu por R$ 70 mil uma máquina que estava registrada por R$ 85 mil, já líquidos de depreciação; o valor baixado é confrontado com a receita da venda e gera perda de R$ 15 mil. (DRE:F0190, F3145)
