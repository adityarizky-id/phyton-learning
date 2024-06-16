#Operasi penjumlahan phyton
"""
addition adalah variabel yang bernilai ekspresi 2+2,
result adalah hasil pengurangan dari variabel addition dikurangi 1
"""

addition = 2+2
result = addition - 1
print(result)


"""
Output: 3
"""

# Variabel ini menyimpan nama 'Perseus Evans'
name = input('Masukan nama Anda: ')
 
"""
Output:
Masukan nama Anda: Perseus Evansasd
Perseus Evans
"""

# Kuis - Variabel
"""
TODO:
- Buatlah sebuah variabel bernama greeting.
- Assign teks "Saya mulai belajar Python!" pada variabel tersebut. 
"""

# Buat variabel bernama greeting
greeting = "Saya mulai belajar Python!"

# Cetak nilai variabel greeting dengan spasi setelah variabel name
print(name + " " + greeting)

age = 17
salary = 5000000.0

print(type(age))
print(type(salary))

"""
Output:
<class ‘int’>
<class ‘float’>
"""

# Mengubah x menjadi 'Dicoding' dengan metode slicing
x = 'Dicoding'
print(x[2:])

"""
Output:
coding
"""

name = "Perseus Evans"
print(f"Hello, nama saya {name}")
 
"""
Output: 
Hello, nama saya Perseus Evans
"""

#Kuis Tipe Data
# TODO: Isi variabel sesuai dengan ketentuan
firstName = "Bard"  # Isi dengan nama depan Anda
lastName = "AI"  # Isi dengan nama belakang Anda
age = 3  # Isi dengan umur Anda (integer)
isMarried = False  # Isi dengan status pernikahan Anda (True/False)

# Cetak variabel
print(f"Nama depan: {firstName}")
print(f"Nama belakang: {lastName}")
print(f"Umur: {age}")
print(f"Status menikah: {isMarried}")

# TODO: Buatlah variabel dictionary Anda di bawah ini.
data_diri = {
    "firstName": "Bard",  # Isi dengan nama depan Anda
    "lastName": "AI",  # Isi dengan nama belakang Anda
    "age": 3,  # Isi dengan umur Anda (integer)
    "isMarried": False  # Isi dengan status pernikahan Anda (True/False)
}

# Akses nilai dictionary
print(f"Nama lengkap: {data_diri['firstName']} {data_diri['lastName']}")
print(f"Umur: {data_diri['age']}")
print(f"Status menikah: {data_diri['isMarried']}")

print("Dicoding Indonesia            ")

#--------------------------------------------------------
#Kuis Operasi List
#--------------------------------------------------------

"""
TODO:
Diberikan sebuah variabel berisi nilai list dengan nama "var_list". 
Berdasarkan list tersebut, cari hal-hal berikut ini:
- Panjang list tersebut dan simpan dengan nama variabel "panjang".
- Nilai maksimal list tersebut dan simpan dengan nama variabel "maksimal".
- Nilai minimal list tersebut dan simpan dengan nama variabel "minimal".
- Berapa banyak angka 605132 dalam list tersebut dan simpan dalam variabel bernama "banyak"

Tips:
- Anda bisa menggunakan berbagai kode yang ada di materi operasi, 
  tidak diperbolehkan memasukan nilai secara langsung.
"""

# Jangan ubah kode ini
var_list = [792564, 465231, 203748, 981037, 857219, 314092, 608345, 123907, 736890, 985026, 
179430, 450218, 680934, 543187, 978260, 283045, 617902, 405826, 820913, 731095, 
592403, 109237, 874956, 605132, 214978, 674519, 391047, 825160, 509317, 768490, 
950283, 307491, 487610, 532198, 605132, 160984, 609873, 245016, 879043, 734126, 
351809, 670594, 920873, 605132, 596410, 135890, 804512, 683420, 290753, 931560, 
175430, 950672, 378490, 284105, 746098, 503624, 605132, 167432, 974810, 519463, 
407835, 740326, 281709, 630921, 953284, 605132, 429731, 183607, 369012, 541380, 
605132, 217605, 496803, 827309, 153607, 605132, 720459, 381904, 594031, 810235, 
673925, 492157, 835096, 260481, 956024, 540329, 806295, 320158, 751903, 980465, 
235780, 857943, 605132, 125094, 620493, 913250
]

# Inisialisasi variabel
panjang = len(var_list)  # Menghitung panjang list
maksimal = max(var_list)  # Mencari nilai maksimal
minimal = min(var_list)  # Mencari nilai minimal
banyak = var_list.count(605132)  # Menghitung jumlah angka 605132

# Menampilkan hasil
print(f"Panjang list: {panjang}")
print(f"Nilai maksimal: {maksimal}")
print(f"Nilai minimal: {minimal}")
print(f"Jumlah angka 605132: {banyak}")

#--------------------------------------------------------
#Ekspresi Phyton
#--------------------------------------------------------

angka = [2, 4, 6, 8]
huruf = ['P', 'Y', 'T', 'H', 'O', 'N']
gabung = angka + huruf

print(gabung)
"""
Output:
['P', 'Y', 'T', 'H', 'O', 'N', 'P', 'Y', 'T', 'H', 'O', 'N']
"""