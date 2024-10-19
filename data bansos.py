import os
import random
import string

# Dictionary untuk menyimpan data bansos
data_bansos = dict()

while True:
    os.system("cls")  # Membersihkan layar setiap kali memasukkan data baru

    # Membuat key acak yang unik (3 huruf kapital)
    keyFinal = "".join(random.choice(string.ascii_uppercase) for _ in range(3))
    
    # Input data penerima bansos
    tanggal = input("Tanggal Penerimaan Bantuan\t: ")
    nama = input("Nama Penerima\t\t\t: ")
    jenis_bantuan = input("Jenis Bantuan (Uang/Sembako)\t: ")
    jumlah_bantuan = input("Jumlah Bantuan\t\t\t: ")

    # Memasukkan data ke dalam dictionary
    data_bansos[keyFinal] = {
        'tanggal_penerimaan': tanggal,
        'nama_penerima': nama,
        'jenis_bantuan': jenis_bantuan,
        'jumlah_bantuan': jumlah_bantuan
    }

    # Meminta input apakah ingin menambahkan data lagi atau tidak
    opsi = input("Input data lagi (y/t) : ").lower()
    if opsi == 't':
        break

# Menampilkan semua data yang sudah diinput
print("-" * 60)
print(f"Key\t Tanggal Penerimaan\t Nama Penerima\t\t Jenis Bantuan\t Jumlah Bantuan")
print("-" * 60)

for key, value in data_bansos.items():
    print(f"{key}\t {value['tanggal_penerimaan']}\t {value['nama_penerima']}\t {value['jenis_bantuan']}\t\t {value['jumlah_bantuan']}")
