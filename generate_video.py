from moviepy import ImageClip, TextClip, CompositeVideoClip, concatenate_videoclips, AudioFileClip, vfx
import json, os

OUTPUT_DIR = "splitted_audio"
FINAL_VIDEO = "final_video.mp4"
ORIGINAL_AUDIO = "quran.mp3"
BG_PATH = "testing/bg.png"
FONT_PATH = "testing/TheYearofTheCamel-Regular.otf"


FADE_DURATION = 0.8  
MIN_DURATION_FOR_FADE = 1.0  

with open(os.path.join(OUTPUT_DIR, "transcriptions.json"), encoding="utf-8") as f:
    data = json.load(f)

print(f"Processing {len(data)} clips...")

clips = []
for i, item in enumerate(data):
    caption_text = item["text"].strip()
    duration = item["duration_ms"] / 1000.0
    
    print(f"Clip {i+1}/{len(data)}: {caption_text[:50]}... (duration: {duration:.2f}s)")

    
    bg_clip = ImageClip(BG_PATH, duration=duration)
    
    
    fade_duration = min(FADE_DURATION, duration / 3) if duration > MIN_DURATION_FOR_FADE else 0
    
    
    txt_clip = (
        TextClip(
            text=caption_text,
            font=FONT_PATH,
            font_size=60,
            color="white",
            size=bg_clip.size,
            method="caption",
        )
        .with_duration(duration)
        .with_position("center")
    )
    
    
    if fade_duration > 0:
        txt_clip = txt_clip.with_effects([
            vfx.FadeIn(fade_duration),
            vfx.FadeOut(fade_duration)
        ])

    
    composite_clip = CompositeVideoClip([bg_clip, txt_clip]).with_duration(duration)
    clips.append(composite_clip)

print("Concatenating clips...")

final_video = concatenate_videoclips(clips, method="compose")
audio = AudioFileClip(ORIGINAL_AUDIO)
final_output = final_video.with_audio(audio)
final_output.write_videofile(FINAL_VIDEO, fps=24)
