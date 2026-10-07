# Pendências

## 🔴 Confirmar com você (intenção do resumo original)

- **Direito Administrativo — resumo de 29/09/2026:** o arquivo "29_09_26 - Resumos - Auditor Fiscal.docx" tem o título "Direito Administrativo" no fim, mas nenhum conteúdo abaixo dele. Faltou colar essa parte? Se sim, mande-a para eu incorporar.

- **Direito Tributário — resumo de 04/10/2026:** o arquivo "04_10_26 - Resumos - Auditor Fiscal.docx" tem o título "Direito Tributário" no começo, mas nenhum conteúdo abaixo dele. Faltou colar essa parte? Se sim, mande-a para eu incorporar.

- **Direito Constitucional — resumo de 06/10/2026:** o arquivo "06_10_26 - Resumos - Auditor Fiscal.docx" tem o título "Direito Constitucional" sem nenhum conteúdo abaixo. Faltou colar essa parte? Se sim, mande-a para eu incorporar (os quatro ajustes pedidos nos temas foram feitos).

- **Direito Tributário — cláusulas pétreas (resumo de 06/10/2026):** o resumo diz que o STF considera cláusulas pétreas a anterioridade, a noventena, a imunidade recíproca e as imunidades de templos, partidos, sindicatos, educação e assistência social e livros. A ADI 939 (1993) trata expressamente da anterioridade e da imunidade recíproca. Você tem a fonte (julgado ou aula) para a noventena e para as demais imunidades? Mantive como no resumo, com ⚠️ em `limitacoes-ao-poder-de-tributar.md`.

- **Direito Administrativo — influências estrangeiras (resumo de 06/10/2026):** a razoabilidade aparece nas influências portuguesa e alemã, e o mandado de segurança é atribuído à influência britânica. Parte da doutrina liga a razoabilidade ao direito anglo-americano (a alemã seria a proporcionalidade) e o mandado de segurança ao amparo mexicano e aos *writs* norte-americanos. Mantive como no resumo, e as questões não cobram esses dois pontos. Qual é a fonte do seu material?

- **Contabilidade — venda à vista com lucro (resumo de 06/10/2026):** o resumo classifica como **misto aumentativo** (permuta do custo + lucro); relato de gabarito de banca trata a operação como **modificativo aumentativo** (receita e custo como fatos separados). Mantive o seu, e as questões evitam cobrar só essa classificação. Quer que eu registre a divergência no tema?

*As quatro pendências da carga inicial foram resolvidas por você em 27/09/2026 (ver `alteracoes.md`, v002).*

## 🟠 Acompanhar (jurisprudência/legislação em aberto)

- **STF — ADIs 6.254 e outras (EC 103/2019):** maioria formada (jun/2024) pela inconstitucionalidade do art. 149, §§1º-A, 1º-B e 1º-C (contribuição de inativos acima do salário mínimo e contribuição extraordinária); julgamento suspenso por vista, sem conclusão na última verificação. Progressividade das alíquotas empatada. → atualizar `Direito Tributário/03 - Espécies Tributárias/contribuicoes-sociais-e-previdenciarias.md` quando concluído.
- **STF — Tema 1.000 (RE 1.133.118): nepotismo em cargos de natureza política.** Em julgamento com repercussão geral, sem tese fixada (último andamento: 19/08/2026, devolução de vista; verificado em 30/09/2026). Hoje vale o entendimento das Turmas (em regra, SV 13 não se aplica, salvo fraude ou falta manifesta de qualificação). → atualizar `Direito Administrativo/04 - Princípios da Administração Pública/principios-expressos.md` (seção Moralidade → Nepotismo) e a Q021 de `Direito Administrativo/Questões Turbo/principios-expressos.md` quando concluído.
- **Reforma Tributária:** alíquotas da CBS e do Imposto Seletivo para 2027 ainda dependiam de lei ordinária na última verificação.
- **Teto do MEI (R$ 81.000):** valor vigente conferido em 04/10/2026 (gov.br); há projetos de lei complementar em tramitação para elevá-lo (ressalva já inserida no tema, entre parênteses). Afeta a dispensa de escrituração do pequeno empresário (`05 - Escrituração/escrituracao-e-livros-contabeis.md`).

## 🟡 Organização / fluxo de trabalho

- **Neon, chaves novas (v008):** os comentários e o ritmo de estudo sincronizam como as chaves `comentarios` e `atividade`. Rode uma vez, no SQL Editor do Neon, o bloco de migração no fim de `sistema/neon.sql` (o `alter table ... estudos_dados_chave`). Sem isso, só essas duas chaves falham ao sincronizar; o resto continua funcionando.

- **Pontos dos temas apontados pelos agentes de questões (06/10/2026), para você decidir se ajusto o texto:**
  - `taxas.md` (Competência): diz que o exercício da competência é facultativo e, na mesma frase, que a LRF (art. 11) exige instituir todos os tributos.
  - `atos-e-fatos-administrativos.md`: a pegadinha do aluguel diz que o fato contábil ocorre "com a apropriação ou o pagamento"; o pagamento de aluguel já apropriado é permutativo (−A/−P).
  - `escrituracao-e-livros-contabeis.md`: a ITG 2000 (R1) cita o Razão entre os livros obrigatórios, enquanto a legislação comercial o trata como facultativo; as questões evitam o ponto.
  - `administracao-direta-e-indireta.md`: empresa pública com "capital 100% público" x Lei 13.303/2016, art. 3º, parágrafo único (admite outras entidades públicas, mantida a maioria votante do ente controlador).
  - `regime-juridico-administrativo.md`: autorização legislativa para alienar imóveis (Lei 14.133/2021, art. 76) tem exceções, por exemplo para autarquias e fundações.
  - `classificacao-das-constituicoes.md`: o aviso "em prova prevalece" é orientação de estudo, não conteúdo constitucional.
- **Servidor do site (`--servir`):** ele guarda o código na memória; depois de mudanças em `gerar.py`, reinicie-o. Em 07/10/2026 ele foi reiniciado (o processo antigo havia sido encerrado).

- **Concurso-alvo e data-base do edital:** saber qual concurso (e se a banca é mesmo CEBRASPE) ajuda a priorizar legislação estadual/municipal e a decidir como tratar a transição PIS/COFINS → CBS.
- **Datas originais dos estudos:** não informadas no arquivo inicial.
- Termo "eficácia prospectiva" (sinônimo de eficácia contida no seu material): mantido; não é a nomenclatura mais usual (Temer: "redutível ou restringível").

## ⚪ Assuntos mencionados, mas ainda não consolidados (estudar)

- **Tributário:** competência tributária; anterioridades e imunidades (demais limitações ao poder de tributar; legalidade já consolidada em 06/10/2026); obrigação tributária (art. 113); impostos em espécie; transação tributária.
- **Constitucional:** processo legislativo (MP, LC, EC); controle de constitucionalidade (ADI, ADO, mandado de injunção); competências legislativas (art. 22); estado de defesa e de sítio; direitos fundamentais em espécie.
- **Administrativo:** poderes administrativos (polícia, regulamentar, hierárquico); atos administrativos (anulação, revogação, convalidação); serviços públicos e concessões; agentes públicos (estabilidade, greve); improbidade; processo administrativo (Lei 9.784/99); bens públicos.
- **Contabilidade:** demonstrações contábeis (Balanço Patrimonial, DRE).
