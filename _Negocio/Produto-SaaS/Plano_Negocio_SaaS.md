# Plano de Negócio — Studio Bolsas SaaS

> Consolidado em 16/06/2026 a partir de pesquisa de mercado/concorrência/benchmarks reais (fontes no fim). Complementa `Posicionamento.md` e `Precificacao.md`. Documento de decisão para a Obralivre: **vale empurrar o Studio Bolsas como produto SaaS, e como?**

---

## 1. Sumário executivo

Transformar o app de gestão do ateliê da Lisandra num SaaS vendável para **artesãos que produzem por receita, consomem insumo fracionado e vendem em marketplace/Instagram** — entrando pelo nicho têxtil (crochê/macramê/bolsas) e expandindo para confeitaria.

**Veredito honesto:** como aposta de SaaS pura, é **negócio de nicho pequeno/lifestyle**, não escala de venture. Potencial de receita direta em 3 anos: **R$ 36k–340k ARR (base ~R$ 115k)**. O teto da categoria inteira (o líder, Calcularte, após 10 anos) é **< R$ 1 mi/ano**. **Vale a pena** porque o produto já está construído (custo afundado baixo), a Lisandra é caso de sucesso grátis, e há uma **janela rara** (fechamento do Elo7 em mai/2026 deslocou dezenas de milhares de artesãos). Melhor enquadrado como **ativo estratégico + isca de leads da Obralivre** do que como bet de assinatura isolada.

---

## 2. Produto

- App de gestão completo (precificação, ficha de receita, estoque de matéria-prima fracionada, caixa/DRE, vitrine). **Estágio: v2.13, funcional, em produção** (1 cliente real: ateliê Lisandra).
- Diferencial técnico real (ver `Posicionamento.md`): **controle de matéria-prima por peso (conta de chegada un→g)**, ficha de receita de pontos, custo de produção por consumo real (pesar a sobra), preço por canal de marketplace — profundidade que os concorrentes genéricos não têm.
- Falta para virar multi-cliente de verdade: cobrança/assinatura (gateway), onboarding guiado (ver `AUDITORIA_UX.md`), landing page.

---

## 3. Mercado (TAM / SAM / SOM)

| Camada | Quem | Tamanho | Receita/ano se 100% pagasse |
|---|---|---|---|
| **TAM** | MEIs de artesanato + confeitaria no BR | ~500k–1,2 mi | R$ 180–430 mi (teórico) |
| **SAM** | Têxtil + confeitaria que vende online com operação estruturada | ~40–80 mil | ~R$ 15–30 mi |
| **SOM (3 anos)** | Capturável de fato | **100–850 pagantes** | **R$ 36k–340k ARR** |

Contexto: ~8,5 mi de artesãos no BR (número mole — inclui hobby), 77% mulheres; ~15,7 mi de MEIs totais. **Elo7 (proxy de "artesão online", pico 130k vendedores) encerrou em mai/2026** → some o termômetro, mas abre janela de migração.

**Âncora de realidade:** Calcularte levou **10 anos** para 74k usuários cadastrados (~2% convertem = ~1,5–3,7k pagantes, MRR ~R$28–66k). É o teto da categoria — e ainda é um negócio pequeno, sem investimento.

---

## 4. Concorrência (resumo — detalhe em `Posicionamento.md`)

| Concorrente | Preço | Tração |
|---|---|---|
| Calcularte (líder) | freemium / R$289,90/ano | 74k usuários, 10 anos, 68k seguidores IG |
| Apreço | R$24,90/mês | 100k+ downloads, 40k ativos, 750 pagantes (2022) |
| Artesaney / ArteIA | R$19,90–49,90 | recentes, web-first, tração baixa |
| **Confeitaria** (ZupConfeitaria, Minha Confeitaria, Lucro na Confeitaria…) | R$9–40/mês | fragmentado, **sem líder claro** → janela maior |

Não é oceano azul. **Diferenciação = profundidade** (matéria-prima/receita/custo real), não ineditismo.

---

## 5. Preço e planos (detalhe em `Precificacao.md`)

| Plano | Preço | ARPU usado no modelo |
|---|---|---|
| Grátis | R$ 0 (isca) | — |
| **Pro** | R$ 29,90/mês ou R$ 299/ano | dominante |
| **Estúdio** | R$ 59,90/mês | minoria |

**ARPU blended estimado: ~R$ 30/mês** (mix Pro + alguns Estúdio − descontos anuais). Recorrente; vitalício só como oferta de fundadores.

---

## 6. Projeção de receita (36 meses)

| Cenário | Premissas-chave | Pagantes mês 36 | MRR | **ARR** |
|---|---|---|---|---|
| **Conservador** | conv. 2%, churn 10%/mês, ~50 free/mês | ~100 | ~R$ 3.000 | **~R$ 36k** |
| **Base** | conv. 3,5%, churn 7%/mês, ~100 free/mês +7%/mês | ~300 | ~R$ 9–10k | **~R$ 115k** |
| **Otimista** | conv. 5%, churn 5%/mês, ~200 free/mês +12%/mês | ~850 | ~R$ 25–28k | **~R$ 340k** |

Ritmo de referência (micro-SaaS BR): R$10k ARR em ~9 meses, R$100k ARR em ~15 meses.

---

## 7. Estrutura de custos

