# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# file name: active_buzzer.py
# version: 1.0
# author: Neal Shen
# ------------------------------------------------------------------
import RPi.GPIO as GPIO
import time
makerobo_BuzzerPin = 11    # active buzzer pin


# gpio inilization
def makerobo_setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(makerobo_BuzzerPin, GPIO.OUT)
    GPIO.output(makerobo_BuzzerPin, GPIO.HIGH) # set buzzer high level, disable buzzer

# enable buzzer
def makerobo_buzzer_on():
    GPIO.output(makerobo_BuzzerPin, GPIO.LOW) # set buzzer low level, enable buzzer


# disable buzzer
def makerobo_buzzer_off():
    GPIO.output(makerobo_BuzzerPin, GPIO.HIGH) # set buzzer high level, disable buzzer


# control buzzer
def makerobo_beep(x):
    makerobo_buzzer_on()    # enable buzzer control
    time.sleep(x)
    makerobo_buzzer_off()   # disable buzzer control
    time.sleep(x)


# loop function
def makerobo_loop():
    while True:
        makerobo_beep(0.5)  # delay time 500ms


# release source
def makerobo_destroy():
    GPIO.output(makerobo_BuzzerPin, GPIO.HIGH)
    GPIO.cleanup()


if __name__ == '__main__':
    makerobo_setup()
    try:
        makerobo_loop()
    except KeyboardInterrupt:
        makerobo_destroy()