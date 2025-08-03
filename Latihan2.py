# Variable

# Snake Case
nilai_bilangan = 20

# Camel Case
nilaiBilangan = 20

# Tipe data
# Number
# Integer & FLoat
num1 = 10
num2 = 20
hasil1 = num1 + num2
hasil2 = num1 + 20
hasil3 = 10 + 20

print(hasil1)
print(hasil2)
print(hasil3)
print(100 + 40)

var1 = 50
var2 = 10

pembagian = var1 / var2
print(pembagian)
print(type(pembagian))
#Pembagian akan selalu menjadi type data float
#Operasi matematika jika ada nilai float akan menghasilkan type data float

#modulo
modulo1 = 0
modulo2 = 4

modulo = modulo1 % modulo2
print(modulo)
print(type(modulo))


#exponensial
eksponensial1 = 0
eksponensial2 = 4

exponensial = eksponensial1 % eksponensial2
print(exponensial)
print(type(exponensial))


#floordivison
floordivision1 = 0
floordivision2 = 4

floordivison = eksponensial1 % eksponensial2
print(floordivison)
print(type(floordivison))

#Tipe data
setring = 'saya'
docstring = '''Lorem
ipsum
'''

var1 = 'saya'
var2 = 'izar'

huruf = var1 + ' ' + var2 #Concate
print(huruf)
print(type(huruf))

#input
nama = input('Masukkan nama anda: ') # Semua input type data nya adalah string
umur = input('Masukkan umur: ')
print('Nama anda adalah ' + nama)
print('Umur ' + nama + ' ' + 'adalah ' + umur)
print(type(nama))
print(type(umur))

#Casting
bil1 = input("Masukkab bilangan pertama: ")
bil2 = input("Masukkan Bilangan Kedua: ")
Jumlah = int(bil1) + int(bil2)

print(Jumlah)
print(type(Jumlah))