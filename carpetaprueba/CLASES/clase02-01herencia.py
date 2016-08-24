### clase02-01"herencia"
# Aquí estamos extendiendo y especializando la clase lista estándar. Tiene todos
# los métodos de la lista más los definidos por nosotros.
# Recordar que para nombrar las clases se utiliza notación CamelCase.
class ContactList(list):
    # buscar es un método específico de esta sub-clase
    def buscar(self, nombre):
        matches = []
        for contacto in self:
            if nombre in contacto.nombre:
                matches.append(contacto)   
        return matches

    
class Contacto:
    # Contacto se compone de una lista de contactos del tipo ContactList
    # contactos_list = [] #así sería para usar una lista común y corriente
    contactos_list = ContactList()
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        Contacto.contactos_list.append(self) # el método append()
        # es heredado de la clase List()

# Familiar es una clase especializada de contacto que permite incluir el tipo de relación
class Familiar(Contacto):
    def __init__(self, nombre, email, relacion): # Overriding sobre el
        # método __init__()
        super().__init__(nombre, email) # Obtiene la instancia del padre
        # y llama a su funcion __init__
        self.relacion = relacion

p1 = Familiar(nombre = "Juan Gomez", email = "jc@hotmail.com", relacion = "padre")
p2 = Contacto(nombre = "Jorge Gonzales", email = "jg@gmail.com")
p3 = Familiar(nombre = "Pablo Gomez", email = "pab_g@gmail.com", relacion = 'primo')

L = [c.nombre for c in p1.contactos_list.buscar("Jorge")]

print('[', end='')
print(*L, sep=', ', end='')
print(']')
