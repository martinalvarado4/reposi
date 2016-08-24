### act01-2016
### agregarObservacion() agregarField() agregarEstrella()
### para cada estrella el promedio y varianza de la magnitud de su brillo
### cada estrella tiene una posicion con coordenadas( RA y DEC), 
###un id unico para un catalogo y un conjunto de observaciones que pueden aumetnar en el tiempo
### cada observacio nesta compuesta por tres numero: tiempo cuando fue ralizda, magnitud de brillo 
## y rango de error correspondiente
### el cielo esta cuempouesto de fields y cada field contiene muchas estrellas
import string
import sys 
import collections

class Observacion:
	'genera observacion'
	def __init__(self, tiempo, magnitud, error):
		self.tiempo = tiempo
		self.magnitud = magnitud
		self.error = error


class Estrella:
	'genera estrella'
	## variable estatica q guarda ultimo id
	last_id = 0
	def __init__(self, RA, DEC, tipo):
		self.RA = RA
		self.DEC = DEC
		self.tipo = tipo
		self.coordenadas = [RA, DEC]
		self.idd = Estrella.last_id
		self.observaciones = []
		Estrella.last_id += 1

	def agregarObservacion(self, observacion):
		self.observaciones.append(observacion)

	def promedioBrillo (self):
		suma = 0
		for i in range(0, len(self.observaciones)):
			suma = suma + int(self.observaciones[i].magnitud)
		prom = suma / int(len(self.observaciones))
		return print(prom)

	def varianzaBrillo (self):
		suma = 0
		for i in range(0, len(self.observaciones)):
			suma = suma + int(self.observaciones[i].error)
		var = (suma**2) / int(len(self.observaciones))
		return print(var)

class Field:
	'genera field'
	def __init__(self, nombre):
		self.nombre = nombre
		self.estrellas = []

	def agregarEstrella(self, estrella):
		self.estrellas.append(estrella)

class Cielo:
	'genera el sistema'
	def __init__(self):
		self.fields = []
		self.opciones = {
						"1": self.agregar_Field,
						"2": self.agregar_Estrella,
						"3": self.agregar_Observacion,
						"4": self.dar_Promedio,
						"5": self.dar_Varianza,
						"6": self.salir
						}

	def display_menu(self):
		print("""
            Menu:
                1: Agregar Field
                2: Agregar Estrella
                3: Agregar Observacion
                4: Dar Promedio
                5: Dar Varianza
                6: Salir
            """)

	def run(self):
		while True:
			self.display_menu()
			eleccion = input("Ingrese Opcion: ")
			accion = self.opciones.get(eleccion)
			if accion:
			    accion()
			else:
			    print("{0} no es una opcion valida".format(eleccion))


	def agregar_Field(self):
		field = input("Agregue nombre del Field:")
		self.fields.append(Field(field))

	def agregar_Estrella(self):
		fil = input("en que field:")
		for i in range(0,len(self.fields)):
			if fil == self.fields[i].nombre:
				RA = input("ingrese coordenada RA:")
				DEC = input("ingrese coordenada DEC:")
				tipo = input("ingrese tipo estrella:")
				est = Estrella(RA, DEC, tipo)
				self.fields[i].agregarEstrella(est)

	def agregar_Observacion(self):
		idd = int(input("ingrese id de la estrella"))
		for i in range (0, len(self.fields)):
			for j in range(0, len(self.fields[i].estrellas)):
				if idd == int(self.fields[i].estrellas[j].idd):
					tiem = input("ingrese tiempo:")
					mag = input("ingrese magnitud")
					err = input("ingrese error:")
					ob = Observacion(tiem, mag, err)
					self.fields[i].estrellas[j].agregarObservacion(ob)

	def dar_Promedio(self):
		idd = int(input("ingrese id de la estrella:"))
		for i in range (0, len(self.fields)):
			for j in range(0, len(self.fields[i].estrellas)):
				if idd == int(self.fields[i].estrellas[j].idd):
					self.fields[i].estrellas[j].promedioBrillo()

	def dar_Varianza(self):
		idd = int(input("ingrese id de la estrella:"))
		for i in range (0, len(self.fields)):
			for j in range(0, len(self.fields[i].estrellas)):
				if idd == int(self.fields[i].estrellas[j].idd):
					self.fields[i].estrellas[j].varianzaBrillo()

	def salir(self):
		print("Gracias por usar nuestro Sistema de inteligencia")
		sys.exit(0)

if __name__ == "__main__":#esto es para que corra en la consola
    Cielo().run()
    



