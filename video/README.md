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

## Render semula (16:9)
```
node render-intro.js intro.html stills 1.6,5.5,7.9      # semak frame
node render-intro.js intro.html video                   # output/curalle_intro_16x9.mp4
node render-intro.js microencap.html video              # output/curalle_microencap_16x9.mp4
```
