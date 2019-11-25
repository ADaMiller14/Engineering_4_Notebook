from picamera import PiCamera
from time import sleep

myCamera = PiCamera()

x = -5
myCamera.start_preview()
for effect in myCamera.IMAGE_EFFECTS:
    myCamera.image_effect = effect
    myCamera.annotate_text = "Effect = %s" % effect
    sleep(5)
    if x < 5 and x > 0:
        myCamera.capture('/home/pi/Desktop/image%s.jpg' % x)
    if x < 6:
        x = x + 1
myCamera.stop_preview()
