import picamera
from time import sleep

with picamera.PiCamera() as camera:
    camera.resolution = (1280, 720)
    camera.framerate = 30
    # Wait for the automatic gain control to settle
    sleep(2)
    # Now fix the values
    camera.shutter_speed = camera.exposure_speed
    camera.exposure_mode = 'off'
    g = camera.awb_gains
    camera.awb_mode = 'off'
    camera.awb_gains = g
    camera.contrast = 100
    picamera.color.Color('green')
    print('cheese green')
    camera.capture('/home/pi/image_g.jpg')
    print('cheese red')
    camera.capture('/home/pi/image_r.jpg')
    print('done')
