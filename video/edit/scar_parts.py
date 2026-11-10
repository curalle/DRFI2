# Content for scar.html (9:16): why scars don't sweat or grow hair.
# Same look as honest/postbiotic: title band over the top on full-screen shots, a Vox tile for the science.
from honest_parts import EXTRA_CSS

TITLE = 'DRFI Scar Tissue Explainer 9:16'
DURATION = 31.6
OUTPUT = 'output/drfi_scar_9x16.mp4'
NFR = 946
PIPNAME = 'Ts. Dr Fareez Ismail · DRFI'
# car at night: head top ~530, face centre ~(460,880)
FRAMING = {'pip': (460, 880), 'full': (470, 900), 'head_top': 520, 'band_bottom': 720}

BAND = r'''
<div id="band">
  <div id="prog"><div class="track"></div><div class="fill" id="pfill"></div></div>
  <div id="b1">
    <div class="bk" style="top:190px" data-in="0.1" data-fx="up">Perasan tak?</div>
    <div class="bt" style="top:240px" data-in="1.4" data-fx="up">Di kawasan <span class="hl" data-hl="3.6">parut</span>…</div>
    <div class="badge" style="left:60px;top:430px" data-in="6.4" data-fx="left"><b style="background:#E4472B">✗</b>Tak berpeluh</div>
    <div class="badge" style="left:400px;top:430px" data-in="8.0" data-fx="left"><b style="background:#E4472B">✗</b>Tak tumbuh bulu semula</div>
  </div>
  <div id="b2">
    <div class="bk" style="top:190px" data-in="27.3" data-fx="up">Giliran anda</div>
    <div class="bt" style="top:240px;font-size:70px" data-in="27.5" data-fx="up">Ada parut yang nak <span class="hl" data-hl="28.9">hilangkan?</span></div>
    <div class="badge" style="left:60px;top:470px;background:#FFE14D" data-in="29.6" data-fx="pop" id="cm2"><b style="background:#1B1B1B">✎</b>Komen di bawah</div>
  </div>
</div>
'''
BANDS = "[['b1',0,10.0],['b2',27.0,999]]"
CHAPTERS = "[['Soalan',0],['Sains',10.1],['Komen',27.3]]"
LOW = "[[0,1]]"
ZOOM = "[[0,9.9,0,.06],[27.3,31.6,0,.07]]"

TILES = r'''
  <!-- T1: normal skin vs scar tissue (0,0) -->
  <div class="tile" id="T1" style="left:0;top:0">
    <div class="kicker" style="left:70px;top:250px" data-in="10.2" data-fx="up"><span style="background:var(--yellow);color:var(--deep);padding:2px 12px;border-radius:6px">Sebabnya</span></div>
    <div class="title" style="left:70px;top:300px;width:620px;font-size:56px">
      <div data-in="11.1" data-fx="up">Tisu parut terbentuk</div>
      <div data-in="14.4" data-fx="up"><span class="hl" data-hl="14.8">sangat berbeza.</span></div>
    </div>
    <div class="body" style="left:70px;top:470px;width:600px;font-size:32px" data-in="15.8" data-fx="up">…dari kulit normal.</div>
    <div class="card" style="left:70px;top:700px;width:450px;height:800px" data-in="15.9" data-fx="card">
      <div class="lbl" style="left:0;width:450px;top:30px;text-align:center;color:#5E9A1E">Kulit normal</div>
      <svg style="left:15px;top:90px" width="420" height="620" viewBox="0 0 420 620" id="norm1"></svg>
    </div>
    <div class="card" style="left:560px;top:700px;width:450px;height:800px" data-in="16.2" data-fx="card">
      <div class="lbl" style="left:0;width:450px;top:30px;text-align:center;color:var(--red)">Tisu parut</div>
      <svg style="left:15px;top:90px" width="420" height="620" viewBox="0 0 420 620" id="scar1"></svg>
      <div class="tag red" style="left:40px;top:540px;font-size:28px;transform-origin:left center" data-in="23.6" data-fx="stamp" data-rot="-3">✗ Tiada kelenjar peluh</div>
      <div class="tag red" style="left:40px;top:640px;font-size:28px;transform-origin:left center" data-in="25.2" data-fx="stamp" data-rot="2">✗ Tiada folikel rambut</div>
    </div>
    <div class="chip" style="left:70px;top:1560px;font-size:32px" data-in="18.8" data-fx="left"><b>⚡</b>Fokus kolagen: cantum luka dengan cepat</div>
  </div>
'''

OVERLAYS = ''
OV = "[]"
TP = "{T1:[0,0]}"
ORDER = "['T1']"
CAM = r'''const CAM=[
 [0,...C('T1'),1],[17.0,...C('T1'),1],[17.8,...C('T1',540,1000),1.05],[22.0,...C('T1',540,1000),1.05],
 [22.7,...C('T1',740,1100),1.2],[26.6,...C('T1',740,1100),1.2],[27.4,...C('T1'),1],[31.6,...C('T1'),1]
];'''
MODE = "[[0,1],[9.8,1],[10.25,0],[26.9,0],[27.35,1]]"
PUNCH = "[[6.4,.05],[9.6,0],[28.9,.05]]"
BR = "[]"

