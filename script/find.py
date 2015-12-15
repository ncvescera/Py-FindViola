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
			if persona.nome.find(nome) >= 0:
				lista.append(persona)
		else:
			break

	if len(lista) <= 0:
		print "Errore, nome inesistente :("
		return

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
	totale = 0
	for a in news:
		a.stampa()
		totale = totale+1
	print "-----------------------------\nPersone Trovate: ",totale
			
def findClass(classe):
	classe = classe.upper()
	#strOpen = "../classi/"+src.upper()
	try:
		myfile = open("../classi/"+classe,"r")
		
	except IOError:
		print "Errore, classe inesistente :("
		return #return non ritorna niente, e' = a return none
	text = myfile.read()
	print text

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
		if linea == '':
			print "Errore, cognome inesistente :("
			return 
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

