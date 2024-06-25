#program data buku

data_buku = []

while True:
    data = []
    judul = input("Masukkan judul buku: ")
    penulis = input("Masukkan penulis buku: ")
    penerbit = input("Masukkan penerbit buku: ")
    
    data.append(judul)
    data.append(penulis)
    data.append(penerbit)
    data_buku.append(data)
    lanjut = input("Apakah anda ingin memasukkan data buku lagi? (y/t): ")
    if lanjut.lower() == 't':
        break



    
print("List Buku saat ini : ")
for i in enumerate(data_buku):
    print(f"Data Buku ke-{i[0]+1}")
    print(f"Judul Buku: {i[1][0]}")
    print(f"Penulis Buku: {i[1][1]}")
    print(f"Penerbit Buku: {i[1][2]}")
    print("\n")
