#!/usr/bin/python

from ClassePersona import *
import sys

def findName(nome):
	nome = nome.upper()
	myfile = open("data","r")	
	lista = []
	while True:
		letto = myfile.readline()
		if letto != '':
			persona = Persona.parse(letto)
			if persona.nome.find(nome,0,len(nome)) >= 0:
				lista.append(persona)
		else:
			break

	if len(lista) <= 0:
		print "Errore, nome inesistente :("
		return

	news = Persona.confrontoPerCognome(lista)
    
	totale = 0
	for a in news:
		a.stampaColor()
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
        lista = []
	while True:
		linea = myfile.readline()
		if linea != '':
			persona = Persona.parse(linea)
            		if persona.cognome.find(cognome,0,len(cognome)) >= 0:
            			lista.append(persona)
        	else:
			break
    	if len(lista) <= 0:
		print "Errore, cognome inesistente :("
		return 
    	news = Persona.confrontoPerNome(lista)
    	totale = 0
    	for p in news:
        	p.stampaColor()
        	totale = totale+1
    	print "-----------------------------\nPersone Trovate: ",totale

if len(sys.argv) > 1:
    if sys.argv[1] == "-n":
        findName(sys.argv[2])
    elif sys.argv[1] == "-c":
        findClass(sys.argv[2])
    elif sys.argv[1] == "-s":
        findSurname(sys.argv[2])
    else:
        print "Funzione Errata!"
else:

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

