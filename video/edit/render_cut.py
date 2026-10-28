# Renders <workdir>/<out>/keep.json into <workdir>/<out>/cut.mkv (30fps, PCM audio), joining parts in order.
# Usage: python3 render_cut.py <config.json> <workdir>
import json,subprocess,sys
cfg=json.load(open(sys.argv[1]));S=sys.argv[2]
FF='/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2'
parts=cfg.get('parts') or [{'src':cfg['src']}]
D=f"{S}/{cfg.get('out',parts[0]['src'])}"
keep=json.load(open(f'{D}/keep.json'))
keep=[k if len(k)==3 else [0,*k] for k in keep]   # older single-source lists
f=[]
for i,(pi,a,b) in enumerate(keep):
    d=b-a
    f.append(f'[{pi}:v]trim={a}:{b},setpts=PTS-STARTPTS,fps=30,scale=1080:1920,setsar=1[v{i}]')
    f.append(f'[{pi}:a]atrim={a}:{b},asetpts=PTS-STARTPTS,aresample=48000,afade=t=in:d=0.012,afade=t=out:st={d-0.012:.3f}:d=0.012[a{i}]')
f.append(''.join(f'[v{i}][a{i}]' for i in range(len(keep)))+f'concat=n={len(keep)}:v=1:a=1[v][a]')
open(f'{D}/fc.txt','w').write(';\n'.join(f))
ins=[]
for p in parts: ins+=['-i',f"{S}/{p['src']}/user.mp4"]
subprocess.run([FF,'-v','error','-y',*ins,'-filter_complex_script',f'{D}/fc.txt','-map','[v]','-map','[a]',
  '-c:v','libx264','-crf','14','-preset','fast','-pix_fmt','yuv420p','-c:a','pcm_s16le',f'{D}/cut.mkv'],check=True)
