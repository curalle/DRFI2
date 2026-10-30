# Content for honest.html (9:16): "jujur, tak semua feedback positif" (CURALLÉ Skin Rebalance).
# Two looks: a dark title band over the top ~38% of the frame while the presenter is full screen
# (framed lower so the band sits above the head), and Vox paper tiles with a floating frame.

TITLE = 'CURALLE Honest Review 9:16'
DURATION = 118.3
OUTPUT = 'output/curalle_honest_9x16.mp4'
NFR = 3520
PIPNAME = 'Ts. Dr Fareez Ismail · CURALLÉ'

# presenter framing (source px): face centre for the floating frame, full-screen centre, head top
FRAMING = {'pip': (430, 720), 'full': (482, 880), 'head_top': 330, 'band_bottom': 720}

EXTRA_CSS = r'''
#band{position:absolute;left:0;top:0;width:1080px;height:860px;pointer-events:none;opacity:0;
  background:linear-gradient(180deg,#1E1236 0,#1E1236 52%,rgba(30,18,54,.86) 70%,rgba(30,18,54,0) 100%)}
#band .bk{position:absolute;left:60px;font-weight:800;font-size:28px;letter-spacing:7px;text-transform:uppercase;color:#FFE14D;white-space:nowrap}
#band .bt{position:absolute;left:60px;width:960px;font-family:Playfair;font-weight:900;font-size:76px;line-height:1.06;color:#fff}
#band .bt .hl{color:#FFE14D;background-image:linear-gradient(transparent 84%,#FFE14D 84%,#FFE14D 95%,transparent 95%)}
#band .badge{position:absolute;display:flex;align-items:center;gap:14px;font-weight:800;font-size:34px;color:#1B1B1B;background:#FBF7EE;padding:12px 24px 12px 12px;border-radius:999px;white-space:nowrap;box-shadow:0 10px 24px rgba(0,0,0,.35)}
#band .badge b{display:inline-flex;align-items:center;justify-content:center;width:48px;height:48px;border-radius:50%;color:#fff;font-size:26px}
#band .step{position:absolute;left:60px;display:flex;align-items:center;gap:18px}
#band .step .n{width:84px;height:84px;border-radius:18px;background:#FFE14D;color:#1E1236;font-family:Playfair;font-weight:900;font-size:52px;display:flex;align-items:center;justify-content:center;transform:rotate(-4deg)}
#band .step .s{font-weight:800;font-size:30px;letter-spacing:6px;color:#fff;text-transform:uppercase}
#prog{position:absolute;left:60px;top:70px;width:960px;height:56px}
#prog .track{position:absolute;left:0;top:22px;width:960px;height:10px;border-radius:99px;background:rgba(255,255,255,.18)}
#prog .fill{position:absolute;left:0;top:22px;height:10px;border-radius:99px;background:#FFE14D;width:0}
#prog .tick{position:absolute;top:0;transform:translateX(-50%);text-align:center}
#prog .tick i{display:block;width:24px;height:24px;margin:15px auto 0;border-radius:50%;background:#3a2a5c;border:4px solid rgba(255,255,255,.35)}
#prog .tick span{display:block;margin-top:8px;font-weight:800;font-size:16px;letter-spacing:3px;color:rgba(255,255,255,.55);text-transform:uppercase;white-space:nowrap}
#prog .tick.on i{background:#FFE14D;border-color:#FFE14D}
#prog .tick.on span{color:#FFE14D}
.dots{position:absolute;display:flex;gap:18px}
.dots i{display:block;width:54px;height:54px;border-radius:50%;border:5px solid #FFE14D;background:transparent}
.bar{position:absolute;height:22px;border-radius:99px;background:rgba(255,255,255,.18);overflow:hidden}
.bar>div{position:absolute;left:0;top:0;bottom:0;border-radius:99px;background:#FFE14D;width:0}
'''

