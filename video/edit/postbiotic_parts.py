# Content for postbiotic.html (9:16): "dua produk postbiotik, kesan sama? strictly no."
# Same look as honest_parts.py: a title band over the top while the presenter is full screen,
# Vox paper tiles with a floating frame for the explanations.
from honest_parts import EXTRA_CSS

TITLE = 'DRFI Postbiotic Explainer 9:16'
DURATION = 109.6
OUTPUT = 'output/drfi_postbiotic_9x16.mp4'
NFR = 3255
FREEZE_AT = 103.6   # after this the camera is being picked up; 'Terima kasih' plays over the held frame
PIPNAME = 'Ts. Dr Fareez Ismail · DRFI'
# office framing: head already sits low in the frame (top ~680), face centre x ~630
FRAMING = {'pip': (630, 960), 'full': (598, 900), 'head_top': 680, 'band_bottom': 720}

BAND = r'''
<div id="band">
  <div id="prog"><div class="track"></div><div class="fill" id="pfill"></div></div>

  <div id="b1">
    <div class="bk" style="top:190px" data-in="0.3" data-fx="up">Pernah nampak?</div>
    <div class="badge" style="left:60px;top:250px" data-in="1.3" data-fx="left"><b style="background:#6A3FA0">A</b>Produk A · "postbiotik"</div>
    <div class="badge" style="left:540px;top:250px" data-in="1.8" data-fx="left"><b style="background:#2a6a85">B</b>Produk B · "postbiotik"</div>
    <div class="bt" style="top:370px" data-in="6.1" data-fx="up">Kesannya <span class="hl" data-hl="9.0">sama?</span></div>
    <div class="tag red" style="position:absolute;left:560px;top:470px;font-size:64px;transform-origin:center" data-in="11.5" data-fx="stamp" data-rot="-6">STRICTLY NO.</div>
  </div>
  <div id="b2">
    <div class="bk" style="top:190px" data-in="13.2" data-fx="up">Siri DRFI</div>
    <div class="bt" style="top:240px" data-in="13.4" data-fx="up">Ts. Dr Fareez Ismail</div>
    <div class="badge" style="left:60px;top:440px" data-in="14.6" data-fx="left"><b style="background:#6A3FA0">✓</b>Penyelidik &amp; pengasas CURALLÉ</div>
  </div>
  <div id="b3">
    <div class="bk" style="top:190px" data-in="41.0" data-fx="up">Di CURALLÉ</div>
    <div class="bt" style="top:240px;width:700px" data-in="41.8" data-fx="up">Postbiotik <span style="color:#FFE14D">+</span> <span class="hl" data-hl="45.4">bahan pelembap</span></div>
    <img src="assets/tube_hand_s.png" style="position:absolute;left:800px;top:160px;width:220px;height:380px;object-fit:cover;object-position:top;border-radius:14px;box-shadow:0 14px 30px rgba(0,0,0,.4)" data-in="41.4" data-fx="pop">
  </div>
  <div id="b4">
    <div class="bk" style="top:190px" data-in="47.9" data-fx="up">Saya nak jujur</div>
    <div class="bt" style="top:240px;font-size:64px" data-in="51.4" data-fx="up">Kajian jenama lain <span class="hl" data-hl="53.8">≠ jaminan produk kami.</span></div>
    <div class="badge" style="left:60px;top:450px" data-in="53.8" data-fx="left"><b style="background:#E4472B">✗</b>Copy-paste success rate</div>
    <div class="badge" style="left:60px;top:550px" data-in="58.0" data-fx="left"><b style="background:#E4472B">✗</b>Jaminan sembuh ekzema / luka</div>
  </div>
  <div id="b5">
    <div class="bk" style="top:190px" data-in="86.2" data-fx="up">Nak faham CURALLÉ?</div>
    <div class="bt" style="top:240px;font-size:96px" data-in="89.4" data-fx="pop"><span class="hl" data-hl="91.0">curalle.co</span></div>
    <div class="badge" style="left:60px;top:450px;background:#25D366;color:#fff" data-in="93.6" data-fx="pop"><b style="background:#fff;color:#25D366">✆</b>WhatsApp kami</div>
  </div>
  <div id="b6">
    <div class="bk" style="top:190px" data-in="95.9" data-fx="up">Video seterusnya</div>
    <div class="bt" style="top:240px;font-size:68px" data-in="98.5" data-fx="up">Postbiotik <span class="hl" data-hl="99.9">apa</span> yang CURALLÉ guna?</div>
    <div class="badge" style="left:60px;top:470px;background:#FFE14D" data-in="100.8" data-fx="pop" id="nx6"><b style="background:#1B1B1B">▶</b>Tunggu video seterusnya</div>
  </div>
  <div id="b7">
    <div class="bt" style="top:300px;text-align:center;width:960px" data-in="103.6" data-fx="pop">Terima kasih kerana menonton!</div>
  </div>
</div>
'''

