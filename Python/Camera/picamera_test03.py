from picamera import PiCamera
from time import sleep

myCamera = PiCamera()

myCamera.start_preview()
myCamera.start_recording('/home/pi/Desktop/myvid.h264')
sleep(10)
myCamera.stop_recording()
myCamera.stop_preview()
