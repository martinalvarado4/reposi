#Tarea-01
import jsonReader
import random
programones=jsonReader.jsonToDict("programones.json")
programonMoves=jsonReader.jsonToDict("programonMoves.json")
routes=jsonReader.jsonToDict("routes.json")
types=jsonReader.jsonToDict("types.json")
moveCategories=jsonReader.jsonToDict("moveCategories.json")
gyms=jsonReader.jsonToDict("gyms.json")
jugadoresEjemplo=jsonReader.jsonToDict("jugadoresEjemplo.json")
# print(moveCategories)
print(programones[0])
# print(random.randint(1,100))


#print(programonMoves[2])
#print(types["water"])
# print(routes[0])
# print(programones[0].get("name"))
# print(programones[0].values())
# print("name" in programones[0])
# print(programonMoves[0])
# c=programonMoves[0].get("power")
# if c == 120:
    # print("hola")

# for items in programones[0]:
    # print(items,":",programones[0][items])
### dciccionaro [ key] te retorna el value
# print(programones[0]["name"])
# print(programones[0])
### clave
# for programon in programones:
  #  if programon["id"]==80:
   #     print(programon)
## evoluciones
## evolveTo no existe pa algunos por eso get pa tirar None
# for programon in programones:
  #  proN=programon["name"]
  #  evol=programon.get("evolveTo")
  #  if evol != None:
   #     for programonevol in programones:
    #        if evol == programonevol["id"]:
     #           print(proN,"evoluciona a :", programonevol["name"])
