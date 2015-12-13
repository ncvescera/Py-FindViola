#!/usr/bin/python
import operator
from ClassePersona import *

myfile = open("data","r")

nomi = []
totale = 0 #conta il numero di persone totali
while True:
    n = myfile.readline()
    if n == '':
        break

    nomi.append(n)
    #print nomi[i]
    #i = i+1
    
myfile.close()       


persone = []
for nome in nomi:
	persone.append((Persona.parse(nome)))

for cl in Persona.dictClassi:
    qLista = []
    for persona in persone:
	
        if persona.classe == cl:
            qLista.append(persona)
	    
    leng = len(qLista)
    if len(qLista) == 0:
        continue
    news = []
    news.append(qLista[0])
    for i in range(1,leng):
        aggiungi = True
        for conf in news:
	    #conf.stampa()
            if qLista[i].cognome == conf.cognome:
                aggiungi = False
                break
        #print aggiungi      
        if aggiungi == True:
            news.append(qLista[i])
    news.sort(key = operator.attrgetter('cognome')) # ordina per cognome crescente
    cinf3 = open("../classi/"+cl,"w")   
    for persona in news:
        cinf3.write(persona.stampa())
	totale = totale+1
    cinf3.write(str(len(news))+"\n")
    cinf3.close()
print "--------------------------------------------\nNumero di persone totali: ",totale

