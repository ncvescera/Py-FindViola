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
* <b><i>ROSSO</i></b>: persone appartenenti alla classe 1Q
* <b><i>VERDE</i></b>: donne
* <b><i>BLU</i></b>: docenti

Questo script genera 2 file:
* <b><i>data</i></b>: che contiene tutti i nomi degli studenti
* <b><i>log</i></b>: simula la schermata del terminale
* <b><i>loginout</i></b>: file formattato in CSV dove vi sono riportati gli accessi delle persone di classe docende (`d.`)

# scritp/analyzer.py
Questo script prende i nomi presenti nel file data, li divide per classi e li scrive nei relativi file dentro la cartella "classi"

#script/find.py
Script che permette di cercare una persona per:
* <b><i>Nome</i></b> (opzione 0): permette di filtare le persone per nome o per le prime lettere di esso. Funziona solo per gli studenti ad eccezzione di una ricerca per la prima lettera!
* <b><i>Classe</i></b> (opzione 1): permette di filtrare le persone per classe. <br><b>N.B.</b> la classe deve essere scritta correttamente!
* <b><i>Cognome</i></b> (opzione 2): permette di filtrare le persone per cognome, come Nome.


#script/isAGirl.py
E' una funzione che permette di distinguere il sesso di una persona in base al nome.<br>
Viene invocata nel file script/catcher.py

#script/ClassePersona.py
Questo file contiene la clsee Persona che è formata da:
##Attributi
* dictClassi: dizionario con tutte le classi dell'istituto
* nome: nome della persona
* classe: classe a cui appartiene la persona
* cognome: cognome della persona


##Metodi
* __init__: costruttore della clasee
* stampa: metodo per stamapare a video i suoi attribti (ad eccezione di dictClassi) e ritorna una stringa con essi
* stampaColor: metodo che distingue il sesso della persona e stampa i suoi attributi a video colorandoli
* confrontoPerCognome: metodo static che permette di confrontare per cognome le persone di una lista tra di loro 
* confrontoPerNome: stessa cosa di confrontoPerCognome solo con il nome
* parse: metodo che data in input una stringa del seguente formato `>NOMECLASSE_COGNOME<` la trasforma in un oggetto Persona e lo ritorna
