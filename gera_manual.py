# -*- coding: utf-8 -*-
# Gerador do Manual do Studio Bolsas — manter atualizado a cada feature nova!
# Requer: reportlab + fontes Lora e Poppins (google-fonts) e DejaVu.
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

G='/usr/share/fonts/truetype/google-fonts/'
D='/usr/share/fonts/truetype/dejavu/'
pdfmetrics.registerFont(TTFont('Lora',G+'Lora-Variable.ttf'))
pdfmetrics.registerFont(TTFont('LoraIt',G+'Lora-Italic-Variable.ttf'))
pdfmetrics.registerFont(TTFont('Pop',G+'Poppins-Regular.ttf'))
pdfmetrics.registerFont(TTFont('PopL',G+'Poppins-Light.ttf'))
pdfmetrics.registerFont(TTFont('PopM',G+'Poppins-Medium.ttf'))
pdfmetrics.registerFont(TTFont('PopB',G+'Poppins-Bold.ttf'))
pdfmetrics.registerFont(TTFont('DJV',D+'DejaVuSans.ttf'))
pdfmetrics.registerFontFamily('Pop',normal='Pop',bold='PopB',italic='PopL',boldItalic='PopM')

ROSE=HexColor('#6B1537'); BLUSH=HexColor('#F8EDF1'); BLUSH_B=HexColor('#E7C9D4')
GOLD=HexColor('#A8843C'); GOLD_L=HexColor('#FBF5E6'); GOLD_D=HexColor('#7A5E28'); GOLD_B=HexColor('#E5D3A8')
IVORY=HexColor('#FDF9F4'); TXT=HexColor('#4A3F39'); MUT=HexColor('#9A8C84'); GREEN=HexColor('#3E7050'); RED=HexColor('#9A3838')

P   =ParagraphStyle('P',fontName='Pop',fontSize=9.8,leading=15.5,textColor=TXT,spaceAfter=6)
PASSO=ParagraphStyle('PASSO',parent=P,leftIndent=16,spaceAfter=4)
H1  =ParagraphStyle('H1',fontName='Lora',fontSize=17,leading=21,textColor=ROSE,spaceBefore=18,spaceAfter=3)
H2  =ParagraphStyle('H2',fontName='PopM',fontSize=10.5,leading=14,textColor=GOLD_D,spaceBefore=12,spaceAfter=4)
DICA=ParagraphStyle('DICA',parent=P,backColor=GOLD_L,borderColor=GOLD_B,borderWidth=0.8,borderPadding=8,borderRadius=7,leftIndent=2,rightIndent=2,spaceBefore=6,spaceAfter=10)
ALER=ParagraphStyle('ALER',parent=DICA,backColor=BLUSH,borderColor=BLUSH_B)
CELL=ParagraphStyle('CELL',parent=P,fontSize=9,leading=13.5,spaceAfter=0)
CELLB=ParagraphStyle('CELLB',parent=CELL,fontName='PopM',textColor=ROSE)
CELLN=ParagraphStyle('CELLN',parent=CELL,fontName='Lora',fontSize=14,textColor=GOLD,alignment=TA_CENTER)

def filete(w=26):
    t=Table([['']],colWidths=[w*mm],rowHeights=[1.1])
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),GOLD)]))
    t.hAlign='LEFT';return t
def capa_bg(c,doc):
    c.saveState()
    c.setFillColor(ROSE); c.rect(0,0,A4[0],A4[1],fill=1,stroke=0)
    c.setStrokeColor(GOLD); c.setLineWidth(1.2); c.rect(11*mm,11*mm,A4[0]-22*mm,A4[1]-22*mm)
    c.setLineWidth(0.4); c.rect(13.5*mm,13.5*mm,A4[0]-27*mm,A4[1]-27*mm)
    c.setLineWidth(1); c.circle(A4[0]/2,A4[1]-72*mm,14*mm)
    c.setFillColor(GOLD); c.setFont('Lora',26); c.drawCentredString(A4[0]/2,A4[1]-76*mm,'SB')
    c.restoreState()
