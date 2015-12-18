#!/usr/bin/python

def isAGirl(nome):
	nomiMaschili = ["LUCA","GIANLUCA","MATTIA","NICOLA","ANDREA","ELIA","ENEA"]
	numeri = ["1","2","3","4","5"] #il numero della classe es 1R
	stampa = True
	for i in numeri:
		#print i	
		if nome.find(i) > 0:
			#print nome.find(i),i
			conf = nome.find(i)
			nome = nome[1:conf]
			#print nome
			
			for maschio in nomiMaschili:
				#print maschio
				if nome == maschio:
					stampa = False
			if stampa and nome[conf-2] == "A":
				return True
			else:
				return False	
		
def isAGirlOnlyN(nome):
    	nomiMaschili = ["LUCA","GIANLUCA","MATTIA","NICOLA","ANDREA","ELIA","ENEA"]
    	stampa = True
	for maschio in nomiMaschili:
        	#print maschio
        	if nome == maschio:
            		stampa = False
    	if stampa and nome[-1] == "A":
        	return True
    	else:
        	return False	
"""
a = ">ELIA2AINF_BERNACCIA<"
if isAGirl(a):
	print "G"
else:
	print "B"

"""
