# LOOPING MENGGUNAKAN FOR IN
# looping ini akan terjadi ketika hanya seberapa banyak yang di miliki oleh kondisi untuk memmunculkan aksi

# contoh
data = "Azfer Jausyaq Fauzi"

for huruf in data:
    print(huruf)

# contoh lain
 
ListHewan = ["Monyet", "Singa", "Gajah", "Jerapah"]
print("Hewan yang di kebun binatang ada : \n")
for hewan in ListHewan:
    print(hewan)
print("\n")

# membuat segitiga dengan for in
angka = 1
space = 5
for i in range(5):
    print("*" * angka)
    angka += 1

    
