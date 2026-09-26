"""Add a Bahasa Melayu voiceover to output/velix_vox_9x16.mp4.

  python3 voiceover.py                 # generate with edge-tts (needs speech.platform.bing.com)
  python3 voiceover.py --voice ms-MY-OsmanNeural
  python3 voiceover.py --audio my.m4a  # use your own recording (15s, starts at 0:00)

Output: output/velix_vox_9x16_vo.mp4
"""
import argparse, asyncio, os, subprocess, tempfile

FF = '/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2'
HERE = os.path.dirname(os.path.abspath(__file__))
VIDEO = os.path.join(HERE, 'output/velix_vox_9x16.mp4')
OUT = os.path.join(HERE, 'output/velix_vox_9x16_vo.mp4')

# (start, end, line): each line is squeezed to fit its scene window
SCRIPT = [
    (0.15, 3.3, 'Kos sara hidup naik, tapi gaji tak naik-naik.'),
    (3.5, 6.5, 'Bulan belum habis, duit dah habis. Anda pun sama?'),
    (6.7, 10.3, 'Kenali Velix PostbioM Choc. Coklat gelap lapan puluh lima peratus, dengan postbiotik dan moringa.'),
    (10.5, 14.8, 'Minum, kongsi, dan tambah pendapatan. Jom sertai Velix hari ini!'),
]


def ff(*args):
    subprocess.run([FF, '-y', '-loglevel', 'error', *args], check=True)


def duration(path):
    r = subprocess.run([FF, '-i', path], capture_output=True, text=True)
    h, m, s = r.stderr.split('Duration: ')[1].split(',')[0].split(':')
    return int(h) * 3600 + int(m) * 60 + float(s)


async def tts(text, voice, path):
    import edge_tts
    await edge_tts.Communicate(text, voice, rate='+10%').save(path)


def build_track(voice, tmp):
    parts = []
    for i, (a, b, line) in enumerate(SCRIPT):
        raw = os.path.join(tmp, f'l{i}.mp3')
        asyncio.run(tts(line, voice, raw))
        speed = max(1.0, duration(raw) / (b - a))
        fit = os.path.join(tmp, f'l{i}.wav')
        ff('-i', raw, '-af', f'atempo={speed:.3f},adelay={int(a * 1000)}:all=1', '-ar', '48000', fit)
        parts.append(fit)
        print(f'line {i + 1}: {duration(raw):.2f}s -> x{speed:.2f}')
    track = os.path.join(tmp, 'vo.wav')
    ins = sum((['-i', p] for p in parts), [])
    ff(*ins, '-filter_complex', f'amix=inputs={len(parts)}:normalize=0,apad', '-t', '15', track)
    return track


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--voice', default='ms-MY-YasminNeural')
    ap.add_argument('--audio', help='use an existing recording instead of TTS')
    args = ap.parse_args()
    with tempfile.TemporaryDirectory() as tmp:
        track = args.audio or build_track(args.voice, tmp)
        ff('-i', VIDEO, '-i', track, '-map', '0:v', '-map', '1:a', '-c:v', 'copy',
           '-af', 'loudnorm=I=-14:TP=-1', '-ar', '48000', '-c:a', 'aac', '-b:a', '192k', '-t', '15',
           '-movflags', '+faststart', OUT)
    print('wrote', OUT)


if __name__ == '__main__':
    main()
