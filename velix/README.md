# VELIX PostbioM Choc: Iklan Gaya VOX (9:16, 15 saat)

Fail: `output/velix_vox_9x16.mp4` (1080×1920, 30fps, tiada audio)

## Storyboard
| Masa | Babak |
|---|---|
| 0–3.4s | Hook: "Kos naik. Gaji tak naik." + graf jurang kos sara hidup vs gaji |
| 3.4–6.6s | Masalah: "Bulan belum habis, duit dah habis." + 4 masalah biasa → "Anda juga?" |
| 6.6–10.4s | Produk: VELIX PostbioM Choc (85% Dark Chocolate, Postbiotics, Ekstrak Moringa, 14 sachet × 25g) |
| 10.4–15s | Peluang: "Minum. Kongsi. Tambah pendapatan." RM1000* seminggu, Modal rendah / Bisnes fleksibel / Mudah dikongsi, CTA "JOM SERTAI VELIX →" |

*Penafian dalam video: "Pendapatan bergantung pada usaha individu dan tidak dijamin."

Tambah muzik berlesen / voiceover dalam CapCut, Meta atau TikTok Ads Manager.

## Render semula
```
(cd ../video && npm install)   # fon + playwright dikongsi dengan folder video/
node render.js stills 3,6.2,10,14.5
node render.js video 15
```
Aset dalam `assets/` dipotong daripada poster Velix.
