# Py-FindViola
Script in Python che analizza le persone online su Moodle ( Prima o poi ti troverò)

# start.sh
File principale che avvia l'operazione di scansione di moodle, attende un KeyboardInterrupt, poi crea la cartella "classi", nel caso non fosse presente, ed infine avvia il file di analisi.

# script/catcher.py
Script che ogni 2 minuti fa una chiamata a moodle e stampa a video le persone online.<br>
L'output presenta diversi colori che rappresentano le seguenti categorie di persone:<br>
* <font color='red'>ROSSO</font>
