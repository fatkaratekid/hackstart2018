import RPi.GPIO as GPIO
import time

def distance(GPIO_TRIGGER, GPIO_ECHO):
    #set the trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    #set the trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    startTime = time.time()
    stopTime = time.time()

    #save starting starting time
    while GPIO.input(GPIO_ECHO)==0:
        startTime = time.time()

    #save end time
    while GPIO.input(GPIO_ECHO)==1:
        stopTime = time.time()

    #time difference between start and end
    timediff = stopTime - startTime
    #multiply with speed of sound (34300 cm/s) and devide by 2 (two ways back and forth)
    distance = (timediff*34300)/2

    return distance
