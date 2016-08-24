### kwargs ** y hay q definir nombre = "algo" en Clase(nombre="algo") y se puede cambiar 
## el orden a meterlo a la funcion y tambien en el init(self,Nombre="")
### pero si pongo * debo definir ña wea sin =
### si se ocupa * usar __mro__ pa ver el orden de elementos q hay q poner
from abc import ABCMeta, abstractmethod

class Atleta(metaclass=ABCMeta):
    def __init__(self, nombre="" , velocidad=""):
        self.nombre = nombre
        self.nivel=100
        self.velocidad = velocidad
    def descansar(self):
    	if self.nivel < 100:
    		self.nivel +=1
    def entrenar(self):
    	print("")
    def __lt__(self,loco2):
    	return self.marcas[0] < loco2.marcas[0]


class Ciclista(Atleta):
    def __init__(self, tipo="", **chili):
        super().__init__(**chili)
        self.tipo = tipo
        self.marcas=[25]

class Nadador(Atleta):

	def __init__(self, **chili):
		super().__init__(**chili)
		self.marcas=[25]

class Corredor(Atleta):

	def __init__(self,**chili):
		super().__init__(**chili)
		self.marcas=[25]


class Triatleta(Ciclista,Nadador,Corredor):
	def __init__(self,**chili):
		super().__init__(**chili)
		self.marcas=[25]



atl1=Nadador(nombre="pedro",velocidad="loco")
atl2=Corredor(nombre="jo",velocidad="looo")
print(atl1<atl2)
#print(Triatleta.__mro__)
class DT:
	def __init__(self, nombre):
		self.nombre=nombres
		self.equipo=[]


#c=Corredor("marcos",5)
#print(c.nombre)
#print(Ciclista.__mro__)
#c = Ciclista('Juan Loco Perez',  'jlp@gmail.com',  '54542331')

#print("{}, {}, {}".format(c.nombre, c.velocidad, c.tipo))