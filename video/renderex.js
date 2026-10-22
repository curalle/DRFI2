// Renders explainer.html (1920x1080, 30fps). Usage:
//   node renderex.js stills 3.2,40,...            -> explainer/stills/*.png
//   node renderex.js video <fromFrame> <toFrame> <out.mp4>   (silent chunk; run several in parallel)
//   node renderex.js sfx                          -> explainer/sfx.json (cue list for mix_explainer.py)
const {chromium}=require('playwright');
const {spawn}=require('child_process');
const fs=require('fs');
const FF=process.env.FF||'/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2';
(async()=>{
  const [mode,a1,a2,a3]=process.argv.slice(2);
  const b=await chromium.launch();
  const p=await b.newPage({viewport:{width:1920,height:1080}});
  p.on('console',m=>{if(m.type()==='warning'||m.type()==='error')console.log('PAGE',m.text());});
  await p.goto('file://'+__dirname+'/explainer.html');
  await p.evaluate(()=>document.fonts.ready);
  await p.waitForTimeout(400);
  if(mode==='stills'){
    fs.mkdirSync(__dirname+'/explainer/stills',{recursive:true});
    for(const t of a1.split(',').map(Number)){
      await p.evaluate(t=>render(t),t);
      await p.screenshot({path:`explainer/stills/${t}.png`});
    }
  } else if(mode==='sfx'){
    fs.writeFileSync(__dirname+'/explainer/sfx.json',JSON.stringify(await p.evaluate(()=>SFX())));
  } else {
    const from=+a1,to=+a2;
    const ff=spawn(FF,['-y','-f','image2pipe','-framerate','30','-c:v','mjpeg','-i','-','-c:v','libx264','-pix_fmt','yuv420p','-crf','18','-preset','medium',a3],{stdio:['pipe','ignore','inherit']});
    for(let i=from;i<to;i++){
      await p.evaluate(t=>render(t),i/30);
      const buf=await p.screenshot({type:'jpeg',quality:94});
      if(!ff.stdin.write(buf)) await new Promise(r=>ff.stdin.once('drain',r));
      if(i%300===0) console.log(a3,i);
    }
    ff.stdin.end(); await new Promise(r=>ff.on('close',r));
  }
  await b.close();
})();
