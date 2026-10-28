# Builds a 16:9 YouTube page from a 9:16 explainer page (default: eczema.html -> eczema169.html).
# The tiles keep their content; at load time each tile's header (kicker/title/body, top < 550px)
# moves to a left column and the illustrations below are grouped and scaled into a right column.
# Usage: python3 edit/make_landscape.py [src.html dst.html]   (run from video/)
import re,sys

SRC,DST=(sys.argv[1],sys.argv[2]) if len(sys.argv)>2 else ('eczema.html','eczema169.html')
ECZ=SRC=='eczema.html'   # the eczema page has hand-tuned overlay positions and camera moves
src = open(SRC).read()
s = src

def rep(a, b, cnt=1):
    global s
    assert s.count(a) == cnt, (s.count(a), a)
    s = s.replace(a, b)

s = re.sub(r'<title>(.*?)9:16</title>', r'<title>\g<1>16:9</title>', s, count=1)
rep('html,body{width:1080px;height:1920px;', 'html,body{width:1920px;height:1080px;')
rep('#stage{position:relative;width:1080px;height:1920px;', '#stage{position:relative;width:1920px;height:1080px;')
rep('.tile{position:absolute;width:1080px;height:1920px;', '.tile{position:absolute;width:1920px;height:1080px;')
rep('.tile .flow,.tile .flow *{position:static}', '.tile .flow,.tile .flow *{position:static}\n.tile>.hdr,.tile>.vis{position:absolute;left:0;top:0;transform-origin:0 0}')

# B-roll: a large card on the right (the presenter floats bottom-left), caption below it
rep('#brbg{position:absolute;left:0;top:0;width:1080px;height:1920px;object-fit:cover}',
    '#brbg{position:absolute;left:0;top:0;width:1920px;height:1080px;object-fit:cover}')
rep('#brcard{position:absolute;left:40px;top:690px;width:1000px;height:563px;',
    '#brcard{position:absolute;left:600px;top:80px;width:1224px;height:699px;')
rep('#brcard img{position:absolute;left:0;top:0;width:976px;height:539px;object-fit:cover}',
    '#brcard img{position:absolute;left:0;top:0;width:1200px;height:675px;object-fit:cover}')
rep('#brfull{position:absolute;left:0;top:0;width:1080px;height:1920px;object-fit:cover}',
    '#brfull{position:absolute;left:0;top:0;width:1920px;height:1080px;object-fit:cover}')
rep('#brcap{position:absolute;left:60px;top:1290px;', '#brcap{position:absolute;left:620px;top:830px;')

# portrait B-roll clips (e.g. tomato, stress) become a tall card on the right over their blurred still
if not ECZ:
    rep('#brfull{position:absolute;left:0;top:0;width:1920px;height:1080px;object-fit:cover}',
        '#brfull{position:absolute;left:1150px;top:50px;width:540px;height:960px;object-fit:cover;border:12px solid #fff;border-radius:6px;box-shadow:0 30px 70px rgba(0,0,0,.45)}')
    rep("$('brbg').style.display=full?'none':'block';","$('brbg').style.display='block';")
    rep("if(full){await setImg($('brfull'),f);","if(full){await setImg($('brbg'),`file://${BROLL}/${id}/bg.jpg`);$('brbg').style.opacity=vis;await setImg($('brfull'),f);")

# presenter frame: 16:9 crop of the portrait source when full, floating card bottom-left otherwise
rep('#vid{position:absolute;left:0;top:0;transform-origin:0 0;width:1080px;height:1920px}',
    '#vid{position:absolute;left:0;top:0;transform-origin:0 0;width:1080px;height:1920px}')
rep('#pipname{position:absolute;left:690px;width:340px;top:652px;text-align:center}',
    '#pipname{position:absolute;left:80px;width:320px;top:1012px;text-align:center}')
# full screen = presenter panel on the right two-thirds, paper on the left for the text cards
rep("const PIP={x:690,y:210,w:340,h:430},FULL={x:0,y:0,w:1080,h:1920};",
    "const PIP={x:80,y:590,w:320,h:410},FULL={x:640,y:0,w:1280,h:1080};")
rep("const scF=1.1*kb*(1+pz), scP=.6;", "const scF=1.19*kb*(1+pz), scP=.55;")
rep("const fx=lerp(510,540,f), fy=lerp(900,lerp(900,880,pz*5),f);",
    "const fx=lerp(510,540,f), fy=lerp(900,lerp(880,860,pz*5),f);")
