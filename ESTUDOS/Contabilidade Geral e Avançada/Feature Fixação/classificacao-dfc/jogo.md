# Fluxo de caixa (DFC)

<!-- jogo: dfc -->
<!-- Jogo da Fixação. Formato e validações no comentário de carregar_jogo_classificacao (sistema/gerar.py). Classe: atividade (operacional, investimento, financiamento, nenhuma) · caixa (aumenta, diminui, neutro) · ajuste no lucro líquido pelo método indireto (soma, subtrai, nao-ajusta; "-" = não conta nesta carta). Fontes: caderno TecConcursos "DFC - 702" (F0001 a F0702), aulas de DFC (Gilmar Possati e Igor Cintra), CPC 03 (R2) com a Revisão 24 e Resolução CVM 237 (CPC 51). Nomes, histórias e explicações reescritos. -->

<!-- ===== Operacional: recebimentos ===== -->

## dfc-venda-vista · Venda à vista de mercadorias ou serviços
- Classe: operacional · aumenta · -
- Nomes: Venda de mercadorias à vista; Venda de produtos com recebimento em dinheiro; Prestação de serviços à vista
- Por quê: Recebimento pela venda de mercadorias e serviços é o exemplo típico de fluxo operacional (CPC 03, item 14, a).
- Questões: F0172, F0365, F0394, F0398, F0702
### Histórias
- Venda do estoque | Uma loja vende todo o estoque e recebe metade no ato; a parte que entrou no caixa é a que se classifica. (F0054)

## dfc-receb-clientes · Recebimento de clientes
- Classe: operacional · aumenta · -
- Nomes: Recebimento de clientes; Recebimento de duplicatas; Recebimento de vendas feitas a prazo; Recebimento por serviços prestados no ano anterior
- Por quê: Quando o cliente paga, o dinheiro entra pelas operações (CPC 03, item 14, a), mesmo que a receita tenha sido reconhecida antes.
- Questões: F0001, F0139, F0340, F0447
### Histórias
- Honorários de perícia | Um escritório prestou o serviço em um ano e só recebeu o valor no ano seguinte; pense na demonstração do ano do recebimento. (F0001)

## dfc-adiant-clientes · Recebimento adiantado de clientes
- Classe: operacional · aumenta · -
- Nomes: Adiantamento recebido de clientes; Receita recebida antecipadamente
- Por quê: Dinheiro do cliente por mercadoria ainda não entregue é fluxo operacional; no balanço fica no passivo até a entrega.
- Questões: F0200, F0398

## dfc-royalties · Royalties, honorários, comissões e outras receitas
- Classe: operacional · aumenta · -
- Nomes: Recebimento de royalties; Recebimento de honorários; Recebimento de comissões
- Por quê: O CPC 03 (item 14, b) lista royalties, honorários, comissões e outras receitas entre os fluxos operacionais. A banca costuma oferecê-los como se fossem de investimento.
- Questões: F0038, F0095, F0125, F0324, F0445
### Histórias
- Royalties | O caixa de uma empresa cresceu com o que terceiros pagaram pelo uso de uma marca dela. (F0095, F0238)

## dfc-aluguel-recebido · Recebimento de aluguéis
- Classe: operacional · aumenta · -
- Nomes: Recebimento de aluguéis
- Por quê: Aluguel é receita e não é venda de ativo nem captação de recurso: fica nas operações, que também recebem tudo o que não é investimento nem financiamento (CPC 03, itens 6 e 14).
- Questões: F0090, F0126

## dfc-venda-ativo-aluguel · Venda de bem que a entidade alugava a terceiros
- Classe: operacional · aumenta · -
- Nomes: Venda de bem mantido para aluguel a terceiros e depois vendido
- Por quê: Exceção do CPC 03, item 14: quando o bem é produzido ou comprado para ser alugado e em seguida vendido (CPC 27, item 68A), o pagamento da compra, os aluguéis e a venda são fluxos operacionais.
- Questões: F0090, F0126, F0170, F0328
### Histórias
- Venda de carros | Uma loja de usados aluga por diária os carros enquanto não os vende; um deles é vendido à vista. (F0126)
- Venda de salas comerciais | Uma imobiliária alugava as salas enquanto não encontrava comprador; em dezembro vendeu e recebeu metade. (F0170)

## dfc-negociacao-venda · Venda de títulos mantidos para negociação
- Classe: operacional · aumenta · -
- Nomes: Venda de títulos mantidos para negociação imediata; Recebimento por contratos disponíveis para venda futura
- Por quê: Títulos para negociação se parecem com estoque comprado para revender: compra e venda são operacionais (CPC 03, itens 14, g, e 15).
- Questões: F0098, F0125, F0445

## dfc-restituicao-ir · Restituição de imposto sobre o lucro
- Classe: operacional · aumenta · -
- Nomes: Restituição de imposto de renda e CSLL
- Por quê: Pagamentos e restituições de tributos sobre o lucro são operacionais, salvo se identificados especificamente com investimento ou financiamento (CPC 03, itens 14, f, e 35).
- Questões: F0471, F0540

## dfc-if-receb-principal · Instituição financeira: recebimento de empréstimo a cliente
- Classe: operacional · aumenta · -
- Nomes: Banco recebe o principal de um empréstimo feito a cliente
- Por quê: Para instituição financeira, emprestar é a atividade principal, por isso concessão e recebimento são operacionais (CPC 03, item 15). Em empresa comum seria investimento.
- Questões: F0274

## dfc-seguradora · Seguradora: prêmios e sinistros
- Classe: operacional · aumenta · -
- Nomes: Seguradora recebe prêmios de apólices
- Por quê: Para a seguradora, prêmios fazem parte da atividade geradora de receita. As bancas citam a antiga alínea do item 14 do CPC 03, retirada na Revisão 21; a classificação continua operacional.
- Questões: F0274, F0506

<!-- ===== Operacional: pagamentos ===== -->

## dfc-pag-fornecedores · Pagamento a fornecedores
- Classe: operacional · diminui · -
- Nomes: Pagamento a fornecedores de mercadorias; Pagamento a fornecedores de matéria-prima; Pagamento a fornecedores de serviços; Quitação de dívida com fornecedores
- Por quê: Pagamentos a fornecedores de mercadorias e serviços são operacionais (CPC 03, item 14, c).
- Questões: F0108, F0152, F0429, F0470
### Histórias
- Pagamento a fornecedor | No prazo comum do setor, de 30 dias, a indústria paga a matéria-prima que havia comprado. (F0133, F0429)

