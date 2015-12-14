#!/usr/bin/python

from ClassePersona import *

def findName(nome):
	nome = nome.upper()
	myfile = open("data","r")	
	lista = []
	while True:
		letto = myfile.readline()
		if letto != '':
			persona = Persona.parse(letto)
			if persona.nome == nome:
				lista.append(persona)
		else:
			break
	news = []
	news.append(lista[0])
	for i in range(1,len(lista)):
		aggiungi = True
		for conf in news:
			#conf.stampa()
			if lista[i].cognome == conf.cognome:
				aggiungi = False
				break
			#print aggiungi      
		if aggiungi == True:
			news.append(lista[i])
	for a in news:
		a.stampa()
			
def findClass(classe):
	classe = classe.upper()
	#strOpen = "../classi/"+src.upper()
	try:
		myfile = open("../classi/"+classe,"r")
		text = myfile.read()
		print text
	except IOError:
		print "Errore:("
	

def findSurname(cognome):
   	cognome = cognome.upper()
	myfile = open("data","r")
	while True:
		linea = myfile.readline()
		if linea.find(cognome) > 0:
			#print linea
            		trovato = Persona.parse(linea)
            		trovato.stampa()
			break

print "\tSeleziona il metodo di ricerca"
print "[0] Nome\t[1] Classe\t[2] Cognome"
valore = raw_input(': ')
valore = int(valore)
if valore == 0:
	src = raw_input("Inserici il nome: ")
	findName(src)
elif valore == 1:
	src = raw_input("Inserici la classe: ")
	findClass(src)
elif valore == 2:
	src = raw_input("Inserici il cognome: ")
	findSurname(src)
else:
	print "Funzione Errata!"

