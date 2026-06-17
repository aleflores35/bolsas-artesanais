# Studio Bolsas SaaS — Precificação

> Rascunho consolidado em 16/06/2026. Base: pesquisa de concorrência real (jun/2026) — apps de artesanato, confeitaria e ERPs micro. Números de concorrentes verificados na web; preços do Studio Bolsas são recomendação a validar.

## TL;DR (a recomendação)

| Plano | Preço | Pra quem |
|---|---|---|
| **Grátis** | R$ 0 | Isca: calculadora de preço + teto de projetos/lançamentos. Aquisição + SEO. |
| **Pro** | **R$ 29,90/mês** ou **R$ 299/ano** (≈ R$ 24,90/mês) | O coração. App completo, 1 ateliê, 1 usuário. |
| **Estúdio** | **R$ 59,90/mês** ou **R$ 599/ano** | Quem já fatura: multiusuário, vitrine/loja com domínio, relatórios, backup automático. |

**Faixa-âncora de entrada: R$ 24,90–29,90/mês.** É onde os líderes (Calcularte, Apreço) estão — entrar aí posiciona como **par dos líderes**, não como o mais barato. Não brigar por preço; brigar por profundidade (ver `Posicionamento.md`).

## A lógica em 3 fatos

1. **Custo de servir é ~zero.** Firebase free tier cobre dezenas de ateliês; no Blaze, o marginal por cliente é R$ 1–5/mês (fotos são o maior peso). Margem em qualquer preço acima de ~R$ 15 já passa de 85%. **O limite é disposição a pagar, não custo.**
2. **Teto da disposição a pagar do cliente.** Artesão/confeiteira MEI são sensíveis a preço. O piso de mercado de entrada está em **R$ 19,90/mês**; resistência forte acima de **R$ 39,90/mês** sem IA/automação. Régua psicológica: o SaaS tem que custar **menos que uma fração de uma peça vendida/mês** (bolsa de luxo R$ 200–500 → R$ 29,90 é <10% de uma peça).
3. **Teto de âncora superior (ERP).** A partir de ~R$ 120–150/mês o cliente pensa "por esse preço pego um Bling/Conta Azul que faz tudo". **Zona segura de micro-SaaS de nicho: R$ 29–97/mês** — aí não se concorre com ERP, se concorre com "planilha" e "não usar nada", briga muito mais fácil de ganhar.

## Mapa de mercado (concorrência real, jun/2026)

### Artesanato (concorrentes diretos)
| Produto | Entrada | Anual | Premium | Modelo |
|---|---|---|---|---|
| Calcularte | R$ 49,90/mês | R$ 289,90/ano (≈R$24/mês) | — | freemium + assinatura |
| Apreço PRO | R$ 24,90/mês | R$ 239,90/ano | — | assinatura (+ cursos) |
| Artesaney | R$ 19,90/mês | — | R$ 39,90/mês (Pro) | assinatura |
| ArteIA | grátis | (−25% anual) | até R$ 89,90/mês | freemium + IA |
| Planilhas Elo7/Hotmart | — | — | R$ 29,90–149,90 **vitalício** | pagamento único |

### Confeitaria (vertical 2 — mais saturado, guerra de preço)
- Entrada concentrada em **R$ 14,90–19,90/mês** (ZupConfeitaria, Minha Confeitaria, Doce Cálculo, BakePro).
- Premium com IA/WhatsApp: R$ 69,90–79,90/mês (Bakerly, Confeit.it, Meslo).
- Maya R$ 449/ano; Confeiteira Pro R$ 9/mês (piso).
- **Confeiteira aceita tier premium (>R$ 50) mais fácil quando há automação de WhatsApp/IA** — guardar esse aprendizado pro vertical 2.

### Âncora superior (ERPs genéricos — o teto)
| ERP | Entrada R$/mês |
|---|---|
| Bling (Cobalto) | 55 |
| Tiny (Avance) | 66 |
| GestãoClick (Bronze) | 119 |
| Conta Azul (Essencial MEI) | 159,90 |

## Modelo de cobrança

- **Recorrente (mensal + anual)** é o modelo dominante e o correto pra SaaS. Anual com 2 meses grátis reduz churn.
- ⚠️ **Cuidado com o "vitalício"** — domina o nicho de planilhas (R$ 29–149 único) e converte bem, mas **mata a receita recorrente** que é a razão de ser do SaaS. Usar só como **oferta de fundadores**.
- **Oferta de fundadores (lançamento):** anual com desconto pesado pros primeiros 20–50 clientes (ex.: R$ 199/ano vitalício do preço, "preço de fundador travado"). Gera caixa inicial + prova social, sem fixar vitalício como modelo permanente.

## Como o Studio Bolsas se encaixa

- **Não ser o mais barato** (R$ 9–14 da confeitaria é guerra de preço suicida com custo de aquisição).
- **Entrar no patamar dos líderes** (R$ 24,90–29,90) e **justificar com profundidade**: ficha de receita, estoque de matéria-prima fracionada (conta de chegada), preço por canal — o que Calcularte/Apreço/Artesaney **não** fazem (ver lacunas em `Posicionamento.md`).
- **Tier Estúdio a R$ 59,90** mira quem fatura (fase 3 da Lisandra) com loja própria + multiusuário — abaixo do teto de âncora do ERP (R$ 120), então seguro.

## Pendências pra fechar o preço

1. **Custo real por peça da Lisandra** (lacuna conhecida em `../Atelie-Lisandra/Contexto-e-Dados.md`) — pra cravar a régua "fração de uma peça".
2. **O que falta no app pra ser multi-tenant + cobrança** (Stripe/Pagar.me/assinatura) — define o custo de construir antes de vender.
3. **Validar willingness-to-pay** com 5–10 artesãs reais (entrevista rápida: "quanto pagaria/mês por isso?").
