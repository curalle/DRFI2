# Generates one English VO clip per script beat (en-US-AndrewNeural) with word timings -> vo/NN.mp3 + vo/words.json
import certifi; certifi.where=lambda: "/root/.ccr/ca-bundle.crt"
import asyncio, edge_tts, json, sys
LINES={
 "a":"She woke up happy. Like any other kid.",
 "b":"Then the itch came back. Again.",
 "v1":"If your child has eczema, you've probably asked this question.",
 "c":"The cream works for a while. Then the redness returns. To understand why, we need to look closer.",
 "v2":"The outer layer of your skin works like a brick wall. Skin cells are the bricks. Natural fats called ceramides are the mortar. In eczema, there isn't enough mortar. Water escapes, irritants get in, and the skin flares up.",
 "v4":"There's a second problem. Billions of bacteria live on your skin. When eczema flares, bad bacteria like Staph aureus take over, and the inflammation gets worse.",
 "d":"So how do you fix both at once?",
 "v6":"That's the question Doctor Fareez Ismail, a biomedical scientist from U.I.T.M., set out to answer with Koo-rah-lay.",
 "v7":"Its key ingredient is postbiotics: what good bacteria produce when they ferment. Not live bacteria, but signals that help your skin rebalance its microbiome.",
 "f":"To get them where they're needed, they travel inside glycerosomes. Soft, flexible carriers that slip between skin cells, and release the postbiotics deep inside.",
 "v8":"Then the rest of the formula rebuilds the wall. Colloidal oatmeal soothes the itch. Ceramides and omega-3 restore the mortar. Panthenol and glycerin hydrate. And a protective layer locks the moisture in.",
 "e":"Apply on clean skin, twice a day. Morning, and night.",
 "v9":"A gold award winner at IIDEX 2025. Registered with Malaysia's Ministry of Health. Lab tested, and free from steroids, SLS and parabens.",
 "g":"Because every child deserves a day without thinking about the itch.",
 "h":"Koo-rah-lay Skin Rebalance. Get yours at curalle dot co, or ask your pharmacist.",
}
async def one(k,t):
    c=edge_tts.Communicate(t,"en-US-AndrewNeural",rate="+0%",boundary="WordBoundary")
    audio=b"";w=[]
    async for ch in c.stream():
        if ch["type"]=="audio": audio+=ch["data"]
        elif ch["type"]=="WordBoundary": w.append([round(ch["offset"]/1e7,3),round((ch["offset"]+ch["duration"])/1e7,3),ch["text"]])
    open(f"vo/{k}.mp3","wb").write(audio); return k,w
async def main():
    r=[]
    for k,t in LINES.items():
        for attempt in range(4):
            try: r.append(await one(k,t)); break
            except Exception as e: print(k,'retry',e.__class__.__name__); await asyncio.sleep(2**attempt)
    json.dump(dict(r),open("vo/words.json","w"),ensure_ascii=False)
asyncio.run(main())
