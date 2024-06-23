jumlah_deret = int(input("Masukkan jumlah deret: "))
spasi = int(jumlah_deret/2)
for i in range(1,jumlah_deret+1):
    if i % 2 != 0:
        print(" "*(spasi),end="")
        print("*"*i)
        spasi -= 1

for i in range(jumlah_deret-1,0,-1):
    if i % 2 != 0:
        spasi += 1
        print(" "*(spasi),end="")
        print("*"*i)