| Custo | Estimativa | Nota |
|---|---|---|
| **Infra (Firebase)** | ~R$ 0 até dezenas de clientes; depois **~R$ 2–5/cliente/mês** | Free tier cobre muito; fotos base64 são o maior peso |
| **Gateway de pagamento** (Asaas/Vindi/Pagar.me) | ~R$ 1 fixo + 2–3% → **~R$ 2/cobrança** | Pix recorrente reduz custo e churn involuntário |
| **Domínio + e-mail** | ~R$ 50–100/ano | marginal |
| **Desenvolvimento** | ✅ já feito (custo afundado) | manutenção = tempo |
| **Suporte + conteúdo/marketing** | **TEMPO do Alessandro/equipe** | o custo real do negócio |

> **Insight-chave:** custos de caixa são quase zero (margem bruta ~83%). O verdadeiro custo é o **tempo do Alessandro** (dev + suporte + conteúdo) — o que importa é o **custo de oportunidade** vs. outras frentes da Obralivre.

---

## 8. Unit economics

| Métrica | Valor | Como |
|---|---|---|
| ARPU | ~R$ 30/mês | mix de planos |
| Custo de servir | ~R$ 5/cliente/mês | infra + gateway |
| **Margem bruta** | **~R$ 25/cliente/mês (~83%)** | ARPU − custo |
| Churn | 7–10%/mês | público MEI baixa renda |
| Vida média | ~10–14 meses | 1/churn |
| **LTV** | **~R$ 350–430** | margem ÷ churn |
| **CAC alvo** | **< R$ 80** (orgânico obrigatório) | mantém LTV/CAC ≥ 4 |
| LTV/CAC | ≥ 3:1 (ideal 3–4:1) | saúde |
| Payback | ~3 meses | se CAC orgânico |

**Travas:** (1) ticket R$30 **não comporta anúncio pago** (CAC R$150–400 queima caixa) → aquisição ~100% orgânica. (2) **Churn é o inimigo nº1** (41% dos MEIs inadimplentes) → exige Pix recorrente + régua de cobrança + produto pegajoso. (3) Concorrente real é a **planilha grátis** → tem que ser 10x mais simples e percebido como "me faz ganhar mais".

---

## 9. Go-to-market

**Fase 0 — Fundação (0–3 meses):** onboarding guiado (ver `AUDITORIA_UX.md`), cobrança (gateway + Pix recorrente), landing page, **depoimento em vídeo da Lisandra** (prova social âncora).

**Fase 1 — Tração orgânica (3–12 meses):**
- Conteúdo de dor #1 ("como precificar crochê/bolsa sem trabalhar de graça") no Instagram + SEO.
- **Grupos de Facebook/WhatsApp de artesanato** (há grupos de 50–200k membros).
- **Surfar a onda Elo7:** conteúdo e captação dos vendedores deslocados ("Elo7 fechou — organize seu ateliê e venda direto").
- Freemium como isca → meta de conversão 2–3,5%.

**Fase 2 — Escala leve (12–24 meses):** referral ("indique 3 amigas, ganhe 1 mês"), parcerias com **fornecedores de fio/insumo** (canal + co-marketing), abrir **vertical confeitaria** (menos saturada).

**Fase 3 — Decisão (24–36 meses):** consolidar ou manter lifestyle. Reavaliar se vale estrutura/investimento.

---

## 10. Riscos

- **Churn involuntário** (cartão/Pix recusado) — mitigar com gateway BR + dunning.
- **Teto de mercado baixo** — nicho satura rápido; é negócio de 300–1.000 pagantes, não milhões.
- **Imitação** — nicho validado é clonado em 3–6 meses; defesa = comunidade + marca + profundidade de produto.
- **Custo de oportunidade** — tempo do Alessandro pode render mais em serviços de agência.
- **Software é o 1º corte em crise** para MEI de baixa renda — posicionar como "ganha-dinheiro", não "organização".

---

## 11. Recomendação estratégica (Obralivre)

1. **Não tratar como bet de escala.** Tratar como **ativo enxuto + isca de leads**: cada artesão que entra é lead potencial pros outros serviços Obralivre (sites, tráfego, social).
2. **Aproveitar a janela Elo7 agora** (dor + migração no pico) — é timing raro.
3. **Custo de entrada é baixíssimo** (app pronto, Lisandra grátis) → ROI incremental favorável mesmo no cenário conservador.
4. **Gate de decisão:** se em ~9–12 meses não chegar perto de R$10k ARR com esforço só orgânico, é sinal de manter como ferramenta interna/portfólio, não SaaS.

**Number-alvo realista para planejar:** base ~R$ 115k ARR / ~300 pagantes em 3 anos; teto ~R$ 340k.

---

## 12. Fontes (principais)

- Mercado: Agência Sebrae (artesanato 8,5 mi; +crescimento), Receita Federal/Sebrae (15,7 mi MEIs), Etsy press release + E-Commerce Brasil (Elo7 56k→encerramento mai/2026), InvesteSP/Sebrae SP (confeitaria R$12bi, +14% MEIs doces).
- Concorrência: Blog Calcularte (74k/10 anos), Projeto Draft (Apreço 40k ativos/750 pagantes), Google Play (downloads), Instagram das marcas.
- Benchmarks SaaS: Userpilot/ChartMogul/FirstPageSage (conversão freemium 2–5%), UserMotion/Kalungi (churn SMB), PagBrasil + MixVale (inadimplência MEI 41%), microsaas.substack.com (ritmo micro-SaaS BR), PhoenixStrategy/CapChase (LTV/CAC).
