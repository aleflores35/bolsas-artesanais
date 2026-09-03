# Studio Bolsas — Especificação Técnica de Desenvolvimento

**Versão:** 1.0 · **Data:** 11/06/2026 · **Status:** Proposta
**Base:** protótipo atual (`index.html` v1.2, Firebase Firestore, deploy Vercel)

---

## 1. Visão geral

O **Studio Bolsas** é um sistema de gestão para ateliês de bolsas artesanais (crochê/macramê de luxo). Ele unifica em um só lugar o ciclo completo do negócio artesanal: criação do projeto (receita de pontos, materiais, fotos), precificação, controle de estoque (materiais e produtos prontos), registro financeiro (vendas e despesas) e acompanhamento do plano de negócio em fases.

O protótipo atual já valida o produto: é um SPA em arquivo HTML único (~1.300 linhas), com sincronização em tempo real via Firestore e publicado na Vercel. Esta spec descreve como reconstruí-lo como produto real, mantendo as funcionalidades validadas e corrigindo as limitações estruturais.

### 1.1 Objetivos da reconstrução

1. **Multiusuário com autenticação** — hoje o banco é aberto, sem login; qualquer pessoa com a URL acessa e altera os dados.
2. **Segurança** — credenciais Firebase expostas no client sem regras de acesso; preciso isolar dados por conta.
3. **Manutenibilidade** — sair do HTML único com JS inline para uma base de código componentizada, tipada e testável.
4. **Evolução** — abrir caminho para upload real de fotos, relatórios, PWA/offline e, futuramente, mais de um ateliê (SaaS).

### 1.2 Não-objetivos (v2.0)

App nativo, marketplace próprio, emissão de NF, integração direta com APIs de Shopee/ML (~~Elo7~~ — encerrou em mai/2026) (taxas continuam como tabela configurável), múltiplos idiomas.

---

## 2. Funcionalidades (estado atual → requisitos)

O produto tem 5 módulos, hoje implementados como abas. Todos devem ser preservados.

### 2.1 Dashboard (`dash`)

- **Fase do plano de negócio**: 3 fases com metas (1 Aprendizado · Jun–Ago/2026, 2 Primeiras Vendas · 10 vendas/R$ 3.000, 3 Crescimento · 40 vendas/R$ 15.000), com barra de progresso calculada por vendas pagas. *Requisito novo: fases e metas configuráveis pelo usuário, não hardcoded.*
- **Resumo mensal** com navegação entre meses.
- **DRE do mês**: receita bruta − custo das peças − taxas de plataforma = lucro bruto; − despesas = lucro líquido + margem %.
- **Pendências**: vendas com `status = pendente`, com ação "marcar como pago".
- **Gráfico de evolução** (6 meses): receita × lucro líquido.
- **Plano vs. Realidade**: metas da fase × realizado; catálogo de modelos (Flora, Jolie, Mini Bag Lis, Duquesa, Bali) e plataformas com status derivado das vendas. *Requisito novo: catálogo de modelos gerenciável.*
- **Top modelos / Plataformas**: ranking por vendas.

### 2.2 Caderno de Projetos (`caderno`)

CRUD de projetos com: nome, tipo, status (rascunho / em andamento / concluído), data, técnica, coleção, descrição, observações, tempo estimado, **materiais** (nome, qtd, unidade, custo unitário, obs — com custo total calculado), **receita de pontos** (seções → passos ordenados), **fotos** (URL + descrição). Ações: visualizar, editar, excluir, "calcular preço" (leva o projeto à calculadora).
*Requisito novo: upload real de imagens (hoje só URL externa).*

### 2.3 Calculadora de Preço (`calc`)

- Entradas: materiais (manuais, importados do projeto ou do estoque), horas × valor/hora (mão de obra), custos fixos (embalagem, outros), plataforma (taxa %) e margem desejada (slider).
- Saídas: custo total, preço mínimo, preço sugerido, lucro estimado.
- Histórico de cálculos salvos (vinculáveis a um projeto), com exclusão individual e limpeza em lote.
- Fórmulas atuais: `custoTotal = materiais + horas·valorHora + embalagem + outros`; `preçoMínimo = custoTotal / (1−taxa)`; `preçoSugerido = custoTotal / (1−taxa−margem)`; `lucro = preçoSugerido·(1−taxa) − custoTotal`.

### 2.4 Estoque (`estoque`)

Dois tipos de item:
- **Material**: nome, categoria (ex.: fio de malha), unidade, qtd, **qtd mínima** (alerta de reposição), custo, fornecedor, última compra, obs. Ajuste rápido de quantidade (+/−).
- **Produto pronto**: nome, coleção, status (disponível/reservado/vendido), custo, preço, qtd, plataforma, projeto vinculado, foto, obs. Ação "vender" cria a transação no caixa.

### 2.5 Caixa (`caixa`)

