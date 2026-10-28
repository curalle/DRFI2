# Builds pompholyx.html (9:16) by splicing edit/pompholyx_parts.py into the eczema.html engine
# (camera, floating presenter frame, B-roll layer, overlays, grain).
# Usage: python3 edit/make_pompholyx.py   (run from video/)
import re,sys
sys.path.insert(0,'edit')
import pompholyx_parts as C
s=open('eczema.html').read()
def cut(a,b,new,keep_b=True):
    global s
    i=s.index(a);j=s.index(b,i)
    s=s[:i]+new+(s[j:] if keep_b else s[j+len(b):])
def rep(a,b):
    global s
    assert s.count(a)==1,(s.count(a),a); s=s.replace(a,b)
rep('<title>DRFI Eczema Explainer 9:16</title>',f'<title>{C.TITLE}</title>')
rep('.tile b,.tile i,.tile br{position:static}','.tile b,.tile i,.tile br{position:static}\n.strike{position:static!important;background-image:linear-gradient(transparent 52%,#E4472B 52%,#E4472B 60%,transparent 60%);background-repeat:no-repeat;background-size:0% 100%}')
cut('<svg id="trail"','\n</div>\n\n<!-- B-roll','<svg id="trail" class="abs" style="left:0;top:0;overflow:visible" width="10" height="10"></svg>\n'+C.TILES)
rep('<div id="pipname"><span>Ts. Dr Fareez Ismail · DRFI</span></div>',f'<div id="pipname"><span>{C.PIPNAME}</span></div>')
cut('<div id="overlay">','</div>\n\n<canvas id="noise"','<div id="overlay">\n'+C.OVERLAYS)
rep("window.DURATION=233.2;window.OUTPUT='output/drfi_eczema_explainer_9x16.mp4';",f"window.DURATION={C.DURATION};window.OUTPUT='{C.OUTPUT}';")
rep("NFR=+(Q.get('n')||6947)",f"NFR=+(Q.get('n')||{C.NFR})")
s=re.sub(r'const TP=\{[^}]*\};',f'const TP={C.TP};',s,count=1)
cut('const CAM=[','\nfunction camAt',C.CAM)
s=re.sub(r"const order=\[[^\]]*\];",f"const order={C.ORDER};",s,count=1)
s=re.sub(r'const MODE=\[.*?\]\];',f'const MODE={C.MODE};',s,count=1)
s=re.sub(r'const PUNCH=\[.*?\]\];',f'const PUNCH={C.PUNCH};',s,count=1)
cut('// ---------------- illustrations ----------------','// grain','// ---------------- illustrations ----------------\n'+C.ILLUSTRATIONS+'\n')
cut('const BR=[','\nasync function setImg',f'const BR={C.BR};')
s=re.sub(r"const OV=\[.*?\]\];",f"const OV={C.OV};",s,count=1,flags=re.S)
cut('  // T1 magnifier scanning, question marks','  // overlays\n',
    "  document.querySelectorAll('[data-st]').forEach(e=>{e.style.backgroundSize=`${out3(P(t,+e.dataset.st,.4))*100}% 100%`;});\n"+C.FRAME)
open('pompholyx.html','w').write(s)
print('wrote pompholyx.html')
