#for Loop
var_list = [1,2,3,4,5,6,7,8,9,10]
for i in var_list:
    print(i)

"""
Output:
1
2
3
4
5
6
7
8
9
10
"""

for i in range(1,10,2):
    print(i)

"""
Output:
1
3
5
7
9
"""

#While Loop
counter = 1
while counter <= 5:
    print(counter)
    counter += 1    # Increment

"""
Output:
1
2
3
4
5
"""

#For Bersarang (Nested Loop)
for i in range(1, 3):
    for j in range(1, 3):
        print(i,j)

"""
Output:
1,1
1,2
2,1
2,2
"""

for i in range(2):  # Perulangan tingkat pertama
    print("Perulangan luar:", i)
    for j in range(10):  # Perulangan tingkat kedua
        print("Perulangan dalam:", j)
        if j == 1:
            break  # Menghentikan perulangan dalam jika j = 1


"""
Output:
Perulangan luar: 0
Perulangan dalam: 0
Perulangan dalam: 1
Perulangan luar: 1
Perulangan dalam: 0
Perulangan dalam: 1
"""

for huruf in 'Dico ding':
    if huruf == ' ':
        break
    print('Huruf saat ini: {}'.format(huruf))

"""
Pada contoh di atas, program akan berhenti jika bertemu huruf " " (spasi) yang berada pada teks "Dico ding". 

Output:
Huruf saat ini: D
Huruf saat ini: i
Huruf saat ini: c
Huruf saat ini: o
"""

#continue statement 
for huruf in 'Dico ding':
    if huruf == ' ':
        continue
    print('Huruf saat ini: {}'.format(huruf))

"""
Pada contoh di atas, kita membuat perulangan yang sama dengan contoh sebelumnya. Namun, alih-alih ada spasi maka program akan berhenti, program akan mengabaikan spasi tersebut dan melanjutkannya pada perulangan selanjutnya.

Dalam contoh di atas, program berusaha untuk menampilkan teks "Dico ding" dengan kondisi jika bertemu " " (spasi) akan dilewati dan melakukan perulangan selanjutnya. Alhasil output yang dihasilkan adalah "d", "i", "c", "o", "d", "i", "n", "g" tanpa adanya spasi.

Output:
Huruf saat ini: D
Huruf saat ini: i
Huruf saat ini: c
Huruf saat ini: o
Huruf saat ini: d   # Perhatikan bahwa harusnya sebelum ini ada spasi, namun dilewati.
Huruf saat ini: i
Huruf saat ini: n
Huruf saat ini: g
"""

#Else setelah For 
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 6:
        print("Angka ditemukan! Program berhenti!")
        break
else:
    print("Angka tidak ditemukan.")

"""
Output:
Angka tidak ditemukan.
"""

#Else setelah While
count = 0

while count < 3:
    print("Dicoding Indonesia")
    count += 1
else:
    print("Blok else dieksekusi karena kondisi pada while salah (3<3 == False).")


"""
Output:
Dicoding Indonesia
Dicoding Indonesia
Dicoding Indonesia
Blok else dieksekusi karena kondisi pada while salah (3<3 == False).
"""

n = 10
while n > 0:
    n = n - 1
    if n == 7:
        break
    print(n)
else:
    print("Loop selesai")

"""
Output:
9
8
"""

#pass statement
#Pass statement adalah pernyataan yang digunakan jika Anda menginginkan sebuah pernyataan atau blok pernyataan (statement), tetapi tidak ada tindakan atau program tidak melakukan apa pun.
x = 10

if x > 5:
    pass
else:
    print("Nilai x tidak memenuhi kondisi")

"""
Output:


"""

#list comprehension
angka = [1, 2, 3, 4]
pangkat = []
for n in angka:
  pangkat.append(n**2)
print(pangkat)

"""
Output:
[1, 4, 9, 16]

"""

angka = [1, 2, 3, 4]
pangkat = [n**2 for n in angka]
print(pangkat)

"""
Output:
[1, 4, 9, 16]
"""