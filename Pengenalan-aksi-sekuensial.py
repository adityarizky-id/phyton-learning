print("Selamat datang dalam program Python!\n")
print("Silakan masukkan data diri Anda.")
nama = input("Masukkan nama Anda: ")
tahun_lahir = input("Masukkan tahun lahir Anda: ")
umur = 2023 - int(tahun_lahir)
 
print(f"Selamat datang {nama} dalam program Python, per 2023 umur Anda adalah {umur} tahun.\n")
print("Terima kasih telah menggunakan program Python!")
 
"""
Output:
Selamat datang dalam program Python!
 
Silakan masukkan data diri Anda:
Masukkan nama Anda: Evans
Masukkan tahun lahir Anda: 2005
Selamat datang Evans dalam program Python, per 2023 umur Anda adalah 18 tahun.
 
Terima kasih telah menggunakan program Python!
"""

for i in range(10):
    print(i)

"""
Output:
IndentationError: expected an indented block
"""

#Program phyton case sensitive, 
teks = "Dicoding"
Teks = "Indonesia"

print(teks)
print(Teks)
print(TEks)

"""
Output:
Dicoding
Indonesia
NameError: name 'TEks' is not defined

Hal ini disebabkan variabel "teks", "Teks", dan "TEks" dianggap sebagai variabel yang berbeda oleh Python.
"""