# band content: everything here is positioned inside the top band (y < ~700)
BAND = r'''
<div id="band">
  <div id="prog"><div class="track"></div><div class="fill" id="pfill"></div></div>

  <div id="b1">
    <div class="bk" style="top:190px" data-in="0.6" data-fx="up">Jujur saya katakan</div>
    <div class="bt" style="top:240px" data-in="2.2" data-fx="up">Tak semua feedback <span class="hl" data-hl="3.8">positif.</span></div>
    <div class="badge" style="left:60px;top:430px" data-in="7.9" data-fx="left"><b style="background:#5E9A1E">✓</b>Ada yang terus lega</div>
    <div class="badge" style="left:60px;top:530px" data-in="11.6" data-fx="left"><b style="background:#E4472B">✗</b>Ada yang rasa tak berkesan</div>
  </div>
  <div id="b2">
    <div class="bk" style="top:190px" data-in="13.4" data-fx="up">Honestly</div>
    <div class="bt" style="top:240px" data-in="15.5" data-fx="up">Ini bukan krim <span class="hl" data-hl="16.3">"ajaib".</span></div>
    <div class="badge" style="left:60px;top:430px" data-in="17.4" data-fx="left"><b style="background:#E4472B">✗</b>Sapu sekali, terus hilang</div>
    <div class="badge" style="left:60px;top:530px" data-in="22.8" data-fx="left"><b style="background:#6A3FA0">→</b>Kena faham punca sebenar</div>
  </div>
  <div id="b3">
    <div class="step" style="top:190px" data-in="59.0" data-fx="left"><div class="n">02</div><div class="s">Formula</div></div>
    <div class="bt" style="top:310px" data-in="59.3" data-fx="up">Jadi apa yang CURALLÉ <span class="hl" data-hl="62.4">buat?</span></div>
  </div>
  <div id="b4">
    <div class="step" style="top:190px" data-in="83.8" data-fx="left"><div class="n">03</div><div class="s">Cara guna</div></div>
    <div class="bt" style="top:300px;font-size:150px;line-height:1" data-in="85.9" data-fx="pop">3–4<span style="font-size:80px">× sehari</span></div>
    <div class="dots" style="left:640px;top:330px" id="dots4"><i></i><i></i><i></i><i></i></div>
    <div class="badge" style="left:60px;top:500px" data-in="89.6" data-fx="left"><b style="background:#6A3FA0">↑</b>Lebih kerap ikut tahap keseriusan</div>
  </div>
  <div id="b5">
    <div class="step" style="top:190px" data-in="93.1" data-fx="left"><div class="n">03</div><div class="s">Cara guna</div></div>
    <div class="bt" style="top:300px" data-in="93.3" data-fx="up">Consistency is <span class="hl" data-hl="95.4">the key.</span></div>
    <div class="bar" style="left:60px;top:500px;width:960px" id="bar5"><div></div></div>
    <div class="bk" style="top:550px;color:#fff;letter-spacing:4px;font-size:24px" data-in="96.3" data-fx="up">Pulihkan lapisan pelindung kulit</div>
  </div>
  <div id="b6">
    <div class="bk" style="top:190px" data-in="106.0" data-fx="up">Mula seimbangkan balik</div>
    <div class="bt" style="top:240px" data-in="107.0" data-fx="up"><span class="hl" data-hl="108.4">Microflora</span> &amp; skin barrier</div>
  </div>
  <div id="b7">
    <div class="bk" style="top:190px" data-in="110.8" data-fx="up">Dapatkan sekarang</div>
    <div class="bt" style="top:240px;width:700px" data-in="111.6" data-fx="up">CURALLÉ Skin Rebalance Cream</div>
    <img src="assets/tube_hand_s.png" style="position:absolute;left:780px;top:150px;width:240px;height:400px;object-fit:cover;object-position:top;border-radius:14px;box-shadow:0 14px 30px rgba(0,0,0,.4)" data-in="111.2" data-fx="pop">
    <div class="badge" style="left:60px;top:500px;background:#FFE14D" data-in="113.6" data-fx="pop" id="cta7"><b style="background:#1B1B1B">→</b>Beg kuning / pautan di bio</div>
  </div>
  <div id="b8">
    <div class="bt" style="top:300px;text-align:center;width:960px" data-in="116.3" data-fx="pop">Terima kasih!</div>
  </div>
</div>
'''

BANDS = "[['b1',0,13.2],['b2',13.2,25.0],['b3',58.8,64.4],['b4',83.6,93.0],['b5',93.0,98.3],['b6',105.7,110.6],['b7',110.6,116.2],['b8',116.2,999]]"
CHAPTERS = "[['Punca',0],['Formula',58.9],['Guna',83.7],['Ingat',98.4]]"
# full-screen parts use the band (low framing) throughout; pip parts are Vox tiles
LOW = "[[0,1]]"
ZOOM = "[[0,13,0,.03],[13.3,24.8,0,.09],[58.9,64.3,0,.05],[83.7,98.2,0,.1],[105.8,118.3,0,.08]]"

