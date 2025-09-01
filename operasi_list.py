# OPERASI LIST

data1 = [1,2,4,3,5,5,6,1,8,9,0,2]
print(data1)
data2 = ["Amara", "Ahmad", "Azfer", "Audrey", "Ananda"]
print(data2)

# Ingin mengetahui jumlah data dalam list
jumlah_angak_1 = data1.count(1)
print(f"\nJumlah angka 1 adalah = {jumlah_angak_1}")
jumlah_angak_6 = data1.count(6)
print(f"Jumlah angka 6 adalah = {jumlah_angak_6}\n")

# Mengambil index dari suatu data 
index_amara = data2.index("Amara")
print(f"Index Amara adalah = {index_amara}")
index_azfer = data2.index("Azfer")
print(f"Index Azfer adalah = {index_azfer}\n")

# Mengurutkan data dari kecil ke besar
print(f"Data normal = \n{data1}")
data1.sort()
print(f"Urutkan data dari kecil ke besar \n{data1}\n")

print(f"Data Normal = \n{data2}")
data2.sort()
print(f"Urutkan data dari kecil ke besar \n{data2}\n")

#  Mengurutkan data dari besar ke kecil
data1 = [1,2,4,3,5,5,6,1,8,9,0,2]
data2 = ["Amara", "Ahmad", "Azfer", "Audrey", "Ananda"]

data1.sort()
data1.reverse()
print(f"Data dari besar ke kecil =\n{data1}")

data2.sort()
data2.reverse()
print(f"Data dari besar ke kecil =\n{data2}")
