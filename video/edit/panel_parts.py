# Content for panel.html (9:16): Dr Sabrina's message to the panel (clinical co-researcher, CURALLÉ).
# For the panel / grant presentation, not social media: formal English, no sales CTA.
# The source already has burned-in subtitles in the lower third, so graphics stay in the top band.
from honest_parts import EXTRA_CSS

TITLE = 'Dr Sabrina Panel Message 9:16'
DURATION = 51.0
OUTPUT = 'output/curalle_panel_drsabrina_9x16.mp4'
NFR = 1510
PIPNAME = 'Dr Sabrina · Dermatologist'
# 576x1024 source upscaled to 1080x1920: head top ~510, face centre ~(460,700)
FRAMING = {'pip': (460, 700), 'full': (470, 900), 'head_top': 500, 'band_bottom': 610}   # head tucks just under the band so the burned-in subtitles stay in frame

BAND = r'''
<div id="band">
  <div id="prog"><div class="track"></div><div class="fill" id="pfill"></div></div>
  <div id="b1">
    <div class="bk" style="top:180px" data-in="0.2" data-fx="up">A message to the panel</div>
    <div class="bt" style="top:230px" data-in="2.2" data-fx="up">Dr <span class="hl" data-hl="2.6">Sabrina</span></div>
    <div class="badge" style="left:60px;top:370px" data-in="3.9" data-fx="left"><b style="background:#6A3FA0">✚</b>Consultant Dermatologist</div>
    <div class="badge" style="left:60px;top:460px" data-in="5.0" data-fx="left"><b style="background:#2a6a85">H</b>Hospital Al-Sultan Abdullah</div>
    <div class="badge" style="left:60px;top:550px" data-in="6.7" data-fx="left"><b style="background:#D99A1E">✓</b>Clinical co-researcher · CURALLÉ</div>
  </div>
  <div id="b2">
    <div class="bk" style="top:180px" data-in="29.4" data-fx="up">CURALLÉ is designed to fill the gap</div>
    <div class="bt" style="top:230px" data-in="31.8" data-fx="up">A <span class="hl" data-hl="32.1">daily moisturiser</span></div>
    <div class="badge" style="left:60px;top:400px" data-in="33.1" data-fx="left"><b style="background:#5E9A1E">✓</b>Used alongside medical treatment</div>
    <div class="badge" style="left:60px;top:500px" data-in="34.7" data-fx="left"><b style="background:#E4472B">✗</b>Not a replacement for it</div>
  </div>
  <div id="b3">
    <div class="bk" style="top:180px" data-in="46.8" data-fx="up">Dr Sabrina</div>
    <div class="bt" style="top:230px;font-size:64px" data-in="47.0" data-fx="up">“I fully support this project and its <span class="hl" data-hl="48.9">path to the patients.</span>”</div>
    <div class="badge" style="left:60px;top:500px" data-in="50.0" data-fx="pop"><b style="background:#6A3FA0">♥</b>Thank you</div>
  </div>
</div>
'''
BANDS = "[['b1',0,10.0],['b2',29.2,35.5],['b3',46.6,999]]"
CHAPTERS = "[['Intro',0],['Need',10.1],['CURALLÉ',29.3],['Study',35.6],['Support',46.7]]"
LOW = "[[0,1]]"
ZOOM = "[[0,9.9,0,.02],[29.4,35.4,0,.03],[46.8,51.0,0,.03]]"

