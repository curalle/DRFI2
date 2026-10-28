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
python3 edit/cuts.py edit/ceramide.json $S        # → S/src/keep.json (salinan: edit/ceramide.keep.json)
python3 edit/render_cut.py edit/ceramide.json $S  # → S/src/cut.mkv
ffmpeg -i $S/src/cut.mkv -q:v 3 frames_dir/f%05d.jpg
ffmpeg -i $S/src/cut.mkv -vn -af "highpass=f=80,loudnorm=I=-14:TP=-1.5:LRA=11" voice.wav
node render-explainer.js stills <framesDir> 5,45,109
node render-explainer.js video  <framesDir> <voice.wav>
```

---

# Siri DRFI: Ekzema (9:16, 3:53, dengan suara)

`output/drfi_eczema_explainer_9x16.mp4`, halaman `eczema.html`, potongan `edit/eczema.json`.

Disunting daripada rakaman 4:11 (`video_20261027_130719.mp4`): jeda >0.35s dipendekkan (ambang −29 dB kerana bunyi latar bilik), ayat tersasul "semestinya start sebab allergic" dibuang, tamat selepas "Thank you" pertama. 17 segmen, 3:51.5.

| Masa | Babak |
|---|---|
| 0–7s | Hook penuh: "Anak naik ruam & gatal-gatal…" → ECZEMA? |
| 7–17s | "Sebut eczema je tak cukup", kanta pembesar atas ruam |
| 17–24s | Kad nama: Ts. Dr Fareez Ismail, Siri DRFI, CURALLÉ |
| 24–52s | Istilah payung, simptom, pathway berbeza, 1 krim ≠ semua ruam |
| 52–89s | Contoh 1 Atopic dermatitis: imun ↔ barrier, IL-4/IL-13, filaggrin ↓, barrier lemah |
| 89–108s | Contoh 2 Irritant contact dermatitis: pinggan, air, sabun, geseran → lapisan luar rosak |
| 108–122s | Contoh 3 Allergic contact dermatitis: imun kenal pasti alergen (nikel, wangian) |
| 122–129s | Zoom keluar atas tiga contoh → gunung ais: sama di permukaan, punca berbeza |
| 129–175s | 3 soalan penting + peta badan (tangan, lipatan), jumpa doktor & ujian |
| 175–190s | Mummies: tak perlu hafal; rupa ruam = petunjuk, bukan diagnosis |
| 190–212s | Pelembap vs rawatan spesifik; tip log ruam & bawa produk |
| 212–233s | Save video, Siri DRFI, terima kasih |

**B-roll** (8 sisipan, senarai dalam `edit/eczema.json` → `broll`): klip melintang dipaparkan sebagai kad foto (zoom masuk/keluar) atas latar kabur, klip menegak penuh skrin; penyampai kekal dalam bingkai terapung.

| Masa | Klip Mixkit | Label |
|---|---|---|
| 0:19 | Saintis & mikroskop (4733) | (kad nama) |
| 1:35 | Ibu & anak membasuh (8716) → air paip (10334) → buih sabun (44799) | Cuci pinggan / Air / Sabun |
| 1:58 | Cincin (5218) | Nikel, cth. barang kemas |
| 2:46 | Saintis sediakan sampel (4767) | Kadang-kadang perlu ujian |
| 3:11 | Sapu krim pelembap (50426) | Pelembap: kekalkan hidrasi |
| 3:22 | Menulis nota (42655) | Catat log ruam |

Lesen: semua klip berlabel **Mixkit Stock Video Free License** (guna komersial, tanpa atribusi). Klip berlabel "Restricted" sengaja tidak digunakan.

```
python3 edit/broll.py edit/eczema.json <klipMixkit> <brollDir>
PAGE=eczema.html BROLL=<brollDir> node render-explainer.js video <framesDir> <voice.wav>
```

## Versi YouTube 16:9

`output/drfi_eczema_explainer_16x9.mp4`: 1920×1080, 30fps, 3:53, dengan suara & B-roll.

`eczema169.html` dijana daripada `eczema.html` oleh `edit/make_landscape.py`, jadi pembetulan pada versi 9:16 dibawa ke 16:9 dengan menjana semula:
- Setiap jubin: tajuk/teks (atas) → lajur kiri; ilustrasi (bawah) → dikumpul & diskala ke lajur kanan.
- Penyampai penuh skrin = panel kanan 1280×1080 (kepala hingga bahu), kad teks atas kertas di kiri; bingkai terapung di kiri bawah.
- B-roll: kad 1200×675 di kanan (bingkai diekstrak semula pada 1280×720).

```
python3 edit/make_landscape.py
python3 edit/broll.py edit/eczema.json <klipMixkit> <brollDir169> 1280:720
PAGE=eczema169.html SIZE=1920x1080 BROLL=<brollDir169> node render-explainer.js video <framesDir> <voice.wav>
```

---

# Siri DRFI: Pompholyx / Dyshidrotic Eczema (9:16 & 16:9, 2:46, dengan suara)

`output/drfi_pompholyx_explainer_9x16.mp4` dan `output/drfi_pompholyx_explainer_16x9.mp4`.

Gabungan dua rakaman (`edit/pompholyx.json`):
- `video_20261028_170527` (1:23): hook, pompholyx, mitos saluran peluh; diambil hingga "that's a big no". Bahagian lepuh pecah → barrier dirakam semula dalam rakaman kedua, dan rakaman ini berakhir dengan tersasul ("Tapi jangan, apa benda ni"), jadi dibuang.
- `video_20261028_170719` (2:06): ambilan semula dari "Bila lepuh ni pecah…" hingga "jumpa lagi".
- Jeda >0.35s dipendekkan (−29 dB). 33 segmen, 2:44.5.

| Masa | Babak |
|---|---|
| 0–9s | Hook penuh: "Bintik air kecil di celah jari?" → GATAL! → kulit menggelupas |
| 9–17s | "Ruam panas? Tangan naik air?" dicoret → Dyshidrotic eczema |
| 17–22s | Kad nama, "a.k.a. Pompholyx" |
| 22–30s | Lepuh kecil & sangat gatal; tangan / kaki / kedua-duanya |
| 30–40s | Fun fact: "saluran peluh tersumbat" → MITOS |
| 40–48s | Pecahkan lepuh ≠ buang punca → "BIG NO." |
| 48–74s | Barrier terganggu; B-roll air/sabun/pencuci; "Ouch!"; kitaran ganas; B-roll memotong (memasak) |
| 75–92s | Zoom keluar → pencetus: B-roll stres, hujan, detergen; rujukan video ekzema |
| 92–97s | Jangan buang semua makanan lepas tengok satu video |
| 97–126s | Keep track (B-roll menulis), apa TIDAK patut buat, bila jumpa doktor |
| 126–140s | Rawatan: kawal keradangan + jaga barrier; krim kosmetik ≠ penawar |
| 140–152s | Tip mak-mak: tangkap gambar masa aktif untuk doktor |
| 152–166s | Save, share (mitos peluh tersumbat), jumpa lagi |

B-roll Mixkit (lesen Free): 8716 (cuci), 40534 (tomato), 39854 (stres), 2716 (hujan), 4564 (detergen), 42655 (menulis). Dalam 16:9, klip menegak dipaparkan sebagai kad potret.

Halaman: `pompholyx.html` dibina oleh `edit/make_pompholyx.py` (kandungan dalam `edit/pompholyx_parts.py`, enjin daripada `eczema.html`); `pompholyx169.html` oleh `python3 edit/make_landscape.py pompholyx.html pompholyx169.html`.

```
python3 edit/cuts.py edit/pompholyx.json $S && python3 edit/render_cut.py edit/pompholyx.json $S   # → S/src3/cut.mkv
python3 edit/broll.py edit/pompholyx.json <klip> <br>; python3 edit/broll.py edit/pompholyx.json <klip> <br169> 1280:720
PAGE=pompholyx.html BROLL=<br> node render-explainer.js video <framesDir> <voice.wav>
PAGE=pompholyx169.html SIZE=1920x1080 BROLL=<br169> node render-explainer.js video <framesDir> <voice.wav>
```
