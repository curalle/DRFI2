# CURALLÉ Skin Rebalance: Iklan Gaya VOX (9:16, 19 saat)

| Fail | Funnel | CTA |
|---|---|---|
| `output/curalle_tofu_9x16.mp4` | TOFU (kesedaran) | Ketahui lebih → curalle.co |
| `output/curalle_bofu_9x16.mp4` | BOFU (jualan) | DAPATKAN SEKARANG → curalle.co |

## Storyboard
| Masa | Babak |
|---|---|
| 0–3.6s | Hook: "Gatal. Garu. Merah. Ulang." + rajah kitaran ekzema |
| 3.6–7.6s | Punca: krim steroid cuma "tampal" flare; skin barrier lemah & mikrobiom tak seimbang (rajah bata "bocor") |
| 7.6–11.6s | Kad definisi "post·bio·tik"; barrier dibina semula |
| 11.6–15.4s | Produk + bahan: Postbiotik, Oatmeal koloid, Ceramide + Omega-3, Panthenol; bebas steroid, SLS & paraben; berdaftar KKM |
| 15.4–19s | TOFU: petikan founder + anugerah IIDEX + CTA · BOFU: anugerah, KKM NOT260403410K, diuji makmal + CTA |

Video ini tiada audio. Tambah muzik berlesen dalam Meta/TikTok Ads Manager.

## Render semula
```
npm install
node render.js stills tofu 2.8,14.9   # semak frame
npm run tofu && npm run bofu           # perlukan ffmpeg dengan libx264 (tukar laluan FF dalam render.js)
```
Aset dalam `assets/` diambil daripada poster A3 CURALLÉ.

---

# CURALLÉ Intro (16:9, 8 saat)

`output/curalle_intro_16x9.mp4`: 1920×1080, 30fps, tiada audio.

| Masa | Babak |
|---|---|
| 0–3.4s | Mikroskop gelap, bakteria merah gelisah: "Some see bacteria as a **threat.**" + amaran patogen |
| 3.4–4.4s | Cahaya mekar dari kanta; bakteria bertukar ungu/emas & mengorbit dengan tenang |
| 4.0–6.0s | "I see them as **a solution.**" + founder dalam kanta (Ts. Dr Muhamad Fareez Ismail) |
| 6.2–8s | Logo CURALLÉ: "The science of postbiotics. Good bacteria, working for healthier skin." |

# Babak Mikroenkapsulasi (16:9, 20 saat)

`output/curalle_microencap_16x9.mp4`: 1920×1080, 30fps, tiada audio.

| Masa | Babak |
|---|---|
| 0–7.3s | "Probiotics are *fragile.*": dua piring (haba & asid perut, pH 7 → 2); bakteria mati perlahan, bar "Live probiotics" jatuh ke CRITICAL |
| 7.3–14.5s | "Micro-encapsulation.": bakteria dikumpul dalam kapsul; haba & titisan asid melantun keluar; ✓ Survives heat / stomach acid; lencana LRGS |
| 14.5–20s | "Patented formulation.": sijil Utility Innovation, meterai GRANTED 2020; penutup logo CURALLÉ "From an LRGS research project to your skin." |

# Babak Produk (16:9, 16 saat)

`output/curalle_products_16x9.mp4`: 1920×1080, 30fps, tiada audio. Produk dilukis (tiada foto produk dalam `assets/`).

| Masa | Babak |
|---|---|
| 0–3.5s | "From the lab to *innovation.*": kapsul besar pecah jadi awan mikrokapsul |
| 3.5–8.8s | PROBIOLOAF: mikrokapsul terbang masuk ke dalam kepingan roti; roset "Award winning" + cip "Award-winning innovation" |
| 8.8–13.6s | BrewCoffee Cube: mikrokapsul masuk ke kiub kopi; kiub jatuh ke dalam cawan, riak & wap; "Just drop, stir & sip" |
| 13.6–16s | "One microcapsule. Many innovations.": PROBIOLOAF + BrewCoffee Cube bersebelahan |

