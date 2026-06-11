# Studio Bolsas v2.0 — Como ativar (passo a passo)

A nova versão tem **login por usuário, dados privados, modo offline, taxas/fases/modelos configuráveis e backup**. Para tudo funcionar, faça estes passos no [console do Firebase](https://console.firebase.google.com) (projeto **bolsas-lisandra**), **nesta ordem**:

## 1. Habilitar os métodos de login
Authentication → Sign-in method → habilite:
- **E-mail/senha**
- **Google** (informe um e-mail de suporte quando pedir)

## 2. Autorizar o domínio do site
Authentication → Settings → **Authorized domains** → adicione o domínio do app no Vercel (ex.: `bolsas-artesanais.vercel.app`). Sem isso o login com Google não abre.

## 3. Publicar o app e migrar os dados
1. Faça o deploy (git push → Vercel, como sempre).
2. Abra o app e **crie a sua conta** (ou entre com Google).
3. O app vai detectar os dados da versão antiga e perguntar se quer **importar para a sua conta** — confirme. ✅

## 4. Ativar as regras de segurança (SÓ DEPOIS da migração!)
Firestore Database → **Rules** → apague o conteúdo e cole o arquivo `firestore.rules` desta pasta → **Publish**.

A partir daí, só usuários logados acessam os próprios dados; as coleções antigas ficam bloqueadas.

## 5. Criar as contas (admin e Lis)
As contas nascem no **primeiro login** — não precisa criar nada no console:
1. **alessandro.flores16@gmail.com** (admin): abra o app e toque **Entrar com Google** com essa conta. ⚠️ O admin PRECISA entrar com Google (e-mail verificado) — senão os poderes de admin não valem nas regras.
2. **lis01sperb@gmail.com**: mesma coisa, Entrar com Google no aparelho dela.

Depois disso, em **⚙️ Ajustes → Conta**, o admin ganha o seletor **"👑 Gerenciar a conta de"** para ver e editar os dados da Lis (um aviso 👁 aparece no topo enquanto estiver na conta dela). Para mudar o e-mail do admin, edite `ADMIN_EMAILS` no `index.html` **e** a lista no `firestore.rules`.

## 6. Conferir
- Entrar/sair funciona; cada conta vê só os próprios dados.
- Aba **⚙️ Ajustes**: edite taxas, fases e modelos → Salvar.
- **Backup**: exporte o JSON e guarde em local seguro (faça isso já!).
- Modo avião: o app abre com os dados e sincroniza ao voltar a rede.

> Dica: se o login com Google falhar com "popup", verifique o passo 2. Se e-mail/senha der "método não habilitado", verifique o passo 1.
