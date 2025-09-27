# FUNCTION DEFULT ARGUMENT

# def variable(argument = nilai defult):
#     print(argument)

# 1
def siswa(nama = "Fauzi"):
    print(f'Nama anda = {nama}')

siswa("Akmal")
siswa() # akan mengeluarkan defult jika tidak di isi

# 2 
def jumlah(angka1,angka2 = 2):
    hasil = angka1 + angka2
    return hasil

print(jumlah(3,7))
print(jumlah(0))

# 3
def chat(pengirim = "Someone", pesan = "Halo bang"):
    print(f"Dari {pengirim}, pesan {pesan}")

chat(pesan = "Aku cinta kamu ")
chat("ku","Alamat")

# 4
def jumlah_input(angka_1 = 0, angka_2 = 0, angka_3 = 0, angka_4 = 0):
    hasil = angka_1 + angka_2 + angka_3 + angka_4
    return hasil

print(jumlah_input())
print(jumlah_input(angka_1=1,angka_2=1))
print(jumlah_input(angka_1=5,angka_2=10,angka_3=7,angka_4=3))
    