TILES = r'''
  <!-- T1: every eczema is different (0,0) -->
  <div class="tile" id="T1" style="left:0;top:0">
    <div class="kicker" style="left:70px;top:250px" data-in="25.2" data-fx="up"><span style="background:var(--yellow);color:var(--deep);padding:2px 12px;border-radius:6px">01</span> Punca</div>
    <div class="title" style="left:70px;top:300px;width:600px">
      <div data-in="25.6" data-fx="up">Setiap ekzema</div>
      <div data-in="28.0" data-fx="up"><span class="hl" data-hl="28.6">berbeza.</span></div>
    </div>
    <div class="body" style="left:70px;top:500px;width:600px;font-size:34px" data-in="29.3" data-fx="up">Jenis &amp; <b>tahap keradangan</b> tak sama.</div>
    <div class="card" style="left:70px;top:680px;width:940px;height:780px" data-in="29.4" data-fx="card">
      <svg style="left:0;top:0" width="940" height="780" viewBox="0 0 940 780" id="sev1"></svg>
    </div>
  </div>

  <!-- T2: moisturiser works on the outer layer (1300,0) -->
  <div class="tile" id="T2" style="left:1300px;top:0">
    <div class="kicker" style="left:70px;top:250px" data-in="33.3" data-fx="up">Krim pelembap</div>
    <div class="title" style="left:70px;top:300px;width:600px">
      <div data-in="34.6" data-fx="up">Fokus pada</div>
      <div data-in="35.8" data-fx="up"><span class="hl" data-hl="36.4">lapisan luar.</span></div>
    </div>
    <svg style="left:60px;top:640px" width="960" height="820" viewBox="0 0 960 820" id="skin2"></svg>
  </div>

  <!-- T3: internal inflammation & triggers (2600,0) -->
  <div class="tile" id="T3" style="left:2600px;top:0">
    <div class="kicker" style="left:70px;top:250px;color:var(--red)" data-in="38.0" data-fx="up">Tapi kalau</div>
    <div class="title" style="left:70px;top:300px;width:640px;font-size:62px">
      <div data-in="39.0" data-fx="up">keradangan dalam</div>
      <div data-in="40.6" data-fx="up">badan <span class="hl" data-hl="41.3">mengamuk…</span></div>
    </div>
    <svg style="left:80px;top:620px" width="460" height="900" viewBox="0 0 460 900" id="body3"></svg>
    <div class="lbl" style="left:560px;top:700px" data-in="42.2" data-fx="up">Contohnya</div>
    <div class="chip no" style="left:560px;top:760px;font-size:34px" data-in="44.0" data-fx="left"><b>1</b>Gula tinggi</div>
    <div class="chip no" style="left:560px;top:870px;font-size:34px" data-in="45.3" data-fx="left"><b>2</b>Makanan terproses</div>
    <div class="chip no" style="left:560px;top:980px;font-size:34px" data-in="47.3" data-fx="left"><b>3</b>Alahan diet</div>
    <div class="hand" style="left:560px;top:1130px;font-size:56px;transform-origin:left center" data-in="50.2" data-fx="pop">badan terus<br>keluarkan reaksi!</div>
  </div>

  <!-- T4: outside-only treatment is not enough (2600,1900) -->
  <div class="tile" id="T4" style="left:2600px;top:1900px">
    <div class="kicker" style="left:70px;top:250px" data-in="53.4" data-fx="up">Jadi</div>
    <div class="title" style="left:70px;top:300px;width:620px;font-size:76px">
      <div data-in="53.7" data-fx="up">Rawatan luaran</div>
      <div data-in="55.1" data-fx="up">sahaja <span class="hl" data-hl="55.9">tak cukup.</span></div>
    </div>
    <div class="card" style="left:70px;top:660px;width:430px;height:360px" data-in="54.6" data-fx="pop">
      <div class="lbl" style="left:0;width:430px;top:40px;text-align:center;color:var(--purple)">Luar</div>
      <div style="left:0;width:430px;top:100px;text-align:center;font-family:Playfair;font-weight:900;font-size:120px;color:#5E9A1E">✓</div>
      <div style="left:0;width:430px;top:270px;text-align:center;font-size:30px;font-weight:700">Krim pada kulit</div>
    </div>
    <div class="card" style="left:580px;top:660px;width:430px;height:360px" data-in="57.0" data-fx="pop">
      <div class="lbl" style="left:0;width:430px;top:40px;text-align:center;color:var(--red)">Dalam</div>
      <div style="left:0;width:430px;top:100px;text-align:center;font-family:Playfair;font-weight:900;font-size:120px;color:var(--red)">?</div>
      <div style="left:0;width:430px;top:270px;text-align:center;font-size:30px;font-weight:700">Pencetus dalaman</div>
    </div>
    <div class="tag red" style="left:150px;top:1120px;font-size:46px;transform-origin:center" data-in="58.0" data-fx="stamp" data-rot="-3">Kawal pencetus dalaman juga</div>
  </div>

  <!-- T5: the formula (1300,1900) -->
  <div class="tile" id="T5" style="left:1300px;top:1900px">
    <div class="kicker" style="left:70px;top:250px" data-in="64.4" data-fx="up"><span style="background:var(--yellow);color:var(--deep);padding:2px 12px;border-radius:6px">02</span> Formula</div>
    <img src="assets/logo.png" style="left:64px;top:300px;width:440px;transform-origin:left center" data-in="64.6" data-fx="pop">
    <div class="body" style="left:70px;top:460px;width:600px;font-size:34px" data-in="65.0" data-fx="up">Skin Rebalance Cream</div>
    <div class="abs" style="left:620px;top:640px;width:420px;height:780px;overflow:hidden;-webkit-mask-image:linear-gradient(#000 72%,transparent 98%)" data-in="64.8" data-fx="drop">
      <img src="assets/tube_hand_s.png" style="left:0;top:0;width:420px" class="cut">
    </div>
    <div class="card" style="left:70px;top:640px;width:520px;height:170px" data-in="66.5" data-fx="left">
      <div class="lbl" style="left:30px;top:26px;color:var(--purple)">Postbiotik</div>
      <div style="left:30px;top:70px;width:470px;font-size:30px;font-weight:700;line-height:1.25">Seimbangkan semula bakteria baik</div>
    </div>
    <div class="card" style="left:70px;top:840px;width:520px;height:170px" data-in="71.6" data-fx="left">
      <div class="lbl" style="left:30px;top:26px;color:var(--purple)">Ceramide + Oatmeal koloid</div>
      <div style="left:30px;top:70px;width:470px;font-size:30px;font-weight:700;line-height:1.25">Baiki skin barrier yang rosak</div>
    </div>
    <div class="card" style="left:70px;top:1040px;width:520px;height:170px" data-in="77.2" data-fx="left">
      <div class="lbl" style="left:30px;top:26px;color:var(--purple)">Panthenol</div>
      <div style="left:30px;top:70px;width:470px;font-size:30px;font-weight:700;line-height:1.25">Kunci kelembapan</div>
    </div>
    <div class="tag pur" style="left:70px;top:1270px;font-size:48px;transform-origin:left center" data-in="81.8" data-fx="stamp" data-rot="-3">100% bebas steroid</div>
  </div>

  <!-- T6: recovery = inside + outside (0,1900) -->
  <div class="tile" id="T6" style="left:0;top:1900px">
    <div class="kicker" style="left:70px;top:250px" data-in="98.5" data-fx="up"><span style="background:var(--yellow);color:var(--deep);padding:2px 12px;border-radius:6px">04</span> Ingat</div>
    <div class="title" style="left:70px;top:300px;width:600px">
      <div data-in="98.9" data-fx="up">Pulihkan ekzema</div>
      <div data-in="100.0" data-fx="up">perlu <span class="hl" data-hl="100.7">kombinasi.</span></div>
    </div>
    <div class="card" style="left:70px;top:660px;width:430px;height:420px" data-in="101.4" data-fx="pop">
      <svg style="left:115px;top:40px" width="200" height="200" viewBox="0 0 200 200" id="diet6"></svg>
      <div class="lbl" style="left:0;width:430px;top:262px;text-align:center;color:var(--purple)">Dari dalam</div>
      <div style="left:0;width:430px;top:310px;text-align:center;font-family:Playfair;font-weight:900;font-size:46px">Jaga diet</div>
    </div>
    <div class="abs" style="left:505px;top:820px;font-family:Playfair;font-weight:900;font-size:90px;color:var(--muted)" data-in="102.8" data-fx="pop">+</div>
    <div class="card" style="left:580px;top:660px;width:430px;height:420px" data-in="102.9" data-fx="pop">
      <img src="assets/logo.png" style="left:85px;top:90px;width:260px">
      <div class="lbl" style="left:0;width:430px;top:262px;text-align:center;color:var(--purple)">Dari luar</div>
      <div style="left:0;width:430px;top:310px;text-align:center;font-family:Playfair;font-weight:900;font-size:46px">Lindungi kulit</div>
    </div>
    <div class="tag" style="left:330px;top:1170px;font-size:56px;transform-origin:center" data-in="104.9" data-fx="stamp" data-rot="-3">= kulit pulih</div>
  </div>
'''

