#================
#INTRODUCTION
#================
#1. Library Request
import requests

response = requests.get("https://api.github.com")
print(response.status_code)
print(response.text)


#2. Library Math 
import math

print(math.sqrt(99))
print(math.pi)


#3. Library Random
import random

angka = random.randint(3, 67)
print("angka acak:", angka)


#4. Library Datetime
from datetime import datetime

sekarang = datetime.now()
print("Waktu sekarang:", sekarang)


#5. Studi Kasus Sederhana
import random

nilai = random.randint(20, 70)
print("Nilai", nilai)

if nilai >= 75:
    print("Lulus")
else:
    print("Tidak lulus")



#=======================
#CONDITIONAL STATEMENT
#=======================
#1. Syntax of the if statement
stok = 5
if (stok > 0):
    print("barang tersedia")


#2. If – else statement
saldo = 50000
if (saldo >= 100000):
    print("saldo cukup untuk belanja")
else:
    print("saldo tidak cukup")


#3. Syntax of the if-elif-else statement
nilai = int(input("masukkan nilai: "))
if (nilai >= 80):
    print("anda mendapat A")
else:
    print("anda belum mendapat A")


#4. Menggunakan Input dari Pengguna 
suhu = int(input("masukkan suhu: "))

if suhu > 30:
    print("cuaca panas")
elif suhu < 20:
    print("cuaca dingin")
else:
    print("cuaca sejuk")


#5. Menggunakan if Bersarang (Nested If)
usia = 22
if (usia >= 17):
    print("boleh membuat SIM")

    if (usia < 50):
        print("kategori usia produktif")
    else:
        print("kategori usia senior")
else:
    print("belum cukup umur")


#6. Menggunakan Operator Logika dalam if
x = int(input("Masukkan nilai x: "))

if x < 0 and x % 2 == 0:
    print("x adalah bilangan negatif dan genap")
elif x < 0 and x % 2 != 0:
    print("x adalah bilangan negatif dan ganjil")
else:
    print("x bukan bilangan negatif")


#7. Menggunakan Ternary Operator (if dalam satu baris)
x = int(input("Masukkan nilai x: "))
hasil = "Genap" if x % 2 == 0 else "Ganjil"
print(f"x adalah bilangan {hasil}")


#8. VARIABEL YANG BISA DIGUNAKAN DALAM IF, ELIF
#8.1 Boolean (bool)
is_login = True

if is_login:
    print("Anda sudah login")


#8.2 Angka (int, float)
x = -5
if x > 0:
    print("Bilangan positif")
elif x < 0:
    print("Bilangan negatif")
else:
    print("Bilangan nol")


 #8.3 String (str) 
username = "budi"

if username:
    print("Username telah diisi")
else:
    print("Username kosong")


#8.4 List, Tuple, Set, Dictionary (list, tuple, set, dict)
buah = ["apel", "jeruk"]

if buah:
    print("List memiliki isi")
else:
    print("List kosong")


#8.5 NoneType (None)
data = None

if data is None:
    print("Data belum tersedia")
else:
    print("Data sudah ada")



#======================
#TRANSFER STATEMENT
#======================
#1. break Statement
for i in range(10):
    if i == 7:
        break
    print(i)


#2. continue Statement
for i in range(10):
    if i == 5:
        continue
    print(i)


#3. pass Statement
x = 10

if x > 5:
    pass
else:
    print("x kecil")


#4. 4. return Statement
def add(a, b):
    return a + b

hasil = add(3, 5)
print(hasil)




#=======================
#ITERATIVE STATEMENT
#=======================
#1. Kontrol dalam Perulangan
#1.1 Break
for i in range(10):
    if i == 7:
        break
    print(i)


#1.2 continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)


#1.3. else pada Loop
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Loop selesai")


#2. Nesteed Loop (Pola Segitiga Terbalik)
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()


#3. Aplikasi Iterasi dalam Algoritma
#3.1. Menghitung Jumlah Total
data = [5, 10, 15]
jumlah = 0

for x in data:
    jumlah += x

print("Jumlah:", jumlah)


#3. 2. Menghitung Faktorial
n = int(input("Masukkan angka: "))
faktorial = 1

for i in range(1, n+1):
    faktorial *= i

print("Faktorial:", faktorial)


#3.4 Validasi Input dengan while
angka = 0

while angka <= 10:
    angka = int(input("Masukkan angka lebih dari 10: "))

print("Angka diterima")