## dfc-compra-estoque-vista · Compra de estoques à vista
- Classe: operacional · diminui · -
- Nomes: Compra de mercadorias para revenda à vista; Compra de matéria-prima à vista; Compra à vista de material de consumo
- Por quê: Estoque faz parte do giro da operação: pagar por ele é fluxo operacional, nunca investimento.
- Questões: F0003, F0129, F0319, F0565
### Histórias
- Farelo de soja | Uma fabricante de ração tira dinheiro do caixa para comprar o insumo que vai para a produção. (F0003)
- Insumos de gráfica | A gráfica compra à vista papel, tinta e peças de reposição que usará nos próximos 18 meses. (F0129)

## dfc-pag-salarios · Pagamento a empregados
- Classe: operacional · diminui · -
- Nomes: Pagamento de salários; Pagamento a empregados ou por conta deles; Quitação de salários do mês anterior
- Por quê: CPC 03, item 14, d.
- Questões: F0108, F0139, F0445, F0513

## dfc-pag-aluguel · Pagamento de aluguel
- Classe: operacional · diminui · -
- Nomes: Pagamento de aluguel; Pagamento antecipado de aluguel
- Por quê: Aluguel é despesa da operação. Pagar adiantado não o transforma em investimento, ainda que fique no ativo por um tempo.
- Questões: F0037, F0069, F0115, F0131, F0202
### Histórias
- Aluguel adiantado | A sociedade paga de uma vez um ano de aluguel das vagas de garagem usadas pela diretoria. (F0069)

## dfc-pag-seguros · Pagamento de seguros
- Classe: operacional · diminui · -
- Nomes: Pagamento de prêmio de seguro; Contratação de seguro paga à vista
- Por quê: Pagamento por serviço usado na operação (CPC 03, item 14, c), mesmo quando reconhecido antes como despesa antecipada.
- Questões: F0242, F0604, F0632

## dfc-pag-despesas · Pagamento de despesas operacionais
- Classe: operacional · diminui · -
- Nomes: Pagamento de energia elétrica; Pagamento de manutenção; Pagamento de publicidade; Pagamento de serviços de terceiros; Pagamento de comissões sobre vendas; Pagamento de frete sobre vendas
- Por quê: Desembolsos que servem à geração de receita e não criam ativo de longo prazo são operacionais (CPC 03, itens 14 e 16).
- Questões: F0225, F0241, F0605, F0632

## dfc-pag-tributos · Pagamento de tributos da operação
- Classe: operacional · diminui · -
- Nomes: Pagamento de impostos sobre vendas; Pagamento de ISS sobre serviços prestados; Pagamento de IPTU ou IPVA
- Por quê: Tributo da operação reduz o caixa operacional quando é pago, inclusive o que incide sobre a propriedade de imóveis e veículos usados pela empresa.
- Questões: F0365, F0641

## dfc-pag-ir · Pagamento de IR e CSLL
- Classe: operacional · diminui · -
- Nomes: Pagamento de imposto de renda; Pagamento de IR e CSLL sobre o lucro
- Por quê: Regra geral operacional (CPC 03, item 35). Vai para investimento ou financiamento quando o imposto pago pode ser ligado especificamente a uma transação dessas.
- Questões: F0203, F0471, F0540
### Histórias
- Imposto sem origem identificável | Não há como ligar o imposto de renda pago a nenhuma transação específica do ano. (F0203)

## dfc-pesquisa · Gastos de pesquisa e pré-operacionais
- Classe: operacional · diminui · -
- Nomes: Pagamento de gastos da fase de pesquisa; Pagamento de gastos pré-operacionais
- Por quê: Só desembolso que resulta em ativo reconhecido pode ser de investimento (CPC 03, item 16). Pesquisa e gastos pré-operacionais vão ao resultado.
- Questões: F0022, F0117
### Histórias
- Escolha de alternativas | No projeto de um software interno, a empresa paga pela avaliação e seleção das alternativas possíveis, etapa que vai para o resultado. (F0022)

## dfc-compra-ativo-aluguel · Compra de bem para alugar e depois vender
- Classe: operacional · diminui · -
- Nomes: Compra de bem destinado a aluguel e posterior venda
- Por quê: CPC 03, item 14: produzir ou comprar ativos para alugar e depois vender é fluxo operacional, exceção à regra do imobilizado.
- Questões: F0126

## dfc-negociacao-compra · Compra de títulos para negociação
- Classe: operacional · diminui · -
- Nomes: Compra de títulos mantidos para negociação imediata; Pagamento por contratos mantidos para negociação
- Por quê: CPC 03, itens 14, g, e 15: funcionam como estoque para revenda. Título mantido até o vencimento ou como aplicação seria investimento.
- Questões: F0135, F0445, F0479

## dfc-imoveis-revenda · Imobiliária: compra de imóvel para revender
- Classe: operacional · diminui · -
- Nomes: Imobiliária compra imóvel para revenda
- Por quê: Para quem tem a venda de imóveis como atividade, o imóvel é estoque.
- Questões: F0068, F0073, F0215
### Histórias
- Imóvel para revenda | Uma entidade que vive de vender imóveis compra um deles à vista com a intenção de passá-lo adiante. (F0068)

## dfc-if-emprestimo · Instituição financeira: empréstimo a cliente
- Classe: operacional · diminui · -
- Nomes: Banco concede empréstimo a cliente
- Por quê: CPC 03, item 15: antecipações e empréstimos de instituição financeira são operacionais.
- Questões: F0260, F0514

<!-- ===== Juros, dividendos e JCP ===== -->

## dfc-juros-pagos · Juros pagos
- Classe: operacional · diminui · -
- Nomes: Pagamento de juros de empréstimo bancário; Juros pagos sobre financiamento; Pagamento de juros por atraso
- Aceita: atividade=financiamento
- Por quê: O CPC 03 permite operacional ou financiamento e encoraja operacional (itens 33 e 34A); nunca investimento. ⚠️ A partir de 2027, com o CPC 51, empresas não financeiras passam a ter só financiamento.
- Questões: F0020, F0045, F0077, F0184, F0271, F0472
### Histórias
- Juros do empréstimo | A parcela paga ao banco traz principal e juros; classifique só a fatia dos juros, sem política divulgada em nota. (F0147, F0271)
- Juros por atraso | Ao quitar com atraso uma parcela, a empresa paga um acréscimo pela demora. (F0077)

