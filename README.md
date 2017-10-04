# Home Power Usage monitor
Code for a Raspberry Pi sampling your home's power usage with a current clamp, sending the data over MQTT.

## How to install
We assume you have a Raspberry Pi with a standard Raspbian install.

`git clone` this repository in your Pi user's home directory, **or** download a zip and extract it to the home directory. The content should be available under `/home/pi/home-power-usage/`.

Install Apache web server:
`sudo apt-get install apache2.0`

Copy the contents of `/home/pi/home-power-usage/website` to `/var/www/`. After doing this you should see a webpage when going to your Pi's IP address in a browser on another computer on the same network.

Install the *Adafruit Python ADS1x15* library on your Pi.

Run the software by executing `/home/pi/home-power-usage/startup.01`.

## TODO

Create your own Clodu MQTT account and replace all usernames and passwords in this software with your own.
