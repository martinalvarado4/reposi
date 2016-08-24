#### clase01-02"multiclases"
#### e interaccion
#Ejemplo: Programa para manejar postits en un panel mural

###trae el date time
import datetime

class PostIt:
    ''' Representa un post it, contiene un mensaje, guarda
    un conjunto de tags y responde si hay match con ciertos tags
        Contiene ademas un id
    '''
    last_id = 0 #variable estática para manejar el ultimo id generado
    def __init__(self, mensaje, tags = ''):
        self.mensaje = mensaje
        self.tags = tags
        ## pueden existir atributos fijos o variables que no requieren
        ## de ser ingresados
        self.creation_date = datetime.date.today()
        #variable de la clase para manejar el ultimo id generado
        ##la clase en si parte con last_id 0 y se modifica
        ## cada vez q se crea otro objeto
        self._id = PostIt.last_id
        ## le suma una a el last_id de la clase
        PostIt.last_id += 1
    def match(self, keyword):
        ''' determina si el mensaje de la nota contiene el keyword o no'''
        return keyword in self.mensaje or keyword in self.tags
    
class Panel:
    ''' Representa un panel con un conjunto de postits (con memos) pegados
        cada hoja ademas de un memo tiene tags, asi podemos buscar hojas
        tambien podemos modificarlas
    '''
    def __init__(self):
        self.postit_dict = {}
    #esta función será necesaria para varios métodos de la clase
    #una mejor opción es usar un diccionario e indexar por el id del postit
    #def _buscar_postit_id(self, postit_id):
    #    ''' Busca el postit correspondiente al id'''
    #    for p in self.postit_dict:
    #        if p._id == postit_id:
    #            return p
    #    return None
    def nuevo_postit(self, texto, tags = ''):
        '''Agrega una hoja con un mensaje a nuestro muro'''
        ### se crea un objeto posti
        p = PostIt(texto, tags)
        self.postit_dict.update({p._id : p})
    def modifica_mensaje(self, postit_id, mensaje_nuevo):
        #este for era una opcion pero es mejor hacer una fucion
        #aparte que busque, para
        #no repetir codigo en la funcion modifica_tags
        #for p in self.postit_dict:
        #    if p._id == postit_id:
        self.postit_dict[postit_id].mensaje = mensaje_nuevo
    def modifica_tags(self, postit_id, tags_nuevos):
        self.postit_dict[postit_id].tags = tags_nuevos
    def buscar_postits(self, keyword):
        return [p for p in self.postit_dict.values() if p.match(keyword)]
    def display(self, keyword = None):
        ''' Muestra todos los post its en el panel'''
        result = []
        if keyword:
            result = [p for p in self.buscar_postits(keyword)]
        else:
            result = self.postit_dict
        for p in result:
            print("post it {0}: \n Mensaje: {1} \n Tags: {2}".format(p._id, p.mensaje, p.tags))

import sys
#from postit import PostIt, Panel#Aquí no es necesario por el iPython,
#pero si tenemos un archivo separado para el menu hay que
#importar estas clases

class Menu:
    def __init__(self):
        self.panel = Panel()
        ## CLAVE si se da 1 se trae el self.display_postits
        self.opciones = {
                        "1": self.display_postits,
                        "2": self.buscar_postits,
                        "3": self.agregar_postit,
                        "4": self.modificar_postit,
                        "5": self.salir
                        }

    def display_menu(self):
        print("""
            Menu:
                1: Mostrar Post-Its
                2: Buscar Post-Its
                3: Agregar nuevo Post-It
                4: Modificar Post-It existente
                5: Salir
            """)
    def run(self):
        ##siempre se corre
        while True:
            ## imprime menu
            self.display_menu()
            ## interactua
            eleccion = input("Ingrese Opcion: ")
            ### get optiene una de las cinco acciones
            accion = self.opciones.get(eleccion)
            if accion:
                accion()#aqui se llama a la funcion
            else:
                print("{0} no es una opcion valida".format(eleccion))
    def display_postits(self, p_list = None):
        if not p_list:
            p_list = self.panel.postit_dict.values()
            #si no dan la lista a mostrar, mostramos todos los post-its

        if not p_list:
            print("No hay Post-Its creados...")
        else:
            for p in p_list:
                print("post it {0}: \n Mensaje: {1} \n Tags: {2}".format(p._id, p.mensaje, p.tags))
    def buscar_postits(self):
        keyword = input("Ingrese keyword: ")
        postit_list = self.panel.buscar_postits(keyword)
        self.display_postits(postit_list)
    def agregar_postit(self):
        mensaje = input("Ingrese Mensaje: ")
        tag_list = input("Ingrese Tags separados por espacios: ")
        tag_list = tag_list.split()#separa los strings por espacio y los pone en una lista
        self.panel.nuevo_postit(mensaje, tag_list)
        print("Nota creada exitosamente!!")
    def modificar_postit(self):
        _id = input("ingrese el id del Post-It que quiere modificar: ")
        _id = int(_id)
        while _id not in self.panel.postit_dict.keys():
            print("El id no existe en la base de datos..")
            _id = input("ingrese el id del Post-It que quiere modificar: ")
            _id = int(_id)
        
        mensaje = input("Ingrese el nuevo mensaje: ")
        tag_list = input("Ingrese los nuevos tags separados por espacios: ")
        if mensaje:
            print(_id)
            self.panel.modifica_mensaje(_id, mensaje)
        if tag_list:
            tag_list = tag_list.split()
            self.panel.modifica_tags(_id, tag_list)
        print("postit modificado exitosamente!!")
    def salir(self):
        print("Gracias por usar nuestro Post-It")
        sys.exit(0)


if __name__ == "__main__":#esto es para que corra en la consola
    Menu().run()

##el método "_call_" se usa para crear una función que será ejecutada
##siemrep q se "llame" a una instancia la clase con paréntesis ( instancia() ).
class Animal():
    def __init__(self, nombre, patas):
        self.nombre = nombre
        self.patas = patas
        self.estomago = []        
## al usar __metodo__ se puede aplicar sobre el objeto con solo meter
## objeto(extra)
    def __call__(self,comida):
        self.estomago.append(comida)
    
    def asimilar(self):
        if len(self.estomago) > 0:
            return self.estomago.pop(0)
        
    def __str__(self):
        return ('Animal llamado: {}'.format(self.nombre))
        
#gato = Animal('Cucho', 4)  #We make a cow
#perro = Animal('Boby', 4) #We can make many animals
#print(gato.nombre)
#print(perro) #aquí funciona el método __str__
#gato('pescado')#aquí le damos pescado al gato usando el método __call__
#print(gato.estomago)
#gato.asimilar()
#print(gato.estomago)
