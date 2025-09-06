# DEEPCOPY NESTED LIST
# Belajar Mengdeepcopy Nested List

data_0 = ["A","B"]
data_1 = ["C","D"]

list_biasa = ['a','b','c','d']
print(f'List biasa = {list_biasa}')

# list dalam list
nested_list = [data_0,data_1,"e"]
print(f'List Bersarang = {nested_list}')

# mengambil data di nested list

x = nested_list[0][0], nested_list[1][0]
print(f'Mengambil index ke-0 pada setiap list = {x}\n')

# melakukan deepcopy pada nestedlist
nested_list_copy = nested_list.copy()

# jika melakukan copy nested list biasa menggunakan .copy()
print(f'List Normal = {nested_list}')
print(f'List Copy = {nested_list_copy}\n')

# melakukan perubahan pada nested list biasa akan memengaruhi hasil pada nested list copy
nested_list[1][1] = ''
print(f'List Normal = {nested_list}')
print(f'List Copy = {nested_list_copy}\n')

# kecuali perubahan di luar list
nested_list[2] = "E"
print(f'List Normal = {nested_list}')
print(f'List Copy = {nested_list_copy}\n')

# maka dari itu cara bisa melakukan deepcopy itu dengan menggunakan libary deepcopy
from copy import deepcopy

nested_list_deepcopy = deepcopy(nested_list)

nested_list[1][1] = "D"
print(f'List Normal = {nested_list}')
print(f'List Copy = {nested_list_copy}')
print(f'List Deepcopy = {nested_list_deepcopy}\n')