## dfc-juros-pagos-alt · Juros pagos com a política alternativa
- Classe: financiamento · diminui · -
- Nomes: Juros pagos por empresa que os trata como custo de obtenção de recursos
- Por quê: Quem não segue o encorajamento do CPC 03 e justifica os juros como custo de captação os leva ao financiamento, com nota (itens 33 e 34A). ⚠️ Com o CPC 51 (2027), essa passa a ser a única opção das empresas não financeiras.
- Questões: F0133, F0186, F0366
### Histórias
- Juros pagos | A entidade avisa em nota que não segue a recomendação do pronunciamento e então paga os juros do empréstimo. (F0186)

## dfc-juros-recebidos · Juros recebidos
- Classe: operacional · aumenta · -
- Nomes: Recebimento de juros de aplicações financeiras; Juros recebidos de empréstimo concedido; Rendimento de equivalentes de caixa recebido
- Aceita: atividade=investimento
- Por quê: Operacional (encorajado) ou investimento, por serem retorno do investimento (CPC 03, itens 33 e 34A); nunca financiamento. ⚠️ Com o CPC 51 (2027), empresas não financeiras passam a ter só investimento.
- Questões: F0066, F0179, F0395, F0473, F0487
### Histórias
- Juros da aplicação | Uma varejista que segue as recomendações do pronunciamento recebe em dinheiro os juros de uma aplicação. (F0179, F0066)

## dfc-dividendos-recebidos · Dividendos recebidos
- Classe: operacional · aumenta · -
- Nomes: Recebimento de dividendos; Dividendos recebidos de coligada; Dividendos recebidos de controlada
- Aceita: atividade=investimento
- Por quê: Operacional (encorajado) ou investimento (CPC 03, itens 33 e 34A). Em investimento avaliado por equivalência patrimonial, o fluxo que aparece é o dividendo, não o resultado da investida (itens 37 e 38). ⚠️ CPC 51 (2027): só investimento nas empresas não financeiras.
- Questões: F0223, F0365, F0440, F0541

## dfc-jcp-recebidos · Juros sobre capital próprio recebidos
- Classe: operacional · aumenta · -
- Nomes: Recebimento de juros sobre o capital próprio
- Aceita: atividade=investimento
- Por quê: Mesmo tratamento dos dividendos recebidos: operacional é o encorajado e, sem nota explicativa, é o esperado (CPC 03, item 34A). ⚠️ CPC 51 (2027): investimento.
- Questões: F0313, F0364, F0398
### Histórias
- JCP da investida | A companhia recebe da empresa de que participa uma transferência a título de juros sobre o capital próprio e não publica nota sobre a política. (F0313)

## dfc-dividendos-pagos · Dividendos pagos
- Classe: financiamento · diminui · nao-ajusta
- Nomes: Pagamento de dividendos; Distribuição de dividendos em dinheiro; Pagamento de dividendos declarados no ano anterior
- Aceita: atividade=operacional
- Por quê: Financiamento é o encorajado, porque remunera quem forneceu capital; operacional é permitido com nota (CPC 03, itens 34 e 34A). Não passa pelo resultado. ⚠️ CPC 51 (2027): só financiamento.
- Questões: F0023, F0166, F0185, F0266, F0370, F0600

## dfc-jcp-pagos · Juros sobre capital próprio pagos
- Classe: financiamento · diminui · -
- Nomes: Pagamento de juros sobre o capital próprio
- Aceita: atividade=operacional
- Por quê: Preferencialmente financiamento (CPC 03, item 34A). ⚠️ CPC 51 (2027): só financiamento.
- Questões: F0355, F0370, F0525, F0589

## dfc-dividendos-pagos-alt · Dividendos pagos com a política alternativa
- Classe: operacional · diminui · -
- Nomes: Dividendos pagos por empresa que escolheu a alternativa ao encorajamento
- Por quê: Quem decide não seguir o encorajamento classifica os dividendos pagos nas operações, para mostrar a capacidade de pagá-los com o caixa operacional, e evidencia isso em nota (CPC 03, itens 34 e 34A).
- Questões: F0060, F0185, F0587
### Histórias
- Dividendos pagos | A sociedade informa em nota que não segue a recomendação do pronunciamento e paga no primeiro trimestre os dividendos do ano anterior. (F0060)

<!-- ===== Investimento: pagamentos ===== -->

## dfc-compra-imobilizado · Compra de imobilizado à vista
- Classe: investimento · diminui · nao-ajusta
- Nomes: Compra de ativo imobilizado à vista; Aquisição de máquinas e equipamentos à vista; Compra de móveis e utensílios; Compra de computadores para uso próprio; Compra de terreno para a nova sede
- Por quê: Pagamento por ativo de longo prazo (CPC 03, item 16, a). Comprar não afeta o resultado, então não há ajuste.
- Questões: F0016, F0108, F0220, F0365, F0494
### Histórias
- Moto de entregas | Uma loja que vende por aplicativo e entrega de graça compra uma moto à vista. (F0057, F0069)
- Reforma do escritório | Ao renovar a sala, o escritório compra à vista mesas e cadeiras que usará por vários anos. (F0034)

## dfc-gastos-capitalizados · Frete, instalação e outros gastos que entram no custo do imobilizado
- Classe: investimento · diminui · nao-ajusta
- Nomes: Pagamento do frete de um bem do imobilizado; Pagamento da instalação de equipamento do escritório
- Por quê: Gastos necessários para pôr o bem em uso compõem o custo do ativo (CPC 27); o pagamento segue o ativo, em investimento (CPC 03, item 16).
- Questões: F0034, F0109, F0188
### Histórias
- Frete e seguro dos móveis | Além do preço dos móveis, paga-se o transporte e o seguro até a sede. (F0188)

## dfc-compra-intangivel · Aquisição de intangível
- Classe: investimento · diminui · nao-ajusta
- Nomes: Compra de software para o processo produtivo; Aquisição de ativo intangível à vista; Pagamento de custos de desenvolvimento ativados
- Por quê: CPC 03, item 16, a: inclui os custos de desenvolvimento ativados e o imobilizado de construção própria.
- Questões: F0199, F0513, F0588

## dfc-prop-investimento-compra · Compra de propriedade para investimento
- Classe: investimento · diminui · nao-ajusta
- Nomes: Compra de propriedade para investimento à vista; Compra à vista de terreno destinado à valorização; Aquisição de imóvel para locação a terceiros
- Por quê: Ativo de longo prazo mantido para renda ou valorização (CPC 03, item 16, a). Não confunda com o bem que será alugado e depois vendido pela operação.
- Questões: F0069, F0082, F0215, F0279

