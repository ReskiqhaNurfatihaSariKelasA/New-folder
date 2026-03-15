import requests

response = requests.get("https://api.github.com")
print(response.status_code)
print(response.text)

import math

print(math.sqrt(99))
print(math.pi)

import random

angka = random.randint(3, 67)
print("angka acak:", angka)

from datetime import datetime

sekarang = datetime.now()
print("Waktu sekarang:", sekarang)

import random

nilai = random.randint(20, 70)
print("Nilai", nilai)

if nilai >= 75:
    print("Lulus")
else:
    print("Tidak lulus")
