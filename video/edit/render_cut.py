import json,subprocess,sys
S=sys.argv[1];FF='/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2'
keep=json.load(open(f'{S}/edit/keep.json'))
f=[]
for i,(a,b) in enumerate(keep):
    d=b-a
    f.append(f'[0:v]trim={a}:{b},setpts=PTS-STARTPTS,fps=30[v{i}]')
    f.append(f'[0:a]atrim={a}:{b},asetpts=PTS-STARTPTS,afade=t=in:d=0.012,afade=t=out:st={d-0.012:.3f}:d=0.012[a{i}]')
f.append(''.join(f'[v{i}][a{i}]' for i in range(len(keep)))+f'concat=n={len(keep)}:v=1:a=1[v][a]')
open(f'{S}/edit/fc.txt','w').write(';\n'.join(f))
subprocess.run([FF,'-v','error','-y','-i',f'{S}/src/user.mp4','-filter_complex_script',f'{S}/edit/fc.txt','-map','[v]','-map','[a]',
  '-c:v','libx264','-crf','14','-preset','fast','-pix_fmt','yuv420p','-c:a','pcm_s16le',f'{S}/edit/cut.mkv'],check=True)
