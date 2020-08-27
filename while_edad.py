edad=int(input("Introduce tu edad: "))

while edad<0:
    print("Has introducido una edad negativa, intentalo de nuevo")
    edad=int(input("introduce tu edad por favor: "))
print("gracias!!!  ")
print("edad del aspirante: " + str(edad))