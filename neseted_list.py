# LIST NESTED
# Belajar List Bersarang

data_0 = ["A","B"]
data_1 = ["C","D"]

list_biasa = ['a','b','c','d']
print(f'List biasa = {list_biasa}')

# list dalam list
nested_list = [data_0,data_1]
print(f'List Bersarang = {nested_list}')

id_1 = ["Jamal",15,"Laki - Laki"]
id_2 = ["Fatimah",13,"Perempuan"]
id_3 = ["Bagas",17,"Laki - Laki"]

grub_id = [id_1,id_2,id_3]

print('\nData Peserta')
for id in grub_id:
    print(f'Nama Lengkap \t: {id[0]}')
    print(f'Umur \t\t: {id[1]}')
    print(f'Jenis Kelamin \t: {id[2]}\n')
