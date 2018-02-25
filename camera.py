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

def get_image():
    output = np.empty((320*240*3), dtype=np.uint8)
    camera.capture(output, 'rgb')
    return  output.reshape(240, 320, 3)

def red_matrix(image_matrix):
    r = np.empty(320*240*3)
    r =  r.reshape(240, 320, 3)

    r[:,:] = np.squeeze(image_matrix[:,:,0])
    r[r < treshold] = 0

    return r

def green_matrix(image_matrix):
    g = np.empty(320*240*3)
    g =  g.reshape(240, 320, 3)

    g[:,:] = np.squeeze(image_matrix[:,:,1])
    g[r < treshold] = 0

    return g


def fallout_location(camera):
    output = get_image()

    r = red_matrix(output)
    g = green_matrix(output)
    
    matrix_diff = r-g
    #eliminate white and see where red dominates above green
    
    red_domination = argmax([sum(matrix_diff[:80]), sum(matrix_diff[80:160]), sum(matrix_diff[160:240])])

    # fallout_location_g = argmin([sum(g[:80]), sum(g[80:160]), sum(g[160:240])])
    # fallout_location_r = argmax([sum(r[:80]), sum(r[80:160]), sum(r[160:240])])

    return red_domination


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
        
        init_image_state = get_image()
    	for _ in '.'*20:
            print(init_image_state - get_image())
            print(detect_red(camera))
            sleep(1)
