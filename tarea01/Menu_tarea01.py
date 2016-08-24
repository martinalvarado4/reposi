## menu tarea017
import jsonReader
import random
import sys
from ClasesT1 import Programon, Prograbola, Progradex, PCBastian, Jugador, Entrenador, Gimnasio, Ciudad, Hierba , Mapa
from ClasesT1 import jprogramones, jprogramonMoves, jroutes, jtypes, jmoveCategories, jgyms, jjugadoresEjemplo, inputCorrecto, inputCorrecto2, inputCorrecto3, sacarNombre
from correr import Batalla, Ataque
arch= jsonReader.jsonToDict("player.json")
class MenuInicial:
	def __init__(self, datos):
		self.jugadores = []
		self.datos = datos
		self.mapa = Mapa(jroutes,jgyms)
		self.opciones={
			"1": self.registrarse,
			"2": self.jugar,
			"3": self.salir
		}
		MenuInicial.cargarJugadores(self)
	def cargarJugadores(self):
		for jugador in self.datos:
			jug = Jugador(jugador["nombre"],jugador["contrasena"],jugador["dinero"],jugador["progradex"],jugador["medallas"],jugador["equipo"],jugador["prograbolas"],jugador["ubicacion"],jugador["gymsinfo"])
			jug.programonclass()
			jug.agregarPrograbola()
			self.jugadores.append(jug)

	def modificar_datos(self):
		jsonReader.dictToJson("player.json",self.datos)
	def actualizar_datos(self,jugador):
		for jug in self.datos:
			if jug.get("name")==jugador.nombre:
				self.datos.remove(jug)
				self.datos.append(jugador.di)
	def salir(self):
		print("Gracias por jugar esta PROGRAMON")
		sys.exit(0)

	def displayMenu(self):
		print("""
Menu:
	1: Registrarse
	2: Jugar
	3: Salir
    """)

	def run(self):
		while True:
			self.displayMenu()
			eleccion = input("Ingrese Opcion :")
			accion = self.opciones.get(eleccion)
			if accion:
				accion()
			else:
				print("{0} no es una opcion valida".format(eleccion))

	def registrarse(self):
		nom = inputCorrecto2("Ingrese nombre de usuario :")
		if len(self.jugadores)==0:
				cont = inputCorrecto2("Ingrese contraseña :")
				din = int(1000)
				b = Jugador(nom,cont,din,[[],[]],[],[],[1,1,1,1,1,1,1,1,1,1],0,[])
				p=inputCorrecto("Que programon desea? Charmander ( 1 ), Squirtle ( 2 ) o Bulbasaur ( 3 ) :",1,2,3,3)
				pok=eleccionProgramon(p)
				for pro in jprogramones:
					if pro.get("name")==pok:
						pok=pro.get("id")
				programon = {"id":pok,"level":5,"win":0,"loss":0,"history":[[],[]]}
				b.agregarEquipo(programon)
				b.agregarPrograbola()
				self.jugadores.append(b)
				self.datos.append(b.di)
				MenuInicial.modificar_datos(self)
		else:
			c=0		
			for nombres in self.jugadores:
				if nom != nombres.nombre:
					c=c+1
					if c==len(self.jugadores):
						cont = inputCorrecto2("Ingrese Contraseña :")
						din = 1000
						b = Jugador(nom,cont,din,[[],[]],[],[],[1,1,1,1,1,1,1,1,1,1],0,[])
						p=inputCorrecto("Que programon desea? Charmander ( 1 ), Squirtle ( 2 ) o Bulbasaur ( 3 )",1,2,3,3)
						pok=eleccionProgramon(p)
						for pro in jprogramones:
							if pro.get("name")==pok:
								pok=pro.get("id")
						programon = {"id":pok,"level":5,"win":0,"loss":0,"history":[[],[]]}
						b.agregarEquipo(programon)
						b.agregarPrograbola()
						self.jugadores.append(b)
						self.datos.append(b.di)
						c=c+10
						MenuInicial.modificar_datos(self)

	def jugar(self):
		nom = inputCorrecto2("Ingrese nombre del jugador :")
		for jugador in self.jugadores:
			if nom == jugador.nombre:
				cont= inputCorrecto2("Ingrese su contraseña :")
				if cont == jugador.contraseña:
					self.mapa.agregarJugadorMapa(jugador,jugador.gymsInfo)
					mon=inputCorrecto("Desea moverse ( 1 ) o consultar ( 0 ) :",1,1,0,0)
					if mon ==1:
						while True:
							b=self.mover(jugador)
							if b=="a":
								break
							elif b%4!=0:
								E=self.enHierba(jugador.ubicacion)
								if E != None:
									b=Batalla(jugador,E)
									b.combate()
									jugador.actualizajugador()
									MenuInicial.actualizar_datos(self,jugador)
									MenuInicial.modificar_datos(self)
									c=inputCorrecto("\nDesea moverse de nuevo ( 1 ) o salir ( 0 )?",1,0,0,0)
									if c==0:
										break
							else:
								self.enCiudad(jugador)
								c=inputCorrecto("\nDesea moverse de nuevo ( 1 ) o salir ( 0 )?",1,0,0,0)
								if c==0:
									break
					elif mon ==0:
						con = inputCorrecto("Que desea consultar: ( 1 ) Batalla por programon, ( 2 ) ranking programon o ( 3 ) datos jugador :",1,2,3,3)
						if con==1:
							print("Programones del Jugador")
							lista=[]
							for p in jugador.equipo:
								lista.append(p)
							for j in jugador.prograbolas:
								if j!=1:
									lista.append(j)
							for i,prog in enumerate(lista):
								print(i,sacarNombre(prog.get("id"))+" "+str(prog.get("name")))
							eq=inputCorrecto3("Numero Programon en equipo a cambiar :",0,len(lista)-1)
							print(lista[eq].get("history"))
						if con ==2:
							lista=[]
							for p in jugador.equipo:
								lista.append(p)
							for j in jugador.prograbolas:
								if j!=1:
									lista.append(j)
							lista2=[]
							b=0
							for k in lista:
								if k.get("win")+k.get("loss")>=10:
									if b==0:
										lista2.append(k)
										b=1
									elif b==1:
										a=0
										while a<len(lista2):
											if k.get("win")-k.get("loss")>=lista2[a].get("win")-lista2[a].get("loss") and a==0:
												lista2.insert(a,k)
												a=a+1
											if a==len(lista2)-1:
												lista2.append(k)
							a=0
							for i,pro in enumerate(lista2):
								a=a+1
								if a<=10:
									print(i+1,sacarNombre(pro.get("id")))


	def enHierba(self,ubicacion):
		hier = self.mapa.orden[ubicacion]
		num= (ubicacion%4)+(4*(ubicacion//4))
		print("ESTAS EN HIERBA {}".format(num))
		b= hier.generarProgramon()
		if b==0:
			print("NO HAY NADA")
			return None 
		else:
			E=Entrenador()
			E.agregarEquipoE(b)
			print("ENFRENTAS A UN PROGRAMON, NIVEL {}".format(E.equipoclass[0].nivel))
			return E


	def enCiudad(self,jugador):
		ciu=self.mapa.orden[jugador.ubicacion]
		print("ESTAS EN CIUDAD {}".format(ciu.nombre))
		while True:
			decision = inputCorrecto("Que desea hacer ir tienda ( 1 ), ir gimnasio ( 2 ), ir centro programon ( 3 ) o salir de ciudad ( 4 )?? :",1,2,3,4)
			if decision ==1:
				ciu.tienda.comprar(jugador)
				MenuInicial.actualizar_datos(self,jugador)
				MenuInicial.modificar_datos(self)
			if decision==2:
				while True:
					gym=ciu.gimnasio
					a=inputCorrecto("\nEsta en el gimnasio desea combatir ( 1 ) o no ( 0 )? :",1,0,0,0)
					if a == 1:
						if len(gym.entrenadores)!=0:
							for e in gym.entrenadores:
								print("{} con {} programones".format(e.nombre,len(e.equipoclass)))
							eleccion=inputCorrecto2("Nombre del entrenador que desea enfrentar? (ingrese correctamente el nombre, considerando puntos y mayusculas) :")
							for en in gym.entrenadores:
								contador=1
								if eleccion == en.nombre and contador==1:
									b=Batalla(jugador,en)
									resultado=b.combate()
									if resultado==0:
										break
									elif resultado==1:
										print("DERROTASTE A {}".format(en.nombre))
										gym.entrenadores.remove(en)
										gym.entrenadoresDerrotados.append(en)
										dic=gym.entrenadorDerrotado(en)
										for gims in jugador.gymsInfo:
											if gims.get("city")==dic.get("city"):
												jugador.gymsInfo.remove(gims)
										jugador.gymsInfo.append(dic)
										MenuInicial.actualizar_datos(self,jugador)
										MenuInicial.modificar_datos(self)
										contador=2
						elif len(gym.entrenadores)==0:
							print("Peleas contra el lider {}".format(gym.lider[0].nombre))
							ba=Batalla(jugador,gym.lider[0])
							resul=ba.combate()
							if resul==1:
								print("GANASTE EL GIMNASIO")
								gym.liderDerrotado.append(gym.lider[0])
								gym.lider.remove(gym.lider[0])
								dic=gym.entrenadorDerrotado(gym.liderDerrotado[0])
								for gims in jugador.gymsInfo:
									if gims.get("city")==dic.get("city"):
										jugador.gymsInfo.remove(gims)
								jugador.gymsInfo.append(dic)
								MenuInicial.actualizar_datos(self,jugador)
								MenuInicial.modificar_datos(self)
								break
					elif a==0:
						break
			if decision==3:
				ciu.centro.ingresar_PC(jugador)
				MenuInicial.actualizar_datos(self,jugador)
				MenuInicial.modificar_datos(self)
				break
			if decision==4:
				print("Saliste del gimnasio")
				break




	def mover (self,jugador):
		nom = str(jugador.nombre)
		dirc = inputCorrecto("\nDesea avanzar ( 1 ) o retroceder ( 0 ) o volver a Menu Principal ( 2 ):",1,1,2,0)
		if dirc == 1:
			self.mapa.orden[jugador.ubicacion].jugadores.remove(jugador)
			self.mapa.orden[jugador.ubicacion+1].jugadores.append(jugador)
			jugador.ubicacion=jugador.ubicacion+1
			for celda in self.datos:
				if celda["nombre"]==nom:
					celda["ubicacion"]=celda["ubicacion"]+1
			MenuInicial.modificar_datos(self)
			self.mapa.mostrarMapa(jugador.ubicacion)
			return (jugador.ubicacion)

		elif dirc==0:
			self.mapa.orden[jugador.ubicacion].jugadores.remove(jugador)
			self.mapa.orden[jugador.ubicacion-1].jugadores.append(jugador)
			jugador.ubicacion=jugador.ubicacion-1
			for celda in self.datos:
				if celda["nombre"]==nom:
					celda["ubicacion"]=celda["ubicacion"]-1
			MenuInicial.modificar_datos(self)
			self.mapa.mostrarMapa(jugador.ubicacion)
			return (jugador.ubicacion)
		elif dirc==2:
			return "a"

def eleccionProgramon(num):
	if num==1:
		a="Charmander"
		return a
	elif num==2:
		b="Squirtle"
		return b
	elif num==3:
		c="Bulbasaur"
		return c
def datosJugador(jugador):
	pass

print(arch)
MenuInicial(arch).run()

