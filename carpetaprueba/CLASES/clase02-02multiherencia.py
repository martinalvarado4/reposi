## clase02-02Multiherencia
class Investigador():
    def __init__(self, area):
        self.area = area
        
class Docente():
    def __init__(self, Departamento):
        self.departamento = Departamento
        
class Academico(Docente, Investigador):
    def __init__(self, nombre, area_investigacion, departamento):
        #esto no es del todo correcto, coming soon...
        Investigador.__init__(self, area_investigacion)
        Docente.__init__(self, departamento)
        self.nombre = nombre

p1 = Academico("Juan Perez", "Inteligencia de Máquina", "Ciencia De La Computación")
print(p1.nombre)
print(p1.area)
print(p1.departamento)

### super() se ocupa del problema de orden de herencia de multiclases
class ClaseB:
    num_llamadas_B = 0
    def llamar(self):
        print("Llamando método en Clase B")
        self.num_llamadas_B += 1


class SubClaseIzquierda(ClaseB):
    num_llamadas_izq = 0
    def llamar(self):
        super().llamar()
        print("Llamando método en Subclase Izquierda")
        self.num_llamadas_izq += 1

class SubClaseDerecha(ClaseB):
    num_llamadas_der = 0
    def llamar(self):
        super().llamar()
        print("Llamando método en Subclase Derecha")
        self.num_llamadas_der += 1

class SubClaseA(SubClaseIzquierda, SubClaseDerecha):
    num_llamadas_subA = 0
    def llamar(self):
        super().llamar()
        print("Llamando método en SubclaseA")
        self.num_llamadas_subA += 1


s = SubClaseA()
s.llamar()
print(s.num_llamadas_subA, s.num_llamadas_izq, s.num_llamadas_der, s.num_llamadas_B)
### nos muestra el orden de jerarquia
SubClaseA.__mro__

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
        rep=Reporte(lat, lon, err, tiem, act, prob)
        if len(self.reportes)==0:
            self.reportes.append(rep.reporte)
        else:
            for i in range(0, len(self.reportes)):
                if rep[3] >= self.reportes[i][3]:
                    self.reportes.index(i,rep.reporte)

    def promedio_error(self):
        total_rep = int(len(self.reportes))
        prom_error = 0
        for i in range(0, len(self.reportes)):
            prom_error += int(self.reportes[i][2])
        return (print("Promedio de error sobre {} es {}" .format(self.nombre, prom_error/total_rep)))

    def tiempo_promedio(self):
        promedio = 0
        for i in range(0,len(self.reportes)-1):
            tiempo1 = int(self.reportes[i][3])
            tiempo2 = int(self.reportes[i+1][3])
            promedio += (tiempo2 - tiempo1)/2
        promedio_final = promedio/(len(self.reportes)-1)
        return (print("Promedio de tiempo por reporte de {} es de {}".format(self.nombre, promedio_final)))


class Pais:
    'Define un pais'
    def __init__(self,pais):
        self.pais = pais
        self.personas = []

    def agregarPersona(self, persona):
        self.personas.append(persona)

p=Persona(mar, al, chi, shit)
p.agregarReporte(lo,la,er,4,la,pr)
c=Pais(Peru)
c.agregarPersona(p)
print(p.reportes)
print(p.persona)
print(c.personas[0].nombre)