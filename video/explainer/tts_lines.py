# Generates one Malay VO clip per script beat (ms-MY-OsmanNeural) with word timings -> vo/NN.mp3 + vo/words.json
import certifi; certifi.where=lambda: "/root/.ccr/ca-bundle.crt"
import asyncio, edge_tts, json, sys
LINES={
 "a":"Pagi tu, dia bangun ceria. Macam budak lain.",
 "b":"Sampailah rasa gatal tu datang balik. Lagi.",
 "v1":"Kalau anak anda ada ekzema, anda mesti pernah tanya soalan ni.",
 "c":"Sapu krim, reda sekejap. Seminggu kemudian, merah balik. Ramai ibu bapa terperangkap dalam kitaran yang sama. Tapi untuk faham kenapa, kita kena tengok lebih dekat. Sangat dekat.",
 "v2":"Lapisan paling luar kulit kita, macam dinding bata. Batanya ialah sel kulit. Simennya pula, lemak semula jadi yang dipanggil ceramide. Pada kulit ekzema, simen ni tak cukup. Dinding jadi bocor. Air keluar, kulit kering. Bahan perengsa masuk, kulit meradang.",
 "v3":"Kulit yang bocor, rasa gatal. Bila digaru, dinding makin rosak. Dan bila makin rosak, makin gatal. Inilah kitaran gatal-garu.",
 "v4":"Ada satu lagi lapisan yang orang jarang cakap. Kulit kita dihuni berbilion bakteria. Pada kulit sihat, bakteria baik dan jahat seimbang. Masa ekzema flare, bakteria jahat seperti Staph aureus ambil alih, dan keradangan jadi lebih teruk.",
 "v5":"Krim steroid ada peranannya, ikut nasihat doktor. Tapi ia meredakan radang. Ia tak membina semula dinding, dan tak seimbangkan semula bakteria.",
 "d":"Jadi persoalannya, macam mana nak baiki kedua-duanya sekali?",
 "v6":"Itu soalan yang Doktor Fareez Ismail, saintis bioperubatan dari U-I-T-M, cuba jawab, bila beliau formulasikan Kurale.",
 "v7":"Bahan utamanya, postbiotik. Ia hasil fermentasi bakteria baik. Bukan bakteria hidup, tapi mesej yang bantu kulit seimbangkan semula mikrobiomnya.",
 "f":"Tapi bahan yang bagus tak berguna, kalau tak sampai ke tempatnya. Sebab itu, postbiotik ni dibawa dalam glycerosome. Gelembung lembut yang boleh melentur, menyelit di celah-celah sel kulit, dan lepaskan postbiotik betul-betul di tempat yang perlu.",
 "v8":"Kemudian, barisan bahan lain sambung kerja. Oatmeal koloid untuk redakan gatal. Ceramide dan omega tiga untuk tampal simen dinding. Panthenol dan gliserin untuk hidrasi. Dan lapisan pelindung, untuk kunci kelembapan.",
 "e":"Cara guna? Mudah. Sapu pada kulit bersih, dua kali sehari. Pagi, dan malam.",
 "v9":"Pemenang pingat emas IIDEX dua ribu dua puluh lima. Berdaftar dengan KKM. Diuji makmal, bebas steroid, SLS dan paraben. Cukup lembut untuk seisi keluarga.",
 "g":"Sebab setiap anak berhak, untuk lalui hari tanpa fikir pasal gatal.",
 "h":"Kurale Skin Rebalance. Dapatkan sekarang di curalle dot co, atau tanya ahli farmasi anda.",
}
async def one(k,t):
    c=edge_tts.Communicate(t,"ms-MY-OsmanNeural",rate="+4%",boundary="WordBoundary")
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