OVERLAYS = ''   # everything full-screen lives in the band
OV = "[]"

TP = "{T1:[0,0],T2:[1300,0],T3:[2600,0],T4:[2600,1900],T5:[1300,1900],T6:[0,1900]}"
ORDER = "['T1','T2','T3','T4','T5','T6']"

CAM = r'''const CAM=[
 [0,...C('T1'),1],[24.6,...C('T1'),1],[32.6,...C('T1'),1.03],
 [33.0,...mid('T1','T2'),.62],[33.4,...C('T2'),1],[37.5,...C('T2'),1.03],
 [37.8,...mid('T2','T3'),.62],[38.2,...C('T3'),1],[49.8,...C('T3'),1],[50.5,...C('T3',540,1100),1.1],[52.9,...C('T3',540,1100),1.1],
 [53.25,...mid('T3','T4'),.62],[53.7,...C('T4'),1],[58.6,...C('T4'),1.03],
 [63.5,...C('T5'),1],[83.4,...C('T5'),1.03],
 // "Ingat": pull back over the whole story, then land on the summary tile
 [96.5,1840,1440,.3],[98.0,1840,1440,.3],[98.7,...C('T6'),1],[105.6,...C('T6'),1.03],[118.3,...C('T6'),1.03]
];'''

MODE = "[[0,1],[25.0,1],[25.45,0],[58.65,0],[59.05,1],[64.2,1],[64.6,0],[83.5,0],[83.9,1],[98.1,1],[98.5,0],[105.5,0],[105.9,1]]"
PUNCH = "[[3.8,.05],[13,0],[16.2,.07],[24,0],[86.0,.06],[93,0],[95.4,.08],[98,0],[113.8,.05]]"

