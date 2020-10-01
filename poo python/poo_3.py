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

        if (self.__enmarcha):
            chequeo=self.__chequeoInterno()
            print("chequeo: ", chequeo)

        if (self.__enmarcha and chequeo):
            return "el coche esta en marcha"
        
        elif (self.__enmarcha and chequeo == False):
            return "Algo anda mal en el chequeo, no se puede arrancar el coche"
 
        else:
            return "el coche esta parado"
#metodo para imprimir el estado del coche
    def estado(self):
        print("el coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis)

#metodo encapsulado
    def __chequeoInterno(self):
        print("realizando chequeo interno")

        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if (self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False
        


        
#instanciamos una clase
miCoche=Coche()

print("\nCon el comportamiento arrancar: ")
print(miCoche.arrancar(True))
miCoche.estado()

print("\n************************** Creamos el segundo objeto *****************************")

miCoche2= Coche()
print(miCoche2.arrancar(False))

miCoche2.estado()
