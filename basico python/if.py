print("Notas de alumnos")

# nota_alumno = int(input("ingresa la nota"))

def evaluacion(nota):
    valoracion="aprobado"
    if nota<5:
        valoracion="suspenso"
    return valoracion

#print(evaluacion(nota_alumno))
#print(type(nota_alumno))

print("verificacion de usuario")
edad = int(input("ingrese la edad: \n"))

if edad>18:
    print("mayor de edad")
elif edad>100:
    print("fuera de rango")
else:
    print("menor de edad")


