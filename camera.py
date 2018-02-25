import picamera
from time import sleep
import numpy as np

def detect_red(camera):
    # saving the picture to an in-program stream rather than a file
    stream = io.BytesIO()

    #scale_down = 6
    red = False

    # capture into stream
    camera.capture(stream, format='jpeg', use_video_port=True)
    # convert image into numpy array
    data = np.fromstring(stream.getvalue(), dtype=np.uint8)

    print(data)
    # # turn the array into a cv2 image
    # img = cv2.imdecode(data, 1)

    # # Resizing the image, blur the image and convert it to HSV values for better recognition
    # # img = cv2.resize(img, (len(img[0]) / scale_down, len(img) / scale_down))
    # # img = cv2.GaussianBlur(img, (5,5), 0)
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # #Defining the red color range and calculating if these values lie in the range
    # red_lower = np.array([0, 150, 0], np.uint8)
    # red_upper = np.array([5, 255, 255], np.uint8)
    # red_binary = cv2.inRange(img, red_lower, red_upper)

    # # Dilates the red space, making it larger
    # dilation = np.ones((15, 15), "uint8")
    # red_binary = cv2.dilate(red_binary, dilation)

    # contours, _ = cv2.findContours(red_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # if not contours == []:
    #     if not red:
    #         red = True
    #         print "Red surface detected!"
    # else:
    #     print "No red surface  detected."

    # red_image.dtype='uint8'
    # cv2.imwrite('image_{}.png'.format(time.Now()), red_image)

    # return red


with picamera.PiCamera() as camera:
    camera.resolution = (320, 240)
    camera.framerate = 30
    # Wait for the automatic gain control to settle
    sleep(2)
    # Now fix the values
    camera.shutter_speed = camera.exposure_speed
    camera.exposure_mode = 'off'
    g = camera.awb_gains
    camera.awb_mode = 'off'
    camera.awb_gains = g
    
    for _ in '.'*10:
        detect_red(camera)
        sleep(1)
