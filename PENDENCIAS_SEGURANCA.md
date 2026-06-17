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

## ✅ Resolvido 17/06 (parte 2) — regras do Firestore PUBLICADAS
O `firestore.rules` (com o fix da vitrine) foi **publicado em produção** via Firebase CLI: `firebase deploy --only firestore:rules --project bolsas-lisandra` (config `firebase.json` + `.firebaserc` no repo). loja.html segue 200 (vitrine pública intacta). **Daqui pra frente, mudou regra → `firebase deploy --only firestore:rules`** (CLI já logado nesta máquina).

---

## ⚠️ PENDENTE (opcional — hardening de console, não trava nada)

### 1. (Opcional — hardening) Restringir a API key + domínios autorizados
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
