#!/usr/bin/python

from ClassePersona import *

def findName(nome):
	pass
def findClass(src):
	strOpen = "../classi/"+src
	try:
		myfile = open(strOpen,"r")
		text = myfile.read()
		print text
	except IOError:
		print "Errore:("
	

def findSurname(cognome):#usare tolower sulle stringhe di confronto
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
	#findClass(src)
	strOpen = "../classi/"+src
	myfile = open(strOpen,"r")
	text = myfile.read()
	print text
elif valore == 2:
	src = raw_input("Inserici il cognome: ")
	findSurname(src)
else:
	print "Funzione Errata!"

