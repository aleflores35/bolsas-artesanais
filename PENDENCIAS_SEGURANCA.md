# Pendências de segurança / configuração — Studio Bolsas

> Ações que **não sobem com o código** (moram em console externo) ou que dependem de decisão.
> Atualizado em 17/06/2026 (app em v2.14, live em project-anmtx.vercel.app).
> Quando formos "usar de verdade" (abrir pra mais clientes / SaaS), revisar esta lista.

---

## ✅ Resolvido nesta rodada (17/06)

**Arquivos internos estavam públicos no Vercel.** O deploy servia a **raiz inteira do repo**, então qualquer um acessava em `project-anmtx.vercel.app/<arquivo>`:
- `_Negocio/...` → **planos de negócio, precificação, modelos** (estratégico!)
- `firestore.rules`, `gera_manual.py`, `CLAUDE.md`, `Manual_Studio_Bolsas.pdf`, `seed.html`

**Correção aplicada:** criado `.vercelignore` — só `index.html` + `loja.html` vão pro ar. Conferir que os paths acima retornam **404** após o deploy. ⚠️ **Não remover o `.vercelignore`** sem motivo (volta a expor tudo).

---

## ⚠️ PENDENTE — só o Alessandro consegue fazer (é no CONSOLE, não no código)

### 1. Publicar as regras do Firestore (`firestore.rules`)
- **O quê:** o arquivo `firestore.rules` foi atualizado (fecha a brecha de um usuário logado **sobrescrever a vitrine pública de outro**). Mas as regras do Firebase moram **dentro do console**, não no deploy do Vercel. **Mudar o arquivo no repo NÃO ativa** — tem que colar e publicar.
- **Quando importa:** risco baixo hoje (app é só você + Lisandra). Importa de verdade **se virar SaaS multi-cliente**.
- **Como (30s):** console.firebase.google.com → projeto **bolsas-lisandra** → **Firestore Database** → aba **Rules** → apagar o conteúdo → colar o conteúdo do arquivo `firestore.rules` (está no repo) → **Publish**.

### 2. (Opcional — hardening) Restringir a API key + domínios autorizados
- A config Firebase no `index.html` é pública (isso é normal no Firebase web, não é segredo). Mas vale confirmar:
  - **Google Cloud Console** → Credentials → restringir a API key ao domínio de produção (`project-anmtx.vercel.app` / domínio próprio) + `localhost`.
  - **Firebase Auth** → Settings → **Authorized domains** → deixar só os domínios certos.
- **Por quê:** impede alguém de hospedar um clone usando a mesma key.

### 3. (Opcional) Chave do Gemini (`gkey`)
- A chave do Google AI Studio (botão "✨ Premium" das fotos) é salva em **texto puro** no Firestore. Visível pro admin; se a conta admin vazar, a chave vaza.
- **Mitigação:** restringir a chave por **referrer HTTP** no Google Cloud, ou não guardar no banco. Só relevante em caso de comprometimento da conta admin.

---

## 📌 Regras permanentes (não esquecer a cada release)
- **Bumpar o badge de versão** no `index.html` (`v2.NN`).
- **Regenerar o PDF** do manual: `python gera_manual.py` (já é cross-platform — roda no Windows com fallback de fontes).
- **Manter o `.vercelignore`** — é o que mantém docs/ferramentas fora do ar.
