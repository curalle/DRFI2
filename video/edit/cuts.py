# Builds a keep-list of speech segments from one or more talking-head recordings.
# Usage: python3 cuts.py <config.json> <workdir>
#   single recording: {"src":"src2","start":0.5,"end":241.9,"noise_db":-29,"remove":[[a,b],...]}
#   several, joined in order: {"out":"src3","noise_db":-29,"parts":[{"src":"src3a","start":..,"end":..,"remove":[..]},...]}
#   reads <workdir>/<src>/audio.wav; writes <workdir>/<out or src>/keep.json as [[partIndex,a,b],...]
import json,os,re,subprocess,sys
cfg=json.load(open(sys.argv[1]));S=sys.argv[2]
FF='/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2'
parts=cfg.get('parts') or [{k:cfg[k] for k in ('src','start','end','remove') if k in cfg}]
PAD=0.12   # pauses longer than 0.35s shrink to ~0.24s
def sub(segs,r):
    out=[]
    for a,b in segs:
        if b<=r[0] or a>=r[1]: out.append([a,b]);continue
        if a<r[0]: out.append([a,r[0]])
        if b>r[1]: out.append([r[1],b])
    return out
keep=[]
for pi,p in enumerate(parts):
    log=subprocess.run([FF,'-hide_banner','-i',f"{S}/{p['src']}/audio.wav",'-af',f"silencedetect=noise={cfg.get('noise_db',-32)}dB:d=0.35",'-f','null','-'],capture_output=True,text=True).stderr
    sil=list(zip([float(x) for x in re.findall(r'silence_start: ([0-9.]+)',log)],[float(x) for x in re.findall(r'silence_end: ([0-9.]+)',log)]))
    A,B=p['start'],p['end'];speech=[];cur=A
    for s,e in sil:
        if e<=A or s>=B: continue
        if s>cur: speech.append([cur,s])
        cur=max(cur,e)
    if cur<B: speech.append([cur,B])
    segs=[[max(A,a-PAD),min(B,b+PAD)] for a,b in speech]
    for r in p.get('remove',[]): segs=sub(segs,r)
    m=[]
    for a,b in sorted(segs):
        if m and a-m[-1][1]<0.08: m[-1][1]=max(m[-1][1],b)
        else: m.append([a,b])
    keep+=[[pi,round(a,3),round(b,3)] for a,b in m if b-a>0.12]
D=f"{S}/{cfg.get('out',parts[0]['src'])}";os.makedirs(D,exist_ok=True)
json.dump(keep,open(f'{D}/keep.json','w'))
print(len(keep),'segments, total',round(sum(b-a for _,a,b in keep),2),'s')