def pag_bg(c,doc):
    c.saveState()
    c.setFillColor(IVORY); c.rect(0,0,A4[0],A4[1],fill=1,stroke=0)
    c.setFillColor(GOLD); c.setFont('Lora',10); c.drawString(17*mm,A4[1]-13*mm,'Studio Bolsas')
    c.setFillColor(MUT); c.setFont('PopL',7.5); c.drawRightString(A4[0]-17*mm,A4[1]-13*mm,'manual de uso · versão 2.2')
    c.setStrokeColor(GOLD_B); c.setLineWidth(0.6); c.line(17*mm,A4[1]-16*mm,A4[0]-17*mm,A4[1]-16*mm)
    c.setFillColor(MUT); c.setFont('PopL',8); c.drawCentredString(A4[0]/2,9*mm,f'·  {doc.page}  ·')
    c.restoreState()

doc=SimpleDocTemplate('Manual_Studio_Bolsas.pdf',pagesize=A4,
    topMargin=24*mm,bottomMargin=18*mm,leftMargin=18*mm,rightMargin=18*mm,
    title='Studio Bolsas — Manual de Uso',author='Studio Bolsas')
S=[]
def p(t,st=P): S.append(Paragraph(t,st))
def sec(n,t):
    S.append(Paragraph(f'<font face="Lora" color="#A8843C">{n}.</font>  {t}',H1)); S.append(filete()); S.append(Spacer(1,3*mm))
def passo(n,t): S.append(Paragraph(f'<font face="PopB" color="#A8843C">{n}</font>&nbsp;&nbsp;{t}',PASSO))
def dica(t): S.append(Paragraph(f'<font face="DJV" color="#A8843C">♥</font> <b>Dica</b> — {t}',DICA))
def alerta(t): S.append(Paragraph(f'<font face="DJV" color="#9A3838">✦</font> <b>Atenção</b> — {t}',ALER))
def C(t,st=CELL): return Paragraph(t,st)

# ═ CAPA ═
S.append(Spacer(1,92*mm))
p('Studio Bolsas',ParagraphStyle('ct',fontName='Lora',fontSize=34,leading=40,textColor=white,alignment=TA_CENTER,spaceAfter=6))
p('MANUAL DE USO & TREINAMENTO',ParagraphStyle('cs',fontName='PopM',fontSize=10,textColor=GOLD_B,alignment=TA_CENTER,spaceAfter=2))
p('versão 2.2',ParagraphStyle('cv',fontName='PopL',fontSize=9,textColor=GOLD_B,alignment=TA_CENTER))
S.append(Spacer(1,52*mm))
p('o seu ateliê, organizado com carinho',ParagraphStyle('ci',fontName='LoraIt',fontSize=12,textColor=GOLD_B,alignment=TA_CENTER,spaceAfter=10))
p('project-anmtx.vercel.app',ParagraphStyle('cl',fontName='PopM',fontSize=12,textColor=white,alignment=TA_CENTER))
S.append(PageBreak())

# ═ 1 ═
sec(1,'Começando')
p('O Studio Bolsas funciona no navegador do celular ou do computador — não precisa instalar nada.')
passo(1,'Abra <b>project-anmtx.vercel.app</b> no navegador (de preferência o Chrome — fora do navegador interno do WhatsApp/Instagram).')
passo(2,'Entre com <b>Google</b> ou com <b>e-mail e senha</b>. Sem senha ainda? Toque em <b>"Esqueci / quero criar uma senha"</b>: chega um e-mail para definir.')
passo(3,'No celular, menu do navegador > <b>"Adicionar à tela inicial"</b> — o app vira um ícone.')
p('O indicador no topo mostra <b>Sincronizado</b> (verde) ou <b>Offline</b> (vermelho).')
dica('O app funciona sem internet: você pode consultar e lançar dados no modo avião — tudo sincroniza quando a conexão voltar.')
alerta('Cada pessoa entra com a própria conta e vê apenas os próprios dados. Faça um backup (Ajustes > Exportar dados) pelo menos uma vez por mês.')

