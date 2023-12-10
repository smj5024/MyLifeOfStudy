# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# file name: Relay.py
# version: 1.0
# author: Neal Shen
# ------------------------------------------------------------------

import RPi.GPIO as GPIO
import time
makerobo_RelayPin = 11                              # define relay pin as pin11


# initial program
def makerobo_setup():
    GPIO.setmode(GPIO.BOARD)                        # physical interface for board
    GPIO.setwarnings(False)                         # filter warnings
    GPIO.setup(makerobo_RelayPin, GPIO.OUT)         # set pin as out mode
    GPIO.output(makerobo_RelayPin, GPIO.LOW)        # close relay


def makerobo_loop():
    while True:
        # cut relay
        GPIO.output(makerobo_RelayPin, GPIO.HIGH)
        time.sleep(1)
        # close relay
        GPIO.output(makerobo_RelayPin, GPIO.LOW)
        time.sleep(1)


def makerobo_destroy():
    GPIO.output(makerobo_RelayPin, GPIO.LOW)        # close relay
    GPIO.cleanup()                                  # release sources


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    makerobo_setup()  # initial setting
    try:
        makerobo_loop()
    except KeyboardInterrupt:           # press the CTRL+C, release sources
        makerobo_destroy()
