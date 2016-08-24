import sys
import collections
import string 

class Reporte:
    'Genera el reporte de una persona'

    def __init__(self, latitud, longitud, error, tiempo, actividad, probabilidad):
        self.reporte = [latitud, longitud, error, tiempo, actividad, probabilidad]


class Persona:
    'Genera a una persona'

    def __init__(self, nombre, apellido, mail, imei):
        self.nombre = nombre
        self.apellido = apellido
        self.mail = mail
        self.imei = imei
        self.reportes = []
        self.persona = [nombre, apellido, mail, imei]

    def agregarReporte(self, lat, lon, err, tiem, act, prob):
        rep = Reporte(lat, lon, err, tiem, act, prob)
        if len(self.reportes) == 0:
            self.reportes.append(rep)
        else:
            for i in range(0, len(self.reportes)):
                if rep.reporte[3] >= self.reportes[i].reporte[3]:
                    self.reportes.index(i, rep)

    def promedio_error(self):
        total_rep = int(len(self.reportes))
        prom_error = 0
        for i in range(0, len(self.reportes)):
            prom_error += int(self.reportes[i].reporte[2])
        return (print("Promedio de error sobre {} es {}" .format(self.nombre, prom_error/total_rep)))

    def tiempo_promedio(self):
        promedio = 0
        for i in range(0,len(self.reportes)-1):
            tiempo1 = int(self.reportes[i].reporte[3])
            tiempo2 = int(self.reportes[i+1].reporte[3])
            promedio += (tiempo2 - tiempo1)/2
        promedio_final = promedio/(len(self.reportes)-1)
        return (print("Promedio de tiempo por reporte de {} es de {}".format(self.nombre, promedio_final)))
    
    def actividad_frecuente(self):
        lista = []
        for i in range(0, len(self.reportes)):
            lista.append(str(self.reportes[i].reporte[4]))
        lista2= collections.Counter(lista)
        lista3 = dict(lista2)
        return print(lista3)


class Pais:
    'Define un pais'
    def __init__(self, pais):
        self.pais = pais
        self.personas = []

    def agregarPersona(self, persona):
        self.personas.append(persona)

    def desplegarPersonas(self):
        print(self.pais)
        lista_de_personas = []
        for i in range (0, len(self.personas)):
            lista_de_personas.append(self.personas[i].nombre+" "+self.personas[i].apellido)
        print(lista_de_personas)



class Continente:
    'define continente'
    def __init__(self, continente):
        self.continente = continente
        self.paises = []

    def agregarPais(self, pais):
        self.paises.append(pais)


class Menu:
    'define sistema'
    def __init__(self):
        self.continentes=[]
        self.opciones = {
                        "1": self.agregar_continente,
                        "2": self.agregar_pais,
                        "3": self.agregar_persona,
                        "4": self.agregar_reporte,
                        "5": self.gente_en_pais,
                        "6": self.caracteristicas_reportes,
                        "7": self.salir
                        }

    def display_menu(self):
        print("""
            Menu:
                1: Agregar Continente
                2: Agregar Pais
                3: Agregar Persona
                4: Agregar Reporte
                5: Gente en Pais
                6: Caracteristicas de Reportes
                7: Salir
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

    def agregar_continente(self):
        cont = input("Agregue nombre del Continente:")
        self.continentes.append(Continente(cont))

    def agregar_pais(self):
        cont = input("En que continente quiere agregar el pais:")
        for i in range (0,len(self.continentes)):
            if cont == self.continentes[i].continente:
                pais = input("nombre del pais")
                self.continentes[i].agregarPais(Pais(pais))

    def agregar_persona(self):
        cont = input("En que continente quiere agregar a la persona:")
        for i in range (0, len(self.continentes)):
            if cont == self.continentes[i].continente:
                pais = input("en que pais:")
                for j in range(0, len(self.continentes[i].paises)):
                    if pais == self.continentes[i].paises[j].pais:
                        nom = input("ingrese nombre:")
                        ape = input("ingrese apellido")
                        mail = input("ingrese mail")
                        imei = input ("ingrese imei")
                        p=Persona(nom,ape,mail,imei)
                        self.continentes[i].paises[j].agregarPersona(p)

    def agregar_reporte(self):
        nom = input("ingrese nombre de la persona")
        for i in range (0, len(self.continentes)):
            for j in range(0, len(self.continentes[i].paises)):
                for k in range(0, len(self.continentes[i].paises[j].personas)):
                    if nom == self.continentes[i].paises[j].personas[k].nombre:
                        lat = input("ingrese latitud:")
                        lon = input("ingrese longitud")
                        err = input("ingrese error")
                        tiem = input("ingrese tiempo")
                        act = input("ingrese activida")
                        prob = input("ingrese probailida")
                        self.continentes[i].paises[j].personas[k].agregarReporte(lat,lon,err,tiem,act,prob)

    def gente_en_pais(self):
        cont = input("En que continente quiere buscar:")
        for i in range (0, len(self.continentes)):
            if cont == self.continentes[i].continente:
                pais = input("en que pais:")
                for j in range(0, len(self.continentes[i].paises)):
                    if pais == self.continentes[i].paises[j].pais:
                        self.continentes[i].paises[j].desplegarPersonas()

    def caracteristicas_reportes(self):
        nom = input("ingrese nombre de la persona")
        for i in range (0, len(self.continentes)):
            for j in range(0, len(self.continentes[i].paises)):
                for k in range(0, len(self.continentes[i].paises[j].personas)):
                    if nom == self.continentes[i].paises[j].personas[k].nombre:
                        self.continentes[i].paises[j].personas[k].promedio_error()
                        self.continentes[i].paises[j].personas[k].actividad_frecuente()
                        self.continentes[i].paises[j].personas[k].tiempo_promedio

    def salir(self):
        print("Gracias por usar nuestro Sistema de inteligencia")
        sys.exit(0)

if __name__ == "__main__":#esto es para que corra en la consola
    Menu().run()
    


p=Persona("mar", "al","chi", "shit")
p.agregarReporte("lo","la","er",4,"la","pr")
c=Pais("Peru")
c.agregarPersona(p)
print(p.reportes)
print(p.persona)
print(c.personas[0].nombre)