class Persona:
    dictClassi = ["1A","1B","1C","1D","1E","1F","1G","1H","1L","1M","1N","1P","1Q","1R","1S","1SPGS","1T","2AC","2AGR","2AET","2AINF","2AM","2BC","2BET","2BGR","2BINF","2BM","2CET","2CINF","2CM","2DET","3AC","3BC","4AC","4BC","5AC","3AINF","3BINF","3CINF","4AINF","4BINF","4CINF","5AINF","5BINF","3AGR","3BGR","4AGR","4BGR","5AGR","5BGR","3AT","4AT","5AT","3BT","4BT","5BT","3CT","3AE","4AE","5AE","3BE","4BE","3AM","4AM","5AM","3BM","4BM","5BM","3CM","4CM","3DM","MAGISTER"]
    def __init__(self,nome,classe,cognome):
        self.nome = nome
        self.classe = classe
        self.cognome = cognome
    def stampa(self):
        strPrint = self.nome+" "+self.classe+" "+self.cognome # nome+classe+cognome
	strReturn = self.nome+" "+self.cognome # nome+cognome
        print  "[+] ",strPrint
        return strReturn+"\n"
    
    @staticmethod
    def confrontoPerCognome(lista):
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
        return news
    
    @staticmethod
    def confrontoPerNome(lista):
        news = []
        news.append(lista[0])
        for i in range(1,len(lista)):
            aggiungi = True
            for conf in news:
                #conf.stampa()
                if lista[i].nome == conf.nome:
                    aggiungi = False
                    break
                    #print aggiungi      
            if aggiungi == True:
                news.append(lista[i])
        return news
    
    @staticmethod
    def parse(nome):
	dizionario = ["1","2","3","4","5"]
	#print nome[:-1]
	for confronto in dizionario:
		if nome.find(confronto)>0:
			numero = nome.find(confronto)
	    		name = nome[:numero]
			classe = nome[numero:nome.find("_")]
			cognome = nome[nome.find("_")+1:-1]
		    	#alunno = 
			#alunno.stampa()
		    	return Persona(name,classe,cognome)
		    	#persone.append(alunno)
		    	#print name+"-"+classe+"-"+cognome
		    	
		elif nome.find("d.") > 0:
		   	numero = nome.find("d.")
		    	name = nome[:numero]
		    	classe = "MAGISTER"
		    	cognome = nome[nome.find(".")+1:-1]
		    	#print name+"-"+classe+"-"+cognome
		    	docente = Persona(name,classe,cognome)
		    	#persone.append(docente)
		    	return docente
		    	#docente.stampa()
		    	break
		elif nome.find("Utente") > 0:
			name = "Amministratore"
			classe = "ADMIN"
			cognome = "Utente"
			admin = Persona(name,classe,cognome)
			return admin
        
        