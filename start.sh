echo "Capturing ..."
cd script
##Controllo esistenza cartella classi##
if [ ! -d ../classi ]
	then
		mkdir ../classi
fi
##FineControllo##

./analyzingLoop.sh & #avvia in background lo script
#gnome-terminal -e 
#./catcher.py
while :
do
        psOn=`ps -a |grep python`
        if [[ !$psOn ]]; then
                        ./catcher.py
        fi
        sleep 1800
done

