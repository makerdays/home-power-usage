# startup01.sh
#!/bin/sh
sleep 15

# Start
sudo python /home/pi/home-power-usage/sample_and_publish/app1.py &
/usr/bin/python /home/pi/home-power-usage/sample_and_publish/Classifyer.py &

