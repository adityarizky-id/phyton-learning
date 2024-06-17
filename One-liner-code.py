x = 1
y = 2

temp = x
x = y
y = temp

print("Setelah pertukaran: ")
print("x = ", x)
print("y =",  y)

"""
Output:
Setelah pertukaran: 
x = 2
y = 1

Mari bedah kode tersebut.

Anda menginisialisasi variabel x dengan nilai 1 dan variabel y dengan nilai 2. 
Anda menginisialisasi variabel temp dengan nilainya adalah variabel x. Hal ini menyebabkan variabel temp memiliki nilai 1.
Anda menginisialisasi variabel x dengan nilai baru, yakni variabel y. Hal ini menyebabkan nilai dari variabel x menjadi 2.
Anda menginisialisasi variabel y dengan nilai baru, yakni variabel temp. Hal ini menyebabkan nilai dari variabel y menjadi 1.
Proses penukaran variabel telah selesai. Selanjutnya, Anda menampilkan nilai pada variabel tersebut dengan sintaks "print()".
Mungkin Anda bertanya, mengapa variabel x dan y bisa berubah? Ingat konsep aksi sekuensial, program akan menjalankan kode tersebut baris per baris. Jadi, nilai dari variabel x dan y setelah inisialisasi pertama akan berubah karena pada sintaks berikutnya Anda menetapkan nilai baru pada variabel x dan y. Anda menggunakan variabel bantuan, yakni variabel "temp" untuk menyimpan nilai awal dari variabel x. 
"""