from pydub import AudioSegment
import simpleaudio as sa
import os

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