BANDS = "[['b1',0,13.0],['b2',13.0,17.2],['b3',40.6,47.7],['b4',47.7,65.4],['b5',85.9,95.7],['b6',95.7,103.4],['b7',103.4,999]]"
CHAPTERS = "[['Soalan',0],['Sains',17.4],['Jujur',40.9],['Pesanan',65.6],['Ikuti',86.1]]"
LOW = "[[0,1]]"
ZOOM = "[[0,10.2,0,.04],[13.2,17.2,0,.03],[40.9,47.6,0,.05],[47.8,65.3,0,.1],[86.1,109.6,0,.07]]"

TILES = r'''
  <!-- T1: postbiotics depend on the organism and the process (0,0) -->
  <div class="tile" id="T1" style="left:0;top:0">
    <div class="kicker" style="left:70px;top:250px" data-in="17.4" data-fx="up"><span style="background:var(--yellow);color:var(--deep);padding:2px 12px;border-radius:6px">Fun fact</span></div>
    <div class="title" style="left:70px;top:300px;width:620px;font-size:58px">
      <div data-in="18.4" data-fx="up">Postbiotik bukan</div>
      <div data-in="19.8" data-fx="up"><span class="hl" data-hl="20.4">bahan kimia ringkas.</span></div>
    </div>
    <div class="body" style="left:70px;top:470px;width:600px;font-size:34px" data-in="22.6" data-fx="up">Ia bergantung kepada:</div>
    <div class="card" style="left:70px;top:720px;width:940px;height:400px" data-in="24.4" data-fx="card">
      <div class="num" style="left:40px;top:40px">1</div>
      <div style="left:160px;top:50px;font-family:Playfair;font-weight:900;font-size:50px">Identiti mikroorganisma</div>
      <svg style="left:160px;top:150px" width="740" height="220" viewBox="0 0 740 220" id="strain1"></svg>
    </div>
    <div class="card" style="left:70px;top:1150px;width:940px;height:400px" data-in="27.4" data-fx="card">
      <div class="num" style="left:40px;top:40px">2</div>
      <div style="left:160px;top:50px;font-family:Playfair;font-weight:900;font-size:50px">Cara ia diproses</div>
      <svg style="left:160px;top:150px" width="740" height="220" viewBox="0 0 740 220" id="proc1"></svg>
    </div>
  </div>

  <!-- T2: different process -> different actives -> same label, different "magic" (1300,0) -->
  <div class="tile" id="T2" style="left:1300px;top:0">
    <div class="kicker" style="left:70px;top:250px" data-in="29.0" data-fx="up">Proses berbeza</div>
    <div class="title" style="left:70px;top:300px;width:620px;font-size:72px">
      <div data-in="31.6" data-fx="up">= komponen aktif</div>
      <div data-in="32.9" data-fx="up">&amp; kesan <span class="hl" data-hl="33.5">berbeza.</span></div>
    </div>
    <svg style="left:60px;top:600px" width="960" height="560" viewBox="0 0 960 560" id="flow2"></svg>
    <div class="card" style="left:70px;top:1200px;width:940px;height:330px" data-in="34.4" data-fx="card">
      <svg style="left:60px;top:30px" width="300" height="270" viewBox="0 0 300 270" id="btlA"></svg>
      <svg style="left:580px;top:30px" width="300" height="270" viewBox="0 0 300 270" id="btlB"></svg>
      <div style="left:330px;top:110px;width:280px;text-align:center;font-family:Playfair;font-weight:900;font-size:90px;color:var(--red)">≠</div>
    </div>
    <div class="tag red" style="left:240px;top:1560px;font-size:46px;transform-origin:center" data-in="38.9" data-fx="stamp" data-rot="-3">Label sama ≠ "magic" sama</div>
  </div>

  <!-- T3: my advice - read the full ingredient list (2600,0) -->
  <div class="tile" id="T3" style="left:2600px;top:0">
    <div class="kicker" style="left:70px;top:250px" data-in="65.6" data-fx="up"><span style="background:var(--yellow);color:var(--deep);padding:2px 12px;border-radius:6px">Pesanan saya</span></div>
    <div class="title" style="left:70px;top:300px;width:620px;font-size:72px">
      <div data-in="67.2" data-fx="up">Bila survey</div>
      <div data-in="68.2" data-fx="up">skincare…</div>
    </div>
    <div class="chip no" style="left:70px;top:720px;font-size:34px" data-in="69.6" data-fx="left"><b>✗</b>Sekadar tanya "ada postbiotik tak?"</div>
    <div class="chip" style="left:70px;top:820px;font-size:34px" data-in="73.2" data-fx="left"><b>✓</b>Semak senarai penuh bahan</div>
    <div class="card" style="left:70px;top:940px;width:940px;height:620px" data-in="73.6" data-fx="card">
      <div class="lbl" style="left:40px;top:34px">Contoh senarai bahan (ilustrasi)</div>
      <svg style="left:40px;top:80px" width="774" height="522" viewBox="0 0 860 580" id="ing3"></svg>
    </div>
    <div class="hand" style="left:260px;top:1590px;font-size:58px;transform-origin:center" data-in="82.0" data-fx="pop" data-rot="-3">bahan lain boleh trigger alahan!</div>
  </div>
'''

