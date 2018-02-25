import time
import RPi.GPIO as GPIO


class DroneInterface:

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(36, GPIO.OUT)
        GPIO.setup(37, GPIO.OUT)
        GPIO.setup(38, GPIO.OUT)
        GPIO.setup(40, GPIO.OUT)
        GPIO.setup(32, GPIO.OUT)
        self.arm = GPIO.PWM(32, 50)
        self.throttle = GPIO.PWM(36, 50)
        self.yaw = GPIO.PWM(40, 50)
        self.roll = GPIO.PWM(38, 50)
        self.pitch = GPIO.PWM(37, 50)


    def start(self):
        print("STARTING")
        self.arm.start(0)
        for dc in range(0, 101, 5):
            self.arm.ChangeDutyCycle(dc)
            time.sleep(0.1)
    
    def stop(self):
        print("STOPPING")
        for dc in range(100, -1, -5):
            self.arm.ChangeDutyCycle(dc)
            time.sleep(0.1)
        self.arm.stop()
            
    def lift_off():
        print("LIFTING OFF")
        self.throttle.start(0)
        for dc in range(0, 101, 5):
            self.throttle.ChangeDutyCycle(dc)
            time.sleep(0.1)
        time.sleep(2)
        for dc in range(100, -1, -5):
            self.throttle.ChangeDutyCycle(dc)
            time.sleep(0.1)

    def move_forward():
        print("MOVING FORWARD")
        self.pitch.start(0)
        for dc in range(0, 26, 5):
            self.pitch.ChangeDutyCycle(dc)
        time.sleep(5)
        for dc in range(25, -1, -5):
            self.pitch.ChangeDutyCycle(dc)

    def rotate_90_left():
        print("ROTATING 90 LEFT")
        # self.yaw.start(0)


    def rotate_90_right():
        print("ROTATINg 90 RIGHT")

    def __exit__(self, exc_type, exc_value, traceback):
        GPIO.cleanup()

