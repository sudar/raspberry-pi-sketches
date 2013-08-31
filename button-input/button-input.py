#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        if GPIO.input(11):
            print "Button is on"
        else:
            print "Button is off"
        time.sleep(0.1)

finally:
    GPIO.cleanup()
