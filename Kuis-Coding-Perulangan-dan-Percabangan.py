"""
TODO:
Buatlah sebuah variabel bertipe list bernama "evenNumber" dengan ketentuan:
- variabel tersebut menampung bilangan genap dari 0 hingga 500 (ingat 0 dan 500 termasuk).

Tips:
Anda bisa menggunakan loop dan if atau list comprehension untuk memudahkan.
"""

# TODO: Silakan buat kode Anda di bawah ini.
evenNumber = []  # Membuat list kosong untuk menampung bilangan genap

for num in range(501):  # Iterasi dari 0 hingga 500 (inklusif)
    if num % 2 == 0:  # Memeriksa apakah bilangan genap
        evenNumber.append(num)  # Menambahkan bilangan genap ke list

print(evenNumber)