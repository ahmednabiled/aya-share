from moviepy import ImageClip, TextClip, CompositeVideoClip

bg_path = "/home/ahmednabiled/Desktop/aya-share/testing/bg.png"

caption_text = "إِنَّ مَعَ الْعُسْرِ يُسْرًا"

bg_clip = ImageClip(bg_path, duration=10)

txt_clip = TextClip(
    font="/home/ahmednabiled/Desktop/aya-share/testing/TheYearofTheCamel-Regular.otf",  # Font that supports Arabic
    text=caption_text,
    font_size=60,
    color="white",
    size=bg_clip.size,
    method='caption'
).with_duration(10).with_position('center')

final_clip = CompositeVideoClip([bg_clip, txt_clip])

final_clip.write_videofile('output.mp4', fps=24)
