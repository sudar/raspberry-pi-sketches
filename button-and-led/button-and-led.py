#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12, GPIO.OUT)

try:
    while True:
        if GPIO.input(11):
            print "Button is on"
            GPIO.output(12, 1)
        else:
            GPIO.output(12, 0)
        time.sleep(0.1)

finally:
    GPIO.cleanup()
