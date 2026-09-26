# Builds the audio bed (synth beat + whooshes/pops on cuts) under the Malay VO and muxes it with bofu15/silent.mp4.
import numpy as np, subprocess, imageio_ffmpeg
FF=imageio_ffmpeg.get_ffmpeg_exe(); SR=48000; DUR=15.0; N=int(SR*DUR)
vo=np.frombuffer(subprocess.run([FF,'-v','quiet','-i','bofu15/vo.wav','-f','f32le','-ac','1','-ar',str(SR),'-'],capture_output=True).stdout,np.float32)
t=np.arange(N)/SR; rng=np.random.default_rng(1)
bed=np.zeros(N)
bpm=112; beat=60/bpm
def add(sig,at,gain=1.0):
    i=int(at*SR); j=min(N,i+len(sig)); bed[i:j]+=sig[:j-i]*gain
for k in range(int(DUR/beat)+1):
    tt=np.arange(int(.25*SR))/SR
    kick=np.sin(2*np.pi*(50+90*np.exp(-tt*30))*tt)*np.exp(-tt*9)
    add(kick,k*beat,.55)
    hat=rng.normal(0,1,int(.05*SR))*np.exp(-np.arange(int(.05*SR))/SR*80)
    add(np.diff(hat,prepend=0),k*beat+beat/2,.12)
chords=[[220,261.6,329.6],[174.6,220,261.6],[261.6,329.6,392],[196,246.9,293.7]]  # Am F C G
for k in range(int(DUR/(beat*2))+1):
    ch=chords[k%4]; tt=np.arange(int(beat*2*SR))/SR
    s=sum(np.sin(2*np.pi*f*tt)+.3*np.sin(4*np.pi*f*tt) for f in ch)*np.exp(-tt*2.2)/3
    add(s,k*beat*2,.16)
def whoosh(d=.35):
    n=int(d*SR); x=rng.normal(0,1,n); x=np.convolve(x,np.ones(12)/12,'same')
    return x*np.sin(np.linspace(0,np.pi,n))**2
def pop():
    tt=np.arange(int(.08*SR))/SR; return np.sin(2*np.pi*(900-5000*tt)*tt)*np.exp(-tt*50)
for c in [3.05,6.75,10.1]: add(whoosh(),c-.2,.35)
for p in [0.25,1.95,7.67,9.39,10.51,11.96,12.73]: add(pop(),p,.35)
# duck bed under VO
v=np.zeros(N); v[int(.1*SR):int(.1*SR)+len(vo)]=vo[:N-int(.1*SR)]
env=np.convolve(np.abs(v),np.ones(4800)/4800,'same'); duck=1-0.45*np.clip(env/0.03,0,1)
bed=bed*duck*0.5
bed[-int(.6*SR):]*=np.linspace(1,0,int(.6*SR))
mix=v*1.0+bed; mix/=max(1,np.abs(mix).max()/0.95)
mix.astype(np.float32).tofile('bofu15/mix.f32')
subprocess.run([FF,'-y','-v','error','-i','bofu15/silent.mp4','-f','f32le','-ar',str(SR),'-ac','1','-i','bofu15/mix.f32',
  '-c:v','copy','-c:a','aac','-b:a','192k','-ac','2','-shortest','-movflags','+faststart','output/curalle_bofu15_vox_9x16.mp4'],check=True)
print('done')
