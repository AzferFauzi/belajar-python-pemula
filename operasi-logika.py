# OPERASI LOGIKA 
a = True
print(f"\na = {a}")
b = False 
print(f"b = {b}")

print("\n====== NOT ======")
# OPERASI LOGIKA NOT
# Mengubah data
x = not a
print(f"NOT {a} = {x}")
x = not b
print(f"NOT {b} = {x}")

print("\n====== OR ======")
# OPERASI LOGIKA OR
# Nilai akan False jika keduanya False
x = a or a
print(f"{a} OR {a} = {x}")
x = a or b
print(f"{a} OR {b} = {x}")
x = b or a
print(f"{b} OR {a} = {x}")
x = b or b
print(f"{b} OR {b} = {x}")

print("\n====== AND ======")
# OPERASI LOGIKA AND
# Nilai akan True jika keduanya True
x = a and a
print(f"{a} AND {a} = {x}")
x = a and b
print(f"{a} AND {b} = {x}")
x = b and a
print(f"{b} AND {a} = {x}")
x = b and b
print(f"{b} AND {b} = {x}")

print("\n====== XOR ======")
# OPERASI LOGIKA XOR
# Nilai akan True jika hanya ada satu True
x = a ^ a
print(f"{a} XOR {a} = {x}")
x = a ^ b
print(f"{a} XOR {b} = {x}")
x = b ^ a
print(f"{b} XOR {a} = {x}")
x = b ^ b
print(f"{b} XOR {b} = {x}")

