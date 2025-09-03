# LIST COPY
# Untuk mengcopy data pada list agar bisa bersifat immutable

a = ["Zaza","Zizi","Zuzu"]
print(f"Data list a = {a}")

b = a
print(f"Data list b = {b}\n")

a.append("NyamNyamNyam")
print(f"Data list a = {a}")
print(f"Data list b = {b}")

c = a.copy()
print(f"Data list c = {c}\n")

a.remove("Zaza")
print(f"Data list a = {a}")
print(f"Data list b = {b}")
print(f"Data list c = {c}\n")



