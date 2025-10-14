# VARIEABLE GLOBAL DAN LOCAL
# Variable di bagi menjadi dua yaitu variable global dan local

# contoh variable global
var_global = "Hello World" # ini adalah variable global karena tidak di dalam  

# contoh variable local
def data():
    var_local = "Hello World" # ini adalah variable local karena ada di dalam

# kenapa begitu ?
# karena variable local tidak bisa di panggil secara global 

# contoh
var = "Hello" # variable global
def exmp():
    var = "Hello World" # variable local

exmp()
print(var) # yang akan terpanggil akan variable global bukan variable local

# terus gimana caranya manggil variable local seperti variable global?
# caranya tinggal ubah variable local dengan variable global dengan cara (global variable)

# contoh
var = "Hello" # variable global
def exmp():
    global var
    var = "Hello World" # variable local

exmp()
print(var) # akan mengambil variable yang ada di local karena sudah di ubah menjadi global