ILLUSTRATIONS_PRE = ""
ILLUSTRATIONS = r'''
// cross-section helper: epidermis on top, dermis below
function section(svg,epiFill){
  el(svg,'rect',{x:0,y:110,width:420,height:510,rx:10,fill:'#F6D9CA'});
  el(svg,'path',{d:'M0 60 q35 -14 70 0 t70 0 t70 0 t70 0 t70 0 t70 0 V110 H0z',fill:epiFill});
  txt(svg,370,100,'EPIDERMIS',{'font-size':14,'letter-spacing':2,'text-anchor':'end',fill:'#9b6a58'});
  txt(svg,370,600,'DERMIS',{'font-size':14,'letter-spacing':2,'text-anchor':'end',fill:'#9b6a58'});
}
// normal skin: basket-weave collagen, a hair follicle and a sweat gland
const N=$('norm1');section(N,'#EFBFAA');
for(let i=0;i<34;i++){const x=20+(i*53)%380,y=150+((i*37)%400),a=(i*47)%180;
  el(N,'path',{d:`M${x-18} ${y} q9 -7 18 0 t18 0`,fill:'none',stroke:'#E2A892','stroke-width':4,'stroke-linecap':'round',transform:`rotate(${a} ${x} ${y})`});}
const fol=el(N,'g',{});
el(fol,'path',{d:'M120 70 C 118 200, 110 300, 112 400',fill:'none',stroke:'#C98F7A','stroke-width':22,'stroke-linecap':'round'});
el(fol,'ellipse',{cx:112,cy:410,rx:24,ry:30,fill:'#C98F7A'});
const hair=el(N,'path',{d:'M116 400 C 118 250, 124 120, 126 -10',fill:'none',stroke:'#3a2a20','stroke-width':6,'stroke-linecap':'round'});
txt(N,112,470,'Folikel rambut',{'font-size':20,fill:'#3d3830'});
el(N,'path',{d:'M300 60 C 300 180, 320 300, 300 420',fill:'none',stroke:'#2a6a85','stroke-width':10,'stroke-linecap':'round'});
el(N,'path',{d:'M300 420 c 40 8, 50 40, 22 60 c -28 20, -72 6, -64 -26 c 8 -26, 46 -26, 52 -6',fill:'none',stroke:'#2a6a85','stroke-width':10,'stroke-linecap':'round'});
txt(N,300,540,'Kelenjar peluh',{'font-size':20,fill:'#2a6a85'});
const sweat=[0,1,2].map(i=>el(N,'circle',{cx:300,cy:420,r:9,fill:'#9ED0E6',opacity:0}));
// scar: flat shiny epidermis, dense parallel collagen, nothing else
const Sc=$('scar1');section(Sc,'#F7D3C6');
el(Sc,'rect',{x:0,y:56,width:420,height:12,fill:'#fff',opacity:.6});
const coll=[...Array(14)].map((_,i)=>drawPath(el(Sc,'path',{d:`M14 ${150+i*28} H406`,fill:'none',stroke:'#C98F7A','stroke-width':12,'stroke-linecap':'round'}),17.4+i*.11,.5));
txt(Sc,210,140,'KOLAGEN PADAT & SELARI',{'font-size':16,'letter-spacing':2,fill:'#a0503c'});
const xs=[[112,300],[300,320]].map(([x,y])=>{const g=el(Sc,'g',{opacity:0});el(g,'circle',{cx:x,cy:y,r:34,fill:'none',stroke:'#E4472B','stroke-width':6,'stroke-dasharray':'8 8'});
  el(g,'path',{d:`M${x-16} ${y-16} L${x+16} ${y+16} M${x+16} ${y-16} L${x-16} ${y+16}`,stroke:'#E4472B','stroke-width':6,'stroke-linecap':'round'});return g;});
'''

FRAME = r'''
  // normal skin: sweat beads rise through the duct, hair sways
  sweat.forEach((d,i)=>{const ph=((t*.5+i*.33)%1);d.setAttribute('cy',420-ph*360);d.setAttribute('cx',300+Math.sin(ph*6)*6);d.style.opacity=t>15.9?.9*(1-ph):0;});
  hair.setAttribute('transform',`rotate(${Math.sin(t*1.6)*3} 116 400)`);
  // scar: dashed "missing" markers where the gland and follicle would be
  xs[0].style.opacity=P(t,25.2,.3);xs[1].style.opacity=P(t,23.6,.3);
'''

BAND_FRAME = r'''
  {const f=modeAt(t);$('band').style.opacity=clamp(f*1.2-.1);
   BANDS.forEach(([id,a,b])=>{const e=$(id);const v=t>=a&&t<b;e.style.visibility=v?'visible':'hidden';e.style.opacity=v&&t>b-.25?1-P(t,b-.25,.25):1;});
   $('pfill').style.width=`${960*clamp(t/DURATION)}px`;
   CH.forEach(c=>c.el.classList.toggle('on',t>=c.t));
   if(t>29.6){$('cm2').style.transform=`scale(${1+.04*Math.sin((t-29.6)*8)})`;}
  }
'''
