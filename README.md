# Py-FindViola
Script in Python che analizza le persone online su Moodle ( Prima o poi ti troverò)

# start.sh
File principale che avvia l'operazione di scansione di moodle, attende un KeyboardInterrupt, poi crea la cartella "classi", nel caso non fosse presente, ed infine avvia il file di analisi.

# script/catcher.py
Script che ogni 2 minuti fa una chiamata a moodle e stampa a video le persone online.<br>
L'output presenta diversi colori che rappresentano le seguenti categorie di persone:<br>
* ROSSO: persone appartenenti alla classe 1Q
* VERDE: donne
* BLU: docenti

Questo script genera 2 file:
* data: che contiene tutti i nomi degli studenti
* log: simula la schermata del terminale

# scritp/analyzer.py
Questo script prende i nomi presenti nel file data, li divide per classi e li stampa nei relativi file dentro la cartella "classi"

#script/isAGirl.py
E' una funzione che permette di distinguere il sesso di una persona in base al nome.<br>
Viene invocata nel file script/catcher.py
