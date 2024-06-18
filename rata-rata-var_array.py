"""
TODO:
Sebuah variabel array diberikan dengan ketentuan berikut.
- Variabel array bernama "var_array" dengan nilai dari 0 hingga 100.
- Hitung nilai rata-rata dari elemen array tersebut.
- Simpan hasil perhitungan dalam variabel bernama "result".

Tips:
- Rumus menghitung rata-rata adalah jumlah seluruh elemen dibagi banyaknya elemen.
- Gunakan percabangan dan perulangan untuk mempermudah, 
  Anda tidak diperbolehkan memberikan nilai secara langsung.
"""
# Jangan ubah kode ini
var_array = [i for i in range(101)]

# TODO: Silakan buat kode Anda di bawah ini.
# Inisialisasi variabel untuk menyimpan jumlah total
total = 0

# Menggunakan perulangan untuk menghitung jumlah total elemen array
for number in var_array:
    total += number

# Menghitung rata-rata
result = total / len(var_array)

# Menampilkan hasil
print("Rata-rata dari elemen array adalah:", result)