## dfc-compra-participacao · Compra de participação em outra empresa
- Classe: investimento · diminui · nao-ajusta
- Nomes: Compra de ações de outras empresas; Aquisição de participação em coligada; Pagamento por participação em joint venture; Compra de instrumentos de dívida de outra entidade
- Por quê: CPC 03, item 16, c (salvo o que for equivalente de caixa ou mantido para negociação).
- Questões: F0069, F0199, F0250, F0266, F0513

## dfc-obtencao-controle · Obtenção de controle de outra empresa
- Classe: investimento · diminui · nao-ajusta
- Nomes: Pagamento para obter o controle de uma controlada
- Por quê: Obter ou perder o controle é investimento, apresentado em separado e líquido do caixa adquirido (CPC 03, itens 39 e 42). O CEBRASPE e a FCC contrastam com a mudança de participação sem troca de controle, que é financiamento.
- Questões: F0130, F0140

## dfc-emprestimo-concedido · Empréstimo concedido a terceiros
- Classe: investimento · diminui · nao-ajusta
- Nomes: Concessão de empréstimo a outra empresa; Empréstimo concedido a um sócio; Adiantamento em dinheiro a terceiros
- Por quê: Emprestar, para quem não é instituição financeira, é investimento (CPC 03, item 16, e). A pegadinha é chamar de financiamento.
- Questões: F0097, F0514, F0564, F0608
### Histórias
- Ajuda ao sócio | Uma empresa de auditoria entrega dinheiro a um dos sócios, que devolverá no ano seguinte. (F0093)

## dfc-aplicacao-nao-equivalente · Aplicação que não é equivalente de caixa
- Classe: investimento · diminui · nao-ajusta
- Nomes: Aplicação financeira de longo prazo; Aplicação em fundo resgatável só daqui a quatro anos
- Por quê: Só é equivalente de caixa a aplicação de curto prazo (em regra até 3 meses da compra), líquida e de risco insignificante (CPC 03, item 7). Fora disso, aplicar é investimento.
- Questões: F0066, F0405, F0489, F0564

## dfc-derivativo · Contratos futuros, a termo, opções e swap
- Classe: investimento · diminui · nao-ajusta
- Nomes: Pagamento por contrato de swap não mantido para negociação
- Aceita: atividade=financiamento
- Por quê: Em regra investimento; podem ser classificados como financiamento e, se forem para negociação, são operacionais (CPC 03, item 16, g). Como proteção (hedge), seguem a posição protegida.
- Questões: F0197

## dfc-hedge-operacional · Derivativo de proteção de item operacional
- Classe: operacional · diminui · -
- Nomes: Pagamento de derivativo usado como hedge de uma posição operacional
- Por quê: O fluxo do contrato de proteção é classificado como o da posição protegida (CPC 03, item 16, parte final).
- Questões: F0197

<!-- ===== Investimento: recebimentos ===== -->

## dfc-venda-imobilizado · Venda de imobilizado ou intangível à vista
- Classe: investimento · aumenta · -
- Nomes: Venda de ativo imobilizado à vista; Venda de móveis e utensílios usados; Venda de um veículo de uso próprio; Venda de ativo intangível; Venda de uma patente
- Por quê: O valor recebido pela venda de ativo de longo prazo é investimento (CPC 03, item 16, b). O ajuste no indireto depende de ter havido ganho ou perda.
- Questões: F0091, F0304, F0451, F0460, F0555
### Histórias
- Veículo pouco usado | Menos de um ano depois de comprar um carro para o negócio, a companhia o vende à vista. (F0026)

## dfc-venda-imob-lucro · Venda à vista de imobilizado com lucro
- Classe: investimento · aumenta · subtrai
- Nomes: Venda à vista de imobilizado com ganho
- Por quê: Todo o dinheiro recebido vai para investimento; como o ganho já está no lucro, ele é retirado das operações no método indireto, para não contar duas vezes.
- Questões: F0062, F0363, F0560
### Histórias
- Venda de terreno | A empresa vende à vista um terreno por valor acima do que ele custou no balanço. (F0062, F0358)
- Caminhão de entregas | Depois de quatro anos de uso, o caminhão é vendido à vista por mais do que o valor contábil. (F0189, F0190)

## dfc-venda-imob-perda · Venda à vista de imobilizado com prejuízo
- Classe: investimento · aumenta · soma
- Nomes: Venda à vista de imobilizado com perda
- Por quê: Entra caixa em investimento; a perda não consumiu caixa nas operações, por isso volta somada ao lucro.
- Questões: F0012, F0329, F0377
### Histórias
- Equipamento usado | Um equipamento é vendido à vista abaixo do valor contábil. (F0012)

## dfc-venda-imob-contabil · Venda de imobilizado sem ganho nem perda
- Classe: investimento · aumenta · nao-ajusta
- Nomes: Venda à vista de imobilizado pelo valor contábil
- Por quê: Sem ganho nem perda, o resultado não muda: há só a entrada de caixa em investimento.
- Questões: F0189, F0354

## dfc-venda-prop-investimento · Venda de propriedade para investimento
- Classe: investimento · aumenta · -
- Nomes: Venda de propriedade para investimento à vista; Venda de terreno destinado à valorização
- Por quê: Venda de ativo de longo prazo (CPC 03, item 16, b), salvo na empresa que tem a venda de imóveis como atividade.
- Questões: F0167, F0168, F0206

## dfc-venda-participacao · Venda de participação em outra empresa
- Classe: investimento · aumenta · -
- Nomes: Venda de participação societária; Venda de instrumentos patrimoniais de outra entidade; Venda de instrumentos de dívida de outra entidade
- Por quê: CPC 03, item 16, d.
- Questões: F0119, F0193, F0209, F0369

## dfc-perda-controle · Perda de controle de uma controlada
- Classe: investimento · aumenta · nao-ajusta
- Nomes: Recebimento pela venda do controle de uma controlada
- Por quê: CPC 03, itens 39 a 42: investimento, em linha própria; o efeito da perda não é abatido do efeito de uma obtenção.
- Questões: F0140

## dfc-receb-emprestimo-concedido · Devolução de empréstimo concedido
- Classe: investimento · aumenta · nao-ajusta
- Nomes: Recebimento do principal de empréstimo concedido a terceiros; Recebimento de parcela de empréstimo feito a coligada
- Por quê: Quem emprestou e recebe de volta está desfazendo um investimento (CPC 03, item 16, f).
- Questões: F0038, F0093, F0193, F0238
### Histórias
- Sócio devolve | No ano seguinte, o sócio devolve à empresa de auditoria o dinheiro que ela lhe havia emprestado. (F0093)