TILES = r'''
  <!-- T1: steroids for flares, daily barrier care in between (0,0) -->
  <div class="tile" id="T1" style="left:0;top:0">
    <div class="kicker" style="left:70px;top:250px" data-in="10.1" data-fx="up">In my clinic</div>
    <div class="title" style="left:70px;top:300px;width:620px;font-size:58px">
      <div data-in="12.5" data-fx="up">Flares need steroids.</div>
      <div data-in="14.4" data-fx="up">Between flares, the barrier</div>
      <div data-in="15.8" data-fx="up">still needs <span class="hl" data-hl="15.9">daily care.</span></div>
    </div>
    <div class="card" style="left:70px;top:680px;width:940px;height:760px" data-in="11.2" data-fx="card">
      <div class="lbl" style="left:40px;top:34px">Eczema activity over time</div>
      <svg style="left:20px;top:90px" width="900" height="640" viewBox="0 0 900 640" id="chart1"></svg>
    </div>
  </div>

  <!-- T2: patient concerns and the lack of options (1300,0) -->
  <div class="tile" id="T2" style="left:1300px;top:0">
    <div class="kicker" style="left:70px;top:250px" data-in="18.0" data-fx="up">What patients ask</div>
    <div class="card" style="left:70px;top:320px;width:620px;height:150px" data-in="18.2" data-fx="left">
      <div style="left:36px;top:30px;width:560px;font-family:Playfair;font-weight:900;font-size:40px;line-height:1.15">“Is long-term steroid use safe?”</div>
    </div>
    <div class="card" style="left:70px;top:500px;width:620px;height:110px" data-in="20.4" data-fx="left">
      <div style="left:36px;top:28px;width:560px;font-family:Playfair;font-weight:900;font-size:40px">“Is this product halal?”</div>
    </div>
    <div class="card" style="left:70px;top:680px;width:940px;height:780px" data-in="22.3" data-fx="card">
      <div class="lbl" style="left:40px;top:36px;color:var(--red)">Very few options are</div>
      <div class="chip" style="left:40px;top:110px" data-in="25.0" data-fx="left"><b>✓</b>Steroid-free</div>
      <div class="chip" style="left:40px;top:230px" data-in="26.4" data-fx="left"><b>✓</b>Halal</div>
      <div class="chip" style="left:40px;top:350px" data-in="27.1" data-fx="left"><b>✓</b>Comfortable in our hot, humid climate</div>
      <svg style="left:40px;top:500px" width="860" height="240" viewBox="0 0 860 240" id="gap2"></svg>
    </div>
  </div>

  <!-- T3: the clinical study (2600,0) -->
  <div class="tile" id="T3" style="left:2600px;top:0">
    <div class="kicker" style="left:70px;top:250px" data-in="35.6" data-fx="up">My role: clinical lead</div>
    <div class="card" style="left:70px;top:320px;width:620px;height:110px" data-in="36.9" data-fx="left">
      <div class="num" style="left:20px;top:7px;width:96px;height:96px">1</div>
      <div style="left:140px;top:32px;font-size:34px;font-weight:800">Screening &amp; recruitment</div>
    </div>
    <div class="card" style="left:70px;top:460px;width:620px;height:110px" data-in="38.7" data-fx="left">
      <div class="num" style="left:20px;top:7px;width:96px;height:96px">2</div>
      <div style="left:140px;top:34px;font-size:30px;font-weight:800;white-space:nowrap">SCORAD assessment</div>
    </div>
    <div class="card" style="left:70px;top:600px;width:620px;height:110px" data-in="40.8" data-fx="left">
      <div class="num" style="left:20px;top:7px;width:96px;height:96px">3</div>
      <div style="left:140px;top:32px;font-size:34px;font-weight:800">Safety monitoring</div>
    </div>
    <div class="card" style="left:70px;top:770px;width:940px;height:720px" data-in="41.8" data-fx="card">
      <div class="lbl" style="left:40px;top:36px;color:var(--purple)">Clinical study</div>
      <div style="left:40px;top:80px;font-family:Playfair;font-weight:900;font-size:150px;line-height:1;color:var(--deep)" id="n60">0</div>
      <div style="left:260px;top:140px;font-size:36px;font-weight:800">participants</div>
      <svg style="left:40px;top:250px" width="860" height="240" viewBox="0 0 860 240" id="dots3"></svg>
      <div class="chip" style="left:40px;top:520px;font-size:30px" data-in="43.3" data-fx="pop"><b>◐</b>Double-blind</div>
      <div class="chip" style="left:340px;top:520px;font-size:30px" data-in="44.0" data-fx="pop"><b>▣</b>Vehicle-controlled</div>
      <div class="chip" style="left:40px;top:620px;font-size:30px" data-in="45.7" data-fx="pop"><b>✓</b>Full ethical approval</div>
    </div>
  </div>
'''

OVERLAYS = ''
OV = "[]"
TP = "{T1:[0,0],T2:[1300,0],T3:[2600,0]}"
ORDER = "['T1','T2','T3']"
CAM = r'''const CAM=[
 [0,...C('T1'),1],[17.4,...C('T1'),1.03],
 [17.75,...mid('T1','T2'),.62],[18.15,...C('T2'),1],[24.6,...C('T2'),1],[25.3,...C('T2',540,1120),1.08],[29.2,...C('T2',540,1120),1.08],
 [33.0,...C('T3'),1],[41.6,...C('T3'),1],[42.3,...C('T3',540,1160),1.08],[46.6,...C('T3',540,1160),1.08],[51.0,...C('T3'),1]
];'''
MODE = "[[0,1],[9.9,1],[10.35,0],[29.0,0],[29.4,1],[35.3,1],[35.75,0],[46.4,0],[46.8,1]]"
PUNCH = "[[2.3,.02],[9.6,0],[32.0,.03],[35,0],[48.9,.03]]"
BR = "[]"

