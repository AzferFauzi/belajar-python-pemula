# BELAJAR MEMANIPULASIKAN DAN OPERASI STRING 

# PART 2

# Mengcase string / merubah case sebuah string

# Merubah semuanya menjadi huruf besar .upper()
data = "Hello World"
print(f"Data normal = {data}")
data = data.upper()
print(f"Data upper = {data}\n")
# Merubah semuanya menjadi huruf kecil .upper()
print(f"Data normal = {data}")
data = data.lower()
print(f"Data lower = {data}\n")
# Merubah semua huruf depan menjadi besar .title()
print(f"Data normal = {data}")
data = data.title()
print(f"Data title = {data}\n")
# Merubah hanya huruf depannya saja yang besar .capitalize()
print(f"Data normal = {data}")
data = data.capitalize()
print(f"Data capitalize = {data}\n")

# mengecek apakah stringnya sesuai dengan case nya

data = "Hello World"
hasil = data.islower()
print(f"Apakah stringnya lower = {str(hasil)}")
hasil = data.isupper()
print(f"Apakah stringnya upper = {str(hasil)}")
hasil = data.istitle()
print(f"Apakah stringnya upper = {str(hasil)}\n")

#  mengecek komponen string dengna .stratswith() dan .endswith()

data = "Akmal Pasha"
hasil = data.startswith("Akmal")
print(f"Apakah {data} diawali dengan Akmal = {hasil}")
hasil = data.endswith("Akmal")
print(f"Apakah {data} diawali dengan Akmal = {hasil}")






