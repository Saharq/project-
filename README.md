# project 
import os
import random
import string

data_bansos = dict()

while True:
    os.system("cls")  # Membersihkan layar setiap kali memasukkan data baru

    keyFinal = "".join(random.choice(string.ascii_uppercase) for _ in range(3))
    
    tanggal = input("Tanggal Penerimaan Bantuan\t: ")
    nama = input("Nama Penerima\t\t\t: ")
    jenis_bantuan = input("Jenis Bantuan (Uang/Sembako)\t: ")
    jumlah_bantuan = input("Jumlah Bantuan\t\t\t: ")

    data_bansos[keyFinal] = {
        'tanggal_penerimaan': tanggal,
        'nama_penerima': nama,
        'jenis_bantuan': jenis_bantuan,
        'jumlah_bantuan': jumlah_bantuan
    }

    opsi = input("Input data lagi (y/t) : ").lower()
    if opsi == 't':
        break
        
print("-" * 60)
print(f"Key\t Tanggal Penerimaan\t Nama Penerima\t\t Jenis Bantuan\t Jumlah Bantuan")
print("-" * 60)

for key, value in data_bansos.items():
    print(f"{key}\t {value['tanggal_penerimaan']}\t {value['nama_penerima']}\t {value['jenis_bantuan']}\t\t {value['jumlah_bantuan']}")
