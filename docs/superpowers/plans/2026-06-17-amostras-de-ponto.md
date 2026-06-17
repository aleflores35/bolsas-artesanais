# Amostras de Ponto — Plano de Implementação

> **Para quem executa:** SUB-SKILL: usar `superpowers:executing-plans` (inline) para implementar tarefa a tarefa. Passos usam checkbox `- [ ]`.

**Goal:** Permitir registrar "amostras de ponto" no caderno de Projetos (sequência + foto + decisão) e gerar um projeto a partir delas pra estimar custo.

**Architecture:** App single-file (`index.html`, HTML+CSS+JS inline, Firebase compat). Amostra = doc na coleção `projetos` com flag `amostra:true` + campo `decisao`; reusa form/lista/detalhe do caderno com ajustes condicionais. Sem coleção nova, sem migração.

**Tech Stack:** HTML/CSS/JS vanilla, Firebase Firestore (compat 10.12.2), reportlab (manual).

## Global Constraints
- Sem suíte automatizada. Validação de cada tarefa = **extrair o JS inline e rodar `node --check`** (helper `C:\tmp\check_bolsas.js` já existe: `node C:\tmp\check_bolsas.js` → gera `C:\tmp\bolsas_inline.js`; depois `node --check C:\tmp\bolsas_inline.js`) + **zero funções duplicadas**.
- UTF-8 sempre; cuidado com mojibake.
- Toda interpolação de dado do usuário em `innerHTML` usa `esc()`.
- Deploy = `git push origin master` → Vercel (project-anmtx.vercel.app). `.vercelignore` mantém docs fora do ar — não mexer.
- Release: bump badge `v2.15` no header do `index.html` + regenerar `Manual_Studio_Bolsas.pdf` (`python gera_manual.py`, já cross-platform).
- Arquivo único alvo: `C:\obralivre\clientes\parcerias\bolsas-artesanais\index.html` (+ `gera_manual.py` na Task 4).
- Trabalhar em branch `feat/amostras-de-ponto`, merge FF → master, push.

---

### Task 1: Filtro Peças|Amostras na lista + helpers

**Files:**
- Modify: `index.html` — HTML da lista (~473-477), `renderLista` (~1500-1519), declarações de estado do caderno, novas funções `setProjFiltro`/`decisaoSelo`.

**Interfaces:**
- Produz: `_projFiltro` (global `'pecas'|'amostras'`), `setProjFiltro(f)`, `decisaoSelo(d)→string HTML`. `renderLista` passa a filtrar por `_projFiltro` e usar `decisaoSelo` p/ amostras.

- [ ] **Passo 1: Adicionar estado global.** Perto das outras vars do caderno (onde está `let _eid`, buscar `let _eid`), adicionar na mesma linha/bloco:
```js
let _projFiltro='pecas',_formAmostra=false;
```

- [ ] **Passo 2: HTML — segmento + botão dinâmico.** Substituir o bloco da lista (linhas ~473-476):
```html
      <div style="display:flex;gap:8px;margin-bottom:.75rem">
        <button class="fb active" id="seg-pecas" onclick="setProjFiltro('pecas')">👜 Peças</button>
        <button class="fb" id="seg-amostras" onclick="setProjFiltro('amostras')">🧪 Amostras</button>
      </div>
      <div style="display:flex;gap:8px;margin-bottom:1rem">
        <div class="sb" style="flex:1;margin:0"><span>🔍</span><input type="text" id="busca" placeholder="Buscar…" oninput="renderLista()"></div>
        <button class="bg" id="btn-novo" onclick="mostrarForm(null)">+ Novo</button>
      </div>
```