## dfc-resgate-aplicacao · Resgate de aplicação que não é equivalente de caixa
- Classe: investimento · aumenta · nao-ajusta
- Nomes: Resgate de aplicação financeira de longo prazo; Resgate de títulos não classificados como equivalentes de caixa
- Por quê: Se a aplicação estava fora do caixa e equivalentes, o resgate traz dinheiro de um investimento.
- Questões: F0489, F0525, F0564

<!-- ===== Financiamento: entradas ===== -->

## dfc-emissao-acoes · Integralização de capital em dinheiro
- Classe: financiamento · aumenta · nao-ajusta
- Nomes: Integralização de capital em dinheiro; Emissão de ações com recebimento em dinheiro; Aumento de capital com emissão de novas ações no mercado; Emissão de instrumentos patrimoniais
- Por quê: Muda o tamanho do capital próprio (CPC 03, itens 6 e 17, a). Não passa pelo resultado.
- Questões: F0056, F0100, F0156, F0394, F0486, F0600
### Histórias
- Sócios aportam | Para constituir a sociedade, os sócios depositam o capital em contas bancárias dela. (F0065, F0131)

## dfc-venda-tesouraria · Venda de ações em tesouraria
- Classe: financiamento · aumenta · -
- Nomes: Venda de ações em tesouraria; Recebimento pela venda de ações de própria emissão
- Por quê: Transação com os próprios instrumentos de capital: financiamento (CPC 03, item 17, a). Eventual resultado vai ao patrimônio líquido.
- Questões: F0250, F0331

## dfc-afac · Adiantamento para futuro aumento de capital recebido
- Classe: financiamento · aumenta · nao-ajusta
- Nomes: Adiantamento dos sócios para aumento de capital, sem devolução
- Por quê: Recurso dos sócios que vai compor o capital: financiamento.
- Questões: F0191

## dfc-captacao-emprestimo · Captação de empréstimos e financiamentos
- Classe: financiamento · aumenta · nao-ajusta
- Nomes: Obtenção de empréstimo bancário; Recebimento de financiamento de longo prazo; Empréstimo obtido de coligada
- Por quê: Capital de terceiros (CPC 03, item 17, c). Mesmo que o dinheiro vá comprar estoque, a captação é financiamento.
- Questões: F0100, F0162, F0356, F0634
### Histórias
- Crédito com recebíveis em garantia | Depois de vender a prazo, a sociedade toma um empréstimo no banco oferecendo essa venda como garantia. (F0336)
- Empréstimo para estoque | A papelaria contrai um empréstimo bancário para comprar mercadorias. (F0356)

## dfc-emissao-debentures · Emissão de debêntures e outros títulos de dívida
- Classe: financiamento · aumenta · nao-ajusta
- Nomes: Emissão de debêntures; Recebimento pela emissão de notas promissórias; Captação por hipoteca
- Por quê: Título de dívida emitido pela própria entidade é financiamento (CPC 03, item 17, c). Não confunda com comprar debênture de outra empresa, que é investimento.
- Questões: F0056, F0156, F0365, F0430, F0490

## dfc-venda-controlada-sem-perda · Venda de parte de controlada sem perder o controle
- Classe: financiamento · aumenta · nao-ajusta
- Nomes: Venda de ações da controlada sem perda do controle
- Por quê: Sem troca de controle, é transação entre sócios, tratada como capital: financiamento (CPC 03, itens 42A e 42B).
- Questões: F0383, F0440, F0458

<!-- ===== Financiamento: saídas ===== -->

## dfc-amortizacao · Pagamento do principal de empréstimos
- Classe: financiamento · diminui · nao-ajusta
- Nomes: Amortização de empréstimo bancário; Pagamento do principal de financiamento; Quitação de passivo bancário de longo prazo
- Por quê: Devolver capital de terceiros é financiamento (CPC 03, itens 12 e 17, d), qualquer que tenha sido o uso do dinheiro.
- Questões: F0036, F0173, F0271, F0328, F0480
### Histórias
- Dívida que comprou estoque | A empresa paga o principal do empréstimo que havia tomado para comprar mercadorias. (F0069, F0328)

## dfc-resgate-debentures · Resgate de debêntures
- Classe: financiamento · diminui · nao-ajusta
- Nomes: Resgate de debêntures emitidas
- Por quê: Pagamento do principal de dívida própria: financiamento, mesmo que o recurso tenha comprado máquinas, imóvel ou estoque.
- Questões: F0284, F0400, F0583
### Histórias
- Debênture das máquinas | Anos atrás a entidade emitiu uma debênture para comprar máquinas; agora devolve o principal. (F0284)

## dfc-arrendamento · Pagamento do passivo de arrendamento
- Classe: financiamento · diminui · nao-ajusta
- Nomes: Pagamento do principal de arrendamento pelo arrendatário; Prestações de arrendamento financeiro de uma máquina
- Por quê: Reduz uma dívida: financiamento (CPC 03, item 17, e).
- Questões: F0125, F0429, F0445, F0556

## dfc-recompra-acoes · Recompra, resgate ou reembolso de ações
- Classe: financiamento · diminui · nao-ajusta
- Nomes: Aquisição de ações próprias para tesouraria; Pagamento a investidores para resgatar ações da entidade; Devolução em dinheiro das quotas a um sócio que se retira
- Por quê: Devolução de capital próprio (CPC 03, item 17, b). A banca tenta passar a recompra como investimento.
- Questões: F0221, F0241, F0429, F0433, F0486

## dfc-custo-emissao · Custos pagos na emissão de ações
- Classe: financiamento · diminui · -
- Nomes: Pagamento de custos da emissão de ações
- Por quê: O gasto de captação reduz o que entrou pelo financiamento; não vai para o resultado (CPC 08).
- Questões: F0563

## dfc-parcela-compra-prazo · Parcelas posteriores de bem comprado a prazo
- Classe: financiamento · diminui · nao-ajusta
- Nomes: Pagamento posterior de imobilizado comprado a prazo
- Por quê: Só a entrada (ou pagamento junto da compra) é investimento. Quitar depois a dívida com o vendedor é amortizar um financiamento: é a posição das provas (FGV e FCC).
- Questões: F0232, F0290, F0421, F0425
### Histórias
- Segunda metade dos computadores | Os computadores foram comprados em um ano, com metade paga no ato; no ano seguinte paga-se o restante. (F0232, F0290)
- Parcelas do imóvel | Um imóvel comprado em novembro, com metade no ato, tem as parcelas restantes pagas no ano seguinte. (F0425)

