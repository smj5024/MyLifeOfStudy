# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# file name: rain_detector.py
# version: 1.0
# author: Neal Shen
# ------------------------------------------------------------------
import PCF8591 as ADC
import RPi.GPIO as GPIO
import time
import math
makerobo_DO = 17		# rain detector pin
GPIO.setmode(GPIO.BCM)	# set BCM pin as GPIO

# pcf8591 analog address setup
def makerobo_setup():
    ADC.setup(0x48)
    GPIO.setup(makerobo_DO, GPIO.IN)
    
# print rain detector module's information
def makerobo_Print(x):
    if x == 1:
        print('')
        print('		*************************')
        print('		* makerobo Not Raining *')
        print('		*************************')
        print('')
    if x == 0:
        print('')
        print('		*************************')
        print('		* makerobo Raining!! *')
        print('		*************************')
        print('')
        
# loop function
def makerobo_loop():
    makerobo_status = 1			# rain detector's status
    while True:
        print(ADC.read(0))	# read AIN0 value
        makerobo_tmp = GPIO.input(makerobo_DO)
        # read digital I/O, read rain detector 's DO
        if makerobo_tmp != makerobo_status:
            makerobo_Print(makerobo_tmp)
            makerobo_status = makerobo_tmp
        time.sleep(0.2) # delay 200ms

# release source
def makerobo_destroy():
    ADC.write(0)	# aout output is 0


if __name__ == '__main__':
    try:
        makerobo_setup()
        makerobo_loop()
    except KeyboardInterrupt:
        pass