- [ ] **Passo 3: `setProjFiltro` + `decisaoSelo`.** Adicionar logo após `function voltarLista(){sv('lista');}` (~1499):
```js
function setProjFiltro(f){_projFiltro=f;
  const sp=document.getElementById('seg-pecas'),sa=document.getElementById('seg-amostras'),b=document.getElementById('btn-novo');
  if(sp)sp.classList.toggle('active',f==='pecas');
  if(sa)sa.classList.toggle('active',f==='amostras');
  if(b)b.textContent=f==='amostras'?'+ Amostra':'+ Novo';
  renderLista();
}
function decisaoSelo(d){
  if(d==='aprovado')return '<span class="tag" style="background:var(--green-l);color:var(--green)">👍 Aprovado</span>';
  if(d==='descartado')return '<span class="tag" style="background:#f0f0f0;color:#888">👎 Descartado</span>';
  return '<span class="tag" style="background:#fff3cd;color:#856404">🧪 Testando</span>';
}
```

- [ ] **Passo 4: Reescrever `renderLista`** (filtra por `_projFiltro`, selo de decisão p/ amostra, e aplica `esc()` — que faltava nos campos do card):
```js
function renderLista(){
  const busca=(document.getElementById('busca')?.value||'').toLowerCase();
  const amo=_projFiltro==='amostras';
  const pl=_P.filter(p=>(!!p.amostra===amo)&&(!busca||[p.nome,p.tipo,p.tecnica,p.colecao].some(x=>(x||'').toLowerCase().includes(busca))));
  const el=document.getElementById('lista-proj');if(!el)return;
  if(!pl.length){el.innerHTML=`<div class="es"><div class="ic">${amo?'🧪':'📓'}</div><p>${amo?'Nenhuma amostra de ponto ainda. Registre um ponto novo que você testou.':'Nenhum projeto ainda.'}</p></div>`;return;}
  el.innerHTML=pl.map(p=>{
    const pid=p.id||p._id;
    const selo=p.amostra?decisaoSelo(p.decisao):`<span class="tag ts-${p.status||'rascunho'}">${sLabel(p.status)}</span>`;
    const pv=_H.filter(h=>h.projetoId===pid);const up=pv[0];
    return `<div class="pc" onclick="verProj('${pid}')">
      <div class="pci">
        <div class="pi"><h3>${esc(p.nome)}</h3><div class="meta">${p.data||''} ${p.tecnica?'· '+esc(p.tecnica):''} ${p.colecao?'· 🎨 '+esc(p.colecao):''}</div>
          <div class="tags">${p.tipo?`<span class="tag tt1">${esc(p.tipo)}</span>`:''}${selo}${(!p.amostra&&up)?`<span class="tag tg">💰 ${esc(up.preco)}</span>`:''}</div>
        </div>
        <div class="pca" onclick="event.stopPropagation()">
          <button class="bi" onclick="mostrarForm('${pid}')">✏️</button>
          <button class="bi" onclick="delProj('${pid}')">🗑️</button>
        </div>
      </div>
    </div>`;
  }).join('');
}
```

- [ ] **Passo 5: Validar.** `node C:\tmp\check_bolsas.js` depois `node --check C:\tmp\bolsas_inline.js` → SINTAXE OK, 0 duplicadas.
- [ ] **Passo 6: Commit.** `git add index.html && git commit -F` com msg "feat(amostras): filtro Peças|Amostras na lista + selo de decisão".

---

### Task 2: Formulário adapta para amostra + salvar

**Files:**
- Modify: `index.html` — HTML do form (status ~487, coleção ~493, tempo ~520, labels nome ~484 e tipo ~486, título receita ~509), `mostrarForm` (~1520-1528), `salvarProj` (~1587).

**Interfaces:**
- Consome: `_projFiltro`, `_formAmostra` (Task 1). Produz: form com `#f-decisao`; `mostrarForm(id, isAmostra)`; `salvarProj` grava `amostra`/`decisao`.

- [ ] **Passo 1: HTML — campo decisão + ids p/ esconder.** Trocar a linha do Status (~487) por (status + decisão lado a lado, um escondido):
```html
          <div class="fg" id="fg-status"><label>Status</label><select id="f-s"><option value="rascunho">Rascunho</option><option value="em-andamento">Em andamento</option><option value="concluido">Concluído</option></select></div>
          <div class="fg" id="fg-decisao" style="display:none"><label>Decisão</label><select id="f-decisao"><option value="testando">🧪 Testando</option><option value="aprovado">👍 Aprovado (vou usar)</option><option value="descartado">👎 Descartado</option></select></div>
```

