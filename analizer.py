#!/usr/bin/python

class Persona:
    def __init__(self,nome,classe,cognome):
        self.nome = nome
        self.classe = classe
        self.cognome = cognome
    def stampa(self):
        string = self.nome+" "+self.classe+" "+self.cognome
        print  string
        return string+"\n"

myfile = open("data","r")

nomi = []
while True:
    nomi.append(myfile.readline())
    if myfile.readline() == '':
        break
        
dizionario = ["1","2","3","4","5"]
persone = []
for nome in nomi:
    #print nome[:-1]
    for confronto in dizionario:
        if nome.find(confronto)>0:
            numero = nome.find(confronto)
            name = nome[:numero]
            classe = nome[numero:nome.find("_")]
            cognome = nome[nome.find("_")+1:-1]
            alunno = Persona(name,classe,cognome)
            persone.append(alunno)
            #print name+"-"+classe+"-"+cognome
            #alunno.stampa()
        elif nome.find("d.") > 0:
            numero = nome.find("d.")
            name = nome[:numero]
            classe = "MAGISTER"
            cognome = nome[nome.find(".")+1:-1]
            #print name+"-"+classe+"-"+cognome
            docente = Persona(name,classe,cognome)
            persone.append(docente)
            #docente.stampa()
            break
dictClassi = ["3CINF","1SPGS","5AGR","1T"]
for cl in dictClassi:
    qLista = []
    for persona in persone:
        if persona.classe == cl:
            qLista.append(persona)
    leng = len(qLista)
    temp = qLista
    news = []
    news.append(qLista[0])
    for i in range(1,leng):
        aggiungi = True
        for conf in news:
            if qLista[i].cognome == conf.cognome:
                aggiungi = False
                break
        #print aggiungi
        """    
        for te in temp:
            #aggiungi = False
            #print aggiungi
            if qLista[i].cognome == te.cognome:
                aggiungi = False
                break
        """        
        if aggiungi == True:
            news.append(qLista[i])
    cinf3 = open(cl,"w")   
    for persona in news:
        cinf3.write(persona.stampa())