## dfc-aumento-controlada · Compra de mais ações de quem já é controlada
- Classe: financiamento · diminui · nao-ajusta
- Nomes: Compra de mais ações de uma controlada, sem mudança de controle
- Por quê: Com o controle já obtido, é transação de capital entre sócios: financiamento (CPC 03, itens 42A e 42B).
- Questões: F0207, F0440, F0458

<!-- ===== Primeira parcela de compra a prazo ===== -->

## dfc-entrada-compra-prazo · Entrada paga na compra de imobilizado
- Classe: investimento · diminui · nao-ajusta
- Nomes: Entrada paga no ato da compra de máquinas
- Por quê: O pagamento feito na própria aquisição do ativo é investimento (CPC 03, item 16, a).
- Questões: F0039, F0162, F0425, F0633
### Histórias
- Metade à vista | A indústria compra máquinas e paga metade no ato; classifique essa metade. (F0039)

<!-- ===== Transações que não envolvem caixa ===== -->

## dfc-compra-ativo-prazo · Aquisição de ativo de longo prazo a prazo
- Classe: nenhuma · neutro · nao-ajusta
- Nomes: Compra de imobilizado a prazo; Aquisição de terreno para pagamento futuro; Aquisição de ativo assumindo a dívida
- Por quê: Investimento e financiamento sem caixa ficam fora da DFC e vão para as notas explicativas (CPC 03, itens 43 e 44).
- Questões: F0081, F0092, F0171, F0266, F0584

## dfc-arrendamento-reconhecimento · Aquisição de ativo por arrendamento
- Classe: nenhuma · neutro · nao-ajusta
- Nomes: Reconhecimento de máquina obtida por arrendamento
- Por quê: Na assinatura não há dinheiro; o fluxo aparece nos pagamentos (CPC 03, item 44, a).
- Questões: F0004

## dfc-integralizacao-bens · Integralização de capital com bens
- Classe: nenhuma · neutro · nao-ajusta
- Nomes: Integralização de capital com terreno; Integralização de capital com estoques; Integralização de capital com computadores; Aumento de capital com entrega de imóveis
- Por quê: Não entra dinheiro: transação fora da DFC, informada em nota (CPC 03, item 43).
- Questões: F0092, F0124, F0206, F0220, F0266

## dfc-capital-reservas · Aumento de capital com reservas ou lucros
- Classe: nenhuma · neutro · nao-ajusta
- Nomes: Aumento de capital com incorporação de reservas de lucros; Capitalização de lucros acumulados
- Por quê: É troca entre contas do patrimônio líquido, sem caixa.
- Questões: F0010, F0096, F0525, F0538

## dfc-capital-subscrito · Capital subscrito e ainda não integralizado
- Classe: nenhuma · neutro · nao-ajusta
- Nomes: Subscrição de capital a integralizar
- Por quê: Só o que foi integralizado em dinheiro aparece na DFC.
- Questões: F0296, F0510

## dfc-conversao-divida · Conversão de dívida em capital
- Classe: nenhuma · neutro · nao-ajusta
- Nomes: Conversão de debêntures em ações; Conversão de dívida em capital social
- Por quê: Exemplo de transação sem caixa do CPC 03 (item 44, c). Reduz o endividamento, mas não aparece no financiamento.
- Questões: F0259, F0297, F0457, F0469, F0640

## dfc-aquisicao-com-acoes · Aquisição paga com ações próprias
- Classe: nenhuma · neutro · nao-ajusta
- Nomes: Compra de prédio entregando ações da companhia; Aquisição de empresa por emissão de ações
- Por quê: CPC 03, itens 43 e 44, b.
- Questões: F0004, F0325

## dfc-permuta · Permuta sem dinheiro
- Classe: nenhuma · neutro · -
- Nomes: Permuta total de imóveis; Pagamento de dividendos com imóveis
- Por quê: Sem entrada nem saída de caixa, não há fluxo.
- Questões: F0092, F0363

## dfc-dividendo-declarado · Dividendos declarados e não pagos
- Classe: nenhuma · neutro · nao-ajusta
- Nomes: Proposta de dividendos ao fim do exercício; Reconhecimento de dividendos a pagar
- Por quê: Destinar o lucro não movimenta caixa; o fluxo só surge no pagamento.
- Questões: F0060, F0664

## dfc-reservas · Constituição de reservas
- Classe: nenhuma · neutro · nao-ajusta
- Nomes: Constituição de reserva de lucros; Constituição de reserva legal
- Por quê: Movimento interno do patrimônio líquido, sem caixa e sem passar pelo resultado.
- Questões: F0538

## dfc-venda-ativo-prazo · Venda de ativo de longo prazo a receber
- Classe: nenhuma · neutro · -
- Nomes: Venda de terreno com recebimento no próximo ano
- Por quê: Sem recebimento, não há fluxo de investimento neste período. O eventual ganho é retirado do lucro no método indireto, e o saldo a receber não entra como variação operacional.
- Questões: F0008, F0198, F0402

<!-- ===== Operações a prazo (entram pela variação das contas) ===== -->

## dfc-venda-prazo · Venda ou serviço a prazo
- Classe: nenhuma · neutro · -
- Nomes: Venda de mercadorias a prazo; Serviço prestado para recebimento futuro
- Por quê: A receita entra no lucro, mas não há caixa. No indireto, o efeito é desfeito pelo aumento de clientes; no direto, nada aparece.
- Questões: F0008, F0099, F0375

## dfc-compra-prazo · Compra de estoques a prazo
- Classe: nenhuma · neutro · -
- Nomes: Compra de mercadorias a prazo; Compra de matéria-prima para pagar depois
- Por quê: Sem pagamento não há fluxo. No indireto, o aumento de estoques e o de fornecedores se compensam.
- Questões: F0167, F0398, F0464

## dfc-despesa-nao-paga · Despesa reconhecida e ainda não paga
- Classe: nenhuma · neutro · -
- Nomes: Reconhecimento de salários a pagar no mês seguinte; Despesas operacionais do mês para pagar depois
- Por quê: A despesa reduz o lucro sem sair dinheiro; no indireto, isso é corrigido pelo aumento do passivo operacional.
- Questões: F0037, F0081, F0144, F0317

<!-- ===== Caixa e equivalentes ===== -->

## dfc-entre-caixa · Movimento entre itens de caixa e equivalentes
- Classe: nenhuma · neutro · nao-ajusta
- Nomes: Depósito do dinheiro do caixa na conta bancária; Saque da conta para o caixa
- Por quê: Movimentos entre itens de caixa e equivalentes são gestão de caixa e ficam fora das três atividades (CPC 03, item 9).
- Questões: F0078, F0120, F0237, F0484

