# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# file name: pcf8591.py
# version: 1.0
# author: Neal Shen
# ------------------------------------------------------------------
import PCF8591 as ADC
# pcf8591 analog address setup
def makerobo_setup():
    ADC.setup(0x48)
    
# loop function
def makerobo_loop():
    while True:
        print(ADC.read(0))	# read AIN0 value
        ADC.write(ADC.read(0))	# control LED

# release source
def makerobo_destroy():
    ADC.write(0)	# aout output is 0


if __name__ == '__main__':
    makerobo_setup()
    try:
        makerobo_loop()
    except KeyboardInterrupt:
        makerobo_destroy()