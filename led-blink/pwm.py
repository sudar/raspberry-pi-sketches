#!/usr/bin/env python

'''
Control the brightness of a LED from Raspberry Pi
Refer to led-blink.png for circuit

Author: Sudar - http://hardwarefun.com
License: BEERWARE ;)
'''
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

p = GPIO.PWM(12, 50)  # channel=12 frequency=50Hz
p.start(0)

try:
    while True:
        for dc in range(0, 101, 5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(100, -1, -5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
finally:
    p.stop()
    GPIO.cleanup()