OVERLAYS = ''
OV = "[]"
TP = "{T1:[0,0],T2:[1300,0],T3:[2600,0]}"
ORDER = "['T1','T2','T3']"

CAM = r'''const CAM=[
 [0,...C('T1'),1],[17.0,...C('T1'),1],[28.4,...C('T1'),1.03],
 [28.8,...mid('T1','T2'),.62],[29.25,...C('T2'),1],[37.0,...C('T2'),1],[37.6,...C('T2',540,1120),1.06],[40.5,...C('T2',540,1120),1.06],
 [62.0,...C('T3'),1],[78.0,...C('T3'),1],[78.8,...C('T3',540,1180),1.06],[85.8,...C('T3',540,1180),1.06],[109.6,...C('T3'),1]
];'''

MODE = "[[0,1],[17.0,1],[17.45,0],[40.6,0],[41.0,1],[65.3,1],[65.7,0],[85.8,0],[86.2,1]]"
PUNCH = "[[11.3,.08],[13,0],[53.8,.06],[58,.0],[60.2,.07],[65,0],[89.4,.05],[95,0]]"
BR = "[]"

ILLUSTRATIONS_PRE = ""
ILLUSTRATIONS = r'''
// T1 three different strains
const st1=$('strain1');const strains1=[['#9A74D0','Strain A'],['#F2C14E','Strain B'],['#8CC63F','Strain C']].map(([c,s],i)=>{
  const g=el(st1,'g',{transform:`translate(${120+i*250} 90)`});
  if(i===0)el(g,'rect',{x:-60,y:-24,width:120,height:48,rx:24,fill:c,stroke:'#1B1B1B','stroke-width':4});
  else if(i===1){for(let k=0;k<4;k++)el(g,'circle',{cx:-45+k*30,cy:0,r:16,fill:c,stroke:'#1B1B1B','stroke-width':4});}
  else el(g,'path',{d:'M-60 0 q15 -30 30 0 t30 0 t30 0 t30 0',fill:'none',stroke:c,'stroke-width':18,'stroke-linecap':'round'});
  txt(g,0,80,s,{'font-size':24});return g;});
// T1 process steps
const pr1=$('proc1');const steps1=['Fermentasi','Haba / lisis','Penapisan'].map((s,i)=>{const g=el(pr1,'g',{transform:`translate(${100+i*270} 90)`});
  el(g,'circle',{cx:0,cy:0,r:56,fill:'#E9DDF6',stroke:'#6A3FA0','stroke-width':5});txt(g,0,10,String(i+1),{'font-family':'Playfair','font-size':44,fill:'#3E1F6B'});
  txt(g,0,100,s,{'font-size':24});if(i<2)el(pr1,'path',{d:`M${170+i*270} 90 h60`,stroke:'#1B1B1B','stroke-width':6,'stroke-linecap':'round'});return g;});
// T2 one strain, two processes, two different sets of actives
const f2=$('flow2');
el(f2,'rect',{x:380,y:20,width:200,height:90,rx:45,fill:'#9A74D0',stroke:'#1B1B1B','stroke-width':5});txt(f2,480,76,'Bakteria',{'font-size':28,fill:'#fff'});
const brA=drawPath(el(f2,'path',{d:'M430 110 C 380 200, 250 220, 220 300',fill:'none',stroke:'#1B1B1B','stroke-width':6,'stroke-linecap':'round'}),30.0,.6);
const brB=drawPath(el(f2,'path',{d:'M530 110 C 580 200, 710 220, 740 300',fill:'none',stroke:'#1B1B1B','stroke-width':6,'stroke-linecap':'round'}),30.2,.6);
const pA=el(f2,'g',{});el(pA,'rect',{x:110,y:300,width:220,height:70,rx:12,fill:'#FBF7EE',stroke:'#6A3FA0','stroke-width':4});txt(pA,220,345,'Proses 1',{'font-size':26,fill:'#3E1F6B'});
const pB=el(f2,'g',{});el(pB,'rect',{x:630,y:300,width:220,height:70,rx:12,fill:'#FBF7EE',stroke:'#2a6a85','stroke-width':4});txt(pB,740,345,'Proses 2',{'font-size':26,fill:'#2a6a85'});
const outA=[...Array(5)].map((_,i)=>el(f2,'circle',{cx:150+i*36,cy:450+(i%2)*30,r:14,fill:'#E4472B'}));
const outB=[...Array(5)].map((_,i)=>el(f2,'rect',{x:660+i*36,y:436+(i%2)*30,width:26,height:26,rx:4,fill:'#D99A1E'}));
txt(f2,220,540,'KOMPONEN AKTIF X',{'font-size':22,'letter-spacing':3});txt(f2,740,540,'KOMPONEN AKTIF Y',{'font-size':22,'letter-spacing':3});
// T2 two bottles with the same label
function bottle(svg,fillC){el(svg,'rect',{x:105,y:10,width:90,height:40,rx:8,fill:'#1B1B1B'});
  el(svg,'rect',{x:60,y:50,width:180,height:210,rx:30,fill:'#fff',stroke:'#1B1B1B','stroke-width':6});
  el(svg,'rect',{x:60,y:110,width:180,height:70,fill:'#E9DDF6'});txt(svg,150,155,'POSTBIOTIC',{'font-size':22,fill:'#3E1F6B'});
  const inside=[...Array(6)].map((_,i)=>el(svg,'circle',{cx:95+(i%3)*55,cy:215+Math.floor(i/3)*24,r:9,fill:fillC,opacity:0}));return inside;}
const inA=bottle($('btlA'),'#E4472B'), inB=bottle($('btlB'),'#D99A1E');
// T3 ingredient list with a magnifier; one line gets flagged
const i3=$('ing3');const ingNames=['Aqua','Glycerin','Postbiotic ferment lysate','Ceramide NP','Colloidal oatmeal','Panthenol','Fragrance (parfum)','Preservative'];
const ingRows=ingNames.map((s,i)=>{const g=el(i3,'g',{});el(g,'text',{x:20,y:50+i*64,'font-family':'Inter','font-weight':600,'font-size':32,fill:'#3d3830'},s);
  const hl=el(g,'rect',{x:6,y:12+i*64,width:600,height:52,rx:8,fill:i===2?'#FFE14D':'#E4472B',opacity:0});g.insertBefore(hl,g.firstChild);return {g,hl};});
const mag3=el(i3,'g',{});el(mag3,'circle',{cx:0,cy:0,r:70,fill:'rgba(255,255,255,.2)',stroke:'#1B1B1B','stroke-width':10});el(mag3,'line',{x1:50,y1:50,x2:110,y2:110,stroke:'#1B1B1B','stroke-width':18,'stroke-linecap':'round'});
const warn3=el(i3,'g',{opacity:0});el(warn3,'circle',{cx:680,cy:422,r:34,fill:'#E4472B'});txt(warn3,680,436,'!',{'font-family':'Playfair','font-size':48,fill:'#fff'});
'''

