#!/usr/bin/python

import sys
import urllib
import time
import color_markup_string as cms
from isAGirl import *


firstTime = True
while True:

	##Apertura file##
	myfile = open("log","a")
	data = open("data","a")
	##------------##

	print '-----------|',(time.strftime("%H:%M:%S %d/%m/%y")),'|-----------'                             
	myfile.write('-----------|'+(time.strftime("%H:%M:%S %d/%m/%y"))+'|-----------\n')

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
	for line in lista:
		#print line
		if line[0:20] == '<liclass="listentry"':
			inizio = line.rindex('16')+4 #trova l'ultimo 16 e aggiunge 4 posizioni, per rendere il uttto graficamente piu' bello
			fine = line.rindex('a')-1    #trova l'ultima a e  toglie una posizione, stessa cosa di prima		
		    
                        nomi.append(line[inizio:fine])
    	#print len(nomi)
        for nome in nomi:
            
            inizioStr = "<white>"
            fineStr = "</white>"            
	    
	    #print len(sys.argv)
		
	    if len(sys.argv) > 1:
		ricerca = sys.argv[1].upper()
	    else:
		ricerca = "1R"	    

            if nome.find(ricerca)>0:
                inizioStr = "<red>"
                fineStr = "</red>"
	    elif isAGirl(nome):
		#print isAGirl(nome)
		inizioStr = "<green>"
		fineStr = "</green>"
            
	    if nome.find("d.") > 0:
                inizioStr = "<blue>"
                fineStr = "</blue>"
		
            print cms.color(inizioStr+nome+fineStr)
            myfile.write(nome+"\n")
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
					aggiungi = True
				    	for conf in old:
					#conf.stampa()
				       		if nome == conf:
					    		aggiungi = False
					    		break
					    #print aggiungi      
				    	if aggiungi == True:
				       		toPrint.append(nome[1:-1])
			loginout = open("loginout","a")
			for o in toPrint:
				loginout.write("d.;"+o.replace('d.','')+";"+(time.strftime("%H:%M:%S %d/%m/%y"))+"\n")
			old = nomi	
	else:
		old = nomi
		loginout = open("loginout","a")
		for a in old:
			if a.find("d.") > 0:
				loginout.write("d.;"+a[1:-1].replace('d.','')+";"+(time.strftime("%H:%M:%S %d/%m/%y"))+"\n")
		firstTime = False

	print "-------------------------------------------"
	myfile.write("-------------------------------------------\n")
	
	##Chiusura file##
	myfile.close()
	data.close()
    	loginout.close()
	sock.close()
	##-------------##
	time.sleep(120) #2 minuti, ogni quanto moodle aggiorna le persone online
                                        

#print htmlSource