## dfc-aplicacao-equivalente · Aplicação em equivalente de caixa
- Classe: nenhuma · neutro · nao-ajusta
- Nomes: Aplicação da sobra de caixa em título resgatável de imediato; Resgate de aplicação classificada como equivalente de caixa
- Por quê: Aplicar o excesso de caixa em equivalente é gestão de caixa (CPC 03, itens 7 e 9): o total de caixa e equivalentes não muda.
- Questões: F0120, F0237, F0320, F0327

## dfc-cheque-especial · Cheque especial na gestão de caixa
- Classe: nenhuma · neutro · nao-ajusta
- Nomes: Uso do cheque especial de curtíssimo prazo, com saldo que oscila
- Por quê: Saldo a descoberto liquidado em pouco tempo, que oscila entre devedor e credor, integra caixa e equivalentes (CPC 03, item 8); usar o limite não é fluxo de financiamento. Empréstimo bancário comum, sim.
- Questões: F0059, F0218, F0240, F0461

## dfc-variacao-cambial-caixa-ganho · Ganho cambial sobre o caixa em moeda estrangeira
- Classe: nenhuma · aumenta · subtrai
- Nomes: Alta da moeda estrangeira mantida em caixa
- Por quê: O saldo cresce sem haver fluxo: o efeito do câmbio sobre caixa e equivalentes aparece em linha separada das três atividades (CPC 03, item 28), e o ganho sai do lucro ajustado.
- Questões: F0349, F0382, F0392, F0439, F0542

## dfc-variacao-cambial-caixa-perda · Perda cambial sobre o caixa em moeda estrangeira
- Classe: nenhuma · diminui · soma
- Nomes: Queda da moeda estrangeira mantida em caixa
- Por quê: CPC 03, item 28: reduz o saldo, é apresentada à parte das três atividades e é devolvida ao lucro ajustado.
- Questões: F0349, F0382, F0542

<!-- ===== Ajustes do método indireto: itens sem caixa ===== -->

## dfc-depreciacao · Depreciação, amortização e exaustão
- Classe: nenhuma · neutro · soma
- Nomes: Despesa de depreciação; Amortização de intangível; Despesa de exaustão
- Por quê: Reduz o lucro sem tirar dinheiro: é somada no indireto (CPC 03, item 20, b) e não aparece no direto. A banca diz que ela "gera caixa" ou é de investimento: errado.
- Questões: F0006, F0092, F0110, F0204, F0495, F0509
### Histórias
- Carga do ano | A empresa registra o desgaste anual dos veículos usados na entrega. (F0006, F0285)

## dfc-impairment · Perda por redução ao valor recuperável
- Classe: nenhuma · neutro · soma
- Nomes: Perda no teste de recuperabilidade; Perda por impairment de imobilizado
- Por quê: Despesa sem saída de caixa; volta somada.
- Questões: F0128, F0329, F0357, F0419

## dfc-reversao-impairment · Reversão de perda por impairment
- Classe: nenhuma · neutro · subtrai
- Nomes: Reversão de perda por redução ao valor recuperável
- Por quê: Receita sem entrada de caixa; é retirada do lucro.
- Questões: F0377, F0419

## dfc-pecld · Perda estimada com créditos de liquidação duvidosa
- Classe: nenhuma · neutro · soma
- Nomes: Constituição de perdas estimadas com clientes; Despesa com créditos de liquidação duvidosa
- Por quê: Estimativa sem caixa (CPC 03, item 20, b). Se o saldo de clientes usado na variação já vier líquido da perda, não some outra vez.
- Questões: F0318, F0406, F0465, F0621

## dfc-reversao-pecld · Reversão de perdas estimadas com clientes
- Classe: nenhuma · neutro · subtrai
- Nomes: Reversão de perdas estimadas com créditos
- Por quê: Aumenta o lucro sem trazer dinheiro.
- Questões: F0335, F0377

## dfc-provisao · Constituição de provisão
- Classe: nenhuma · neutro · soma
- Nomes: Constituição de provisão para contingências; Despesa com provisão para riscos trabalhistas
- Por quê: Despesa estimada, ainda sem pagamento (CPC 03, item 20, b).
- Questões: F0128, F0204, F0406

## dfc-ajuste-estoque · Ajuste de estoque ao valor realizável líquido
- Classe: nenhuma · neutro · soma
- Nomes: Perda para reduzir o estoque ao valor realizável líquido
- Por quê: Despesa sem caixa. Se a variação de estoques já vier líquida do ajuste, não conte duas vezes.
- Questões: F0329, F0465

## dfc-mep-ganho · Resultado positivo de equivalência patrimonial
- Classe: nenhuma · neutro · subtrai
- Nomes: Receita de equivalência patrimonial; Ganho na equivalência patrimonial
- Por quê: Aumenta o lucro sem entrada de dinheiro; só o dividendo efetivamente recebido é fluxo (CPC 03, itens 20, b, e 37).
- Questões: F0164, F0248, F0398, F0515, F0635

## dfc-mep-perda · Resultado negativo de equivalência patrimonial
- Classe: nenhuma · neutro · soma
- Nomes: Despesa de equivalência patrimonial; Perda na equivalência patrimonial
- Por quê: Reduz o lucro sem saída de caixa.
- Questões: F0009, F0462, F0524

## dfc-juros-nao-pagos · Despesa de juros ainda não paga
- Classe: nenhuma · neutro · soma
- Nomes: Despesa financeira não paga no exercício; Juros apropriados para pagamento no vencimento
- Por quê: Aumenta a dívida, não tira dinheiro: soma no indireto. Se a banca diz que os juros não foram pagos, o aumento do passivo não é captação.
- Questões: F0023, F0067, F0145, F0169, F0276

## dfc-receita-financeira-nao-recebida · Rendimento apropriado e não recebido
- Classe: nenhuma · neutro · subtrai
- Nomes: Juros de aplicação de longo prazo incorporados ao saldo
- Por quê: Receita sem entrada de caixa; sai do lucro ajustado.
- Questões: F0066, F0642

## dfc-cambio-divida-perda · Perda cambial não realizada sobre dívida
- Classe: nenhuma · neutro · soma
- Nomes: Perda cambial não realizada; Variação cambial que aumenta um empréstimo
- Por quê: Não é fluxo de caixa (CPC 03, itens 20, b, e 28): soma-se ao lucro. Cuidado com a frase que manda somá-la junto com resultado positivo de equivalência.
- Questões: F0009, F0515, F0621, F0635

