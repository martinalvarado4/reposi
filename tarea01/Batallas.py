### Batallas
import jsonReader
import random
import sys
from Tarea01 import Programon , Prograbola, Progradex, PCBastian, Jugador, Entrenador, Gimnasio, Ciudad, Hierba , Mapa
from Tarea01 import jprogramones, jprogramonMoves, jroutes, jtypes, jmoveCategories, jgyms, jjugadoresEjemplo
from Tarea01 import inputCorrecto, inputCorrecto2
class Batalla:
	def __init__(self,jugador,entrenador):
		self.jugador = jugador
		self.entrenador = entrenador
	def elegirProgramon(self):
		for pro in self.jugador.equipoclass:
			print("-Tienes a {}".format(pro.nombre))
		nom = input("Cual programon eliges (ingrese nombre correctamente)? :")
		for programon in self.jugador.equipoclass:
			if nom == programon.nombre:
				self.jugador.equipoclass.remove(programon)
				print("Te quedan {} programones en prograbolas \n".format(len(self.jugador.equipoclass)))
				programon.estadisticas(1)
				return programon
	def eligeEntrenador(self):
		for prok in self.entrenador.equipoclass:
			if self.entrenador.tipo!="":
				print("El entrenador tiene a {}".format(prok.nombre))
			else:
				print("Enfrentas al programon salvaje {}".format(prok.nombre))
		if len(self.entrenador.equipoclass)>0:
			programon=self.entrenador.equipoclass[0]
			self.entrenador.equipoclass.remove(programon)
			programon.estadisticas(1)
			return programon
	def turno(self,programonj,programone):
		b=0
		c=1
		if programonj.velocidad>programone.velocidad:
			print("Tu atacas primero")
			return b
		else:
			print("{} ataca primero".format(programone.nombre))
			return c

	def ataqueJugador(self,programonj):
		print(programonj.moves)
		ataq=input("Elige ataque :")
		for mov in programonj.moves:
			if ataq == mov:
				ataque=Ataque(ataq)
				if len(programonj.ataquesBatalla)==0:
					ataque.pp=ataque.pp-1
					programonj.ataquesBatalla.append(ataque)
					print("{} es tu primer ataque y le quedan {} pp".format(ataque.nombre, ataque.pp))
					return ataque
				elif len(programonj.ataquesBatalla)!=0:
					a=1
					for ataques in programonj.ataquesBatalla:
						if ataques.nombre==ataque.nombre:
							a=a+1
							ataques.pp=ataques.pp-1
							print("{} le quedan {} pp".format(ataques.nombre, ataques.pp))
							return ataques
					if a==1:
							ataque.pp=ataque.pp-1
							programonj.ataquesBatalla.append(ataque)
							print("Primera vez que usas {}, le quedan {} pp".format(ataque.nombre, ataque.pp))
							return ataque

	def ataqueEntrenador(self,programone):
		c=random.randint(0,len(programone.moves)-1)
		ataque = programone.moves[c]
		for mov in programone.moves:
			if ataque == mov:
				ataq=Ataque(ataque)
				if len(programone.ataquesBatalla)==0:
					ataq.pp=ataq.pp -1
					programone.ataquesBatalla.append(ataq)
					print("Te atacaron por primera vez con {} y le quedan {} pp".format(ataq.nombre, ataq.pp))
					return ataq
				elif len(programone.ataquesBatalla)!=0:
					a=1
					for ataques in programone.ataquesBatalla:
						if ataques.nombre==ataq.nombre:
							a=a+1
							ataques.pp=ataques.pp-1
							print("De nuevo te atacaron con {} y le quedan {} pp".format(ataques.nombre, ataques.pp))
							return ataques
					if a==1:
							ataq.pp=ataq.pp-1
							programone.ataquesBatalla.append(ataq)
							print("Te atacaron con {} y le quedan {}".format(ataq.nombre, ataq.pp))
							return ataq

	def daño(self,programon1,programon2,ataque):
		nivel=programon1.nivel
		esp=0
		for especiales in jmoveCategories["special_moves"]:
			if ataque.tipo== especiales:
				esp=1
		if esp==0:
			ata=programon1.ataque
			defe=programon2.defensa
		elif esp==1:
			ata=programon1.ataque_especial
			defe=programon2.defensa_especial
		base=ataque.power
		if ataque.tipo==programon1.tipo:
			stab=1.5
		else:
			stab=1
		try :
			tipo=jtypes[ataque.tipo][programon2.tipo]
		except:
			tipo=1
		p=random.randint(0,256)
		t=programon1.velocidad / 2
		if p<=t:
			critico=2
		else:
			critico=1
		rand=(random.randint(85,100))/100
		modificador=float(stab)*tipo*critico*float(rand)
		daño=round((((2*nivel+10)/250)*(ata/defe)*base+2)*modificador)
		return daño
	def probAcierto(self,ataque):
		b=1
		c=0
		prob = random.randint(0,100)
		if prob <= (ataque.precision)*100:
			return b
		else:
			return c

	def combate(self):
		while True:
			s=inputCorrecto("Estas en batalla deseas continuar ( 1 ) o retirarte ( 0 ) :",1,0,0,0)
			print(" ")
			if s==0:
				return 0
				break
			print("A LUCHAR!! \n")
			J=Batalla.elegirProgramon(self)
			E=Batalla.eligeEntrenador(self)
			dex=self.jugador.progradexclass
			dex.revisarBatalla(E)
			print("Combates a {}".format(E.nombre))
			DerrotadosE=[]
			DerrotadosJ=[]
			T=Batalla.turno(self,J,E)
			if T==0:
				while True:
					if self.entrenador.tipo=="":
						p=inputCorrecto("Desea atrapar pokemon si ( 1 ) o no ( 0 ) ? :",1,0,0,0)
						if p==1:
							if self.jugador.prograbolas[0]==1:
								b = self.jugador.prograbolasclass[0].atrapar(E)
								if b==1:
									self.jugador.prograbolas.pop(0)
									self.jugador.prograbolas.append(self.jugador.prograbolasclass[0].capturado[0])
									self.jugador.prograbolasclass.append(Prograbola(self.jugador.prograbolasclass[0].capturado[0]))
									self.jugador.prograbolasclass.pop(0)
									dex.revisarCapturado(E)
									self.jugador.equipoclass.append(J)
									break
							else:
								print("NO TIENES PROGRABOLAS LIBRES\n")
						else:
							print(" ")
					AJ=Batalla.ataqueJugador(self,J)
					dañoJ=Batalla.daño(self,J,E,AJ)
					prob=Batalla.probAcierto(self,AJ)
					E.HP=E.HP-dañoJ*prob
					print("Inflingiste {} daño y {} queda con {}/{} de vida\n".format(dañoJ*prob, E.nombre, E.HP, E.vida))
					if E.HP<=0:
						DerrotadosE.append(E)
						J.finBatalla(0,E,1,self.entrenador.tipo)
						self.jugador.equipoclass.append(J)
						print("Derrotaste a {}".format(E.nombre))
						break
					AE=Batalla.ataqueEntrenador(self,E)
					dañoE=Batalla.daño(self,E,J,AE)
					prob=Batalla.probAcierto(self,AE)
					J.HP=J.HP-dañoE*prob
					print("{} hizo {} daño y {} queda con {}/{} de vida\n".format(E.nombre, dañoE*prob, J.nombre, J.HP, J.vida))
					if J.HP<=0:
						J.finBatalla(0,E,0,self.entrenador.tipo)
						DerrotadosJ.append(J)
						self.entrenador.equipoclass.append(E)
						print("Haz sido derrotado")
						break
			else:
				while True:
					if self.entrenador.tipo=="":
						p=inputCorrecto("\nDesea atrapar pokemon si ( 1 ) o no ( 0 ) ? :",1,0,0,0)
						if p ==1:
							if self.jugador.prograbolas[0]==1:
								b = self.jugador.prograbolasclass[0].atrapar(E)
								if b==1:
									self.jugador.prograbolas.pop(0)
									self.jugador.prograbolas.append(self.jugador.prograbolasclass[0].capturado[0])
									self.jugador.prograbolasclass.append(Prograbola(self.jugador.prograbolasclass[0].capturado[0]))
									self.jugador.prograbolasclass.pop(0)
									dex.revisarCapturado(E)
									self.jugador.equipoclass.append(J)
									break
							else:
								print("NO TIENES PROGRABOLAS LIBRES\n")
						else:
							print(" ")
					AE=Batalla.ataqueEntrenador(self,E)
					dañoE=Batalla.daño(self,E,J,AE)
					prob=Batalla.probAcierto(self,AE)
					J.HP=J.HP-dañoE*prob
					print("{} hizo {} daño y {} queda con {}/{} de vida\n".format(E.nombre, dañoE*prob, J.nombre, J.HP, J.vida))
					if J.HP<=0:
						J.finBatalla(0,E,0,self.entrenador.tipo)
						DerrotadosJ.append(J)
						self.entrenador.equipoclass.append(E)
						print("Haz sido derrotado")
						break
					AJ=Batalla.ataqueJugador(self,J)
					dañoJ=Batalla.daño(self,J,E,AJ)
					prob=Batalla.probAcierto(self,AJ)
					E.HP=E.HP-dañoJ*prob
					print("Inflingiste {} daño y {} queda con {}/{} de vida\n".format(dañoJ*prob, E.nombre, E.HP,E.vida))
					if E.HP<=0:
						J.finBatalla(0,E,1,self.entrenador.tipo)
						DerrotadosE.append(E)
						self.jugador.equipoclass.append(J)
						print("Derrotaste a {}".format(E.nombre))
						break
			if 0==len(self.entrenador.equipoclass):
				print("GENIAL, Ganaste")
				a=1
				if self.entrenador.tipo=="leader":
					self.jugador.medallas.append("@ medalla de {} en {}".format(self.entrenador.nombre,self.entrenador.city))
				for programon in DerrotadosJ:
					programon.finBatalla(1,2,2,2)
					self.jugador.equipoclass.append(programon)
				for pro in self.jugador.equipoclass:
					if pro == J:
						J.finBatalla(1,2,2,2)
				return a
				break
			if 0==len(self.jugador.equipoclass):
				print(":( Fuiste  Derrotado")
				a=0
				for programon in DerrotadosJ:
					self.jugador.equipoclass.append(programon)
				return a
				break

