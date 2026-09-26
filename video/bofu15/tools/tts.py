import certifi; certifi.where=lambda: "/root/.ccr/ca-bundle.crt"
import asyncio, edge_tts, json, sys
LINES=[
 "Dah cuba macam-macam krim, tapi gatal datang balik?",
 "Cuba Kurale Skin Rebalance. Krim postbiotik untuk kulit ekzema.",
 "Menang anugerah emas IIDEX, dan berdaftar KKM.",
 "Promo lima puluh lima ringgit je! Stok terhad, tekan Beli Sekarang!",
]
async def main(rate):
  out=[]
  for i,t in enumerate(LINES):
    c=edge_tts.Communicate(t,"ms-MY-OsmanNeural",rate=rate,boundary="WordBoundary")
    words=[]; audio=b""
    async for ch in c.stream():
      if ch["type"]=="audio": audio+=ch["data"]
      elif ch["type"]=="WordBoundary": words.append([ch["offset"]/1e7,(ch["offset"]+ch["duration"])/1e7,ch["text"]])
    open(f"vo{i}.mp3","wb").write(audio); out.append(words)
  json.dump(out,open("words.json","w"),ensure_ascii=False,indent=0)
asyncio.run(main(sys.argv[1]))
