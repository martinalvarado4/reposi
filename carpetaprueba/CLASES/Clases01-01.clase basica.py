### Haciendo clases

# get(): Devuelve el valor que corresponde con la key introducida.
print(diccionario.get('Piloto 1'))
Fernando Alonso
 
# "key" in diccionario: devuelve verdadero (True) o falso (False) si la key existe en el diccionario.
print ("Piloto 1" in diccionario)
True
print ("piloto 1" in diccionario)
False
print ("Fernando Alonso" in diccionario)
False
 
# "definición" in diccionario.values(): devuelve verdadero (True) o falso (False) si la definición existe en el diccionario.
print ("Fernando Alonso" in diccionario.values())
True
 
# pop():  Devuelve el valor que corresponde con la key introducida, y luego borra la key y el valor.
print(diccionario.pop('Piloto 1'))
Fernando Alonso
print(diccionario)
{'Piloto 3': 'Felipe Massa', 'Piloto 2': 'Kimi Raikkonen'}
 
# del lista['key']: Elimina el valor (y el key) asociado a la key indicada. A LO MEJOR SE PUEDE QUITAR TAMBIÉN.
del diccionario['Piloto 2']
print(diccionario)
{'Piloto 3': 'Felipe Massa'}
class Vector:
    ## descripcion de la clase, se aparece al usar help
    ''' Vector en 3D '''
    ## define q hay en el objeto
    def __init__(self , x , y ,z):
        self.x=x
        self.y=y
        self.z=z
    ## metodo de clase, despliega el vector como lista
    def desplegar(self):
        ## self.x el valor ingresado en el atributo x del vector
        vec=[self.x,self.y,self.z]
        print(vec)
    def modulo(self):
        mod=((self.x**2)+(self.y)**2+(self.z**2))**(1/2)
        ### unir string con +
        print("modulo del vector es "+str(mod))
    ### un metodo puede requerir de otro elento externo
    ### para este metodo(self, extra)
    def multiplicar(self,multiplicador):
        nuevovec=[self.x*multiplicador,self.y*multiplicador,self.z*multiplicador]
        ### return devuelve el elemento en si
        ### en este caso una lista
        return nuevovec
### crea un objeto v de la clase Vector
### Vector(x,y,z) requiere de tres atributos en x,y ,z
v=Vector(2,4,4)
### objeto.metodo se le aplica el metodo al objeto
v.desplegar()
v.modulo()
## v.x arroja el atributo x del objeto v
print(v.x)
### al utilizar un metodo que requiere un extra, se usa objeto.metodo(extra)
y=v.multiplicar(2)
### como metodo tiene return se puede igualar a una variable y
###transformarla en este objeto
### en este caso una lista y podemos imprimir su segundo elemento
print(y)
print(y[2])



## Para ver descripcion de clase (tres lineas vec 3d se ve al usar help)
help(Vector)


#### PROGRA 1ER SEM 2016 ####

class Departamento:#CamelCase notation (PEP8)
    '''Clase que representa un departamento en venta
       valor esta en UF
    '''
    def __init__(self, _id, mts2, valor, num_dorms, num_banos):
        self._id = _id
        self.mts2 = mts2
        self.valor = valor
        self.num_dorms = num_dorms
        self.num_banos = num_banos
        self.vendido = False

    def vender(self):
        if not self.vendido:
            self.vendido = True
        else:
            print("Departamento {} ya se vendio".format(self._id))
d1 = Departamento(_id = 1, mts2 = 100, valor = 5000, num_dorms = 3, num_banos = 2)
print(d1.vendido)
d1.vender()
print(d1.vendido)
d1.vender()

### Metodo o variable de tipo interno
class PalabraSecreta:
    ''' clase que guarda un string sin mucha seguridad
    '''
    def __init__(self, palabra_clave, frase_secreta):
        ### al usar __ antes del atributo bloquemos que puede ser
        ### llamado facilmente o directamente
        self.__palabra_clave = palabra_clave
        self.__frase_secreta = frase_secreta

    def decriptar(self, frase_secreta):
        ''' Solo si la frase_secreta es correcta'''
        if frase_secreta == self.__frase_secreta:
            return self.__palabra_clave
        else:
            return ''

s = PalabraSecreta("animal","tiene patas")
print(s.decriptar("tiene patas"))
### para poder llamar al atributo __palabra_clave del objeto s
## se debe agreagar _Clase en este caso _PalabraSecreta
s._PalabraSecreta__palabra_clave
