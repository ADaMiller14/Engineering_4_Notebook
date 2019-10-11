import RPi.GPIO as GPIO
from gpiozero import LED
from time import sleep

led = LED(6)
led2 = LED(17)

while True:
    led.off()
    led2.on()
    sleep(.5)
    led.on()
    led2.off()
    sleep(.5)
