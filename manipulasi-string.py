# BELAJAR MEMANIPULASIKAN DAN OPERASI STRING 

# PART 1

# mengkelompokan string
nm_dpn = "James"
nm_blkng = "Wazosky"

nm_lngkp = nm_dpn + " " + nm_blkng
print(nm_lngkp)

# menghitung jumlah huruf dalam string
jmlh = len(nm_lngkp)
print(f"Jumlah huruf dalam {nm_lngkp} adalah = {jmlh}")

# memeriksa adanya data yang di cari dalam sebuah data
Jhon = "Jhon" in nm_lngkp
print(f"Apakah ada kata Jhon dalam {nm_lngkp} = {Jhon}")

Jhon = "Jhon" not in nm_lngkp
print(f"Apakah tidak ada kata Jhon dalam {nm_lngkp} = {Jhon}")

James = "James" in nm_lngkp
print(f"Apakah ada kata James dalam {nm_lngkp} = {James}")

# mengindex/mencari urutan dari sebuah string
# mengambil huruf Pertama
print(f"Huruf pertama adalah = {nm_lngkp[0]}")
# mengambil huruf Terakhir
print(f"Huruf terakhir adalah = {nm_lngkp[-1]}")
# mengambil huruf James
print(f"Mengambil huruf James adalah = {nm_lngkp[0:5]}")
# mengambil huruf Terakhir
print(f"Mengambil huruf dengan kelipatan 3 adalah = {nm_lngkp[0:13:3]}")

# menghitung jumlah huruf tertentu dalam sebuah data
jumlah = nm_lngkp.count("a")
print(f"Huruf a berjumlah =  {jumlah}")
