# Amostras de Ponto — Design

> Spec de feature pro Studio Bolsas (app de gestão de ateliê, single-file `index.html` + Firebase). Data: 2026-06-17. App em v2.14. Aprovado por Alessandro (relaying pedido da Lisandra).

## Problema
A Lisandra testa **pontos novos**: faz uma sequência, registra, bate uma foto, e decide se vai usar aquele ponto em alguma peça (bolsa, blusão, cachecol…). Hoje não há lugar pra isso — vira projeto bagunçado misturado com as peças reais. Ela também quer estimar: "se eu fizer o blusão com esse ponto, quanto custa o material? e com outro ponto?".

## Solução (resumo)
Uma **amostra de ponto** é um item do caderno de Projetos (mesma coleção `projetos`), distinguido por uma flag, com um campo de **decisão** próprio. Reaproveita a receita-de-pontos, fotos e materiais que o projeto já tem. Um botão **"Criar projeto a partir desta amostra"** leva sequência + materiais pro caderno, onde a **calculadora existente** estima o custo. Sem motor de simulação novo.

## Modelo de dados (coleção `projetos`)
Dois campos novos, o resto reusado:
- `amostra: true` — discriminador. Projetos existentes não têm o campo → tratados como peça (falsy). **Sem migração.**
- `decisao: 'testando' | 'aprovado' | 'descartado'` — só em amostras; default `'testando'`. Substitui o `status` (rascunho/em-andamento/concluído), que não é usado em amostra.
- **Reusados:** `nome` (= nome do ponto), `secoes` (= a sequência do ponto), `fotos`, `materiais` (o fio testado), `tecnica`, `tipo` (= "onde cabe": bolsa/blusão/cachecol…), `obs`, `created_at`/`updated_at`.
- Não usados em amostra (escondidos no form): `colecao`, `tempo`, e o `status`.

## UI

### Lista de Projetos (`renderLista`)
- Seletor de segmento no topo: **Peças** (padrão, `!p.amostra`) | **Amostras** (`p.amostra`). Estado em var `_projFiltro` (`'pecas'`|`'amostras'`).
- Card de amostra: foto (se houver) + selo de **decisão** no lugar do status — 🧪 Testando (âmbar) · 👍 Aprovado (verde) · 👎 Descartado (cinza). Reusa as classes de tag existentes (`.tag`, cores `--green-l`/`#fff3cd`/`#f0f0f0`).
- Botão de criar respeita o segmento ativo: na aba Amostras, **"+ Nova amostra"**; na aba Peças, **"+ Novo projeto"**.

### Formulário (`mostrarForm(id, isAmostra)`)
Mesmo DOM do caderno, adaptado por `isAmostra` (no create vem do segmento; no edit vem de `p.amostra`):
- Título: "Nova amostra de ponto" / "Editar amostra" vs "Novo projeto".
- Rótulo de `f-n` → "Nome do ponto".
- Mostra um seletor de **decisão** (Testando/Aprovado/Descartado) e esconde o seletor de `status`, `colecao` e `tempo`.
- Rótulo de `tipo` (`f-t`) → "Onde cabe (bolsa, blusão, cachecol…)".
- Mantém: técnica, **materiais** (o fio testado — sub-form `_mf` já existe, com vínculo ao estoque), **receita de pontos** (seções/passos `_sf` = a sequência), **fotos** (`_ff`).
- Novo elemento no HTML: um `<select id="f-decisao">` com as 3 opções, exibido só quando amostra.

### Salvar (`salvarProj`)
- Inclui `amostra:true` + `decisao` (lido de `f-decisao`) quando é amostra; senão grava como hoje (sem `amostra`, com `status`).

### Detalhe (`verProj`)
- Amostra mostra: selo de decisão, a sequência (receita), fotos, materiais, obs.
- Botões da amostra: **Editar** · **▶ Trabalhar** (reusa `abrirAtelie` — serve pra seguir/testar o ponto) · **🧶 Criar projeto a partir desta amostra**. (Esconde Calcular/Conferir/Produzir, que são de peça.)

## "Criar projeto a partir desta amostra" (`criarProjetoDeAmostra(id)`)
- Pré-preenche o **formulário de NOVO projeto** (não cria doc descartável) com dados copiados da amostra:
  - `_sf` ← cópia da sequência (`secoes`) da amostra.
  - `_mf` ← cópia dos materiais da amostra (pra calculadora ter de onde partir).
  - técnica ← a da amostra; nome sugerido ← `"${tipo||'Peça'} — ${nome do ponto}"` (editável).
  - `amostra` = false (é peça), status 'rascunho'.
- Abre o form de peça pré-preenchido; a Lisandra **ajusta as quantidades** pro tamanho real (cachecol usa pouco, blusão usa muito) e salva. Daí usa **Calcular** (fluxo existente `calcProj`/`importarDoProjeto` → calculadora) pra ver o custo.
- ⚠️ Detalhe de implementação: `mostrarForm(null,false)` **reseta** `_mf`/`_sf`/`_ff`. Então `criarProjetoDeAmostra` deve **popular `_mf`/`_sf`/`_ff` (e o nome) DEPOIS de chamar `mostrarForm`** e re-renderizar (`renderMF`/`renderSF`/`renderFF`) — ou passar um objeto de prefill pro `mostrarForm` aplicar após o reset. Não setar antes (seria sobrescrito).
- Comparar ponto A × B = criar 2 rascunhos a partir de 2 amostras e comparar os preços salvos no histórico.

## Fora de escopo (YAGNI)
- Simulador dedicado com escala automática por tipo de peça.
- Link de rastreabilidade amostra→projetos criados.
- Filtro por decisão dentro de Amostras (pode entrar depois; v1 mostra todas com o selo).

## Compatibilidade / migração
Nenhuma. Projetos existentes (sem `amostra`) continuam como peças. Backups (export/import JSON) carregam o campo novo naturalmente.

## Validação (sem suíte automatizada; app single-file)
- `node --check` no JS extraído + sem funções duplicadas (gate do projeto).
- Smoke manual (em produção, conforme decisão do Alessandro de não usar localhost): criar amostra → aparece na aba Amostras com o selo → editar decisão → "criar projeto a partir da amostra" → materiais e sequência vieram → Calcular dá custo.

## Release
- Bump badge `v2.15` no `index.html` + regenerar `Manual_Studio_Bolsas.pdf` (nova subseção "Amostras de ponto" em Projetos) + `.vercelignore` mantém docs fora do ar.
