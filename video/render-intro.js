// Renders intro.html (1920x1080, 8s @30fps) to output/curalle_intro_16x9.mp4.
// Usage: node render-intro.js stills 1,3.5,7   |   node render-intro.js video [workers=4]
const {chromium}=require('playwright');
const {spawnSync}=require('child_process');
const fs=require('fs'),path=require('path');
const FF='/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2';
const FPS=30,DUR=8,N=FPS*DUR,FR=path.join(__dirname,'frames');
async function page(b){
  const p=await b.newPage({viewport:{width:1920,height:1080}});
  await p.goto('file://'+__dirname+'/intro.html');
  await p.evaluate(()=>document.fonts.ready);
  await p.waitForTimeout(300);
  return p;
}
(async()=>{
  const [mode,arg]=process.argv.slice(2);
  const b=await chromium.launch();
  if(mode==='stills'){
    const p=await page(b);
    for(const t of arg.split(',').map(Number)){
      await p.evaluate(t=>render(t),t);
      await p.screenshot({path:`still_intro_${t}.png`});
    }
  } else {
    const W=+(arg||4);
    fs.mkdirSync(FR,{recursive:true});
    await Promise.all([...Array(W)].map(async(_,w)=>{
      const p=await page(b);
      for(let i=w;i<N;i+=W){
        const f=path.join(FR,`f${String(i).padStart(4,'0')}.png`);
        if(fs.existsSync(f))continue;
        await p.evaluate(t=>render(t),i/FPS);
        await p.screenshot({path:f});
      }
    }));
    spawnSync(FF,['-y','-framerate',String(FPS),'-i',path.join(FR,'f%04d.png'),'-c:v','libx264','-pix_fmt','yuv420p','-crf','16','-preset','slow','-movflags','+faststart','output/curalle_intro_16x9.mp4'],{stdio:'inherit'});
    fs.rmSync(FR,{recursive:true});
  }
  await b.close();
})();
