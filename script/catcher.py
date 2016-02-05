#!/usr/bin/python

import sys
import urllib
import time
import color_markup_string as cms
from isAGirl import *


firstTime = True
while True:

	##Apertura file##
	myfile = open("log.html","a")
	data = open("data","a")
	##------------##

	#print '-----------|',(time.strftime("%H:%M:%S %d/%m/%y")),'|-----------'                             
	myfile.write('-----------|'+(time.strftime("%H:%M:%S %d/%m/%y"))+'|-----------<br>')

	sock = urllib.urlopen("http://moodlevolta.ictvalleumbra.it/") 

	lista = []
	while True:
		line = sock.readline().replace(' ','')
		#print line
	
		if line == '':
			break
		else:
			lista.append(line)
			#print "Aggiunto"
        nomi = []
        tempo = []
	for line in lista:
		#print line
		if line[0:20] == '<liclass="listentry"':
			#print line
			inizio = line.rindex('16')+4 #trova l'ultimo 16 e aggiunge 4 posizioni, per rendere il uttto graficamente piu' bello
			fine = line.rindex('a')-1    #trova l'ultima a e  toglie una posizione, stessa cosa di prima		
		    
                        nomi.append(line[inizio:fine])
			
			inizioT = line.index('title="')+7
			fineT = line.index('<img')-2
			
			tempo.append(line[inizioT:fineT])
    	#print len(nomi)
	i = 0
        for nome in nomi:
            
            inizioStr = "<font>"
            fineStr = "</font>"            
	    
	    #print len(sys.argv)
		
	    if len(sys.argv) > 1:
		ricerca = sys.argv[1].upper()
	    else:
		ricerca = "1R"	    

            if nome.find(ricerca)>0:
                inizioStr = "<font color=\"red\">"
                fineStr = "</font>"
	    elif isAGirl(nome):
		#print isAGirl(nome)
		inizioStr = "<font color=\"green\">"
		fineStr = "</font>"
            
	    if nome.find("d.") > 0:
                inizioStr = "<font color=\"blue\">"
                fineStr = "</font>"
	    
            tab = "\t\t\t"
	    if len(nome) > 32:
		tab = "\t"
	    elif len(nome) >= 25:
		tab = "\t\t"
	    elif len(nome) < 16:
		tab = "\t\t\t\t"
          
            #print cms.color(inizioStr+nome+fineStr)+tab+tempo[i]
            #print tempo[i]
	   
	    myfile.write(inizioStr+nome+fineStr+"<br>")
	    i = i+1 
	    if nome.find("RobertoMancino")>0:
		continue
	    else:
            	data.write(nome[1:-1]+"\n")
	
	#print len(nomi)	
	if firstTime == False:
		if len(nomi) > 0:	
			toPrint = []
			for nome in nomi:
				if nome.find("d.") > 0:		
					#print nome
					aggiungi = True
					for conf in old:
					#conf.stampa()
				   		if nome == conf:
					    		aggiungi = False
					    		break
					    #print aggiungi      
				    	if aggiungi == True:
				       		toPrint.append(nome[1:-1])
			exitList = []
			for vecchio in old:
				if vecchio.find("d.") > 0:
					#print vecchio
					add = True
					for confronto in nomi:
						if vecchio == confronto:
							add = False
							break
					if add == True:
						exitList.append(vecchio[1:-1])
			loginout = open("loginout","a")
			for o in toPrint:
				loginout.write("d.;"+o.replace('d.','')+";0;"+(time.strftime("%H:%M:%S %d/%m/%y"))+"\n")
			for exit in exitList:
				loginout.write("d.;"+exit.replace('d.','')+";1;"+(oldTime)+"\n")
			old = nomi
			oldTime = time.strftime("%H:%M:%S %d/%m/%y")	
	else:
		old = nomi	
		oldTime = time.strftime("%H:%M:%S %d/%m/%y")
		loginout = open("loginout","a")
		for a in old:
			if a.find("d.") > 0:
				loginout.write("d.;"+a[1:-1].replace('d.','')+";0;"+(time.strftime("%H:%M:%S %d/%m/%y"))+"\n")
		firstTime = False

	#print "-------------------------------------------"
	myfile.write("<hr>")
	
	##Chiusura file##
	myfile.close()
	data.close()
    	loginout.close()
	sock.close()
	##-------------##
	time.sleep(120) #2 minuti, ogni quanto moodle aggiorna le persone online
                                        

#print htmlSource


