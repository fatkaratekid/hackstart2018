import time
import RPi.GPIO as GPIO
from ultrasonicsensor import *
from camera import *


#GPIO.setmode(GPIO.BCM)

MAX_VALUE = 100
MIN_VALUE = 50

neutral = 7.2

GPIO.setmode(GPIO.BOARD)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.IN)
GPIO.setup(32, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)

#     self.throttle = GPIO.PWM(36, 50)
#     self.yaw = GPIO.PWM(40, 50)
#     self.roll = GPIO.PWM(38, 50)
#     self.pitch = GPIO.PWM(37, 50)
arm = GPIO.PWM(32, MIN_VALUE)
pitch = GPIO.PWM(37, MIN_VALUE)
yaw = GPIO.PWM(40, MIN_VALUE)
roll = GPIO.PWM(38, MIN_VALUE)
throttle = GPIO.PWM(36, MIN_VALUE)

HOVER_DISTANCE = 70

def _arm():
    print("STARTING")
    #arm = GPIO.PWM(32, MIN_VALUE)
    
    pitch.start(neutral)
    yaw.start(neutral)
    roll.start(neutral) 
    
    throttle.start(4)
   
    time.sleep(2)  

    arm.start(4.5)

    time.sleep(2)
    arm.ChangeDutyCycle(10)

    time.sleep(4)

def wait_for_signal():
    with picamera.PiCamera() as camera:
    	camera.resolution = (320, 240)
    	camera.framerate = 30
    	sleep(2)
    	# Now fix the values
    	camera.shutter_speed = camera.exposure_speed
    	camera.exposure_mode = 'off'
    	g = camera.awb_gains
    	camera.awb_mode = 'off'
    	camera.awb_gains = g
	while True:
	    if not detect_red(camera):
		break

def disarm():
    print("DISARMING")
    arm.ChangeDutyCycle(4)
    time.sleep(3)     
   
def _throttle(dst=None):
    print("THROTTLE")
    print("dst is  "+ str(dst))
    if (dst is None):
    	for dc in range(5, 11, 1):
            throttle.ChangeDutyCycle(dc)
            time.sleep(0.4)
        time.sleep(4)
        for dc in range(10, 8, -1):
            throttle.ChangeDutyCycle(dc)
            time.sleep(0.4)
    else:
	dc = 5
	throttle.ChangeDutyCycle(dc)
        while True:
	    x = distance(33, 35)

	    print("DISTANCE IS " + str(x))
            if x < dst:
		dc += 1
		throttle.ChangeDutyCycle(dc)
	        time.sleep(0.4)
	    else:
		break 

def _pitch():
    print("PITCH")
    for dc in range(5, 11, 1):
        pitch.ChangeDutyCycle(dc)
        time.sleep(0.3)
    time.sleep(3)
    for dc in range(11, 5, -1):
        pitch.ChangeDutyCycle(dc)
        time.sleep(0.3)

def _yaw(factor):
    print("YAW")
    yaw.ChangeDutyCycle(10)
    time.sleep(3 * factor)
    yaw.ChangeDutyCycle(5)

def land():
    print("LANDING")
    dc = 8
    throttle.ChangeDutyCycle(dc)
    while True:
    	x = distance(33, 35)
    	if x < 15:
	    break
    	else:
	    dc -= 0.1
	    throttle.ChangeDutyCycle(dc)
	    time.sleep(0.8)

def _complex():
    _arm()
    wait_for_signal()
    _throttle(HOVER_DISTANCE)
    _yaw(1)
    _pitch()
    _yaw(2)
    _pitch()
    land()
    disarm()

def up_down():
    _arm()
    wait_for_signal()
    _throttle(HOVER_DISTANCE)
    land()
    disarm()



up_down()
#_complex()
