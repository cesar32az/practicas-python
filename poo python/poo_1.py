class Coche():
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enmarcha=False

#metodo de la clase coche
    def arrancar(self):
        self.enmarcha=True

    def estado(self):
        if self.enmarcha:
            return "el coche esta en marcha"
        else:
            return "el coche esta parado"

        
#instanciamos una clase
miCoche=Coche()

print("el largo del coche es: ", miCoche.largoChasis)
print("el coche tiene ", miCoche.ruedas, " ruedas\n")

print(miCoche.estado())

print("\nCon el comportamiento arrancar: ")
miCoche.arrancar()

print(miCoche.estado())
