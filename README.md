# Py-FindViola
Script in Python che analizza le persone online su Moodle ( Prima o poi ti troverò)

# Run
`./start.sh`

# start.sh
File principale che controlla se la cartella classi esiste (in caso contrario la crea), lancia `notADeamon.sh` in background che avvia e controlla l'operazione di scansione di moodle, `catcher.py`, ed infine fa prartire il file di analisi, `analyzer.py` ogni 30 minuti.

#script/notADeamon.sh
Script che controlla ogni ora se il file catcher.py è in esecuzione, se non è così lo avvia in una nuova finestra di terminale.

# script/catcher.py
Script che ogni 2 minuti fa una chiamata a moodle e stampa a video le persone online.<br>
L'output presenta diversi colori che rappresentano le seguenti categorie di persone:<br>
* ROSSO: persone appartenenti alla classe 1Q
* VERDE: donne
* BLU: docenti

Questo script genera 2 file:
* data: che contiene tutti i nomi degli studenti
* log: simula la schermata del terminale
* loginout: file formattato in CSV dove vi sono riportati gli accessi delle persone di classe docende (`d.`)

# scritp/analyzer.py
Questo script prende i nomi presenti nel file data, li divide per classi e li scrive nei relativi file dentro la cartella "classi"

#script/find.py
Script che permette di cercare una persona per:
* Nome (opzione 0): permette di filtare le persone per nome o per le prime lettere di esso. Funziona solo per gli studenti ad eccezzione di una ricerca per la prima lettera!
* Classe (opzione 1): permette di filtrare le persone per classe. <br><b>N.B.</b> la classe deve essere scritta correttamente!
* Cognome (opzione 2): permette di filtrare le persone per cognome, come Nome.


#script/isAGirl.py
E' una funzione che permette di distinguere il sesso di una persona in base al nome.<br>
Viene invocata nel file script/catcher.py