BR = "[]"

ILLUSTRATIONS = r'''
// T1 three people, three severity levels
const sv=$('sev1');
[['Ringan',.3,'#8CC63F'],['Sederhana',.6,'#F2C14E'],['Teruk',.92,'#E4472B']].forEach(([s,v,c],i)=>{
  const y=90+i*230;const g=el(sv,'g',{});
  el(g,'circle',{cx:110,cy:y+40,r:44,fill:'#F4D3C2',stroke:'#C79A86','stroke-width':4});
  el(g,'path',{d:`M60 ${y+150} q50 -70 100 0`,fill:'#F4D3C2',stroke:'#C79A86','stroke-width':4});
  for(let k=0;k<Math.round(v*6);k++)el(g,'circle',{cx:90+(k%3)*18,cy:y+30+Math.floor(k/3)*20,r:6,fill:c,opacity:.8});
  el(g,'text',{x:210,y:y+30,'font-family':'Inter','font-weight':800,'font-size':30,fill:'#1B1B1B'},s);
  el(g,'rect',{x:210,y:y+60,width:660,height:30,rx:15,fill:'#E6DCC8'});
  const b=el(g,'rect',{x:210,y:y+60,width:0,height:30,rx:15,fill:c});b.dataset.v=v;b.dataset.i=i;sevBars.push(b);
});
// T2 skin section with a cream layer sitting on top
const s2=$('skin2');
el(s2,'rect',{x:0,y:300,width:960,height:520,fill:'#F6D9CA'});
el(s2,'rect',{x:0,y:560,width:960,height:260,fill:'#EFBFAA'});
for(let r=0;r<2;r++)for(let c=0;c<8;c++){const off=r%2?-60:0;el(s2,'rect',{x:c*125+off+4,y:220+r*46,width:116,height:40,rx:6,fill:['#6A3FA0','#9A7AC4'][r]});}
txt(s2,860,350,'LAPISAN LUAR',{'font-size':22,'letter-spacing':4,fill:'#fff'});
const cream2=el(s2,'path',{d:'M0 220 C 120 150, 240 190, 360 160 S 600 150, 720 170 S 900 150, 960 200 L960 222 L0 222Z',fill:'#FBF7EE',stroke:'#C9C0AE','stroke-width':4,opacity:0});
const arr2=drawPath(el(s2,'path',{d:'M760 40 C 700 60, 640 100, 610 150',fill:'none',stroke:'#E4472B','stroke-width':8,'stroke-linecap':'round'}),36.2,.5);
const arr2t=el(s2,'text',{x:770,y:40,'font-family':'Caveat','font-weight':700,'font-size':54,fill:'#E4472B'},'krim di sini');
const deep2=txt(s2,480,700,'keradangan lebih dalam?',{'font-family':'Caveat','font-weight':700,'font-size':52,fill:'#a0503c'});
// T3 body with internal fire
const b3=$('body3');
el(b3,'circle',{cx:230,cy:110,r:90,fill:'#F4D3C2',stroke:'#C79A86','stroke-width':6});
el(b3,'path',{d:'M90 230 h280 l50 330 h-50 l-40 -240 v540 h-90 v-330 h-20 v330 h-90 v-540 l-40 240 h-50 z',fill:'#F4D3C2',stroke:'#C79A86','stroke-width':6,'stroke-linejoin':'round'});
const fires3=[[230,380,1],[180,470,.8],[280,480,.8],[230,560,.7]].map(([x,y,s])=>el(b3,'path',{d:`M${x} ${y+40*s} c${-40*s} 0 ${-56*s} ${-32*s} ${-40*s} ${-64*s} c${8*s} ${-16*s} ${24*s} ${-24*s} ${24*s} ${-48*s} c${24*s} ${16*s} ${48*s} ${40*s} ${48*s} ${72*s} c${8*s} ${-8*s} ${8*s} ${-16*s} ${8*s} ${-24*s} c${16*s} ${16*s} ${24*s} ${32*s} ${16*s} ${48*s} c${-8*s} ${12*s} ${-32*s} ${16*s} ${-56*s} ${16*s}z`,fill:'#E4472B',opacity:0}));
const rings3=[0,1,2].map(i=>el(b3,'circle',{cx:230,cy:470,r:40,fill:'none',stroke:'#E4472B','stroke-width':5,opacity:0}));
// T6 a simple plate for "jaga diet"
const d6=$('diet6');
el(d6,'circle',{cx:100,cy:100,r:90,fill:'#fff',stroke:'#1B1B1B','stroke-width':6});
el(d6,'circle',{cx:100,cy:100,r:62,fill:'none',stroke:'#E6DCC8','stroke-width':4});
el(d6,'path',{d:'M70 80 q20 -30 40 0 q-20 30 -40 0z',fill:'#8CC63F'});el(d6,'circle',{cx:122,cy:118,r:18,fill:'#E4472B'});el(d6,'path',{d:'M66 122 h40',stroke:'#F2C14E','stroke-width':14,'stroke-linecap':'round'});
'''
ILLUSTRATIONS_PRE = "const sevBars=[];"

