import math as m

print("calcular raiz cuadrada")
numero=int(input("Introduce tu numero: "))

intentos=0

while numero<0:
    print("no se puede hallar la raiz de un negativo")

    if intentos==2:
        print("has consumido todos tus intentos. bye!")
        break
    numero=int(input("Introduce tu numero: "))
    if numero<0:
        intentos = intentos+1
if intentos<2:
    solucion=m.sqrt(numero)
    print("la raiz cuadrada de: " + str(numero) + " es " + str(solucion))
