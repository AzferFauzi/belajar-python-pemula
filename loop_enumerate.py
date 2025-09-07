# LIST LOOP ENUMRATE
# Belajar meloop list dan mengenali jenis jenis nya

# List loop menggunakan for in 2
print('==== for in loop 1 ====')
id_grub = [1,2,4,1,10,6]

many = len(id_grub)


for i in range(many):
    print(f'Data = {id_grub[i]}')

print('\n')

# List loop menggunakan for in 1
print('==== for in loop 2 ====')
id_grub = [1,4,5,2,3,6]

for i in id_grub:
    print(f'Data = {i}')

print('\n')

# List loop menggunakan while 1
print('==== while loop 1 ====')
id_grub = [1,4,3,2,6,7]

jumlah = len(id_grub)
i = 0

while i < jumlah:
    x = id_grub[i]
    print(f'Data = {x}')
    i += 1

print('\n')

# List loop menggunakan while 2
print('==== while loop 2 ====')
id_grub = [2,5,4,1,7,0]

jumlah = len(id_grub)
i = 0

while i < jumlah:
    print(f'Data = {id_grub[i]}')
    i += 1

print('\n')

# List loop chomperhassion
print('==== list chomperhasion ====')
id_grub = [1,2,6,4,9,10]

[print(f'Data = {i}') for i in id_grub]
print('\n')

# List loop enumerate 
print('==== list enumerate ====')

id_grub = [6,5,4,3,2,1]

for i,index in enumerate(id_grub):
    print(f'Data = {i}, index = {index}')


