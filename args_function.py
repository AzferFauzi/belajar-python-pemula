# BELAJAR *args PADA FUNCTION
# Berguna untuk memasukan banyak data pada function

# contoh tanpa *args
def fungsi(nama, kelas, jenis_kelamin):
    print(f"Nama = {nama}")
    print(f"Kelas = {kelas}")
    print(f"Jenis Kelamin = {jenis_kelamin}")

fungsi("Radit", 12, 'Laki laki')

# jika berbentuk list tanpa *args
def func(data_list):
    data_list = data_list.copy()
    nama = data_list[0]
    kelas = data_list[1]
    jenis_kelamin = data_list[2]

    print(f"Nama = {nama}")
    print(f"Kelas = {kelas}")
    print(f"Jenis Kelamin = {jenis_kelamin}")

func(['Zku',12,'Laki laki'])

# Sekarang menggunakan *args (sebenarnyab gak harus *args yang penting ada bintangnya)
def data(*args):
    barang1 = args[0]
    barang2 = args[1]
    barang3 = args[2]
    barang4 = args[3]

    list_args = [barang1,barang2,barang3,barang4]
    print('Barang yang di beli :')
    for i in list_args:
        print(f'- {i}')

data("Piring",'Pisau',"Jajan",'Garpu')
data('Alamak','Gunting','Sendok','Pencil')

    
