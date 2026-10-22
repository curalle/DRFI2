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

# BOFU 15 saat: gaya VOX + suara latar BM + Dr. Fareez "bercakap"

Fail: `output/curalle_bofu15_vox_9x16.mp4` (1080×1920, 15s, dengan audio)

| Masa | Babak | Suara latar (ms-MY-OsmanNeural) |
|---|---|---|
| 0–3.05s | Hook: Dr. Fareez (foto sut) bercakap ke kamera | "Dah cuba macam-macam krim, tapi gatal datang balik?" |
| 3.05–6.75s | Produk + kad definisi post·bio·tik | "Cuba Curallé Skin Rebalance. Krim postbiotik untuk kulit ekzema." |
| 6.75–10.1s | Bukti: IIDEX Gold + KKM NOT260403410K + foto keluarga | "Menang anugerah emas IIDEX, dan berdaftar KKM." |
| 10.1–15s | Tawaran: Dr. Fareez (kot makmal) bercakap, RM79 → RM55, STOK TERHAD, BELI SEKARANG | "Promo lima puluh lima ringgit je! Stok terhad, tekan Beli Sekarang!" |

Animasi mulut dijana daripada foto (warp rahang ikut kelantangan suara), bukan AI lip-sync.

## Render semula
```
pip install edge-tts imageio-ffmpeg pillow opencv-python-headless numpy
cd bofu15 && python3 tools/tts.py "+18%" && python3 tools/audio.py && python3 tools/talking.py   # suara + frame mulut (laluan dalam skrip mungkin perlu ditukar)
cd .. && node render15.js stills 1,4.2,8.2,12.3   # semak
node render15.js video && python3 mix_audio.py
```

---

# Explainer 3 minit: gaya VOX, 16:9 (`output/curalle_explainer_16x9.mp4`)

3:08, 1920×1080, suara latar BM (ms-MY-OsmanNeural), sari kata BM dibakar ke dalam video. Menggunakan footage `CURALLE VIDEO.mp4` (botol pam) + 9 babak penerangan gaya Vox. Skrip penuh: `script_2min_vox.md`.

Aliran: hook (footage) → soalan "Kenapa ekzema asyik datang balik?" → dinding bata (skin barrier) → kitaran gatal-garu → mikrobiom → steroid "tampal ≠ bina semula" → produk → Dr. Fareez → post·bio·tik → glycerosome (footage 3D) → dinding dibina semula → cara guna → bukti (IIDEX, KKM) → CTA (RM55, curalle.co / ahli farmasi).

## Render semula
```
pip install edge-tts imageio-ffmpeg numpy
cd explainer && python3 tts_lines.py                       # suara latar per babak -> vo/
python3 build_timeline.py "/path/CURALLE VIDEO.mp4"        # masa babak + potong footage -> foot/
cd .. && node renderex.js stills 13,40,72,124              # semak
node renderex.js sfx                                       # senarai bunyi
for i in 0 1 2 3; do node renderex.js video $((i*1412)) $(((i+1)*1412)) explainer/part$i.mp4 & done; wait
# gabung part0-3 -> explainer/silent.mp4 (ffmpeg concat), kemudian:
python3 mix_explainer.py
```