rep("  $('pipname').style.opacity=clamp(1-f*3);", "  $('fullbg').style.opacity=f;\n  $('pipname').style.opacity=clamp(1-f*3);")
rep('<!-- presenter -->', '<div id="fullbg" style="position:absolute;inset:0;background:radial-gradient(circle at 30% 45%,#FBF7EE 0,#F3ECDC 60%,#E9DFC8 100%);opacity:0"></div>\n<!-- presenter -->')

# full-screen overlays: left side over the 16:9 presenter shot
ov = {
 'id="o1" style="left:60px;top:230px;width:960px"': 'id="o1" style="left:50px;top:110px;width:600px"',
 'id="o1s" style="left:200px;top:1250px;font-size:110px;': 'id="o1s" style="left:70px;top:640px;font-size:88px;',
 'id="o2" style="left:60px;top:1300px;width:960px;': 'id="o2" style="left:50px;top:90px;width:600px;',
 'id="o3" style="left:60px;top:230px;width:960px"': 'id="o3" style="left:50px;top:110px;width:600px"',
 'id="o4" style="left:60px;top:230px;width:960px"': 'id="o4" style="left:50px;top:110px;width:600px"',
 'id="o4b" style="left:60px;top:1200px;width:960px;': 'id="o4b" style="left:50px;top:620px;width:600px;',
 'id="o5" style="left:60px;top:230px;': 'id="o5" style="left:50px;top:110px;',
 'id="o6" style="left:60px;top:1180px;width:960px"': 'id="o6" style="left:50px;top:520px;width:600px"',
 'id="o7" style="left:60px;top:1180px;width:960px;': 'id="o7" style="left:50px;top:820px;width:600px;',
}
if ECZ:
    for a, b in ov.items():
        rep(a, b)
else:
    # generic: every overlay moves into the paper column on the left, upper or lower half
    rep("// ---------------- camera over the tiles ----------------", r'''(function(){
  [...document.getElementById('overlay').children].forEach(o=>{
    const top=parseFloat(o.style.top||'0');
    o.style.left='50px';
    o.style.top=(top<800?100:top<1250?600:760)+'px';
    if(o.classList.contains('ocard')){const z=.8;o.style.zoom=z;o.style.left=(50/z)+'px';o.style.top=(parseFloat(o.style.top)/z)+'px';o.style.width=(600/z)+'px';}
    else{const fs=parseFloat(o.style.fontSize||'44');o.style.fontSize=Math.min(fs,fs*.75)+'px';}
  });
})();
// ---------------- camera over the tiles ----------------''')

rep("$('world').style.transform=`translate(${540-cx*s}px,${960-cy*s}px) scale(${s})`;",
    "$('world').style.transform=`translate(${960-cx*s}px,${540-cy*s}px) scale(${s})`;")
rep("c.style.width='1200px';c.style.height='2040px';", "c.style.width='2040px';c.style.height='1200px';")
s = re.sub(r"(window.OUTPUT='[^']*)_9x16\.mp4'", r"\1_16x9.mp4'", s, count=1)