- [ ] **Passo 2: HTML — ids p/ rótulos e blocos que somem na amostra.**
  - Nome (~484): `<label>Nome *</label>` → `<label id="lbl-nome">Nome *</label>`
  - Tipo (~486): `<label>Tipo</label>` → `<label id="lbl-tipo">Tipo</label>`
  - Coleção (~493): a `<div class="fr s">` da coleção → adicionar `id="fr-colecao"`: `<div class="fr s" id="fr-colecao">`
  - Tempo (~520): a `<div class="fg" style="margin-top:10px">` do tempo → `id="fg-tempo"`: `<div class="fg" id="fg-tempo" style="margin-top:10px">`
  - Título receita (~509): `<h2>🪡 Receita de pontos</h2>` → `<h2 id="tit-receita">🪡 Receita de pontos</h2>`

- [ ] **Passo 3: Reescrever `mostrarForm`** para receber `isAmostra` e adaptar:
```js
function mostrarForm(id,isAmostra){
  _eid=id;_mf=[];_sf=[];_ff=[];_lf=[];
  const amo = id ? !!(_P.find(x=>(x.id||x._id)===id)?.amostra) : (isAmostra!==undefined?isAmostra:(_projFiltro==='amostras'));
  _formAmostra=amo;
  document.getElementById('form-tit').textContent=id?(amo?'Editar amostra':'Editar projeto'):(amo?'Nova amostra de ponto':'Novo projeto');
  document.getElementById('lbl-nome').textContent=amo?'Nome do ponto *':'Nome *';
  document.getElementById('lbl-tipo').textContent=amo?'Onde cabe (bolsa, blusão…)':'Tipo';
  document.getElementById('fg-status').style.display=amo?'none':'';
  document.getElementById('fg-decisao').style.display=amo?'':'none';
  document.getElementById('fr-colecao').style.display=amo?'none':'';
  document.getElementById('fg-tempo').style.display=amo?'none':'';
  document.getElementById('tit-receita').textContent=amo?'🪡 Sequência do ponto':'🪡 Receita de pontos';
  if(id){const p=_P.find(x=>(x.id||x._id)===id);if(p){
    document.getElementById('f-n').value=p.nome||'';document.getElementById('f-t').value=p.tipo||'Clutch';document.getElementById('f-s').value=p.status||'rascunho';document.getElementById('f-decisao').value=p.decisao||'testando';document.getElementById('f-d').value=p.dataIso||'';document.getElementById('f-tc').value=p.tecnica||'';document.getElementById('f-col').value=p.colecao||'';document.getElementById('f-desc').value=p.descricao||'';document.getElementById('f-obs').value=p.obs||'';document.getElementById('f-tmp').value=p.tempo||'';
    _mf=(p.materiais?JSON.parse(JSON.stringify(p.materiais)):[]).map(m=>({nome:m.nome||'',qtd:parseFloat(m.qtd)||0,und:m.und||'un',custoUnit:parseFloat(m.custoUnit)||0,estoqueId:m.estoqueId||null,obs:m.obs||''}));_sf=p.secoes?JSON.parse(JSON.stringify(p.secoes)):[];_ff=p.fotos?JSON.parse(JSON.stringify(p.fotos)):[];_lf=p.links?JSON.parse(JSON.stringify(p.links)):[];
  }}else{['f-n','f-tc','f-desc','f-obs','f-tmp','f-col'].forEach(i=>document.getElementById(i).value='');document.getElementById('f-t').value='Clutch';document.getElementById('f-s').value='rascunho';document.getElementById('f-decisao').value='testando';document.getElementById('f-d').value=new Date().toISOString().split('T')[0];addMatF();addSec();addFot();if(!amo)addMatF();}
  renderMF();renderSF();renderFF();renderLF();sv('form');
}
```

- [ ] **Passo 4: `salvarProj` grava amostra/decisao.** Logo após a linha que monta `const proj={...}` (~1587) e antes do `try{`, inserir:
```js
  if(_formAmostra){proj.amostra=true;proj.decisao=document.getElementById('f-decisao').value||'testando';}
```