- **Venda**: valor, data, descrição, projeto vinculado, plataforma, forma de pagamento, status (pago/pendente), custo da peça, cliente.
- **Despesa**: valor, data, descrição, categoria, forma de pagamento.
- Extrato com filtro (todos/vendas/despesas) por mês; lucro líquido por venda = `valor − custoPeça − valor·taxaPlataforma`.
- Tabela de taxas: Shopee 16% · Instagram 10% · Mercado Livre 15% · Feira/WhatsApp/Direto 0%. *Requisito novo: tabela editável pelo usuário.*

### 2.6 Requisitos não funcionais

| Requisito | Alvo |
|---|---|
| Sincronização | tempo real entre dispositivos (comportamento atual via `onSnapshot`) |
| Offline | leitura offline + fila de escrita (persistência local do Firestore) |
| Mobile | mobile-first; uso principal é no celular do ateliê (menu inferior já existe) |
| Performance | TTI < 3s em 4G; listas até ~5.000 transações sem paginação visível |
| Idioma/moeda | pt-BR, BRL (formato `R$ 1.234,56`) |
| Backup | export/import JSON de todos os dados do usuário |

---

## 3. Arquitetura proposta

### 3.1 Decisão: manter Firebase, adicionar Auth

O protótipo já usa Firestore com sync em tempo real — recurso caro de replicar com backend próprio. Para uma equipe pequena, a opção de menor risco é **evoluir o stack Firebase** em vez de migrar para backend dedicado.

| Opção | Prós | Contras | Decisão |
|---|---|---|---|
| **A. Firebase (Auth + Firestore + Storage)** | sync realtime pronto, offline grátis, zero servidor, custo ~zero no free tier | lock-in, queries limitadas | ✅ **escolhida** |
| B. Backend próprio (Node + Postgres) | controle total, SQL | precisa implementar realtime, auth, infra; +2–3 meses | ❌ prematuro |
| C. Supabase | Postgres + realtime | migração total dos dados e do modelo | ⏸ reavaliar se houver necessidade de SQL/relatórios pesados |

### 3.2 Stack

| Camada | Tecnologia | Justificativa |
|---|---|---|
| Frontend | **React 18 + TypeScript + Vite** | componentização do HTML único; tipos para o modelo de dados |
| UI | Tailwind CSS | reproduz o design atual (tema claro, rosé/dourado) com rapidez |
| Estado/servidor | TanStack Query + listeners Firestore | cache + realtime |
| Backend | **Firebase**: Auth (e-mail/senha + Google), Firestore, Storage (fotos), Hosting ou Vercel | já validado no protótipo |
| Gráficos | Recharts | substitui o gráfico de barras feito à mão em divs |
| Testes | Vitest (unit) + Playwright (e2e) + Firebase Emulator | regras de segurança testáveis |
| CI/CD | GitHub Actions → preview por PR → produção | já existe git + Vercel |

### 3.3 Estrutura do repositório

```
studio-bolsas/
├── src/
│   ├── app/                # rotas, layout (tabs), providers
│   ├── features/
│   │   ├── dashboard/      # fase, DRE, gráfico, pendências, plano
│   │   ├── projetos/       # caderno: lista, form, detalhe
│   │   ├── calculadora/
│   │   ├── estoque/
│   │   └── caixa/
│   ├── lib/                # firebase.ts, money.ts, taxas.ts, datas.ts
│   ├── domain/             # tipos + funções puras (precificação, DRE, lucro)
│   └── components/         # UI compartilhada
├── firestore.rules
├── storage.rules
└── tests/
```

**Regra de ouro:** toda lógica de negócio (precificação, DRE, lucro líquido, progresso de fase) vive em `domain/` como funções puras testáveis — hoje ela está espalhada em handlers de DOM.

---

## 4. Modelo de dados (Firestore)

Migração do modelo atual (coleções raiz globais) para dados **isolados por usuário**:

```
users/{uid}
├── profile            { nome, ateliê, criadoEm }
├── settings/config    { taxasPlataforma: {Shopee:0.16,...}, valorHoraPadrao,
│                        fases: [{nome, inicio, fim, metaVendas, metaReceita}],
│                        modelos: [{nome, desc}] }
├── projetos/{id}      { nome, tipo, status: 'rascunho'|'em-andamento'|'concluido',
│                        dataIso, tecnica, colecao, descricao, obs, tempo,
│                        materiais: [{nome, qtd, und, custoUnit, obs}],
│                        custoMateriais,            // derivado, denormalizado
│                        secoes: [{titulo, passos: [string]}],
│                        fotos: [{storagePath|url, desc}],
│                        created_at, updated_at }
├── historico/{id}     { nome, projetoId?, projetoNome?, precoNum, custoNum,
│                        lucroNum, breakdown: {materiais, mdo, fixos, taxa, margem},
│                        created_at }
├── transacoes/{id}    { tipo: 'venda'|'despesa', valor, dataIso, descricao, obs,
│                        projetoId?, projetoNome?,
│                        // venda:
│                        plataforma, formaPagamento, status: 'pago'|'pendente',
│                        custoPeca, cliente,
│                        // despesa:
│                        categoria,
│                        created_at }
└── estoque/{id}       { tipo: 'material'|'produto', nome, qty, custo, obs,
│                        // material: categoria, und, qtyMin, fornecedor, ultimaCompra
│                        // produto: colecao, status, preco, plataforma, projetoId, foto
│                        created_at }
```

