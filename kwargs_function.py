# BELAJAR *kwargs PADA FUNCTION
# Berguna untuk memasukan banyak data pada function

# contoh tanpa **kwargs
def func(nama,umur):
    print(f'Nama : {nama}, Umur : {umur}')

func(nama = 'sico', umur = 69)

# jika mengguanakn **kwargs
# jika *args akan menghasilkan data list maka **kwargs
def fung(**kwargs):
    nama = kwargs["nama"]
    umur = kwargs["umur"]
    
    print(f'Nama : {nama}, Umur : {umur}')

fung(nama='Radit',umur=12)
    
# jika operasi menggunakan *args dan **kwargs
def kalkulator(*angka,**operasi):
    if operasi["operasi"] == "tambah":
        x = 0
        for a in angka:
            x += a
    elif operasi["operasi"] == "kali":
        x = 1
        for a in angka:
            x *= a
    else:
        print('Tolong isi operasi yang benar')
    return x
hasil = kalkulator(1,2,3, operasi="tambah")
print(f'Hasil tambah = {hasil}')
hasil = kalkulator(1,2,3, operasi="kali")
print(f'Hasil kali = {hasil}')