ILLUSTRATIONS_PRE = ""
ILLUSTRATIONS = r'''
// T1 activity curve: flare peaks (steroid) and calm valleys (daily care)
const ch=$('chart1');
el(ch,'line',{x1:40,y1:520,x2:880,y2:520,stroke:'#1B1B1B','stroke-width':4});
el(ch,'line',{x1:40,y1:40,x2:40,y2:520,stroke:'#1B1B1B','stroke-width':4});
txt(ch,860,560,'TIME',{'font-size':20,'letter-spacing':4,'text-anchor':'end'});
const pk=[[180,110],[470,150],[760,120]];
let dd='M40 430';pk.forEach(([x,y],i)=>{dd+=` C ${x-90} 430, ${x-40} ${y}, ${x} ${y} S ${x+90} 430, ${x+140} 430`;});dd+=' L880 430';
const curve=drawPath(el(ch,'path',{d:dd,fill:'none',stroke:'#E4472B','stroke-width':8,'stroke-linecap':'round'}),11.4,2.4);
const flareTags=pk.map(([x,y],i)=>{const g=el(ch,'g',{opacity:0});el(g,'rect',{x:x-80,y:y-70,width:160,height:46,rx:23,fill:'#E4472B'});txt(g,x,y-38,'Steroid',{'font-size':22,fill:'#fff'});return g;});
const valley=[[250,400],[540,690]].map(([x0,x1])=>{const g=el(ch,'g',{opacity:0});
  el(g,'rect',{x:x0,y:360,width:x1-x0,height:160,rx:12,fill:'#6A3FA0',opacity:.18});
  el(g,'rect',{x:x0+6,y:470,width:x1-x0-12,height:40,rx:20,fill:'#6A3FA0'});txt(g,(x0+x1)/2,498,'Daily care',{'font-size':20,fill:'#fff'});return g;});
// T2 a small bar showing how few options tick all three boxes
const g2=$('gap2');
txt(g2,0,30,'OPTIONS THAT TICK ALL THREE',{'font-size':20,'letter-spacing':3,'text-anchor':'start'});
el(g2,'rect',{x:0,y:60,width:860,height:40,rx:20,fill:'#E6DCC8'});
const gbar=el(g2,'rect',{x:0,y:60,width:0,height:40,rx:20,fill:'#E4472B'});
const gT=el(g2,'text',{x:0,y:170,'font-family':'Caveat','font-weight':700,'font-size':56,fill:'#E4472B'},'very few…');
// T3 sixty participant dots
const d3=$('dots3');const pdots=[];
for(let i=0;i<60;i++){const c=el(d3,'circle',{cx:30+(i%15)*56,cy:40+Math.floor(i/15)*56,r:20,fill:'#E6DCC8'});pdots.push(c);}
'''

FRAME = r'''
  flareTags.forEach((g,i)=>g.style.opacity=P(t,12.8+i*.35,.3));
  valley.forEach((g,i)=>g.style.opacity=P(t,14.5+i*.4,.4));
  gbar.setAttribute('width',860*.12*out3(P(t,22.6,.8)));gT.style.opacity=P(t,23.6,.3);
  const k3=P(t,42.2,1.0);$('n60').textContent=Math.round(60*out3(k3));
  pdots.forEach((c,i)=>{const on=i<Math.round(60*out3(k3));c.setAttribute('fill',on?(i%2?'#6A3FA0':'#9A74D0'):'#E6DCC8');});
'''

BAND_FRAME = r'''
  {const f=modeAt(t);$('band').style.opacity=clamp(f*1.2-.1);
   BANDS.forEach(([id,a,b])=>{const e=$(id);const v=t>=a&&t<b;e.style.visibility=v?'visible':'hidden';e.style.opacity=v&&t>b-.25?1-P(t,b-.25,.25):1;});
   $('pfill').style.width=`${960*clamp(t/DURATION)}px`;
   CH.forEach(c=>c.el.classList.toggle('on',t>=c.t));
  }
'''
