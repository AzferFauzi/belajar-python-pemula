# CASTING TIPE DATA / MERUBAH TIPE DATA
# Mengubah tipe data, contoh dari integer ke string

data_int = 1
print(data_int)
print(type(data_int))
# di ubah ke string
data_str_int = str(data_int)
print(data_str_int)
print(type(data_str_int))
print("\n")

# contoh lain jika float ke integer , maka hasilnya akan di bulatkan
data_float = 1.9
print(data_float)
print(type(data_float))
# diubah ke integer
data_int_float = int(data_float)
print(data_int_float)
print(type(data_int_float))
print("\n")

# jika int ke boolean, maka hanya yang kepakai hanya angka >= 1 lebih dan 0, karena itu mempresentasikan nilai True dan False
data_int = 1000000000000000000000000000000000000000000000000000
print(data_int)
print(type(data_int))
# diubah ke bool
data_bool_int = bool(data_int)
print(data_bool_int)
print(type(data_bool_int))
print("\n")

# jika string di ubah ke string maka hasilnya akan False jika kita mengisi hanya dengan "", tetapi selain itu maka hasilnya akan True termasuk "False", " ", dan "0"
data_str = ""
print(data_str)
print(type(data_str))
# di ubahke bool
data_bool_str = bool(data_str)
print(data_bool_str)
print(type(data_bool_str))


















