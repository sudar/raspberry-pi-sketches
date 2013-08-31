#!/usr/bin/env python

import RPi.GPIO as GPIO  
from time import sleep     # this lets us have a time delay (see line 12)  

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)    # set pin as input (button)  
GPIO.setup(12, GPIO.OUT)   # set pin as an output (LED)  
  
try:  
    while True:            # this will carry on until you hit CTRL+C  
        if GPIO.input(11): # if pin 11 == 1  
            print "Button is on"  
            GPIO.output(12, 1)         # set port/pin value to 1/HIGH/True  
        else:  
            #print "Button is off"  
            GPIO.output(12, 0)         # set port/pin value to 0/LOW/False  
        sleep(0.1)         # wait 0.1 seconds  
  
finally:                   # this block will run no matter how the try block exits  
    GPIO.cleanup()         # clean up after yourself  

