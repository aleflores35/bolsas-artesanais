# Studio Bolsas — contexto do projeto

App de gestão para o ateliê de bolsas artesanais da Lisandra. Aplicativo web de página única (single-file HTML/CSS/JS) com backend Firebase. **Versão atual: v2.12.**

## Negócio (duas trilhas)
Em `_Negocio/` há duas frentes que devem ser mantidas separadas:
- **Ateliê da Lisandra** — uso real do ateliê (receitas, custos, produção).
- **SaaS vendável** — versão genérica do app para vender a outros ateliês.

## Stack e arquivos principais
- `index.html` — **o app inteiro** (HTML + CSS + JS num arquivo só, ~2700 linhas). Firebase compat SDK 10.12.2 (app, auth, firestore). O badge de versão fica no header (procure `v2.NN</span>`, ~linha 279).
- `loja.html` — vitrine/loja pública.
- `gera_manual.py` — gera o `Manual_Studio_Bolsas.pdf`.
- `firestore.rules` — regras de segurança do Firestore.
- `_Negocio/Atelie-Lisandra/Receitas-de-Bolsas/` — receitas (`.md` + `.studio-bolsas.json`), `Indice-Receitas.xlsx`, `Lista-Compras-por-Bolsa.xlsx`.

## Dados (Firestore)
Por usuário: `users/{uid}/` com coleções `projetos`, `historico`, `transacoes`, `estoque`; config em `settings/config` (objeto `CFG`: `taxas`, `fases`, `modelos`, `categorias`, `whats`, `gkey`).

## Módulos do app (abas)
Painel (`dash`), Projetos (`caderno`), Preço (`calc`), Estoque, Caixa, Ajustes (`config`).

### Estoque (área mais complexa)
Materiais e produtos prontos. Recursos: **conta de chegada** (comprei por unidade, estoco/gasto em grama → calcula estoque em g e custo por grama), **rótulos dinâmicos** quando a unidade é "g", **categoria "Outros"** dinâmica (salva em `CFG.categorias`), filtros/ordenação, lançar compra no caixa, importar cupom de e-commerce, baixa automática na produção.

## Convenções e regras (importantes)
1. **Versionamento:** toda release faz bump do badge em `index.html` (`v2.NN`). Mensagem de commit no formato `vX.Y: descrição`.
2. **Manual sempre atualizado:** toda feature nova deve atualizar o `Manual_Studio_Bolsas.pdf` rodando `gera_manual.py`.
3. **Receita nova:** gerar o JSON do app (`<Nome>.studio-bolsas.json`) + atualizar `Indice-Receitas.xlsx` + sincronizar a pasta.
4. **Encoding:** sempre UTF-8. Cuidado com mojibake de dupla codificação (ex.: "produÃ§Ã£o" no lugar de "produção") — já ocorreu em edições anteriores.
5. **Validar antes de salvar:** o JS do `index.html` deve passar em `node --check` (extrair o `<script>` inline). Conferir que funções não ficaram duplicadas.

## Git
Remoto: `github.com/aleflores35/bolsas-artesanais`, branch `master`.

## ⚠️ OneDrive (se a pasta ainda estiver sincronizada)
Se o projeto estiver dentro do OneDrive, o sync pode servir cópias **truncadas/desatualizadas** dos arquivos e corromper o índice do `.git`. **Recomendado mover o repositório para fora do OneDrive** (ex.: `C:\obralivre\...`). Se um `git status` acusar `index file corrupt`, conserte com: `del .git\index` e depois `git reset`.