Notas:
- `historico` passa a guardar **números + breakdown** (hoje guarda strings formatadas `"R$ 120,00"`, o que impede relatórios).
- `projetoNome`/`plataforma` continuam denormalizados (padrão Firestore para evitar joins); atualização em cascata não é necessária — snapshot do momento da venda é o comportamento desejado.
- Índices compostos: `transacoes(tipo, status, dataIso)`, `estoque(tipo, nome)`.

### 4.1 Regras de segurança (essência)

```
match /users/{uid}/{collection}/{doc} {
  allow read, write: if request.auth != null && request.auth.uid == uid;
}
```
Validações adicionais nas rules: `valor >= 0`, `tipo in [...]`, tamanho máximo de arrays. Storage: fotos somente em `users/{uid}/fotos/**`, máx. 5 MB, content-type imagem.

---

## 5. Lógica de negócio (contratos)

Funções puras em `domain/` (assinaturas TypeScript):

```ts
// precificação
calcularPreco(input: {materiais: Material[]; horas: number; valorHora: number;
  custosFixos: number; taxaPlataforma: number; margem: number}): {
  custoTotal: number; precoMinimo: number; precoSugerido: number; lucro: number}
// precoMinimo  = custoTotal / (1 - taxa)
// precoSugerido = custoTotal / (1 - taxa - margem)   // margem sobre o preço de venda

// financeiro
lucroLiquidoVenda(t: Venda, taxas: TabelaTaxas): number   // valor − custoPeca − valor·taxa
calcularDRE(transacoes: Transacao[], mes: number, ano: number, taxas: TabelaTaxas): DRE
serieEvolucao(transacoes: Transacao[], meses: number): PontoGrafico[]

// plano
faseAtual(fases: Fase[], hoje: Date): Fase
progressoFase(fase: Fase, vendasPagas: Venda[], projetos: Projeto[]): {pct: number; label: string}
```

Cada função recebe a tabela de taxas como parâmetro (vinda de `settings/config`) — nunca hardcoded.

---

## 6. Migração do protótipo

1. **Congelar** o protótipo atual (tag `v1-prototipo`).
2. Script one-shot (Admin SDK) que copia `projetos|historico|transacoes|estoque` da raiz para `users/{uid-da-lisandra}/...`, convertendo strings monetárias do `historico` para números.
3. Importar também os dados legados de `localStorage` (`bolsas_projetos`, `bolsas_historico` dos HTMLs antigos `caderno_projetos.html` / `calculadora_preco.html`) via tela de import JSON, se ainda relevantes.
4. Ativar as security rules **somente após** a migração (hoje precisam estar abertas para o protótipo funcionar).
5. **Rotacionar a chave/API do Firebase** e restringir domínios autorizados — a config atual está pública no HTML.

---

## 7. Roadmap

| Fase | Entrega | Estimativa |
|---|---|---|
| **M1 — Fundação** | Setup React+TS+Vite, Firebase Auth (login), regras de segurança, migração de dados, `domain/` com testes | 2–3 semanas |
| **M2 — Paridade** | Reimplementar os 5 módulos com paridade total ao protótipo; deploy substituindo o atual | 3–4 semanas |
| **M3 — Melhorias** | Upload de fotos (Storage), taxas/fases/modelos configuráveis, export/import JSON, PWA + offline | 2–3 semanas |
| **M4 — Polimento** | Relatórios (DRE anual, ranking de modelos), paginação do extrato, e2e Playwright, monitoramento de erros (Sentry) | 2 semanas |

**Critério de aceite do M2:** usuária realiza o fluxo completo (criar projeto → calcular preço → cadastrar produto no estoque → vender → ver DRE) sem regressão em relação ao protótipo, agora logada e com dados privados.

---

## 8. Riscos

| Risco | Impacto | Mitigação |
|---|---|---|
| Banco aberto no protótipo enquanto M1 não sai | perda/vazamento de dados | priorizar rules + auth; backup JSON manual imediato |
| Histórico com valores em string | quebra relatórios | conversão na migração (item 6.2) |
| Custos Firebase ao crescer | financeiro | free tier cobre 1 ateliê com folga; monitorar leituras (dashboards re-renderizam em todo snapshot — debounce) |
| Fotos por URL externa quebram | UX | M3: Storage próprio com redimensionamento |

---

## Apêndice A — Inventário do protótipo

| Arquivo | Papel | Destino |
|---|---|---|
| `index.html` (1.320 linhas) | app principal v1.2: 5 abas, Firestore realtime | substituído pelo app React (referência de UX) |
| `calculadora_preco.html` | v1 standalone (localStorage `bolsas_historico`) | aposentar; importar dados |
| `caderno_projetos.html` | v1 standalone (localStorage `bolsas_projetos`) | aposentar; importar dados |
| `Plano_Negocio_Bolsas_Artesanais.docx` | plano de negócio (fonte das fases/metas/modelos) | fonte para defaults de `settings/config` |
