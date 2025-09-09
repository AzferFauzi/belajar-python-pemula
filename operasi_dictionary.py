# OPERASI DICTIONARY
# Belajar operator yang ada di dectionary

data_dict = {
    'Pak':'Bambang',
    'Bu':'Ayu',
    'Mas':'Ozi',
}

# menghitung jumlah data yang ada pada data dict
jumlah_data = len(data_dict)
print(f'Jumlah data yang ada di data dict adalah = {jumlah_data}\n')


# mengecek apakah ada tidaknya sebuah data pada data dict
key = 'Kak'
cek = key in data_dict
print(f'Data "{key}" apakah ada di data dict = {cek}')
key = 'Pak'
cek = key in data_dict
print(f'Data "{key}" apakah ada di data dict = {cek}\n')


# membaca apakah ada data di dalam data dict
key = 'Kak'
print(f'Mencari data "{key}" apakah ada = {data_dict.get(key)}')
key = 'Bu'
print(f'Mencari data "{key}" apakah ada = {data_dict.get(key)}\n')


# mengupdate sebuah data di data dict (bisa di ganti dan bisa menambah data)
print(f'Data sebelum di update = {data_dict}')
# jika sudah ada data di dalam data dict, maka update akan hanya mengganti nama datanya
data_dict.update({'Mas':'Azfer'}) 
print(f'Data setelah di update = {data_dict}')
# jika belum ada data di dalama data dict, maka update akan menambahkan data tersebut
data_dict.update({'Kak':'Alisa'})
print(f'Data setelah di update = {data_dict}\n')


# menghapus data di data dict
del data_dict['Kak'] 
print(f'Data setelah di update = {data_dict}\n')