- [ ] **Passo 5: Validar** (`node --check` como Task 1, passo 5).
- [ ] **Passo 6: Commit** — "feat(amostras): form adapta (decisão, rótulos) + salva amostra/decisao".

---

### Task 3: Detalhe da amostra + "Criar projeto a partir desta amostra"

**Files:**
- Modify: `index.html` — `verProj` (~1590-1610), nova função `criarProjetoDeAmostra`.

**Interfaces:**
- Consome: `decisaoSelo` (Task 1), `mostrarForm(null,false)` (Task 2), `addMatF`/`addSec`/`renderMF`/`renderSF` (existentes). Produz: `criarProjetoDeAmostra(id)`.

- [ ] **Passo 1: Reescrever `verProj`** (botões e selo condicionais ao `p.amostra`; resto do corpo igual ao atual, só trocar a fileira de botões inicial e o selo de status). Substituir do `function verProj(id){` até a linha `<span class="tag ts-${p.status||'rascunho'}">${sLabel(p.status)}</span>` por:
```js
function verProj(id){
  const p=_P.find(x=>(x.id||x._id)===id);if(!p)return;
  const amo=!!p.amostra;
  const pv=_H.filter(h=>h.projetoId===id);
  const botoes=amo
    ?`<button class="bbk" onclick="sv('lista')">‹</button>
      <button class="bg" onclick="mostrarForm('${id}')">✏️ Editar</button>
      <button class="bg" style="background:linear-gradient(135deg,var(--green),#1d4a30)" onclick="abrirAtelie('${id}')">▶ Trabalhar</button>
      <button class="bgn" onclick="criarProjetoDeAmostra('${id}')">🧶 Criar projeto a partir desta amostra</button>`
    :`<button class="bbk" onclick="sv('lista')">‹</button>
      <button class="bg" onclick="mostrarForm('${id}')">✏️ Editar</button>
      <button class="bgn" onclick="calcProj('${id}','${(p.nome||'').replace(/'/g,"\\'")}')">💰 Calcular</button>
      <button class="bg" onclick="produzirPeca('${id}')">🧵 Produzir</button>
      <button class="bgr" onclick="conferirMateriais('${id}')">🛒 Conferir</button>
      <button class="bg" style="background:linear-gradient(135deg,var(--green),#1d4a30)" onclick="abrirAtelie('${id}')">▶ Trabalhar</button>`;
  document.getElementById('det-ctr').innerHTML=`<div style="padding-top:.5rem">
    <div style="display:flex;gap:8px;align-items:center;margin-bottom:12px;flex-wrap:wrap">${botoes}</div>
    <h2 style="font-size:20px;font-weight:700;margin-bottom:6px">${esc(p.nome)}</h2>
    <div style="font-size:13px;color:#888;margin-bottom:8px">${esc(p.tipo||'')} ${p.data?'· '+p.data:''} ${p.tecnica?'· '+esc(p.tecnica):''} ${p.colecao?'· 🎨 '+esc(p.colecao):''}</div>
    ${amo?decisaoSelo(p.decisao):`<span class="tag ts-${p.status||'rascunho'}">${sLabel(p.status)}</span>`}
