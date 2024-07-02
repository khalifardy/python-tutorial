data_dict = {
    "sirius":"bintang terang",
    "betelguese":"bintang merah",
    "rigel":"bintang biru"
}

#mengecek key exist

key = "matahari"
cekkey = key in data_dict
print(cekkey)

#mengakses value dari  get
value = data_dict.get("sirius")
print(value)

#datanone
value = data_dict.get("matahari")
print(value)

#data none dengan peringatan custom
value = data_dict.get("matahari","maaf, data tidak ditemukan")
print(value)


#uodate data
data_dict.update({"matahari":"bintang terbesar"})
data_dict.update({"sirius":"bintang terang dan panas"})
print(data_dict)


#delete data
del data_dict["matahari"]
print(data_dict)


#looping key
for key in data_dict.keys():
    print(key)

#looping value
for value in data_dict.values():
    print(value)

#looping item
for key, value in data_dict.items():
    print(f"{key} : {value}")

item = data_dict.items()
print(item)


#copy dictionary
data_dict2 = data_dict.copy()
print(data_dict2)

#pop dictionary
data_pop = data_dict2.pop('sirius')
print(data_pop)
print(data_dict2)

#popitem dictionary
data_popitem = data_dict2.popitem()
print(data_popitem)
print(data_dict2)


