// Renders explainer.html (1080x1920) with the presenter's frames and voice track.
// Page: explainer.html by default, or set PAGE=eczema.html. BROLL=<dir> points at B-roll frames from edit/broll.py.
// Usage:
//   node render-explainer.js stills <framesDir> 1,5.5,30
//   node render-explainer.js video  <framesDir> <voice.wav> [workers=4]
// framesDir holds f00001.jpg... (the cut presenter video at 30fps).
const {chromium}=require('playwright');
const {spawnSync}=require('child_process');
const fs=require('fs'),path=require('path');
const FF='/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2';
const FPS=30,FR=path.join(__dirname,'frames');
const [mode,framesDir,arg,workers]=process.argv.slice(2);
const PAGE=process.env.PAGE||'explainer.html';
const n=fs.readdirSync(framesDir).filter(f=>f.endsWith('.jpg')).length;
async function page(b){
  const p=await b.newPage({viewport:{width:1080,height:1920}});
  await p.goto('file://'+path.join(__dirname,PAGE)+`?frames=${encodeURIComponent(path.resolve(framesDir))}&n=${n}`+(process.env.BROLL?`&broll=${encodeURIComponent(path.resolve(process.env.BROLL))}`:''));
  await p.evaluate(()=>document.fonts.ready);
  await p.waitForTimeout(300);
  return p;
}
(async()=>{
  const b=await chromium.launch({args:['--allow-file-access-from-files']});
  if(mode==='stills'){
    const p=await page(b);
    for(const t of arg.split(',').map(Number)){
      await p.evaluate(t=>render(t),t);
      await p.screenshot({path:`still_${path.basename(PAGE,'.html')}_${t}.png`});
    }
  } else {
    const W=+(workers||4);
    const probe=await page(b);
    const {dur,out}=await probe.evaluate(()=>({dur:window.DURATION,out:window.OUTPUT}));
    await probe.close();
    const N=Math.round(FPS*dur);
    fs.rmSync(FR,{recursive:true,force:true});fs.mkdirSync(FR,{recursive:true});
    let done=0;
    await Promise.all([...Array(W)].map(async(_,w)=>{
      const p=await page(b);
      for(let i=w;i<N;i+=W){
        await p.evaluate(t=>render(t),i/FPS);
        await p.screenshot({path:path.join(FR,`f${String(i).padStart(5,'0')}.jpg`),type:'jpeg',quality:93});
        if(++done%300===0)console.log(`${done}/${N}`);
      }
    }));
    spawnSync(FF,['-y','-v','error','-framerate',String(FPS),'-i',path.join(FR,'f%05d.jpg'),'-i',arg,
      '-filter_complex','[0:v]hqdn3d=1.5:1.5:6:6[v];[1:a]apad[a]','-map','[v]','-map','[a]','-t',String(dur),
      '-c:v','libx264','-pix_fmt','yuv420p','-crf','21','-maxrate','5M','-bufsize','10M','-preset','slow','-c:a','aac','-b:a','192k','-movflags','+faststart',out],{stdio:'inherit'});
    fs.rmSync(FR,{recursive:true});
  }
  await b.close();
})();