# camera: landscape tiles on a 2200x1300 grid; zooms aim at the illustration column
# portrait grid (1300 x 1900 spacing) -> landscape grid (2200 x 1300)
m = re.search(r'const TP=\{([^}]*)\};', s)
PTP = {k: (int(x), int(y)) for k, x, y in re.findall(r'(T\d+):\[(\d+),(\d+)\]', m.group(1))}
LTP = {k: (x*2200//1300, y*1300//1900) for k, (x, y) in PTP.items()}
s = s.replace(m.group(0), 'const TP={' + ','.join(f'{k}:[{x},{y}]' for k, (x, y) in LTP.items()) + '};')
rep("const C=(k,dx=540,dy=960)=>[TP[k][0]+dx,TP[k][1]+dy];", "const C=(k,dx=960,dy=540)=>[TP[k][0]+dx,TP[k][1]+dy];")
cam_old = s[s.index('const CAM=['):s.index('];', s.index('const CAM=['))+2]
cam_ecz = """const V=(k)=>C(k,960,560);   // gentle push-in that keeps the titles in frame
const CAM=[
 [0,...C('T1'),1],[13.0,...C('T1'),1],[13.8,...V('T1'),1.04],[16.8,...V('T1'),1.04],
 [23.0,...C('T2'),1],[39.6,...C('T2'),1.03],
 [40.0,...mid('T2','T3'),.6],[40.45,...C('T3'),1],[52.0,...C('T3'),1.03],
 [52.5,...mid('T3','T4'),.6],[52.95,...C('T4'),1],
 [64.2,...C('T4'),1],[65.0,...V('T4'),1.04],[78.4,...V('T4'),1.04],[79.2,...C('T4'),1],[89.0,...C('T4'),1.03],
 [89.5,...mid('T4','T5'),.6],[89.95,...C('T5'),1],[107.6,...C('T5'),1.03],
 [108.05,...mid('T5','T6'),.6],[108.5,...C('T6'),1],[121.8,...C('T6'),1.02],
 // "on the surface they all look the same": pull back over the three examples, then drop to the iceberg
 [122.8,3160,1840,.28],[123.9,3160,1840,.28],[124.6,...C('T7'),1],[129.1,...C('T7'),1.03],
 [137.0,...C('T8'),1],[165.4,...C('T8'),1.03],
 [165.85,...mid('T8','T9'),.6],[166.3,...C('T9'),1],[174.8,...C('T9'),1.03],
 [189.6,...C('T10'),1],[200.7,...C('T10'),1.03],
 [201.1,...mid('T10','T11'),.6],[201.55,...C('T11'),1],[233.2,...C('T11'),1.04]
];"""
def cam_generic(c):
    c = re.sub(r"C\('(T\d+)',[0-9.]+,[0-9.]+\),([0-9.]+)\]", lambda m: f"C('{m.group(1)}',960,560),{min(float(m.group(2)),1.04)}]", c)
    c = re.sub(r"\],1\.(0[5-9]|[1-9][0-9]*)\]", "],1.04]", c)
    def raw(m):
        t, X, Y, sc = float(m.group(1)), float(m.group(2)), float(m.group(3)), float(m.group(4))
        return f"[{t},{(X-540)*2200/1300+960:.0f},{(Y-960)*1300/1900+540:.0f},{sc*1.05 if sc<.9 else sc:.2f}]"
    return re.sub(r"\[([0-9.]+),([0-9.]+),([0-9.]+),([0-9.]+)\]", raw, c)
s = s.replace(cam_old, cam_ecz if ECZ else cam_generic(cam_old))

# re-layout each tile at load: header -> left column, illustrations -> scaled right column
layout = r"""
// ---------------- landscape re-layout of the portrait tiles ----------------
(function(){
  const COL={x0:820,x1:1860,y0:60,y1:1020};
  document.querySelectorAll('.tile').forEach(tile=>{
    const kids=[...tile.children];
    const hdr=document.createElement('div');hdr.className='hdr';
    const vis=document.createElement('div');vis.className='vis';
    tile.appendChild(hdr);tile.appendChild(vis);
    kids.forEach(k=>{const top=parseFloat(k.style.top||'0');(top<550?hdr:vis).appendChild(k);});
    hdr.style.transform='translate(20px,-140px)';
    // bounds of the illustration group in tile coordinates (no transforms applied yet)
    const tr=tile.getBoundingClientRect();let x0=1e9,y0=1e9,x1=-1e9,y1=-1e9;
    [...vis.children].forEach(k=>{const r=k.getBoundingClientRect();if(!r.width)return;
      x0=Math.min(x0,r.left-tr.left);y0=Math.min(y0,r.top-tr.top);x1=Math.max(x1,r.right-tr.left);y1=Math.max(y1,r.bottom-tr.top);});
    if(x1<x0)return;
    const w=x1-x0,h=y1-y0,sc=Math.min(1,(COL.x1-COL.x0)/w,(COL.y1-COL.y0)/h);
    const ox=COL.x0+((COL.x1-COL.x0)-w*sc)/2-x0*sc, oy=COL.y0+((COL.y1-COL.y0)-h*sc)/2-y0*sc;
    vis.style.transform=`translate(${ox}px,${oy}px) scale(${sc})`;
  });
})();
"""
rep("// ---------------- camera over the tiles ----------------", layout + "\n// ---------------- camera over the tiles ----------------")
# tiles sit on the landscape grid used by TP above
def tilepos(m):
    x,y=LTP[m.group(1)]
    return f'<div class="tile" id="{m.group(1)}" style="left:{x}px;top:{y}px">'
s,n=re.subn(r'<div class="tile" id="(T\d+)" style="left:[0-9]+(?:px)?;top:[0-9]+(?:px)?">',tilepos,s)
assert n==len(LTP),n
open(DST, 'w').write(s)
print('wrote',DST)
