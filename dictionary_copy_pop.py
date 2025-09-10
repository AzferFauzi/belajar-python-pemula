# DICTIONARY COPY DAN POP

data_dict = {
    1:'Ahmad',
    2:'Amara',
    3:'Ananda',
    4:'Audey',
    5:'Asfir'
}

# jika ingin mengcopy dictionary tinggal menggunakan .copy()
absen = data_dict.copy()

print(f'data_dict = {data_dict}\n')
print(f'absen = {absen}\n')

# menggunakan .pop() dan .popitem()

# .pop() 
dict_3 = data_dict.pop(3) # harus di kasih key karena tidak bisa seperti di list
print(f'Data Ananda = {dict_3}')
print(f'data_dict = {data_dict}\n')

# .popitem()
data_terakhir = absen.popitem() 
print(f'Data Terakhir = {data_terakhir}')
print(f'data_dict = {absen}\n')


