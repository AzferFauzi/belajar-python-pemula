# BELAJAR PASS, CONTINUE, DAN BREAK

# PASS
# Berfungsi untuk menjadi dummy 
# contoh
data = 1
while data < 6:
    print(f"Anak Ke-{data}")
    data += 1

    if data == 3:
        pass #untuk mempresentasikan bahwa data ini telah di persiapkan tapi masih kosng jadinya di kasih "pass" agar tetap bisa berjalan dengan normal

print("Itulah Keluarga Kami \n")
        
# CONTINUE
# Berfungsi untuk menjadi seperti tombol "skip"
# contoh
buah = 1
while buah < 5:
    print(f"Buah ke-{buah}")
    buah += 1

    if buah == 2:
        buah += 1
        continue
print("\n")

# BREAK
# Berfungsi untuk memberhentikan sebuah program
# contoh
angka = 1
inputuser = int(input("Kamu ingin menghitung sampai angka berapa = "))
while True:
    print(f"Angka ke-{angka}")
    angka += 1

    if angka == inputuser:
        print(f"Angka ke-{angka}")
        print("Selesai!!")
        break

    
   
