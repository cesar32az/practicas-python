class Carro():
    def desplazamiento(self):
        print("me desplazo con 4 ruedas")

class Moto():
    
    def desplazamiento(self):
        print("me desplazo con 2 ruedas")

class Camion():
    def desplazamiento(self):
        print("me desplazo con 6 ruedas")

#recibimos como parametro el objeto y dependiendo a que clase pertenece ese vehiculo
#ya ejecuta el metodo desplazamiento segun la clase del objeto
def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

miVehiculo=Moto()

desplazamientoVehiculo(miVehiculo)