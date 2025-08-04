'''
buatkan sebuah program sederhana dengan input sebagai berikut
- Nama
- kota
- gaji

Gaji bersih adalah gaji yang di input di potong pajak 2.5 persen
buatkan output nya menjadi
contoh
nama saya uno, saya tinggal di bogor. Penghasilan saya sebesar Rp. 100000000
'''

#Opsi 1
Nama = input ("Masukkan nama anda: ")
Kota = input ("Masukkan kota tinggal anda: ")
Gaji = input ("Masukkan gaji anda: ")
Pajak = 2.5 / 100 # Karena tidak bisa input langsung 2.5%, jadinya saya ubah seperti ini
gajiBersih = int(Gaji) * (1 - Pajak)
print(int(gajiBersih))
print(type(gajiBersih))
print("Nama saya " + Nama + "," + " " + "saya tinggal di " + Kota + "." + " " + "Penghasilan saya sebesar Rp. " + str(int(gajiBersih)))

# Opsi 2
nama = input ("Masukkan nama anda: ")
kota = input ("Masukkan kota tinggal anda: ")
gaji = input ("Masukkan gaji anda: ")
perhitungan_gaji = int(gaji) * 0.025 # Menghitung gaji jika di kalikan 2.5%
gaji_bersih = int(gaji) - int(perhitungan_gaji) # Lalu gaji di kurangin dengan hasil perhitungan gaji yang dikalikan 2.5%
print(perhitungan_gaji)
print(gaji_bersih)
print(type(gaji_bersih))
print("Nama saya " + nama + "," + " " + "saya tinggal di " + kota + "." + " " + "Penghasilan saya sebesar Rp. " + str(gaji_bersih))