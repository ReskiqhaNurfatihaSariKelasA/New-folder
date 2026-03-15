#Library Request
import requests

response = requests.get("https://api.github.com")
print(response.status_code)
print(response.text)


#Library Math 
import math

print(math.sqrt(99))
print(math.pi)


#Library Random
import random

angka = random.randint(3, 67)
print("angka acak:", angka)


#Library Datetime
from datetime import datetime

sekarang = datetime.now()
print("Waktu sekarang:", sekarang)


#Studi Kasus Sederhana
import random

nilai = random.randint(20, 70)
print("Nilai", nilai)

if nilai >= 75:
    print("Lulus")
else:
    print("Tidak lulus")
