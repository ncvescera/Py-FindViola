#!/usr/bin/python

"""
	print line.find('class="block_online_users  block"')
	if line.count('class="block_online_users  block"'):	
	#if line == "<div id=\"inst71\" class=\"block_online_users  block\" role=\"complementary\" data-block=\"online_users\" data-instanceid=\"71\" aria-labelledby=\"instance-71-header\" data-dockable=\"1\">":
		print line
"""	
"""
while exit:
	htmlSource = sock.readline()  
	print htmlSource 
	if htmlSource == "</html>":
		exit = False
"""
"""
	if htmlSource[0:49] == '<div id="inst71" class="block_online_users  block"':
		print htmlSource
	elif htmlSource == '<span id="sb-3" class="skip-block-to"></span>':
		break
	"""



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

