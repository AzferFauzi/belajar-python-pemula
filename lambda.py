# BELAJAR LAMBDA DAN ANONYMUS PADA FUNCTION DI PYTHON
# Berguna unutk mempersingkat function

# tanpa lambda
def perhitungan(x ,y):
    return x + y
print(f"Output tanpa lambda = {perhitungan(2,1)}")

# menggunakan lambda 
perhitungan = lambda x, y : x + y 
print(f"Output menggunakan lambda = {perhitungan(2,1)}\n")

# Map 
# berfungsi untuk menghitung angka 

# logika
kumpulan_angka = [1,2,3,4,5,6,7,8,9,10,11,12]
hasil = []
for i in kumpulan_angka:
    # ingin membuat setiap angka di kumpulan_angka di kali dua
    hasil.append(i * 2)
print(f"Logika = {hasil}")

# jika menggunakan map
hasil = list(map(lambda x: x * 2, kumpulan_angka))
print(f"Menggunakan map lambda = {hasil}\n")

# Filter
# Seperti namanya berfungsi untuk mengfilter atau mengklompokan data

# logika 
hasil = []
for i in kumpulan_angka:
    # ingin membuat setiap angka di kumpulan_angka di hanya mengeluarkan angka genap
    if i % 2 == 0:
        hasil.append(i)
print(f"Logika = {hasil}")

# jika menggunakan filter 
hasil = list(filter(lambda x:x % 2 == 0, kumpulan_angka))
print(f"Menggunaakn filter lambda = {hasil}\n")

# Sorted
# Berfungsi untuk mengurutkan data, bisa dari besar ke kecil dan begitu sebaliknya

# Pada Integer
# logika
data = [1,3,5,2,5,6,7,9,10]
data.sort()
print(f"Logika = {data}")

data.reverse()
print(f"Logika = {data}")

# menggunakan sorted lambda
data_sorted = sorted(data)
print(f"Menggunakan sorted lambda = {data_sorted}")

data_sorted = sorted(data, reverse=True)
print(f"Menggunakan sorted lambda = {data_sorted}\n")

# Pada String 
# Logika
data = ["azfir","audrey","amara","ananda","ahmad"]
data.sort()
print(f"Logika = {data}")

data.reverse()
print(f"Logika = {data}")

# menggunakan sorted lambda
hasil = sorted(data)
print(f"Menggunakan sorted lambda = {hasil}")

hasil = sorted(data, reverse=True)
print(f"Menggunakan sorted lambda = {hasil}")

# berdasarkan jumlah huruf

jamal = list(sorted(data, key=lambda x: len(x)))
print(f"Menggunakan sorted lambda = {jamal}")

    



