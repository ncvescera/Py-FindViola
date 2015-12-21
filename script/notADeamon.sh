while :
do
	psOn=`ps -A |grep catcher.py`
	if [ !$psOn ]
		then
			gnome-terminal -e  ./catcher.py
	fi
	sleep 1800
done
