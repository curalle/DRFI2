const {chromium}=require('../video/node_modules/playwright');
const {spawn}=require('child_process');
const FF='/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2';
(async()=>{
  const [mode,arg]=process.argv.slice(2);
  const b=await chromium.launch();
  const p=await b.newPage({viewport:{width:1080,height:1920}});
  await p.goto('file://'+__dirname+'/video.html');
  await p.evaluate(()=>document.fonts.ready);
  await p.waitForTimeout(300);
  if(mode==='stills'){
    for(const t of arg.split(',').map(Number)){
      await p.evaluate(t=>render(t),t);
      await p.screenshot({path:`still_${t}.png`});
    }
  } else {
    const fps=30,dur=+arg,N=Math.round(fps*dur);
    const ff=spawn(FF,['-y','-f','image2pipe','-framerate',String(fps),'-c:v','png','-i','-','-c:v','libx264','-pix_fmt','yuv420p','-crf','18','-preset','medium','-movflags','+faststart','output/velix_vox_9x16.mp4'],{stdio:['pipe','ignore','inherit']});
    for(let i=0;i<N;i++){
      await p.evaluate(t=>render(t),i/fps);
      const buf=await p.screenshot({type:'png'});
      if(!ff.stdin.write(buf)) await new Promise(r=>ff.stdin.once('drain',r));
    }
    ff.stdin.end(); await new Promise(r=>ff.on('close',r));
  }
  await b.close();
})();
