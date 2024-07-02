import datetime
import os
import string
import random
# template dictionaru mahasiswa
mahasiswa_template = {
    'nama':'nama',
    'nim':'00000000',
    'sks_lulus':0,
    'lahir':datetime.datetime(1111,1,11)
    
}

data_mahasiswa = {}
os.system("clear")
print(f"{'SELAMAT DATANG':^20}")
print(f"{'DATA MAHASISWA':^20}")
print("="*20)


#membuat dictionaru baru kosong berdasarkan template keys
while True:
    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    mahasiswa['nama'] = input("Nama: ")
    mahasiswa['nim'] = input("NIM: ")
    mahasiswa['sks_lulus'] = int(input("SKS Lulus: "))
    mahasiswa['lahir'] = datetime.datetime.strptime(input("Tanggal Lahir (YYYY-MM-DD): "),"%Y-%m-%d")
    
    KEY = "".join(random.choice(string.ascii_uppercase) for _ in range(6))
    data_mahasiswa.update({KEY:mahasiswa})
    
    ulangi = input("Ulangi input data mahasiswa (y/n)? ")
    if ulangi.lower() != 'y':
        break        

print(f"{'KEY':<6} {'NAMA':<17} {'NIM':^10} {'SKS':^10} {'LAHIR':^10}")
print("-"*55)
for mhs in data_mahasiswa:
        KEY = mhs
        NAMA = data_mahasiswa[mhs]['nama']
        NIM = data_mahasiswa[mhs]['nim']
        SKS = data_mahasiswa[mhs]['sks_lulus']
        LAHIR = data_mahasiswa[mhs]['lahir'].strftime("%x")
        
        print(f"{KEY:<6} {NAMA:<17} {NIM:^10} {SKS:^10} {LAHIR:^10}")