import json, subprocess, numpy as np, imageio_ffmpeg
FF=imageio_ffmpeg.get_ffmpeg_exe(); SR=48000
def load(f):
    raw=subprocess.run([FF,'-v','quiet','-i',f,'-f','f32le','-ac','1','-ar',str(SR),'-'],capture_output=True).stdout
    return np.frombuffer(raw,np.float32)
W=json.load(open('words.json'))
out=[]; words=[]; lines=[]; t=0.0
GAP=0.12; MAXPAUSE=0.22
for i,ws in enumerate(W):
    a=load(f'vo{i}.mp3')
    # segments: split at internal pauses longer than MAXPAUSE
    segs=[]; cur=[ws[0]]
    for w in ws[1:]:
        if w[0]-cur[-1][1]>MAXPAUSE: segs.append(cur); cur=[w]
        else: cur.append(w)
    segs.append(cur)
    lstart=t
    for k,sg in enumerate(segs):
        s0=max(0,sg[0][0]-0.03); s1=sg[-1][1]+0.06
        for w in sg: words.append([round(t+w[0]-s0,3),round(t+w[1]-s0,3),w[2],i])
        out.append(a[int(s0*SR):int(s1*SR)]); t+=s1-s0
        if k<len(segs)-1: out.append(np.zeros(int(0.14*SR),np.float32)); t+=0.14
    lines.append([round(lstart,3),round(t,3)])
    out.append(np.zeros(int(GAP*SR),np.float32)); t+=GAP
y=np.concatenate(out); print('speech total',t)
# envelope @30fps for mouth
hop=SR//30; env=[float(np.sqrt(np.mean(y[i*hop:(i+1)*hop]**2))) if i*hop<len(y) else 0 for i in range(int(len(y)/hop)+1)]
json.dump({'words':words,'lines':lines,'env':env,'dur':t},open('timeline.json','w'),ensure_ascii=False)
y.astype(np.float32).tofile('vo.f32')
subprocess.run([FF,'-y','-v','quiet','-f','f32le','-ar',str(SR),'-ac','1','-i','vo.f32','vo.wav'])
for l in lines: print(l)
