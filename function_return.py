# FUNCTION RETURN

# membedakan function pake return dengan tidak

# menggunakan return
def orang(nama):
    return nama

print(orang("al"))
id = orang("al")
print(f"Nama saya : {id}\n")

# tidak menggunakan return
def hewan(nama_hewan):
    print(nama_hewan)

hewan("kelinci")
i = hewan("kelinci")
print(f"Nama Hewan = {i}\n")

# 
def angka(angka1,angka2):
    return angka1 + angka2

print(f"hasil = {angka(1,2)}\n")

# 
def hitung(angka_1,angka_2):
    tambah = angka_1 + angka_2    
    kurang = angka_1 - angka_2    
    kali = angka_1 * angka_2    
    bagi = angka_1 / angka_2    

    return tambah,kurang,kali,bagi

t,ku,ka,b = hitung(3,3)

print(f'Hasil tambah = {t}')
print(f'Hasil kurang = {ku}')
print(f'Hasil kali = {ka}')
print(f'Hasil bagi = {b}')

















