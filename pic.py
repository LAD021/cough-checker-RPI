#-*-coding:utf-8-*-
import config
from picamera import PiCamera
from time import sleep

def getPic():
    camera = PiCamera()

    camera.rotation = config.CAM_ROTATION 
    camera.start_preview()
    for i in range(3):
        print('* Going to capture: {}'.format(3 - i))
        sleep(1)
    camera.capture(config.PIC_OUTPUT_FILENAME)
    camera.stop_preview()

