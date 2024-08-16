from PIL import Image, ImageFilter
import os

# Memuat gambar
image = Image.open('./images/wallpapers.jpg')

if not os.path.exists('./result'):
    os.makedirs('./result')

# Menyimpan gambar
image.save('./result/result.jpg')

cropped_image = image.crop((10, 10, 200, 200)) # (kiri, atas, kanan, bawah)
cropped_image.save('./result/cropped_result.jpg')

resized_image = cropped_image.resize((100, 100)) # (lebar, tinggi)
resized_image.save('./result/resized_result.jpg')

filtered_image = image.filter(ImageFilter.BLUR)
filtered_image.save('./result/filtered_result.jpg')

# Jika gambar dalam mode RGBA, ubah menjadi RGB
if filtered_image.mode == 'RGBA':
    filtered_image = filtered_image.convert('RGB')

# Membuka gambar
image2 = Image.open('./images/hitori_gotou.png')

# Mengubah ukuran gambar
resized_image2 = image2.resize((100, 100))

# Menambahkan efek blur
filtered_image2 = resized_image2.filter(ImageFilter.BLUR)

# Menyimpan gambar hasil sebagai PNG tanpa perlu mengonversi mode warna
filtered_image2.save('./result/filtered_result2.png')


from pydub import AudioSegment
import simpleaudio as sa

# Memuat file audio MP3
audio = AudioSegment.from_file('./music/mclr.mp3')

# Membuat folder output jika belum ada
if not os.path.exists('./result/audio'):
    os.makedirs('./result/audio')

# Mengonversi ke WAV
audio.export('./result/audio/result.wav', format='wav')

# Memutar audio
wave_obj = sa.WaveObject.from_wave_file('./result/audio/result.wav')
play_obj = wave_obj.play()

# Menunggu sampai audio selesai diputar
play_obj.wait_done()

# Memotong audio
clipped_audio = audio[:10000]  # Mendapatkan 10 detik pertama
clipped_audio.export('./result/audio/clipped_result.mp3', format='mp3')

# Menggabungkan dua audio
combined_audio = audio + clipped_audio
combined_audio.export('./result/audio/combined_result.mp3', format='mp3')

# Konversi ke WAV
audio.export('./result/audio/result.wav', format='wav')

louder_audio = audio + 10  # Meningkatkan volume sebesar 10dB
louder_audio.export('./result/audio/louder_result.mp3', format='mp3')



