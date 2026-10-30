# Builds an explainer page by splicing a content module (edit/<name>_parts.py) into the
# eczema.html engine (camera over paper tiles, floating presenter frame, B-roll layer, overlays).
# Optional extras a parts module may define:
#   FRAMING  presenter framing {'pip':(x,y),'full':(x,y),'head_top':y,'band_bottom':y} (source px)
#   EXTRA_CSS, BAND (+BANDS, CHAPTERS, BAND_FRAME)  a title band over the top of full-screen shots
#   LOW      [[t,0|1],...] when full-screen shots are framed low so the band sits above the head
#   ZOOM     [[t0,t1,z0,z1],...] slow, eased push-ins while the presenter is full screen
#   ILLUSTRATIONS_PRE  code that must run before the illustrations
# Usage: python3 edit/make_page.py <name> <out.html>   (run from video/)
import importlib,re,sys
sys.path.insert(0,'edit')
C=importlib.import_module(sys.argv[1]+'_parts')
OUT=sys.argv[2]
s=open('eczema.html').read()
def cut(a,b,new):
    global s
    i=s.index(a);j=s.index(b,i)
    s=s[:i]+new+s[j:]
def rep(a,b):
    global s
    assert s.count(a)==1,(s.count(a),a); s=s.replace(a,b)
rep('<title>DRFI Eczema Explainer 9:16</title>',f'<title>{C.TITLE}</title>')
rep('.tile b,.tile i,.tile br{position:static}','.tile b,.tile i,.tile br,.tile .kicker span{position:static}\n.strike{position:static!important;background-image:linear-gradient(transparent 52%,#E4472B 52%,#E4472B 60%,transparent 60%);background-repeat:no-repeat;background-size:0% 100%}'+getattr(C,'EXTRA_CSS',''))
cut('<svg id="trail"','\n</div>\n\n<!-- B-roll','<svg id="trail" class="abs" style="left:0;top:0;overflow:visible" width="10" height="10"></svg>\n'+C.TILES)
rep('<div id="pipname"><span>Ts. Dr Fareez Ismail · DRFI</span></div>',f'<div id="pipname"><span>{C.PIPNAME}</span></div>'+getattr(C,'BAND',''))
cut('<div id="overlay">','</div>\n\n<canvas id="noise"','<div id="overlay">\n'+C.OVERLAYS)
rep("window.DURATION=233.2;window.OUTPUT='output/drfi_eczema_explainer_9x16.mp4';",f"window.DURATION={C.DURATION};window.OUTPUT='{C.OUTPUT}';")
rep("NFR=+(Q.get('n')||6947)",f"NFR=+(Q.get('n')||{C.NFR})")
s=re.sub(r'const TP=\{[^}]*\};',f'const TP={C.TP};',s,count=1)
cut('const CAM=[','\nfunction camAt',C.CAM)
s=re.sub(r"const order=\[[^\]]*\];",f"const order={C.ORDER};",s,count=1)
s=re.sub(r'const MODE=\[.*?\]\];',f'const MODE={C.MODE};',s,count=1)
s=re.sub(r'const PUNCH=\[.*?\]\];',f'const PUNCH={C.PUNCH};',s,count=1)
cut('// ---------------- illustrations ----------------','// grain','// ---------------- illustrations ----------------\n'+getattr(C,'ILLUSTRATIONS_PRE','')+'\n'+C.ILLUSTRATIONS+'\n')
cut('const BR=[','\nasync function setImg',f'const BR={C.BR};')
s=re.sub(r"const OV=\[.*?\]\];",f"const OV={C.OV};",s,count=1,flags=re.S)
cut('  // T1 magnifier scanning, question marks','  // overlays\n',
    "  document.querySelectorAll('[data-st]').forEach(e=>{e.style.backgroundSize=`${out3(P(t,+e.dataset.st,.4))*100}% 100%`;});\n"+C.FRAME+getattr(C,'BAND_FRAME',''))
if hasattr(C,'FRAMING'):
    Fr=C.FRAMING
    rep("const kb=1+.0175*(1-Math.cos(t*.35)), pz=punchAt(t);   // smooth drift between 1 and 1.035",
        "const kb=1+.015*Math.sin(t*.21), pz=punchAt(t), zm=zoomAt(t), L=lowAt(t);   // smooth drift (no sawtooth reset)")
    rep("const scF=1.1*kb*(1+pz), scP=.6;","const scF=1.12*kb*(1+pz+zm), scP=.6;")
    rep("const fx=lerp(510,540,f), fy=lerp(900,lerp(900,880,pz*5),f);",
        f"const fyLow={Fr['head_top']}+(960-{Fr['band_bottom']})/scF;   // head top lands just under the title band\n"
        f"  const fx=lerp({Fr['pip'][0]},{Fr['full'][0]},f), fy=lerp({Fr['pip'][1]},lerp(lerp({Fr['full'][1]},{Fr['full'][1]-20},pz*5),fyLow,L),f);")
    rep("function placeVideo(t){",
        f"const LOW={getattr(C,'LOW','[[0,0]]')};\n"
        "function lowAt(t){let i=0;while(i<LOW.length-1&&LOW[i+1][0]<=t)i++;if(i>=LOW.length-1)return LOW[LOW.length-1][1];const a=LOW[i],b=LOW[i+1];return lerp(a[1],b[1],inout(P(t,a[0],b[0]-a[0])));}\n"
        f"const ZOOM={getattr(C,'ZOOM','[]')};\n"
        "function zoomAt(t){for(const [a,b,z0,z1] of ZOOM){if(t>=a&&t<b)return lerp(z0,z1,inout(P(t,a,b-a)));}return 0;}\n"
        "function placeVideo(t){")
if hasattr(C,'BAND'):
    rep("const OV=[",f"const BANDS={C.BANDS};\nconst CH=({C.CHAPTERS}).map(([s,t])=>{{const d=document.createElement('div');d.className='tick';d.innerHTML=`<i></i><span>${{s}}</span>`;d.style.left=`${{960*t/DURATION+12}}px`;$('prog').appendChild(d);return {{el:d,t}};}});\nconst OV=[")
# the bookmark wiggle belongs to pages that have a "Save" overlay
s=s.replace("  $('bm').style.transform=t>212.4?","  if($('bm'))$('bm').style.transform=t>212.4?")
open(OUT,'w').write(s)
print('wrote',OUT)
