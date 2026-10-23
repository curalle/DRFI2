import json,re,subprocess,sys
S=sys.argv[1]
FF='/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2'
log=subprocess.run([FF,'-hide_banner','-i',f'{S}/src/audio.wav','-af','silencedetect=noise=-32dB:d=0.35','-f','null','-'],capture_output=True,text=True).stderr
st=[float(x) for x in re.findall(r'silence_start: ([0-9.]+)',log)]
en=[float(x) for x in re.findall(r'silence_end: ([0-9.]+)',log)]
sil=list(zip(st,en))
# speech = complement of silence within [3.30, 167.95]
A,B=3.30,167.95
speech=[];cur=A
for s,e in sil:
    if e<=A or s>=B: continue
    if s>cur: speech.append([cur,s])
    cur=max(cur,e)
if cur<B: speech.append([cur,B])
PAD=0.12
keep=[[max(A,a-PAD),min(B,b+PAD)] for a,b in speech]
# manual removals (original seconds)
remove=[(140.40,147.22),   # first "sesuai untuk segala jenis kulit" (said again at 147.3)
        (157.30,164.40)]   # first "Jangan lupa" attempt + pause; restarted at 164.5
def sub(segs,r):
    out=[]
    for a,b in segs:
        if b<=r[0] or a>=r[1]: out.append([a,b]);continue
        if a<r[0]: out.append([a,r[0]])
        if b>r[1]: out.append([r[1],b])
    return out
for r in remove: keep=sub(keep,r)
# merge overlaps / tiny gaps, drop slivers
m=[]
for a,b in sorted(keep):
    if m and a-m[-1][1]<0.08: m[-1][1]=max(m[-1][1],b)
    else: m.append([a,b])
keep=[[round(a,3),round(b,3)] for a,b in m if b-a>0.12]
tot=sum(b-a for a,b in keep)
json.dump(keep,open(f'{S}/edit/keep.json','w'))
print(len(keep),'segments, total',round(tot,2),'s')
