
jumlah_deret = int(input("Masukkan jumlah deret: "))
for i in range(1,jumlah_deret+1):
    print(" "*(jumlah_deret-i),end="")
    print("*"*i)