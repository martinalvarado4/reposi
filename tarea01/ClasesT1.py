## prueba
#### CORREGIR JUGADORES EN MENU E INICIO
#### DEFINIR SOLO EN UNO
import jsonReader
import random
jprogramones = jsonReader.jsonToDict("programones.json")
jprogramonMoves = jsonReader.jsonToDict("programonMoves.json")
jroutes = jsonReader.jsonToDict("routes.json")
jtypes = jsonReader.jsonToDict("types.json")
jmoveCategories = jsonReader.jsonToDict("moveCategories.json")
jgyms = jsonReader.jsonToDict("gyms.json")
jjugadoresEjemplo = jsonReader.jsonToDict("jugadoresEjemplo.json")

class Programon:
	def __init__(self, nivel,iden,win,loss,hist):
		for pro in jprogramones:
			if pro["id"]==iden:
				self.idd = pro["id"]
				self.x=jprogramones.index(pro)
				self.nombre = jprogramones[self.x]["name"]
				self.moves = jprogramones[self.x]["moves"]
				self.tipo = jprogramones[self.x]["type"]
				self.vida = jprogramones[self.x]["hp"]
				self.HP = jprogramones[self.x]["hp"]
				self.velocidad = jprogramones[self.x]["speed"]
				self.ataque = jprogramones[self.x]["attack"]
				self.ataque_especial = jprogramones[self.x]["special_attack"]
				self.defensa = jprogramones[self.x]["defense"]
				self.defensa_especial = jprogramones[self.x]["special_defense"]
				self.nivel = nivel
				self.nivel_evol = jprogramones[self.x].get("evolveLevel")
				self.evoluciona = jprogramones[self.x].get("evolveTo")
				self.ataquesBatalla=[]
				self.ganadas=win
				self.perdidas=loss
				self.Batallas=hist

	def evolucionar(self):
		if self.nivel==self.nivel_evol:
			for programon in jprogramones:
				if programon["id"]==self.evoluciona:
					self.x = jprogramones.index(programon)
					self.idd = jprogramones[self.x]["id"]
					self.nombre = jprogramones[self.x]["name"]
					self.moves = jprogramones[self.x]["moves"]
					self.tipo = jprogramones[self.x]["type"]
					self.vida = jprogramones[self.x]["hp"]
					self.HP = jprogramones[self.x]["hp"]
					self.velocidad = jprogramones[self.x]["speed"]
					self.ataque = jprogramones[self.x]["attack"]
					self.ataque_especial = jprogramones[self.x]["special_attack"]
					self.defensa = jprogramones[self.x]["defense"]
					self.defensa_especial = jprogramones[self.x]["special_defense"]
					self.nivel_evol = jprogramones[self.x].get("evolveLevel")
					self.evoluciona = jprogramones[self.x].get("evolveTo")

	def finBatalla(self , resultadoT,programon,resultadoI,trainer):
		if resultadoT == 1:
			self.nivel = self.nivel + 1
		if resultadoI==1:
			self.ganadas=self.ganadas+1
			self.Batallas[0].append({"trainer":trainer,"result":"victoria","name":programon.nombre})
		if resultadoI==0:
			self.perdidas=self.perdidas+1
			self.Batallas[1].append({"trainer":trainer,"result":"derrota","name":programon.nombre})


	def estadisticas(self,batalla):
		## cuando acanvaza de nivel o es capturado
		### dividri hp por 100
		if batalla==1:
			IV=random.randint(0,15)
			EV=random.randint(0 ,65535)
		self.vida=(((((jprogramones[self.x]["hp"] + IV)*2 + (((EV**(1/2))//1) + 1)/4)*self.nivel)/100)//1)+self.nivel + 10
		self.HP=(((((jprogramones[self.x]["hp"] + IV)*2 + (((EV**(1/2))//1) + 1)/4)*self.nivel)/100)//1)+self.nivel + 10
		self.velocidad=((((((jprogramones[self.x]["speed"])+IV)*2+(((EV**(1/2))//1) + 1)/4)*self.nivel)/100)//1) + 5
		self.ataque=((((((jprogramones[self.x]["attack"])+IV)*2+(((EV**(1/2))//1) + 1)/4)*self.nivel)/100)//1) + 5
		self.ataque_especial=((((((jprogramones[self.x]["special_attack"])+IV)*2+(((EV**(1/2))//1) + 1)/4)*self.nivel)/100)//1) + 5
		self.defensa=((((((jprogramones[self.x]["defense"])+IV)*2+(((EV**(1/2))//1) + 1)/4)*self.nivel)/100)//1) + 5
		self.defensa_especial=((((((jprogramones[self.x]["special_defense"])+IV)*2+(((EV**(1/2))//1) + 1)/4)*self.nivel)/100)//1) + 5


class Prograbola:
	def __init__(self,inn):
		self.capturado = [inn]
	def sacarProgramon (self):
		prog= self.capturado[0]
		return prog
	def atrapar(self,programon):
		capturado = random.randint(0,100)
		prob= (((programon.vida - programon.HP)/programon.vida)*0.8)+0.2
		if capturado <= prob*100:
			a=1
			self.capturado.pop(0)
			self.capturado.append({"id":programon.idd,"level":programon.nivel,"win":programon.ganadas,"loss":programon.perdidas,"history":programon.Batallas})
			print("LO TIENES\n")
			return a
		else:
			b=0
			print("SE ESCAPO\n")
			return b


class Progradex:
	def __init__(self,nombre,visto_batalla,visto_capturados):
		self.nombre_jugador = nombre
		self.visto_batalla = visto_batalla
		self.visto_capturados = visto_capturados
	def revisarBatalla(self,programon):
		a=0
		for visto in self.visto_capturados:
			if visto["name"] == programon.nombre:
				a=1
		for vistob in self.visto_batalla:
			if vistob["name"]==programon.nombre:
				a=1
		if a==0:
			self.visto_batalla.append({"name":programon.nombre,"id":programon.idd})
	def revisarCapturado(self,programon):
		a=0
		for visto in self.visto_capturados:
			if visto.get("name")==programon.nombre:
				self.visto_capturados.remove(visto)
		for vistob in self.visto_batalla:
			if vistob.get("name")==programon.nombre:
				self.visto_batalla.remove(vistob)
		if a ==0:
			self.visto_capturados.append({"name":programon.nombre,"id":programon.idd,"level":programon.nivel})


class PCBastian:
	def __init__(self):
		self.jugador = "jugador"
		self.programonesteam= "jugador.equipo"
		self.programonesprog= "jugador.prograbolas"

	def ingresar_PC (self,jugador):
		self.jugador=jugador
		self.programonesteam= jugador.equipo
		self.programonesprog= jugador.prograbolas
		print("Equipo :")
		for i,prog in enumerate(self.programonesteam):
			print(i,sacarNombre(prog.get("id"))+" "+str(prog.get("level")))
		print("En PC :")
		a=0
		for j,pro in enumerate(self.programonesprog):
			if pro!=1:
				a=a+1
				print(j,sacarNombre(pro.get("id"))+" "+str(pro.get("level")))
		eq=inputCorrecto3("Numero Programon en equipo a cambiar :",0,len(self.programonesteam)-1)
		pr=inputCorrecto3("Numero Programon en PC a cambiar :",(len(self.programonesprog)-a),(len(self.programonesprog)-1))
		self.programonesteam.append(self.programonesprog[pr])
		self.programonesprog.append(self.programonesteam[eq])
		self.programonesteam.pop(eq)
		self.programonesprog.pop(pr)
		jugador.equipoclass=[]
		jugador.prograbolasclass=[]
		jugador.programonclass()
		jugador.agregarPrograbola()


class Jugador:
	last_id = 0
	def __init__(self,nombre,contraseña,dinero,progradex,medallas,equipo,prograbolas,ubicacion,gymInfo):
		self.idd = Jugador.last_id
		self.nombre = nombre
		self.contraseña = contraseña
		self.dinero = dinero
		self.progradexclass = Progradex(nombre,progradex[0],progradex[1])
		self.progradex=[self.progradexclass.visto_batalla,self.progradexclass.visto_capturados]
		self.medallas = medallas
		self.equipoclass= []
		self.equipo = equipo
		self.prograbolas =prograbolas
		self.prograbolasclass = []
		self.ubicacion = ubicacion
		self.gymsInfo= gymInfo
		self.di = {"id":self.idd, "nombre":self.nombre,"contrasena":self.contraseña,"dinero":self.dinero,"progradex":self.progradex,"medallas":self.medallas,"equipo":self.equipo,"prograbolas":self.prograbolas,"ubicacion":self.ubicacion,"gymsinfo":self.gymsInfo}
		Jugador.last_id +=1

	def programonclass(self):
		for programon in self.equipo:
			self.equipoclass.append(Programon(programon.get("level"),programon.get("id"),programon.get("win"),programon.get("loss"),programon.get("history")))
	def agregarPrograbola(self):
		for prograbol in self.prograbolas:
			self.prograbolasclass.append(Prograbola(prograbol))
	def actualizajugador(self):
		for programon in self.equipoclass:
			for prog in self.equipo:
				if programon.idd==prog.get("id"):
					self.equipo.remove(prog)
					if programon.nivel==programon.nivel_evol:
						programon.evolucionar()
					self.equipo.append({"id":programon.idd,"level":programon.nivel,"win":programon.ganadas,"loss":programon.perdidas,"history":programon.Batallas})

	def agregarEquipo(self,programon):
		self.equipo.append(programon)
		self.equipoclass.append(Programon(programon.get("level"),programon.get("id"),programon.get("win"),programon.get("loss"),programon.get("history")))


class Entrenador:
	def __init__(self,nombre="",city="",tipo=""):
		self.nombre = nombre
		self.city =city
		self.equipo = []
		self.equipoclass =[]
		self.tipo = tipo
	def programonclassE(self):
		for programon in self.equipo:
			self.equipoclass.append(Programon(programon.get("level"),programon.get("id")))
	def agregarEquipoE(self,programon):
		self.equipo.append(programon)
		self.equipoclass.append(Programon(programon.get("level"),programon.get("id"),programon.get("win"),programon.get("loss"),programon.get("history")))

class Gimnasio:
	def __init__(self,gym):
		self.gym=gym
		self.nombre=""
		self.idd=""
		self.entrenadores = []
		self.entrenadoresDerrotados = []
		self.lider = []
		self.liderDerrotado=[]
		Gimnasio.generarGym(self)
	def entrenadorDerrotado(self,entrenador):
		lista=[]
		b={"city":self.nombre,"trainers":lista}
		for entre in self.entrenadoresDerrotados:
			lista.append({"name":entre.nombre,"derrotado":True})
		if entrenador.tipo=="leader":
			b={"city":self.nombre,"trainers":lista,"leader":{"name":entrenador.nombre,"derrotado":True}}
		return b

	def generarGym(self):
		if self.gym!=None:
			self.nombre=self.gym.get("city")
			self.idd=self.gym.get("id")
			for entrenador in self.gym.get("trainers"):
				E=Entrenador(entrenador.get("name"),self.nombre,"trainers")
				for pok in entrenador.get("programones"):
					E.agregarEquipoE(pok)
				self.entrenadores.append(E)
			lid=self.gym.get("leader")
			L=Entrenador(lid.get("name"),self.nombre,"leader")
			for pro in lid.get("programones"):
				L.agregarEquipoE(pro)
			self.lider.append(L)

	def modificarGym(self,gymsinfo):
		for gym in gymsinfo:
			if gym.get("city")==self.nombre:
				for trainer in gym.get("trainers"):
					for entrenador in self.entrenadores:
						if trainer.get("name")==entrenador.nombre:
							if trainer.get("derrotado")==True:
								self.entrenadores.remove(entrenador)
								self.entrenadoresDerrotados.append(entrenador)
				if gym.get("leader")!=None:
					if gym.get("leader").get("name")==self.lider[0].nombre:
						if gym.get("leader").get("derrotado")==True:
							self.liderDerrotado.append(self.lider[0])
							self.lider.pop(0)



class Ciudad:
	last_id = 1
	def __init__(self, nombre,gym):
		self.nombre = nombre
		self.idciu = Ciudad.last_id
		self.tienda = Tienda()
		self.centro = PCBastian()
		self.gimnasio = Gimnasio(gym)
		self.jugadores = []
		Ciudad.last_id +=1

class Tienda:
	def __init__(self):
		self.tienda =Prograbola(1)
	def comprar(self,jugador):
		while True:
			com = inputCorrecto("Desea comprar prograbola ( 1 ) o salir ( 2 ) ??",1,2,1,1)
			if com ==1:
				if jugador.dinero>=500:
					jugador.dinero = int(jugador.dinero) - int(500)
					jugador.prograbolasclass.insert(0,Prograbola(1))
					jugador.prograbolas.insert(0,1)
					print("Compraste una prograbola")
				else:
					print("Dinero insuficiente $$")
			if com==2:
				print(" ")
				break


class Hierba:
	num = 1
	def __init__(self,niveles):
		self.nombre = "hierba"
		self.niveles = niveles
		self.probabilidad = 35
		self.jugadores = []
		Hierba.num +=1

	def generarProgramon (self):
		r = random.randint(1,100)
		if r <= self.probabilidad:
			lista=[]
			lista2=[]
			lista3=[]
			niv = random.randint(self.niveles[0] , self.niveles[1])
			idd = random.randint(0,len(jprogramones))
			for pro in jprogramones:
				if type(pro.get("evolveLevel"))!=type(1):
					lista.append(pro)
				else:
					lista2.append(pro)
			for prog in lista2:
				for prog2 in lista2:
					if prog.get("evolveTo")==prog2.get("id"):
						lista2.remove(prog)
						lista3.append(prog)
			programon = {"id":Hierba.revisaProgramon(self,niv,idd,lista,lista2,lista3),"level":niv,"win":0,"loss":0,"history":[[],[]]}
			return programon
		else:
			b=0
			return b
	def revisaProgramon(self,niv,idd,lista,lista2,lista3):
		for pro in lista3:
			if pro.get("id")==idd:
				b=pro
				for prog in lista2:
					if prog.get("id")==b.get("evolveTo"):
						c=prog
						for proga in lista:
							if proga.get("id")==c.get("evolveTo"):
								d=proga
								if niv < b.get("evolveTo"):
									return b.get("id")
								elif c.get("evolveLevel")>niv>b.get("evolveLevel"):
									return c.get("id")
								elif niv>c.get("evolveLevel"):
									return d.get("id")
			elif pro.get("id")!=idd:
				b=pro
				for prog in lista2:
					if prog.get("id")==idd:
						c=prog
						for proga in lista:
							if proga.get("id")==prog.get("evolveTo"):
								d=proga
								if b.get("evolveTo")==c.get("id"):
									if niv <b.get("evolveLevel"):
										return b.get("id")
									elif c.get("evolveLevel")>niv>b.get("evolveLevel"):
										return c.get("id")
									elif niv>c.get("evolveLevel"):
										return d.get("id")
								elif b.get("evolveTo")!=c.get("id"):
									if c.get("evolveLevel")>niv:
										return c.get("id")
									elif niv>c.get("evolveLevel"):
										return d.get("id")
					elif prog.get("id")!=idd:
						c=prog
						for proga in lista:
							if proga.get("id")==idd:
								d=proga
								if d.get("id")==c.get("evolveTo"):
									if c.get("id")==b.get("evolveTo"):
										if niv <b.get("evolveLevel"):
											return b.get("id")
										elif c.get("evolveLevel")>niv>b.get("evolveLevel"):
											return c.get("id")
										elif niv>c.get("evolveLevel"):
											return d.get("id")
									elif c.get("id")!=b.get("evolveTo"):
										if niv<c.get("evolveLevel"):
											return c.get("id")
										elif niv>c.get("evolveLevel"):
											return d.get("id")
								elif d.get("id")!=c.get("evolveTo"):
									return d.get("id")


class Mapa:
	def __init__(self,routes,gyms):
		self.routes = routes
		self.gyms = gyms
		self.orden = []
		Mapa.crearMapa(self)
	def crearMapa(self):
		largo = len(self.routes)
		contador = 1
		for ruta in self.routes:
			num_ruta = ruta["route"]
			niveles = ruta["levels"]
			if contador != largo:
				if contador == num_ruta:
					nom_ciu = ruta["starting_point"]
					gim=None
					for gym in self.gyms:
						if gym["city"]==nom_ciu:
							gim =gym
					self.orden.append(Ciudad(nom_ciu,gim))
					self.orden.append(Hierba(niveles))
					self.orden.append(Hierba(niveles))
					self.orden.append(Hierba(niveles))
					contador +=1


			else :
				if contador == num_ruta:
					nom_ciu_ini = ruta.get("starting_point")
					nom_ciu_fin = ruta.get("destination")
					gim1=None
					for gym in self.gyms:
						if gym["city"]==nom_ciu_ini:
							gim1 =gym
					self.orden.append(Ciudad(nom_ciu_ini,gim1))
					self.orden.append(Hierba(niveles))
					self.orden.append(Hierba(niveles))
					self.orden.append(Hierba(niveles))
					gim2=None
					for gym in self.gyms:
						if gym["city"]==nom_ciu_fin:
							gim2 =gym
					self.orden.append(Ciudad(nom_ciu_fin,gim2))
					contador +=1

	def mostrarMapa(self,pos):
		lista =[]
		for i in range(0, len(self.orden)):
			if i ==0 or (i%4)==0:
				lista.append(self.orden[i].nombre)
			else:
				lista.append("####")
		lista.insert(pos, "X ->")
		print("\n{}\n".format(lista))

	def agregarJugadorMapa(self,jugador,gymsinfo):
		self.orden[jugador.ubicacion].jugadores.append(jugador)
		for ciu in self.orden:
			if self.orden.index(ciu)%4==0:
				ciu.gimnasio.modificarGym(gymsinfo)
def inputCorrecto(pregunta,r1,r2,r3,r4):
	while True:
		try:
			a=int(input(pregunta))
			if a==r1 or a==r2 or a==r3 or a==r4:
				return a
				break
			else:
				print("Numero no valido")
		except:
			print("Valor no valido")
def inputCorrecto2(pregunta):
	while True:
		try:
			a=str(input(pregunta))
			return a
			break
		except:
			print("Argumento no valido")
def sacarNombre(idd):
	for programon in jprogramones:
		if programon.get("id")==idd:
			return programon.get("name")
def inputCorrecto3(pregunta,ran1,ran2):
	while True:
		try:
			a=int(input(pregunta))
			if ran1<=a<=ran2:
				return a
				break
		except:
			print("Valor no esta en rango")