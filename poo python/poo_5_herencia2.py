class Vehiculos():
    
    def __init__(self, marca, modelo):
        #parametros a pasar, obligatorios
        self.marca = marca
        self.modelo = modelo
        #parametros propios de la clase
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        
        self.enmarcha = True

    def acelerar(self):
        
        self.acelera = True
    
    def frenar(self):
        
        self.frena = True
    
    def estado(self):
        print("Marca: ",self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha, "\nAcelerando: ", 
        self.acelera, "\nFrenando: ", self.frena)

class Furgoneta(Vehiculos):
    
    def carga(self, cargar):
        self.cargado=cargar
        if (self.cargado):
            return "la furgoneta esta cargada"
        else:
            return "la furgonega no esta cargada"



#heredamos de la clase vehiculos a la clase moto
class Moto(Vehiculos):
    hwheelie=""

    def wheelie(self):
        self.hwheelie="voy haciendo un wheelie"
    
    def estado(self):
        print("Marca: ",self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha, "\nAcelerando: ", 
        self.acelera, "\nFrenando: ", self.frena, "\n", self.hwheelie)

class VElectricos(Vehiculos):
    def __init__(self, marca, modelo):

        super().__init__(marca, modelo)
        self.autonomia=100
    
    def cargarEnergia(self):
        self.cargando=True


miMoto = Moto("honda", "cb190")
miMoto.wheelie()
miMoto.estado()

print("\n*********************\n")
miFurgoneta=Furgoneta("renault", "strip")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

print("\n*********************\n")
class BiciElectrica(VElectricos,Vehiculos):
    pass

miBici=BiciElectrica("xiaomi", "mibiomi")
miBici.estado()