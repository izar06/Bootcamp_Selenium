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

Nama = input("Masukkan nama anda: ")
Kota = input("Masukkan kota tinggal anda: ")
Gaji = input("Masukkan gaji anda: ")
Pajak = 2.5 / 100
gajiBersih = int(Gaji) * (1 - Pajak)
# print(int(gajiBersih))
print("Nama saya" + " " + Nama + "," + " " + "saya tinggal di" + " " + Kota + "." + " " + "Penghasilan saya sebesar Rp." + str(int(gajiBersih)))