import csv
import RPi.GPIO as GPIO
import time
from ultrasonicsensor import distance(GPIO_TRIGGER, GPIO_ECHO)

#GPIO mode (board/BCM)
GPIO.setmode(GPIO.BCM)

#GPIO pins
GPIO_TRIGGER_FRONT = 17
GPIO_ECHO_FRONT = 18
GPIO_TRIGGER_LEFT = 27
GPIO_ECHO_LEFT = 22
GPIO_TRIGGER_RIGHT = 23
GPIO_ECHO_RIGHT = 24
GPIO_TRIGGER_BACK = 5
GPIO_ECHO_BACK = 6
GPIO_TRIGGER_BOTTOM = 13
GPIO_ECHO_BOTTOM = 19

#Direction of the PPIO-pins (IN/OUT)
GPIO.setup(GPIO_TRIGGER_FRONT, GPIO.OUT)
GPIO.setup(GPIO_ECHO_FRONT, GPIO.IN)
GPIO.setup(GPIO_TRIGGER_LEFT, GPIO.OUT)
GPIO.setup(GPIO_ECHO_LEFT, GPIO.IN)
GPIO.setup(GPIO_TRIGGER_RIGHT, GPIO.OUT)
GPIO.setup(GPIO_ECHO_RIGHT, GPIO.IN)
GPIO.setup(GPIO_TRIGGER_BACK, GPIO.OUT)
GPIO.setup(GPIO_ECHO_BACK, GPIO.IN)
GPIO.setup(GPIO_TRIGGER_BOTTOM, GPIO.OUT)
GPIO.setup(GPIO_ECHO_BOTTOM, GPIO.IN)

while True:
    line = [distance(GPIO_TRIGGER_FRONT, GPIO_ECHO_FRONT),distance(GPIO_TRIGGER_LEFT, GPIO_ECHO_LEFT),distance(GPIO_TRIGGER_RIGHT, GPIO_ECHO_RIGHT),distance(GPIO_TRIGGER_BACK, GPIO_ECHO_BACK),distance(GPIO_TRIGGER_BOTTOM, GPIO_ECHO_BOTTOM)]
    with open(distance.csv, "wb") as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            for line in data:
                writer.writerow(line)
