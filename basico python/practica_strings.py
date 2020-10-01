nombre=input("introduce el nombre: ")

print("nombre upper: ", nombre.upper())

print("nombre lower: ", nombre.lower())

print("nombre capitalize: ", nombre.capitalize())

edad=input("introduce la edad: ")

while (edad.isdigit()==False):
    print("por favor introduce un valor numerico")
    edad=input("introduce la edad: ")

if (int(edad)<18):
    print("no puede pasar")
else:
    print("si puede pasar")
