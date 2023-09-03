# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# file name: Laser.py
# version: 1.0
# author: Neal Shen
# ------------------------------------------------------------------

import RPi.GPIO as GPIO
import time
makerobo_LaserPin = 11                              # define relay pin as pin11


# initial program
def makerobo_setup():
    GPIO.setmode(GPIO.BOARD)                        # physical interface for board
    GPIO.setwarnings(False)                         # filter warnings
    GPIO.setup(makerobo_LaserPin, GPIO.OUT)         # set pin as out mode
    GPIO.output(makerobo_LaserPin, GPIO.LOW)        # close laser


def makerobo_loop():
    while True:
        # open laser
        GPIO.output(makerobo_LaserPin, GPIO.HIGH)
        time.sleep(0.5)
        # close laser
        GPIO.output(makerobo_LaserPin, GPIO.LOW)
        time.sleep(0.5)
        # GPIO.setup(makerobo_LaserPin, GPIO.IN)      # set pin as in mode
        # res = GPIO.input(makerobo_LaserPin)         # read pin signal
        # if res != 0:
        #     print('read pin signal: ', res)


def makerobo_destroy():
    # GPIO.setup(makerobo_LaserPin, GPIO.OUT)         # set pin as out mode
    GPIO.output(makerobo_LaserPin, GPIO.LOW)        # close laser
    GPIO.cleanup()                                  # release sources


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    makerobo_setup()  # initial setting
    GPIO.output(makerobo_LaserPin, GPIO.HIGH)
    try:
        makerobo_loop()
    except KeyboardInterrupt:           # press the CTRL+C, release sources
        makerobo_destroy()