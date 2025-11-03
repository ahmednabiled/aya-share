from pydub import AudioSegment
from pydub.silence import split_on_silence

# Corrected version
audio = AudioSegment.from_file("/home/ahmednabiled/Desktop/aya-share/testing/quran.mp3", format="mp3")

chunks = split_on_silence(
    audio,
    min_silence_len=200,
    silence_thresh=-40,
    keep_silence=50
)

for i, chunk in enumerate(chunks):
    out_file = f"chunk_{i}.wav"
    print(f"Exporting {out_file}")
    chunk.export(out_file, format="wav")
