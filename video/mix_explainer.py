# Mixes the explainer soundtrack: per-scene Malay VO + soft piano bed (ducked) + SFX cues, then muxes with the rendered video.
import json, subprocess, numpy as np, imageio_ffmpeg, sys
FF=imageio_ffmpeg.get_ffmpeg_exe(); SR=48000
TL=json.load(open('explainer/timeline.json')); DUR=TL['total']; N=int(SR*DUR)+SR
def load(f):
    return np.frombuffer(subprocess.run([FF,'-v','quiet','-i',f,'-f','f32le','-ac','1','-ar',str(SR),'-'],capture_output=True).stdout,np.float32)
vo=np.zeros(N); bed=np.zeros(N); fx=np.zeros(N); rng=np.random.default_rng(7)
def add(buf,sig,at,g=1.0):
    i=int(at*SR); j=min(len(buf),i+len(sig))
    if j>i: buf[i:j]+=sig[:j-i]*g
for s in TL['scenes']: add(vo,load(f"explainer/vo/{s['key']}.mp3"),s['vo'])
# --- piano-ish bed: Am F C G, 84 bpm, warmer in act 3/4
bpm=84; beat=60/bpm
def note(f,d,amp=1):
    t=np.arange(int(d*SR))/SR
    s=(np.sin(2*np.pi*f*t)+.45*np.sin(4*np.pi*f*t)*np.exp(-t*3)+.2*np.sin(6*np.pi*f*t)*np.exp(-t*5))
    return s*np.exp(-t*1.6)*np.minimum(1,t*200)*amp
CH=[[220,261.63,329.63],[174.61,220,261.63],[261.63,329.63,392],[196,246.94,293.66]]
BASS=[110,87.31,130.81,98]
act3=TL['scenes'][[x['key'] for x in TL['scenes']].index('d')]['a']
bar=0; t=0.0
while t<DUR:
    c=bar%4
    add(bed,note(BASS[c]/2*2,beat*4,.55),t)
    for k in range(8):   # arpeggio eighths
        f=CH[c][[0,1,2,1,0,2,1,2][k]]*(2 if k%4==2 else 1)
        add(bed,note(f,beat*1.5,.22),t+k*beat/2)
    if t>=act3:          # soft kick + shaker for lift
        for k in range(4):
            tt=np.arange(int(.22*SR))/SR
            add(bed,np.sin(2*np.pi*(45+70*np.exp(-tt*28))*tt)*np.exp(-tt*10),t+k*beat,.35)
            sh=rng.normal(0,1,int(.04*SR))*np.exp(-np.arange(int(.04*SR))/SR*90); add(bed,np.diff(sh,prepend=0),t+k*beat+beat/2,.06)
    t+=beat*4; bar+=1
# --- SFX
def swipe(d=.45):
    n=int(d*SR); x=rng.normal(0,1,n); x=np.convolve(x,np.ones(6)/6,'same'); return x*np.sin(np.linspace(0,np.pi,n))**2*.5
def whoosh(d=.9):
    n=int(d*SR); x=rng.normal(0,1,n); x=np.convolve(x,np.ones(30)/30,'same'); return x*np.linspace(0,1,n)**2*np.exp(-np.linspace(0,3,n))*3
def pop():
    tt=np.arange(int(.09*SR))/SR; return np.sin(2*np.pi*(700-3800*tt)*tt)*np.exp(-tt*45)
def tick():
    tt=np.arange(int(.05*SR))/SR; return np.sin(2*np.pi*1600*tt)*np.exp(-tt*90)
for kind,at in json.load(open('explainer/sfx.json')):
    {'swipe':lambda:add(fx,swipe(),at-.15,.5),'whoosh':lambda:add(fx,whoosh(),at-.3,.5),'pop':lambda:add(fx,pop(),at,.32),'tick':lambda:add(fx,tick(),at,.18)}[kind]()
# duck bed under voice
env=np.convolve(np.abs(vo),np.ones(9600)/9600,'same'); duck=1-0.6*np.clip(env/0.025,0,1)
bed=bed*0.16*duck
fade=int(2.5*SR); end=int(DUR*SR); bed[end-fade:end]*=np.linspace(1,0,fade); bed[end:]=0
bed[:int(1.4*SR)]*=np.linspace(0,1,int(1.4*SR))
mix=(vo+bed+fx)[:end]; mix/=max(1,np.abs(mix).max()/0.95)
mix.astype(np.float32).tofile('explainer/mix.f32')
out=sys.argv[1] if len(sys.argv)>1 else 'output/curalle_explainer_16x9.mp4'
subprocess.run([FF,'-y','-v','error','-i','explainer/silent.mp4','-f','f32le','-ar',str(SR),'-ac','1','-i','explainer/mix.f32',
  '-c:v','copy','-c:a','aac','-b:a','192k','-ac','2','-shortest','-movflags','+faststart',out],check=True)
print('wrote',out)
