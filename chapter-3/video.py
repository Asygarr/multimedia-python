from moviepy.editor import VideoFileClip
from moviepy.editor import concatenate_videoclips
from moviepy.editor import vfx
import os

# Memuat file video
video = VideoFileClip('./video/meme.mp4')

if not os.path.exists('./result/video'):
    os.makedirs('./result/video')

# Menyimpan file video
video.write_videofile('./result/video/result.mp4')

# Memotong video
short_video = video.subclip(0, 10)  # Mendapatkan 10 detik pertama
short_video.write_videofile('./result/video/short_result.mp4')

# Menggabungkan dua video
combined_video = concatenate_videoclips([video, short_video])
combined_video.write_videofile('./result/video/combined_result.mp4')

# Membalikkan video
reversed_video = short_video.fx(vfx.time_mirror)  # Membalikkan video
reversed_video.write_videofile('./result/video/reversed_result.mp4')

# Mempercepat video
sped_up_video = short_video.fx(vfx.speedx, 2)  # Mempercepat video 2x
sped_up_video.write_videofile('./result/video/sped_up_result.mp4')