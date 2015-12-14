#!/usr/bin/python

import urllib
import time
import color_markup_string as cms
from isAGirl import *

myfile = open("log","a")
data = open("data","a")

while True:
	print '-----------|',(time.strftime("%H:%M:%S")),'|-----------'                             
	myfile.write('-----------|'+(time.strftime("%H:%M:%S"))+'|-----------\n')

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
    
        for nome in nomi:
            
            inizioStr = "<white>"
            fineStr = "</white>"
	    
            if nome.find("1R")>0:
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
            data.write(nome[1:-1]+"\n")

	print "----------------------------------"
	myfile.write("----------------------------------\n")

	sock.close()
	time.sleep(120) #5 minuti, ogni quanto moodle aggiorna le persone online
                                        
myfile.close()
#print htmlSource


