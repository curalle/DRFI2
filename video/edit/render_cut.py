# Renders <workdir>/<src>/keep.json from <workdir>/<src>/user.mp4 into cut.mkv (30fps, PCM audio).
# Usage: python3 render_cut.py <config.json> <workdir>
import json,subprocess,sys
cfg=json.load(open(sys.argv[1]));D=f"{sys.argv[2]}/{cfg['src']}"
FF='/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2'
keep=json.load(open(f'{D}/keep.json'))
f=[]
for i,(a,b) in enumerate(keep):
    d=b-a
    f.append(f'[0:v]trim={a}:{b},setpts=PTS-STARTPTS,fps=30[v{i}]')
    f.append(f'[0:a]atrim={a}:{b},asetpts=PTS-STARTPTS,afade=t=in:d=0.012,afade=t=out:st={d-0.012:.3f}:d=0.012[a{i}]')
f.append(''.join(f'[v{i}][a{i}]' for i in range(len(keep)))+f'concat=n={len(keep)}:v=1:a=1[v][a]')
open(f'{D}/fc.txt','w').write(';\n'.join(f))
subprocess.run([FF,'-v','error','-y','-i',f'{D}/user.mp4','-filter_complex_script',f'{D}/fc.txt','-map','[v]','-map','[a]',
  '-c:v','libx264','-crf','14','-preset','fast','-pix_fmt','yuv420p','-c:a','pcm_s16le',f'{D}/cut.mkv'],check=True)
