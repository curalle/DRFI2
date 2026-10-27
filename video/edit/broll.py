# Extracts B-roll frames for an explainer page.
# Usage: python3 broll.py <config.json> <clipsDir> <outDir>
# For each event: <outDir>/<id>/f00001.jpg... (30fps, card 1000x563, or 1080x1920 when "full")
# and <outDir>/<id>/bg.jpg (blurred, darkened full-screen still for the card background).
import json,os,subprocess,sys
cfg=json.load(open(sys.argv[1]));CL=sys.argv[2];OUT=sys.argv[3]
FF='/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2'
for e in cfg['broll']:
    d=os.path.join(OUT,e['id']);os.makedirs(d,exist_ok=True)
    dur=e['end']-e['start']+0.6
    src=os.path.join(CL,e['clip']+'.mp4')
    size='1080:1920' if e.get('full') else '1000:563'
    subprocess.run([FF,'-v','error','-y','-ss',str(e['in']),'-t',f'{dur:.2f}','-i',src,
        '-vf',f'fps=30,scale={size}:force_original_aspect_ratio=increase,crop={size}','-q:v','3',os.path.join(d,'f%05d.jpg')],check=True)
    subprocess.run([FF,'-v','error','-y','-ss',str(e['in']+dur/2),'-i',src,'-frames:v','1',
        '-vf','scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=40:3,eq=brightness=-0.12:saturation=0.8','-q:v','4',os.path.join(d,'bg.jpg')],check=True)
    print(e['id'],len([f for f in os.listdir(d) if f.startswith('f')]),'frames')
