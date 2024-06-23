import random as rd

lst_angka = [rd.randint(1,10) for _ in range(11)]

#count element tertentu
print(lst_angka)

print(lst_angka.count(7))

#remove element tertentu
lst_angka.remove(7)
print(lst_angka)