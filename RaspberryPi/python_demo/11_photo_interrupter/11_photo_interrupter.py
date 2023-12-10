# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# file name: photo_interrupter.py
# version: 1.0
# author: Neal Shen
# ------------------------------------------------------------------
import RPi.GPIO as GPIO
makerobo_LBPin	 	= 11    # photo interrupter pin
makerobo_Rpin   	= 12    # red led pin
makerobo_Gpin   	= 13    # green led pin


# gpio inilization
def makerobo_setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(makerobo_Rpin, GPIO.OUT)
    GPIO.setup(makerobo_Gpin, GPIO.OUT)
    GPIO.setup(makerobo_LBPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    # set BtnPin mode is input, pull up to high(3.3V)
    # interupt function
    GPIO.add_event_detect(makerobo_LBPin, GPIO.BOTH, callback=makerobo_detect, bouncetime=200)


def double_color(x):
    if x == 0:
        GPIO.output(makerobo_Rpin, 1)
        GPIO.output(makerobo_Gpin, 0)
    if x == 1:
        GPIO.output(makerobo_Rpin, 0)
        GPIO.output(makerobo_Gpin, 1)


def makerobo_print(x):
    if x == 0:
        print('******************************************')
        print('* makerobo Light was blocked! *')
        print('******************************************')


# interrupt function
def makerobo_detect(chn):
    double_color(GPIO.input(makerobo_LBPin))
    makerobo_print(GPIO.input(makerobo_LBPin))


# loop function
def makerobo_loop():
    while True:
        pass


# release source
def makerobo_destroy():
    GPIO.output(makerobo_Rpin, GPIO.HIGH)
    GPIO.output(makerobo_Gpin, GPIO.HIGH)
    GPIO.cleanup()


if __name__ == '__main__':
    makerobo_setup()
    try:
        makerobo_loop()
    except KeyboardInterrupt:
        makerobo_destroy()