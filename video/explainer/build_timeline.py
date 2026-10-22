# Lays out scenes from VO durations -> timeline.json, and cuts the matching footage into 30fps JPEG sequences (foot/<key>/).
import json, os, subprocess, imageio_ffmpeg, sys
FF=imageio_ffmpeg.get_ffmpeg_exe(); SRC=sys.argv[1] if len(sys.argv)>1 else 'CURALLE_VIDEO.mp4'
W=json.load(open('vo/words.json'))
# key, kind, footage (src_in, src_out) or None, lead, tail, enter-transition
PLAN=[('a','foot',(0.0,4.0),1.2,0.4,'cut'),('b','foot',(4.5,7.5),0.2,0.5,'cut'),('v1','vox',None,0.5,0.6,'slide'),
('c','foot',(8.5,15.5),0.3,0.5,'fade'),('v2','vox',None,0.6,0.6,'zoom'),('v4','vox',None,0.4,0.6,'wipe'),
('d','foot',(19.0,22.4),0.3,0.5,'fade'),('v6','vox',None,0.3,0.5,'slide'),('v7','vox',None,0.3,0.5,'wipe'),
('f','foot',(28.5,42.0),0.3,0.5,'fade'),('v8','vox',None,0.4,0.5,'fade'),('e','foot',(23.5,28.05),0.3,0.5,'slide'),
('v9','vox',None,0.3,0.6,'slide'),('g','foot',(42.1,47.0),0.3,0.6,'fade'),('h','foot',(47.3,50.8),0.3,2.6,'fade')]
t=0; scenes=[]
for k,kind,src,lead,tail,tr in PLAN:
    sp=W[k][-1][1]; dur=round(lead+sp+tail,3)
    scenes.append(dict(key=k,kind=kind,a=round(t,3),b=round(t+dur,3),vo=round(t+lead,3),src=src,enter=tr))
    t+=dur
total=round(t,3); print('total',total)
json.dump(dict(scenes=scenes,words=W,total=total),open('timeline.json','w'),ensure_ascii=False)
for s in scenes:
    if s['kind']!='foot': continue
    d=f"foot/{s['key']}"; os.makedirs(d,exist_ok=True)
    for f in os.listdir(d): os.remove(f'{d}/{f}')
    i0,i1=s['src']; T=s['b']-s['a']+0.6   # +0.6s headroom for overlapping transitions
    k=T/(i1-i0)
    subprocess.run([FF,'-v','error','-ss',str(i0),'-t',str(i1-i0),'-i',SRC,'-vf',f'setpts={k:.4f}*PTS,fps=30,scale=1920:1080','-q:v','3',f'{d}/%04d.jpg'],check=True)
    s['n']=len(os.listdir(d)); print(s['key'],f'{k:.2f}x slow',s['n'],'frames')
json.dump(dict(scenes=scenes,words=W,total=total),open('timeline.json','w'),ensure_ascii=False)
open('timeline.js','w').write('window.TL='+json.dumps(dict(scenes=scenes,words=W,total=total),ensure_ascii=False)+';')