FRAME = r'''
  strains1.forEach((g,i)=>{const k=P(t,24.6+i*.3,.4);g.style.opacity=k;});
  steps1.forEach((g,i)=>{const k=P(t,27.6+i*.3,.4);g.style.opacity=k;});
  pA.style.opacity=P(t,30.5,.3);pB.style.opacity=P(t,30.7,.3);
  outA.forEach((c,i)=>c.style.opacity=P(t,32.4+i*.08,.2));outB.forEach((c,i)=>c.style.opacity=P(t,32.6+i*.08,.2));
  inA.forEach((c,i)=>c.style.opacity=P(t,36.6+i*.06,.2));inB.forEach((c,i)=>c.style.opacity=P(t,37.0+i*.06,.2));
  // magnifier scans down the list, highlights the postbiotic, then flags the fragrance line
  const sc3=P(t,74.0,6.5);const row=Math.min(7,Math.floor(sc3*8));
  mag3.setAttribute('transform',`translate(${640+Math.sin(t*2)*20} ${40+sc3*7*64})`);mag3.style.opacity=t>73.8&&t<86?1:0;
  ingRows.forEach((r,i)=>{r.hl.setAttribute('opacity',i===2?.85*P(t,75.2,.4):i===6?.35*P(t,81.6,.4):0);});
  warn3.style.opacity=P(t,81.8,.3);
'''

BAND_FRAME = r'''
  {const f=modeAt(t);$('band').style.opacity=clamp(f*1.2-.1);
   BANDS.forEach(([id,a,b])=>{const e=$(id);const v=t>=a&&t<b;e.style.visibility=v?'visible':'hidden';e.style.opacity=v&&t>b-.25?1-P(t,b-.25,.25):1;});
   $('pfill').style.width=`${960*clamp(t/DURATION)}px`;
   CH.forEach(c=>c.el.classList.toggle('on',t>=c.t));
   if(t>100.8){$('nx6').style.transform=`scale(${1+.04*Math.sin((t-100.8)*8)})`;}
  }
'''