FRAME = r'''
  // T1 severity bars fill
  sevBars.forEach(b=>{const k=out3(P(t,29.8+(+b.dataset.i)*.5,1.0));b.setAttribute('width',660*(+b.dataset.v)*k);});
  // T2 cream settles on top, "deeper" hint later
  cream2.style.opacity=P(t,35.4,.6);cream2.setAttribute('transform',`translate(0 ${(1-out3(P(t,35.4,.6)))*-60})`);arr2t.style.opacity=P(t,36.4,.3);deep2.style.opacity=P(t,37.2,.3);
  // T3 inflammation flares and radiates
  fires3.forEach((f,i)=>f.style.opacity=P(t,40.9+i*.2,.4)*(.65+.35*Math.sin(t*9+i)));
  rings3.forEach((r,i)=>{const ph=((t-49.6+i*.5)%1.5)/1.5;const on=t>49.6;r.setAttribute('r',40+ph*200);r.style.opacity=on?.8*(1-ph):0;});
'''

BAND_FRAME = r'''
  // top band: visible whenever the presenter is full screen
  {const f=modeAt(t);$('band').style.opacity=clamp(f*1.2-.1);
   BANDS.forEach(([id,a,b])=>{const e=$(id);const v=t>=a&&t<b;e.style.visibility=v?'visible':'hidden';e.style.opacity=v&&t>b-.25?1-P(t,b-.25,.25):1;});
   // chapter progress
   const T=DURATION;$('pfill').style.width=`${960*clamp(t/T)}px`;
   CH.forEach((c,i)=>{c.el.classList.toggle('on',t>=c.t);});
   // 3-4x dots and consistency bar
   [...$('dots4').children].forEach((d,i)=>{d.style.background=t>86.1+i*.35?'#FFE14D':'transparent';});
   $('bar5').firstElementChild.style.width=`${960*inout(P(t,94.0,4.0))}px`;
   if(t>113.6){$('cta7').style.transform=`scale(${1+.04*Math.sin((t-113.6)*8)})`;}
  }
'''
