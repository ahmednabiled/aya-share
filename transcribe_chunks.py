import requests, json, os
from pydub import AudioSegment, silence

API_URL = "xxxx/transcribe"
CHUNKS_DIR = "splitted_audio"
OUTPUT_JSON = os.path.join(CHUNKS_DIR, "transcriptions.json")

data = []

for file in sorted(os.listdir(CHUNKS_DIR)):
    if file.endswith(".wav"):
        path = os.path.join(CHUNKS_DIR, file)
        with open(path, "rb") as f:
            res = requests.post(API_URL, files={"file": f})
        text = res.json().get("text", "")
        print(f"Done {file} → {text}")
        duration = AudioSegment.from_file(path).duration_seconds * 1000
        data.append({"file": path, "text": text, "duration_ms": duration})

with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Saved all transcriptions to", OUTPUT_JSON)
