# Ateliê Lisandra — Contexto e Dados conhecidos

> Consolidado em 14/06/2026 a partir do que já temos no projeto (app Studio Bolsas, spec técnica e histórico). É o ponto de partida da estruturação — confirmar e atualizar com a Lisandra.

## O negócio
- **O que é:** ateliê de bolsas artesanais de luxo (crochê / macramê em fio de malha).
- **Dona:** Lisandra (lis01sperb@gmail.com).
- **Localização:** Cachoeira do Sul (RS) — referência para frete de fornecedores.
- **Gestão:** usa o app **Studio Bolsas** (projetos, precificação, estoque, caixa, dashboard).

## Catálogo de modelos
Modelos já definidos no app: **Flora, Jolie, Mini Bag Lis, Duquesa, Bali**.
_(Falta: foto, faixa de preço e custo de cada um — preencher.)_

## Plano de negócio (fases e metas)
| Fase | Período | Meta |
|---|---|---|
| 1 — Aprendizado | 01/06 – 31/08/2026 | estruturar produção e processo |
| **2 — Primeiras Vendas** | **a partir de 01/09/2026** | **10 vendas / R$ 3.000** |
| 3 — Crescimento | a partir de 01/12/2026 | 40 vendas / R$ 15.000 |

_(**Fase atual: 2 — Primeiras Vendas**, iniciada em 01/09/2026. Datas conferidas contra `CFG_PADRAO.fases` no `index.html`; as metas são editáveis no app, então o código é a fonte.)_

## Canais de venda e taxas
| Canal | Taxa |
|---|---|
| Shopee | 16% |
| Instagram | 10% |
| Mercado Livre | 15% |
| Feira / WhatsApp / Direto | 0% |

- **Vitrine online:** `loja.html` — catálogo público com compra via WhatsApp (MVP de venda online). Checkout e frete próprios ficaram fora do escopo por ora.

## Precificação (modelo em uso)
- **Custo total** = materiais + (horas × valor/hora) + embalagem + outros custos fixos.
- **Preço mínimo** = custo ÷ (1 − taxa da plataforma).
- **Preço sugerido** = custo ÷ (1 − taxa − margem desejada).
- **Lucro líquido por venda** = valor − custo da peça − (valor × taxa da plataforma).

## Estrutura de custos
- **Materiais:** fio náutico de poliéster (ver `Fios-e-Fornecedores.md` — custo/metro: Poli 3mm ~R$0,16–0,18, Perla 4mm ~R$0,24–0,28). Controlados no estoque, com qtd mínima e fornecedor.
- **Mão de obra:** horas de produção × valor/hora.
- **Embalagem** e outros custos fixos por peça.
- **Taxa de plataforma** conforme o canal.

---

## Lacunas a preencher (próximos passos)
1. **Formalização** — MEI / ME? CNPJ? Situação fiscal atual.
2. **Custo e preço por modelo** — levantar custo real e preço praticado de Flora, Jolie, Mini Bag Lis, Duquesa, Bali.
3. **Capacidade de produção** — quantas peças/mês a Lisandra consegue fazer.
4. **Valor/hora da mão de obra** — definir quanto vale a hora de trabalho dela.
5. **Meta de faturamento** e ponto de equilíbrio do ateliê.
6. **Vendas até hoje** — histórico real (se houver) para validar as fases.
