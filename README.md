
```bash
sudo apt-get install python-picamera
pip install virtualenv
sudo /usr/bin/easy_install virtualenv
virtaulenv venv
source venv/bin/activate
pip install picamera
sudo raspi-config #enable camera
sudo pip install hcsr04sensor
reboot
hcsr04.py -t 17 -e 27
```