# ═ 2 ═
sec(2,'O fluxo do ateliê — visão geral')
p('O app acompanha o ciclo completo de uma peça. Esta é a ordem natural de uso:')
rows=[
 ('1','Comprou material','Estoque > botão <b>Cupom</b>: foto ou PDF do cupom. Entra no estoque e lança a despesa no caixa.'),
 ('2','Criou o modelo','Projetos > <b>+ Novo</b>: receita de pontos, materiais, fotos e links dos fornecedores.'),
 ('3','Definiu o preço','Preço: importa os materiais do projeto, ajusta horas e margem, salva o cálculo.'),
 ('4','Conferiu e produziu','Botão <b>Conferir</b> mostra o que falta comprar; <b>Produzir</b> dá baixa no estoque e cria o produto com custo real e foto.'),
 ('5','Vendeu','Loja/WhatsApp ou plataformas. Registrar a venda dá <b>baixa automática</b> no produto pronto.'),
 ('6','Acompanhou','Painel: DRE do mês, pendências, alerta de reposição, plano vs. realidade.'),
]
t=Table([[C(a,CELLN),C(b,CELLB),C(c)] for a,b,c in rows],colWidths=[10*mm,36*mm,128*mm])
t.setStyle(TableStyle([
 ('VALIGN',(0,0),(-1,-1),'MIDDLE'),('ROWBACKGROUNDS',(0,0),(-1,-1),[white,BLUSH]),
 ('LINEBELOW',(0,0),(-1,-2),0.5,GOLD_B),
 ('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7),
 ('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),8),
]))
S.append(t); S.append(Spacer(1,4*mm))
p('<b>Planejado vs. real:</b> a lista de materiais do projeto é o <b>planejado</b>. Na hora de <b>Produzir</b>, você informa o que usou <b>de verdade</b> — o app compara, dá baixa no estoque e grava o custo real na peça. É esse custo que vai para a venda e o DRE.')

# ═ 3 ═
sec(3,'Painel')
p('A tela de chegada: um resumo vivo do negócio.')
p('<b>Faixa da fase</b> — em que fase do plano você está e o progresso da meta. <b>Cartões do mês</b> — receita, despesas, lucro, saldo, ticket médio, margem e estoque baixo.')
p('<b>DRE</b> — receita bruta − custo das peças − taxas de plataforma = lucro bruto; − despesas = lucro líquido.')
p('<b>Pendências</b> — vendas aguardando pagamento. <b>Repor materiais</b> — o que ficou abaixo do mínimo.')
dica('Nas vendas, escreva o nome do modelo na descrição (ex.: "Bolsa Flora coral — cliente Ana"). É assim que os rankings contam.')

# ═ 4 ═
sec(4,'Projetos — o caderno do ateliê')
passo(1,'<b>+ Novo</b>: nome, tipo, técnica e coleção.')
passo(2,'<b>Materiais:</b> o que a peça leva, com quantidade, unidade e custo. "Do estoque" puxa o custo certinho.')
passo(3,'<b>Fornecedores e links de compra:</b> guarde onde comprar cada coisa — loja, link do produto, WhatsApp do fornecedor. Esses links aparecem na conferência de materiais.')
passo(4,'<b>Receita de pontos:</b> seções (Base, Corpo, Alça...) e os passos.')
passo(5,'<b>Fotos:</b> botão <b>"Da câmera/galeria"</b> tira a foto na hora (o app comprime sozinho) — ou cole um link.')
passo(6,'Salve. Na tela do projeto ficam <b>Calcular</b>, <b>Produzir</b>, <b>Conferir</b> e <b>Trabalhar</b>.')
p('Modo Ateliê — para a hora de fazer',H2)
p('Toque em <b>▶ Trabalhar</b> no projeto: a receita abre em tela cheia, com letra grande, pensada para quem está de agulha na mão.')
passo(1,'<b>Risque os passos</b> conforme avança — tocou, riscou. Saiu e voltou? Continua de onde parou.')
passo(2,'<b>Contador de carreiras</b> com botões grandes − / + (vibra de leve a cada toque).')
passo(3,'<b>Cronômetro</b>: dê o play quando começar e pause nas paradas. O tempo fica guardado na peça.')
passo(4,'🌙 alterna o <b>modo escuro</b>, para trabalhar à noite sem cansar a vista.')
dica('O tempo cronometrado vira a mão de obra REAL na hora de Produzir — o preço da peça passa a refletir o seu trabalho de verdade, não uma estimativa.')

# ═ 5 ═
sec(5,'Preço — a calculadora')
passo(1,'<b>"Do projeto"</b> importa os materiais planejados.')
passo(2,'Horas de trabalho × valor/hora; embalagem e custos fixos.')
passo(3,'<b>Plataforma</b> (taxa de Ajustes) e <b>margem</b> no controle deslizante.')
p('Mostra custo total, <b>preço mínimo</b> e <b>preço sugerido</b>. Salve vinculado ao projeto — vira sugestão de preço e de mão de obra na produção.')
dica('Margem de 40–50% é a faixa saudável para peça artesanal de luxo.')

# ═ 6 ═
sec(6,'Estoque')
p('Duas listas: <b>materiais</b> e <b>produtos prontos</b>.')
p('Entrada de material — botão Cupom',H2)
passo(1,'<b>Cupom</b>: foto do cupom ou PDF da nota. O app lê os itens sozinho — <b>confira cada linha</b>.')
passo(2,'Para cada item: criar material novo ou somar em um existente. Deixe marcado <b>"Lançar como despesa"</b>.')
alerta('Cadastro manual (+ Material) NÃO lança despesa — é para acerto de inventário. Compra de verdade entra pelo Cupom.')
p('Conferir materiais e lista de compras',H2)
passo(1,'No projeto, toque em <b>Conferir</b>: cada material ganha um selo — <b>✓ tem</b>, <b>⚠ parcial</b> ou <b>✕ falta</b>.')
passo(2,'Dos que faltam, o app monta a <b>lista de compras</b> com quantidades, custo estimado e o <b>link do fornecedor</b> (um toque e abre a página).')
passo(3,'<b>"Pedir por WhatsApp"</b> abre a conversa com o pedido pronto; <b>"Copiar lista"</b> leva para onde quiser.')
passo(4,'Comprou? O cupom entra no estoque e os selos viram ✓ sozinhos.')
p('Produzir uma peça',H2)
passo(1,'<b>Produzir</b> > escolha o projeto. Ajuste as quantidades para o que <b>realmente usou</b>; o app avisa se faltar estoque.')
passo(2,'Tire a <b>foto da peça pronta</b> (📷) — e, se quiser, toque em <b>✨ Premium (IA)</b>: vira foto de catálogo com fundo neutro e luz de estúdio, sem alterar a peça. Você compara antes/depois e escolhe.')
passo(3,'No quadro <b>Sugestão de preço</b>, a mão de obra já vem preenchida — do cronômetro do Modo Ateliê (tempo real!) ou do cálculo salvo; ajuste a margem e toque em "Usar este preço".')
passo(4,'<b>Concluir produção</b>: baixa nos materiais + produto pronto com custo real — e já publicado na loja, se marcado.')
p('Vender um produto pronto',H2)
p('<b>Registrar venda</b>: o caixa abre preenchido. Ao salvar, o app <b>dá baixa automática</b> — zerou, vira "Vendido" e sai da loja.')

# ═ 7 ═
sec(7,'Loja — sua vitrine pública')
p('Os produtos com o selo <b>"na loja"</b> aparecem numa página pública sempre atualizada:')
p('<b>project-anmtx.vercel.app/loja.html</b>',ParagraphStyle('lk',parent=P,fontName='PopM',textColor=ROSE,fontSize=11))
passo(1,'Em <b>Ajustes > Loja</b>, informe o <b>WhatsApp</b> e salve. Use <b>Copiar link</b> / <b>Compartilhar</b> para divulgar (bio do Instagram, status do WhatsApp).')
passo(2,'Publique as peças: na produção a opção já vem marcada; nos produtos existentes use <b>Publicar</b>.')
passo(3,'A cliente toca em <b>"Comprar pelo WhatsApp"</b> e cai na sua conversa com a mensagem pronta — frete e pagamento combinados ali, sem taxa.')
passo(4,'Fechou? Registre a venda: a peça sai da loja e do estoque sozinha.')
dica('Foto vende: use a foto premium da IA nas peças publicadas.')

# ═ 8 ═
sec(8,'Ajustes')
p('<b>Conta</b> — quem está conectado; o admin tem o seletor "Gerenciar a conta de". <b>Taxas de plataformas</b> — valem na calculadora, caixa e DRE. <b>Fases do plano</b> e <b>Modelos do catálogo</b> — alimentam o Painel. <b>Loja</b> — WhatsApp + link da vitrine.')
p('<b>✨ IA de imagens</b> — cole a sua chave do Google AI Studio (grátis em <b>aistudio.google.com/apikey</b>) para ativar o botão Premium das fotos.')
p('<b>Backup</b> — Exportar dados (guarde no Drive!) e Importar backup.')
alerta('Depois de editar, toque em "Salvar configurações".')

# ═ 9 ═
sec(9,'Boas práticas do dia a dia')
for t9 in ['Lançou na hora, não esquece: registre a venda assim que fechar, mesmo pendente.',
 'Toda compra entra pelo Cupom — estoque e despesa de uma vez.',
 'Use o nome do modelo na descrição das vendas.',
 'Antes de produzir, toque em Conferir — sem surpresa de material faltando no meio.',
 'Produza sempre pelo botão Produzir — estoque e custo real corretos.',
 'Guarde os links dos fornecedores no projeto: a lista de compras usa eles.',
 'Foto boa (ou premium da IA) na peça publicada — a vitrine é seu cartão de visitas.',
 'Exporte o backup uma vez por mês.']:
    S.append(Paragraph(f'<font face="DJV" color="#A8843C">♥</font>&nbsp;&nbsp;{t9}',PASSO))

# ═ 10 ═
sec(10,'Problemas comuns')
faq=[
 ('Aparece "Offline" o tempo todo','Verifique a internet e recarregue. O que foi lançado offline sincroniza sozinho.'),
 ('Login Google "cancelado" no celular','Abra o link no Chrome de verdade (menu > "Abrir no Chrome" — não no navegador do WhatsApp/Instagram). Ou use e-mail e senha: "Esqueci / quero criar uma senha" resolve na hora.'),
 ('Criar conta diz que o e-mail já existe','A conta já foi criada (provavelmente pelo Google). Toque em "Esqueci / quero criar uma senha", defina a senha pelo e-mail e entre.'),
 ('A leitura do cupom veio errada','Corrija na tela de revisão. Foto esticada, com luz, de cima.'),
 ('A loja não mostra a peça','Produto precisa estar "Disponível", qtd acima de zero e com o selo "na loja". E o WhatsApp salvo em Ajustes.'),
 ('O botão Premium (IA) não funciona','Confira a chave em Ajustes > IA de imagens, e se tem foto carregada (não vale link externo).'),
 ('Apaguei algo sem querer','Restaure pelo último backup (Ajustes > Importar backup).'),
]
t=Table([[C(f'<b>{a}</b>',CELLB),C(b)] for a,b in faq],colWidths=[52*mm,122*mm])
t.setStyle(TableStyle([
 ('VALIGN',(0,0),(-1,-1),'TOP'),('ROWBACKGROUNDS',(0,0),(-1,-1),[white,BLUSH]),
 ('LINEBELOW',(0,0),(-1,-2),0.5,GOLD_B),
 ('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7),
 ('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),8),
]))
S.append(t)
S.append(Spacer(1,10*mm))
p('feito à mão, gerido com carinho — boas vendas!',ParagraphStyle('fim',fontName='LoraIt',fontSize=12,textColor=GOLD_D,alignment=TA_CENTER))

doc.build(S,onFirstPage=capa_bg,onLaterPages=pag_bg)
print('Manual gerado')
