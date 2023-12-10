# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# file name: vibration_switch.py
# version: 1.0
# author: Neal Shen
# ------------------------------------------------------------------
import RPi.GPIO as GPIO
import time
makerobo_VibratePin = 11    # press vibrate pin
makerobo_Rpin   = 12    # red light pin
makerobo_Gpin   = 13    # green light pin


# gpio inilization
def makerobo_setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(makerobo_Rpin, GPIO.OUT)
    GPIO.setup(makerobo_Gpin, GPIO.OUT)
    GPIO.setup(makerobo_VibratePin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    # set VibratePin mode is input, pull up to high(3.3V)


def double_color(x):
    if x == 0:
        GPIO.output(makerobo_Rpin, 1)
        GPIO.output(makerobo_Gpin, 0)
    if x == 1:
        GPIO.output(makerobo_Rpin, 0)
        GPIO.output(makerobo_Gpin, 1)


def makerobo_print(x):
    global clb_tmp
    if x != clb_tmp:
        if x == 0:
            print('***************')
            print('* makerobo on *')
            print('***************')
        if x == 1:
            print('***************')
            print('* makerobo off*')
            print('***************')
        clb_tmp = x


# loop function
def makerobo_loop():
    clb_state = 0
    while True:
        if GPIO.input(makerobo_VibratePin) == 1:
            clb_state = clb_state + 1
            if clb_state > 1:
                clb_state = 0
            double_color(clb_state)
            makerobo_print(clb_state)
            time.sleep(1)


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