class Ataque:
	last_id=0
	def __init__(self,nombre):
		self.pp = 0
		self.tipo = ""
		self.nombre = nombre
		self.precision = 0
		self.power = 0
		self.last_id=Ataque.last_id
		Ataque.armar(self)
		Ataque.last_id+=1
	def armar(self):
		for moves in jprogramonMoves:
			if self.nombre==moves["name"]:
				self.pp=int(moves["pp"])
				self.tipo=str(moves["type"])
				self.precision=int(moves["accuracy"])
				self.power=int(moves["power"])
"""
for pro in jprogramones:
	if pro.get("name")=="Dodrio":
		print(pro)
lista=[]
lista2=[]
lista3=[]
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
for pr in lista2:
	if pr.get("id")==84:
		print(pr)
		"""
#pokj= Programon(10,2)
#pokj2=Programon(12,6)
#poke=Programon(7,0)
#pokj.estadisticas(1)
#poke.estadisticas(1)
#pokj2.estadisticas(1)
#print(pokj.moves)
#print(pokj2.moves)
#print(poke.moves)
#j=Jugador("carlos","dedo",1000,[[],[]],[],[],[Prograbola()],2)
#e=Entrenador("pedro","santiago")
#j.agregarEquipo(pokj)
#e.agregarEquipoE(poke)
#j.agregarEquipo(pokj2)
#b=Batalla(j,e)
#print(b.combate())
#print(j.equipoclass[1].nombre)
#print(j.equipoclass[1].nivel)
#print(j.progradex.visto_batalla)
#print(j.progradex.visto_capturados)
#print(j.prograbolas[0].capturado[0].nombre)
### PELEA LIDER
#pokj= Programon(10,2)
#pokj2=Programon(12,6)
#poke2=Programon(7,0)
#poke= Programon(25,4)
#pokj.estadisticas(1)
#poke.estadisticas(1)
#pokj2.estadisticas(1)
#poke2.estadisticas(1)
#print(pokj.moves)
#print(poke.moves)
#j=Jugador("carlos","dedo",1000,[[],[]],[],[],[Prograbola()],2)
#e=Entrenador("pedro","santiago","leader")
#j.agregarEquipo(pokj)
#e.agregarEquipoE(poke)
#j.agregarEquipo(pokj2)
#e.agregarEquipoE(poke2)
#b=Batalla(j,e)
#print(b.combate())


#f=b.elegirProgramon()
#=b.eligeEntrenador()
#print(jprogramones[0])
#print(jprogramonMoves[0])
#print(jtypes.get("water"))
#print(jmoveCategories)