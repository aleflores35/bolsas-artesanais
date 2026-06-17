# Auditoria UX/UI — Studio Bolsas (16/06/2026)

> Revisão de 5 dimensões em paralelo + cruzamento com o CSS. Filtro: **Lisandra — artesã, não-técnica, usa no celular, luz variável do ateliê.** Achados de CSS verificados no código.

## 🔴 Atrapalha o uso (todo dia)

| Tema | Problema (confirmado) | Por que dói | Fix |
|---|---|---|---|
| **Contraste fraco** | Labels `#888` (~3.5:1), datas/metadados `#aaa` (~2.4:1), ícones editar/excluir `.bd/.bds #ccc` (~1.6:1), `.bhd #ddd` (~1.3:1) sobre creme | Botão de apagar e rótulos somem no sol; falham WCAG AA | Labels→`#555`, metadados→`#666`, ícones→`#666/#777` |
| **Tap targets** | +/− estoque **28×28px**, ✕ modal, voltar `‹` (`padding:0`), 4 botões do produto grudados (`gap:6px`) incl. 🗑️ | Dedo erra; deleta venda/produto sem querer (sem desfazer) | Mínimo **44×44px**; afastar/realocar o 🗑️ |
| **Tabelas no mobile** | Grades de 6 colunas (materiais calc/produção, DRE, resumo 6 meses) não colapsam; `.d4` fica 2 col em 320px | Valores cortados nas telas de dinheiro | Card empilhado no mobile; `.d4`→1 col <380px |
| **Dinheiro `type=number`** | `c-val`, `em-c`, `ep-p`… | iOS sem vírgula no teclado → não digita "89,90" | `type="text" inputmode="decimal"` (replace já existe) |
| **Troca de aba apaga form** | `aba()` troca view sem checar form aberto | Cadastrando bolsa longa, toca em outra aba → perde tudo | Confirmar antes / rascunho em localStorage |
| **Toast atrás da barra** | `.toast{bottom:24px}` × nav ~64px | Não vê o "✓ Salvo" | `bottom:80px` + `env(safe-area-inset-bottom)` |

## 🟠 Atrito / adoção
- **Sem onboarding / estados vazios mudos**: banco zerado sem guia; "Nenhum X" sem CTA. → card "Por onde começar" + CTA em cada vazio.
- **`prompt()`/`confirm()` nativos + microcopy técnica**: importar do estoque (calc) e **balança/pesar-sobra usam `prompt()`**; "Excluir?" sem nome; **"❌ Erro." genérico (~12×)**; jargão "DRE", "conta de chegada", "lucro bruto". → usar o modal de "conta de chegada" como padrão; nomear o que apaga; traduzir erros (offline×falha); renomear "conta de chegada"→"Calcular gramas e custo".
- **Ações-chave escondidas**: "Produzir" mora no Estoque; "Conferir materiais" entre 6 botões. → Produzir/Trabalhar primários no projeto.
- **Status só por cor**: pago/pendente, estoque ok/baixo/zerado só por cor; badge texto em **10px**. → manter texto/ícone + subir pra 12-13px.

## 🟡 Polish / marca / manutenção
- **Design system inchado**: 13 classes de botão + estilos inline; 4 cores de "ação primária" no Painel. → ~4 botões semânticos, 1 primário por tela.
- **Vitrine `loja.html` genérica**: header pequeno, sem-foto = emoji. → header maior em Playfair, placeholder estilizado. (Obs: loja.html já é seguro p/ XSS.)
- **Acessibilidade fina**: faltam `aria-label` em botões só-ícone (‹ ▶ 🌙 ⚖️), `for/id` nos labels, `role=tablist`, foco de teclado mais visível.
- **Microcopy**: toast 2,5s curto; voz inconsistente; 💰 em "Preço" e 💵 em "Caixa" (dois ícones de dinheiro).

## ✅ Pontos fortes (não mexer)
Paleta rosé/dourado certa; **Modo Ateliê** (cronômetro + carreiras + dark) = diferencial real; erro de login com caso "popup bloqueado no WhatsApp → abra no Chrome"; revisão antes de salvar no import de cupom; foco dourado nos inputs.

## Como atacar (decisão pendente)
- **Lote UX rápido (CSS, baixo risco):** contraste, tap targets ≥44px, `inputmode=decimal`, tabelas/`.d4` no mobile, toast acima da barra, badges 10→12px. Faz na branch, valida `node --check`.
- **Lote estrutural:** onboarding + estados vazios, trocar `prompt()` por modal (inclui o pesar-sobra novo), guarda "sair sem salvar", realocar Produzir/Conferir, vitrine luxo.