## dfc-cambio-ganho · Ganho cambial não realizado sobre dívida
- Classe: nenhuma · neutro · subtrai
- Nomes: Ganho cambial não realizado sobre um empréstimo
- Por quê: Aumenta o lucro sem dinheiro (CPC 03, item 20, b).
- Questões: F0392

## dfc-ir-diferido · Tributos diferidos
- Classe: nenhuma · neutro · soma
- Nomes: Despesa de imposto de renda diferido
- Por quê: Item sem caixa citado no item 20, b, do CPC 03. A receita de tributo diferido é subtraída.

## dfc-ganho-venda · Ganho na venda de ativo de longo prazo
- Classe: nenhuma · neutro · subtrai
- Nomes: Lucro na venda de imobilizado, linha da DRE; Ganho na alienação de investimento; Lucro na venda de terreno
- Por quê: O ganho não é um fluxo próprio: o dinheiro todo da venda fica em investimento, e o ganho é tirado do lucro no indireto (CPC 03, itens 14 e 20, c).
- Questões: F0062, F0272, F0465, F0635

## dfc-perda-venda · Perda na venda ou baixa de ativo de longo prazo
- Classe: nenhuma · neutro · soma
- Nomes: Prejuízo na venda de imobilizado, linha da DRE; Perda na alienação de investimento
- Por quê: A perda não gastou caixa nas operações; volta somada.
- Questões: F0012, F0329, F0377

## dfc-doacao · Bem recebido em doação e reconhecido como receita
- Classe: nenhuma · neutro · subtrai
- Nomes: Receita com terreno recebido em doação sem condições
- Por quê: Aumenta o lucro sem entrada de dinheiro; a aquisição também fica fora da DFC.
- Questões: F0365

<!-- ===== Variações das contas operacionais ===== -->

## dfc-aum-clientes · Aumento de clientes
- Classe: operacional · diminui · subtrai
- Nomes: Aumento do saldo de clientes; Aumento de duplicatas a receber
- Por quê: Parte do lucro ficou a receber: em relação ao lucro, o caixa operacional é menor. Ativo operacional que sobe, subtrai.
- Questões: F0247, F0480, F0493, F0613, F0635

## dfc-dim-clientes · Diminuição de clientes
- Classe: operacional · aumenta · soma
- Nomes: Redução do saldo de clientes; Diminuição de duplicatas a receber
- Por quê: Recebeu-se mais do que se vendeu no período: ativo operacional que cai, soma.
- Questões: F0398, F0480

## dfc-aum-estoques · Aumento de estoques
- Classe: operacional · diminui · subtrai
- Nomes: Aumento de estoques; Aumento do saldo de mercadorias
- Por quê: Dinheiro (ou crédito) foi parar no estoque sem passar pelo custo: subtrai.
- Questões: F0121, F0143, F0512, F0620

## dfc-dim-estoques · Diminuição de estoques
- Classe: operacional · aumenta · soma
- Nomes: Redução de estoques; Diminuição do saldo de mercadorias
- Por quê: O custo no resultado veio de estoque comprado antes: soma.
- Questões: F0269, F0408

## dfc-aum-antecipadas · Aumento de despesas antecipadas
- Classe: operacional · diminui · subtrai
- Nomes: Aumento de despesas antecipadas; Aumento de seguros antecipados; Aumento de aluguéis pagos antecipadamente
- Por quê: Pagou-se mais do que virou despesa.
- Questões: F0258, F0465

## dfc-dim-antecipadas · Diminuição de despesas antecipadas
- Classe: operacional · aumenta · soma
- Nomes: Redução de seguros antecipados; Apropriação de despesas pagas antecipadamente
- Por quê: A despesa do período já tinha sido paga antes: volta somada.
- Questões: F0373, F0587

## dfc-aum-recuperar · Aumento de tributos a recuperar e adiantamentos a fornecedores
- Classe: operacional · diminui · subtrai
- Nomes: Aumento de tributos a recuperar; Aumento de adiantamentos a fornecedores
- Por quê: Ativos operacionais que sobem consomem caixa.
- Questões: F0398

## dfc-aum-fornecedores · Aumento de fornecedores
- Classe: operacional · aumenta · soma
- Nomes: Aumento do saldo de fornecedores; Aumento de contas a pagar a fornecedores
- Por quê: Parte das compras não foi paga: passivo operacional que sobe, soma.
- Questões: F0121, F0398, F0512, F0480

## dfc-dim-fornecedores · Diminuição de fornecedores
- Classe: operacional · diminui · subtrai
- Nomes: Redução do saldo de fornecedores
- Por quê: Pagou-se mais do que se comprou: subtrai. Não é financiamento.
- Questões: F0269, F0470

## dfc-aum-passivos · Aumento de salários, impostos e contas a pagar
- Classe: operacional · aumenta · soma
- Nomes: Aumento de salários a pagar; Aumento de impostos a recolher; Aumento de imposto de renda a pagar; Aumento de contas a pagar
- Por quê: Despesa que ainda não saiu do caixa: soma.
- Questões: F0116, F0143, F0307, F0398

## dfc-dim-passivos · Diminuição de salários, impostos e contas a pagar
- Classe: operacional · diminui · subtrai
- Nomes: Redução de salários a pagar; Redução de impostos a pagar; Redução de aluguéis a pagar
- Por quê: Quitaram-se obrigações de períodos anteriores: subtrai.
- Questões: F0116, F0247

## dfc-aum-receita-antecipada · Aumento de adiantamentos de clientes
- Classe: operacional · aumenta · soma
- Nomes: Aumento de receitas antecipadas; Aumento de adiantamentos de clientes
- Por quê: Entrou dinheiro que ainda não é receita: soma ao lucro.
- Questões: F0200, F0398, F0656

## dfc-dim-receita-antecipada · Diminuição de adiantamentos de clientes
- Classe: operacional · diminui · subtrai
- Nomes: Redução de receitas antecipadas
- Por quê: Parte da receita do período já tinha sido recebida antes: sai do lucro ajustado.
- Questões: F0619, F0656

<!-- ===== Imposto ligado a investimento ===== -->

## dfc-ir-investimento · Imposto identificado com a venda de um ativo
- Classe: investimento · diminui · -
- Nomes: Pagamento do imposto ligado especificamente à venda de um imobilizado
- Por quê: Quando é praticável identificar o imposto com a transação de investimento ou financiamento, ele segue a mesma atividade (CPC 03, itens 35 e 36).
- Questões: F0181, F0358, F0471
### Histórias
- Imposto da venda do veículo | A sociedade calcula e paga o tributo que nasceu da venda de um veículo usado na operação. (F0181)
