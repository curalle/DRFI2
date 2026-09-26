// Renders bofu15.html to a silent 15s 9:16 video (frames piped to ffmpeg). Audio is muxed by mix_audio.py.
const {chromium}=require('playwright');
const {spawn}=require('child_process');
const FF=process.env.FF||'/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2';
(async()=>{
  const [mode,arg]=process.argv.slice(2);
  const b=await chromium.launch();
  const p=await b.newPage({viewport:{width:1080,height:1920}});
  await p.goto('file://'+__dirname+'/bofu15.html');
  await p.evaluate(()=>document.fonts.ready);
  await p.waitForTimeout(300);
  if(mode==='stills'){
    for(const t of arg.split(',').map(Number)){
      await p.evaluate(t=>render(t),t);
      await p.screenshot({path:`bofu15/still_${t}.png`});
    }
  } else {
    const fps=30,N=fps*15;
    const ff=spawn(FF,['-y','-f','image2pipe','-framerate',String(fps),'-c:v','png','-i','-','-c:v','libx264','-pix_fmt','yuv420p','-crf','18','-preset','medium','bofu15/silent.mp4'],{stdio:['pipe','ignore','inherit']});
    for(let i=0;i<N;i++){
      await p.evaluate(t=>render(t),i/fps);
      const buf=await p.screenshot({type:'png'});
      if(!ff.stdin.write(buf)) await new Promise(r=>ff.stdin.once('drain',r));
    }
    ff.stdin.end(); await new Promise(r=>ff.on('close',r));
  }
  await b.close();
})();
