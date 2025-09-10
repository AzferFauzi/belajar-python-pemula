# DICTIONARY LOOP

data_dict = {
    1:'Ahmad',
    2:'Amara',
    3:'Ananda',
    4:'Audey',
    5:'Azfir'
}

# jika menggunakan loop biasa maka akan hanya mengeluarkan key nya saja (tapi tidak secara spesifik)
for data in data_dict:
    print(data)
print("\n")

# jika ingin melakukan loop dan mengeluarkan key dengan spesifik dengan cara data_dict.keys()
for key in data_dict.keys():
    print(f"Key = {key}")
print("\n")

# jika hanya ingin hanya ingin mengambil valeu nya dengan spesifik menggunakan data_dict.valeus()
for value in data_dict.values():
    print(f"Valeu = {value}")
print("\n")

# jika ingin mengambil semua nya bisa menggunakan data_dict.items()
for item in data_dict.items():
    print(f"Data Item = {item}") #dan ini akan menghasilkan tipe data tiple
print("\n")
# bisa juga mengambil kedua nya secara terpisah
for key,value in data_dict.items():
    print(f"Valeu = {value} dan Key = {key}")
