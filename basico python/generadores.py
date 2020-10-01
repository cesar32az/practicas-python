#GENERAR NUMEROS PARES

#con una funcion normal

def generaPares(limite):

    num=1

    miLista= []

    while num<limite:
        
        miLista.append(num*2)

        num+=1

    return miLista

#print(generaPares(10))

#lo mismo pero con GENERADOR

def generdorPares(limite):

    num=1

    while num<limite:
        
        yield num*2

        num+=1
devuelvePares=generdorPares(10)

#devolver todos los pares
#for i in devuelvePares:
#    print(i)

#devolver solo un primer valor, luego el siguiente, etc
#primer valor
print(next(devuelvePares))

print("aca podria ir codigo")

print(next(devuelvePares))

print("aca podria ir mas codigo")

print(next(devuelvePares))

print("aca podria ir mas codigo")


def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        yield elemento

ciudades_devueltas = devuelve_ciudades("madrid", "barcelona", "bilbao", "valencia")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))