# Babak Pengiktirafan (16:9, 30 saat)

`output/curalle_recognition_16x9.mp4`: 1920×1080, 30fps, tiada audio.

| Masa | Babak |
|---|---|
| 0–7.5s | "Born from *research.*": kad geran FRGS, kaunter RM0 → RM186,000 |
| 7.5–14s | "From lab to *market.*": tiub CURALLÉ + langkah Research (FRGS) → Incubation (PMI · UiTM) → Market |
| 14–22s | "Award-*winning.*": lencana ITEX, MTE (dilukis) + IIDEX Gold 25 & Silver 24 (aset asal) |
| 22–30s | "Shared with *the world.*": peta titik Asia (Natural Earth), pin Malaysia → Indonesia, Korea Selatan, Jepun; penutup logo |

`assets/asia_dots.js` dijana daripada `world-atlas` (land-50m) dengan unjuran Mercator 860×780.

## Render semula (16:9)
```
node render-intro.js intro.html stills 1.6,5.5,7.9      # semak frame
node render-intro.js intro.html video                   # output/curalle_intro_16x9.mp4
node render-intro.js microencap.html video              # output/curalle_microencap_16x9.mp4
node render-intro.js products.html video                # output/curalle_products_16x9.mp4
node render-intro.js recognition.html video             # output/curalle_recognition_16x9.mp4
```

---

# Video Penerangan Ceramide (9:16, 2:17, dengan suara)

`output/curalle_ceramide_explainer_9x16.mp4`: 1080×1920, 30fps, audio AAC (suara asal, highpass 80Hz + loudnorm −14 LUFS).

Disunting daripada rakaman selfie 2:51 (`video_20261023_170430.mp4`):
- Jeda panjang (>0.35s) dipendekkan kepada ~0.25s; 40 segmen, 2:15.6.
- Ayat berulang dibuang: "sesuai untuk segala jenis kulit" pertama (diulang semula) dan cubaan pertama "Jangan lupa…".
- Grafik gaya Vox pada "jubin kertas"; kamera zoom keluar / pan / zoom masuk antara jubin.
- Penyampai skrin penuh untuk hook, "Tapi masalahnya", "Apa bezanya?" dan CTA; selebihnya bingkai terapung (atas kanan, elak butang TikTok).

| Masa | Babak |
|---|---|
| 0–5s | Hook: "Semua pelembap ceramide sama je?" + 3 balang |
| 5–16s | Formulasi tentukan meresap masuk vs duduk di atas (keratan kulit) |
| 16–24.6s | Contoh Ceramide NP: repair barrier, lock in moisture |
| 24.6–44s | "TAPI…" molekul keras, susah stabil; perlu campur lipid berasingan |
| 44–55s | CURALLÉ: Omega-3 Ceramide Flex = linseed oil + palm oil → aminopropanediol esters |
| 55–67s | Pseudo-ceramide biomimetik; omega-3 diikat dalam rantai |
| 67–71s | "Apa bezanya?" |
| 71–108s | 1 Lebih stabil · 2 Dual action · 3 Kawal 5-alpha reductase, tanpa melekit |
| 108–126s | Zoom keluar penuh → "Advanced barrier support"; tenang, kuat & sihat |
| 126–137s | Ekzema + CTA "Tekan beg kuning" |

Render (rakaman asal tidak disimpan dalam repo):
```
# 1) S=<folder kerja> dengan S/src/user.mp4 dan S/src/audio.wav (16kHz mono)
python3 edit/cuts.py $S          # → S/edit/keep.json (senarai segmen; salinan dalam edit/keep.json)
python3 edit/render_cut.py $S    # → S/edit/cut.mkv
ffmpeg -i $S/edit/cut.mkv -q:v 3 frames_dir/f%05d.jpg
ffmpeg -i $S/edit/cut.mkv -vn -af "highpass=f=80,loudnorm=I=-14:TP=-1.5:LRA=11" voice.wav
node render-explainer.js stills <framesDir> 5,45,109
node render-explainer.js video  <framesDir> <voice.wav>
```
