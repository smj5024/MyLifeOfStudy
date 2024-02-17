# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# file name: joystick_PS2.py
# version: 1.0
# author: Neal Shen
# ------------------------------------------------------------------
import PCF8591 as ADC
import time

# pcf8591 analog address setup
def makerobo_setup():
    ADC.setup(0x48)
    global makerobo_state
    
# direction judge function
def makerobo_direction():
    state = ['home', 'up', 'down', 'left', 'right', 'pressed']
    # direction status information
    i = 0
    if ADC.read(0) <= 30:
        i = 1					# up
    if ADC.read(0) >= 225:
        i = 2					# down
    if ADC.read(1) >= 225:
        i = 4					# left
    if ADC.read(1) <= 30:
        i = 3					# right
    if ADC.read(2) == 0 and ADC.read(1) == 128:
        i = 5					# pressed
    # initial position
    if ADC.read(0) - 125 < 15 and ADC.read(0) - 125 > -15 and ADC.read(1) - 125 < 15 and ADC.read(1) - 125 > -15 and ADC.read(2) == 255:
        i = 0
    return state[i]				# return state
        
# loop function
def makerobo_loop():
    makerobo_status = ''			# status is null
    while True:
        makerobo_tmp = makerobo_direction()	# callback direction judge function
        if makerobo_tmp != None and makerobo_tmp != makerobo_status:
            print(makerobo_tmp)
            makerobo_status = makerobo_tmp

# release source
def makerobo_destroy():
    pass


if __name__ == '__main__':
    makerobo_setup()
    try:
        makerobo_loop()
    except KeyboardInterrupt:
        makerobo_destroy()