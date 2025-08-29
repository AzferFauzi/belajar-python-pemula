# MANIPULASI LIST
# Belajar memanipulasi string di python

# DATA
data = ["Bambang","Ayu","Azfer"]

# mengindex sebuah list
data_index_pertama = data[0]
print(f"Data Index pertama adalah = {data_index_pertama}")
data_index_terakhir = data[-1]
print(f"Data Index terakhir adalah = {data_index_terakhir}")
index_azfer = data.index("Azfer")
print(f"Azfer terdapat di index = {index_azfer}\n")

# mengetahui list memiliki berapa data
jumlah_data_list = len(data)
print(f"Jumlah data di dalam list berjumlah = {jumlah_data_list}\n")

# casting data di list
print(f"Data sebelum di ubah = \n{data}")

# jika ingin menambahkan data secara kompleks menggunakan .insert(index, "data yang ingin di tambah")
data.insert(3,"Alisha")
print(f"Data setelah di tambahkan menggunakan insert = \n{data}")

# jika ingin menambahkan data langsung di posisi indes paling belakang menggunakan .append("data yang ingin di tambah")
data.append("Atha")
print(f"Data setelah di tambah menggunakan append = \n{data}")

# jika ingin mengubah data dengan cara data[index data yang ingin di ubah] = "data yang ingin di ubah" 
data[2] = "Fauzi"
print(f"Data setelah mengubah nama 'Azfer' = \n{data}")

# jika ingin menggabungkan list dengan list .extend(list yang ingin di tambah)
data2 = ["Akung", "Uti"]
data.extend(data2)
print(f"Data setelah list degabungkan dengan list menggunakan extend =\n {data}")

# jika ingin menghapus data secara kompleks .remove("nama data yang ingin di hapus")
data.remove("Akung")
print(f"Data stelah di hapus menggunakan remove = \n{data}")

# jika ingin menghapus data tapi hanya yang di belakangnya saja menggunakan .pop()
data_yang_dihapus = data.pop()
print(f"Data setelah di hapus menggunakan pop = \n{data}")

# pengen tau data yang di hapus (hanya berlaku ketika menggunakan .pop)
print(f"Data yang di apus adalah = {data_yang_dihapus}")
