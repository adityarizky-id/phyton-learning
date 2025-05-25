# Program Menghitung Gaji Karyawan - Tugas 2

# Input golongan dan jam lembur
golongan = input("Masukkan Golongan Karyawan (A/B/C): ").upper()
jam_lembur = int(input("Masukkan Jumlah Jam Lembur: "))

# Menentukan gaji pokok berdasarkan golongan
if golongan == 'A':
    gaji_pokok = 5000000
elif golongan == 'B':
    gaji_pokok = 6500000
elif golongan == 'C':
    gaji_pokok = 9500000
else:
    print("Golongan tidak valid!")
    gaji_pokok = 0

# Menentukan besaran persentase lembur
if jam_lembur == 1:
    persen_lembur = 0.30
elif jam_lembur == 2:
    persen_lembur = 0.32
elif jam_lembur == 3:
    persen_lembur = 0.34
elif jam_lembur == 4:
    persen_lembur = 0.36
elif jam_lembur >= 5:
    persen_lembur = 0.38
else:
    persen_lembur = 0.0

# Hitung gaji lembur dan total penghasilan
gaji_lembur = persen_lembur * gaji_pokok
total_penghasilan = gaji_pokok + gaji_lembur

# Tampilkan hasil
print("=========================================")
print(f"Golongan Karyawan        : {golongan}")
print(f"Gaji Pokok               : Rp {gaji_pokok:,.0f}")
print(f"Jam Lembur               : {jam_lembur} Jam")
print(f"Gaji Lembur              : Rp {gaji_lembur:,.0f}")
print(f"Total Penghasilan        : Rp {total_penghasilan:,.0f}")
print("=========================================")
