#!/usr/bin/python

import urllib
import time

print '-----------|',(time.strftime("%H:%M:%S")),'|-----------'                             

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


for line in lista:
	#print line
	if line[0:20] == '<liclass="listentry"':
		inizio = line.rindex('16')+4 #trova l'ultimo 16 e aggiunge 4 posizioni, per rendere il uttto graficamente piu' bello
		fine = line.rindex('a')-1    #trova l'ultima a e  toglie una posizione, stessa cosa di prima
		print line[inizio:fine]
print "----------------------------------"
sock.close()                                        
#print htmlSource

