// Renders a 1920x1080 scene page to MP4. The page defines window.render(t), window.DURATION and window.OUTPUT.
// Usage: node render-intro.js [page.html] stills 1,3.5,7   |   node render-intro.js [page.html] video [workers=4]
const {chromium}=require('playwright');
const {spawnSync}=require('child_process');
const fs=require('fs'),path=require('path');
const FF='/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2';
const FPS=30,FR=path.join(__dirname,'frames');
const args=process.argv.slice(2);
const PAGE=args[0].endsWith('.html')?args.shift():'intro.html';
const [mode,arg]=args;
async function page(b){
  const p=await b.newPage({viewport:{width:1920,height:1080}});
  await p.goto('file://'+path.join(__dirname,PAGE));
  await p.evaluate(()=>document.fonts.ready);
  await p.waitForTimeout(300);
  return p;
}
(async()=>{
  const b=await chromium.launch();
  if(mode==='stills'){
    const p=await page(b);
    for(const t of arg.split(',').map(Number)){
      await p.evaluate(t=>render(t),t);
      await p.screenshot({path:`still_${path.basename(PAGE,'.html')}_${t}.png`});
    }
  } else {
    const W=+(arg||4);
    const probe=await page(b);
    const {dur,out}=await probe.evaluate(()=>({dur:window.DURATION||8,out:window.OUTPUT||'output/curalle_intro_16x9.mp4'}));
    await probe.close();
    const N=Math.round(FPS*dur);
    fs.rmSync(FR,{recursive:true,force:true});fs.mkdirSync(FR,{recursive:true});
    await Promise.all([...Array(W)].map(async(_,w)=>{
      const p=await page(b);
      for(let i=w;i<N;i+=W){
        await p.evaluate(t=>render(t),i/FPS);
        await p.screenshot({path:path.join(FR,`f${String(i).padStart(4,'0')}.png`)});
      }
    }));
    spawnSync(FF,['-y','-framerate',String(FPS),'-i',path.join(FR,'f%04d.png'),'-c:v','libx264','-pix_fmt','yuv420p','-crf','16','-preset','slow','-movflags','+faststart',out],{stdio:'inherit'});
    fs.rmSync(FR,{recursive:true});
  }
  await b.close();
})();
