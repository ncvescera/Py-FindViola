echo "Capturing ..."
cd script
./catcher.py
echo "Analizing ..."
if [ ! -d ../classi ]
	then
		mkdir ../classi
fi
./analyzer.py
echo "DONE"

