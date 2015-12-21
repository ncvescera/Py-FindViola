echo "Capturing ..."
cd script
##Controllo esistenza cartella classi##
if [ ! -d ../classi ]
	then
		mkdir ../classi
fi
##FineControllo##

./notADeamon.sh & #avvia in background lo script
#gnome-terminal -e 
#./catcher.py
while :
do
	echo "Waiting ..."
	sleep 3600	
	echo "Analizing ..."

	./analyzer.py
	echo "DONE"
done
