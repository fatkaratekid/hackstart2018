import picamera
import io
from time import sleep
import numpy as np

treshold =  230
snapshot_enabled = False

def detect_red(camera):
    output = np.empty((320*240*3), dtype=np.uint8)
    camera.capture(output, 'rgb')
    output =  output.reshape(240, 320, 3)

    r = np.empty(320*240*3)
    r =  r.reshape(240, 320, 3)
    g = np.copy(r)

    r[:,:,0] = output[:,:,0]
    r[r < treshold] = 0

    g[:,:,1] = output[:,:,1]
    g[g < treshold] = 0
    
    if snapshot_enabled:
         from PIL import Image
         im = Image.fromarray(np.squeeze(r).astype('uint8'), 'RGB')
         im.save("r.jpeg")
         im = Image.fromarray(np.squeeze(g).astype('uint8'), 'RGB')
         im.save("g.jpeg")

    return r.sum() > g.sum()

def fallout_location(camera):
    output = np.empty((320*240*3), dtype=np.uint8)
    camera.capture(output, 'rgb')
    output =  output.reshape(240, 320, 3)

    r = np.empty(320*240*3)
    r =  r.reshape(240, 320, 3)
    g = np.copy(r)

    r[:,:,0] = output[:,:,0]
    r[r < treshold] = 0

    g[:,:,1] = output[:,:,1]
    g[g < treshold] = 0

    fallout_location_g = argmin([sum(g[:80]), sum(g[80:160]), sum(g[160:240])])
    fallout_location_r = argmax([sum(r[:80]), sum(r[80:160]), sum(r[160:240])])
    
    if fallout_location_g == fallout_location_r:
        return fallout_location_r
    else:
        return fallout_location_r

if __name__=="__main__":
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
    
    	for _ in '.'*20:
            print(detect_red(camera))
            sleep(1)
