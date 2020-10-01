#clase coche
class Coche():

#constructor
    def __init__(self):
        
        self.__largoChasis=250   # encapsulamiento, la variable prece dos guiones bajos para encapsularla, no permite ser modificada fuera de la clase
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enmarcha=False

#metodo de la clase coche
    def arrancar(self, arrancamos):
        self.__enmarcha=arrancamos  #dentro de la clase si permite modificar la variable encapsulada

        if self.__enmarcha:
            return "el coche esta en marcha"
        else:
            return "el coche esta parado"
#metodo para imprimir el estado del coche
    def estado(self):
        print("el coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis)

        
#instanciamos una clase
miCoche=Coche()

print("\nCon el comportamiento arrancar: ")
print(miCoche.arrancar(True))
miCoche.estado()

print("\n************************** Creamos el segundo objeto *****************************")

miCoche2= Coche()
print(miCoche2.arrancar(False))

miCoche2.ruedas=3   #al estar encapsulada no permite modificar su valor fuera de la clase   
miCoche2.estado()
