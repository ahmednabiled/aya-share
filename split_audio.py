from pydub import AudioSegment, silence
import os, json

AUDIO_PATH = "quran2.mp3"
OUTPUT_DIR = "splitted_audio"

os.makedirs(OUTPUT_DIR, exist_ok=True)

audio = AudioSegment.from_file(AUDIO_PATH, format="mp3")


chunks = silence.split_on_silence(
    audio,
    min_silence_len=100,
    silence_thresh=audio.dBFS - 16,
    keep_silence=25
)

metadata = []

for i, chunk in enumerate(chunks):
    out_path = os.path.join(OUTPUT_DIR, f"chunk_{i}.wav")
    chunk.export(out_path, format="wav")
    metadata.append({
        "file": out_path,
        "duration_ms": len(chunk)
    })

with open(os.path.join(OUTPUT_DIR, "chunks.json"), "w", encoding="utf-8") as f:
    json.dump(metadata, f, ensure_ascii=False, indent=2)

print(f"Done! {len(chunks)} chunks saved in {OUTPUT_DIR}/")
