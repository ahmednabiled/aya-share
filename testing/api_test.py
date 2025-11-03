import requests


API_URL = "https://b7da3dc62f65.ngrok-free.app/transcribe"

audio_path = "/home/ahmednabiled/Desktop/aya-share/testing/chunk_0.wav"

with open(audio_path, "rb") as f:
    files = {"file": f}
    response = requests.post(API_URL, files=files)


if response.ok:
    print("✅ Transcription successful:")
    print(response.json())
else:
    print("❌ Error:")
    print(response.status_code, response.text)
