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

print('Proses selesai')