```
  ⚠️ Manter o RESTANTE do corpo do `verProj` como está hoje (descrição, materiais, receita/sequência, links, fotos, obs, tempo, fechamento `</div>` + `sv('det')`), **exceto** o bloco de "Preços calculados" (`pv`), que deve só aparecer pra peça — trocar `${pv.length?` por `${(!amo&&pv.length)?`.

- [ ] **Passo 2: Função `criarProjetoDeAmostra`.** Adicionar logo após `verProj`:
```js
function criarProjetoDeAmostra(id){
  const a=_P.find(x=>(x.id||x._id)===id);if(!a||!a.amostra)return;
  mostrarForm(null,false);                 // abre form de PEÇA novo (reseta _mf/_sf/_ff)
  // popula DEPOIS do reset (mostrarForm zera os globais)
  _mf=(a.materiais?JSON.parse(JSON.stringify(a.materiais)):[]).map(m=>({nome:m.nome||'',qtd:parseFloat(m.qtd)||0,und:m.und||'un',custoUnit:parseFloat(m.custoUnit)||0,estoqueId:m.estoqueId||null,obs:m.obs||''}));
  _sf=a.secoes?JSON.parse(JSON.stringify(a.secoes)):[];
  if(!_mf.length)_mf=[{nome:'',qtd:0,und:'un',custoUnit:0,obs:''}];
  if(!_sf.length)_sf=[{titulo:'Nova seção',passos:['']}];
  document.getElementById('f-n').value=(a.tipo||'Peça')+' — '+(a.nome||'ponto');
  document.getElementById('f-tc').value=a.tecnica||'';
  renderMF();renderSF();
  toast('Ajuste a quantidade pro tamanho real e toque em Calcular 💰');
}
```

- [ ] **Passo 3: Validar** (`node --check`).
- [ ] **Passo 4: Commit** — "feat(amostras): detalhe da amostra + criar projeto a partir dela".

---

### Task 4: Release (v2.15 + manual + deploy)

**Files:**
- Modify: `index.html` (badge), `gera_manual.py` (versão + subseção), `Manual_Studio_Bolsas.pdf` (gerado).

- [ ] **Passo 1: Bump badge.** No `index.html`, `>v2.14<` → `>v2.15<` (no header, span do badge).
- [ ] **Passo 2: Manual — versão.** Em `gera_manual.py`: `'manual de uso · versão 2.14'` → `2.15` e `p('versão 2.14',...)` → `2.15`.
- [ ] **Passo 3: Manual — subseção.** Na seção 4 (Projetos), após o passo 6 (`passo(6,'Salve...')`), inserir:
```python
p('Amostras de ponto — testar antes de comprometer',H2)
p('Na lista de Projetos há um seletor <b>Peças | Amostras</b>. Em <b>Amostras</b> você registra um ponto novo que testou: a sequência, uma foto e a <b>decisão</b> (🧪 Testando · 👍 Aprovado · 👎 Descartado).')
passo(1,'Aba <b>Amostras</b> > <b>+ Amostra</b>: dê o nome do ponto, em que peça ele cabe (bolsa, blusão…), registre a sequência e bata a foto.')
passo(2,'Marque a <b>decisão</b> conforme for testando.')
passo(3,'Gostou? Na amostra, toque em <b>🧶 Criar projeto a partir desta amostra</b>: a sequência e os materiais vão para um projeto novo. Ajuste a quantidade pro tamanho real e use <b>Calcular</b> para ver o custo — dá pra comparar o mesmo modelo com pontos diferentes.')
```

- [ ] **Passo 4: Regenerar PDF.** `cd` no repo e `python gera_manual.py` → "Manual gerado".
- [ ] **Passo 5: Validar JS** final (`node --check`).
- [ ] **Passo 6: Commit + deploy.** `git add index.html gera_manual.py Manual_Studio_Bolsas.pdf && git commit` ("v2.15: amostras de ponto + manual"); `git checkout master && git merge feat/amostras-de-ponto --ff-only && git push origin master`.
- [ ] **Passo 7: Verificar no ar.** Poll `project-anmtx.vercel.app/index.html` até badge `v2.15`; confirmar que o HTML contém `criarProjetoDeAmostra` e `seg-amostras`.

---

## Self-review (cobertura do spec)
- Flag `amostra` + `decisao` (testando/aprovado/descartado) → Task 2 (salvarProj) ✓
- Filtro Peças|Amostras + selo no card → Task 1 ✓
- Form adapta (rótulos, decisão no lugar do status, esconde coleção/tempo, "sequência do ponto") → Task 2 ✓
- Detalhe + botões da amostra + "criar projeto a partir desta amostra" → Task 3 ✓
- Reuso da calculadora (sem motor novo): criarProjetoDeAmostra → form de peça → Calcular existente ✓
- Sem migração (projetos antigos = peça) → filtro usa `!!p.amostra` ✓
- Release v2.15 + manual → Task 4 ✓
- Bônus: `esc()` em renderLista (faltava) corrigido na Task 1 ✓
