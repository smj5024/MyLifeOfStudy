# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# file name: DuleColorLED.py
# version: 1.0
# author: Neal Shen
# ------------------------------------------------------------------

import RPi.GPIO as GPIO
import time
colors = [0xff0000, 0x00ff00, 0x0000ff, 0xffff00, 0xff00ff, 0x00ffff]
makerobo_pins = (11, 12, 13)                # pin


# initial program
def makerobo_setup(RGBpin):
    global pins
    global p_R, p_G, p_B
    pins = {'pin_R': RGBpin[0], 'pin_G': RGBpin[1], 'pin_B': RGBpin[2]}
    GPIO.setmode(GPIO.BOARD)                # pyshical interface for board
    GPIO.setwarnings(False)                 # filter warnings
    for i in pins:
        GPIO.setup(pins[i], GPIO.OUT)       # set pin as out mode
        GPIO.output(pins[i], GPIO.LOW)      # set pin as low volat
    # to same lightness need different volats for different color
    p_R = GPIO.PWM(pins['pin_R'], 2000)     # set frequency is 2kHz
    p_G = GPIO.PWM(pins['pin_G'], 1999)     # set frequency is 1999Hz
    p_B = GPIO.PWM(pins['pin_B'], 5000)     # set frequency is 5kHz

    # close LED
    p_R.start(0)
    p_G.start(0)
    p_B.start(0)


# map makerobo_pwm
def makerobo_pwm_map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


# close all LED
def makerobo_off():
    GPIO.setmode(GPIO.BOARD)            # pyshical interface for board
    for i in pins:
        GPIO.setup(pins[i], GPIO.OUT)   # set pin as out mode
        GPIO.output(pins[i], GPIO.LOW)  # set pin as low volat


# set color
def makerobo_set_color(col):    # col == 0x112233
    r_val = (col & 0xff0000) >> 16
    g_val = (col & 0x00ff00) >> 8
    b_val = (col & 0x0000ff) >> 0
    # 0-255 --> 0-100
    r_val = makerobo_pwm_map(r_val, 0, 255, 0, 100)
    g_val = makerobo_pwm_map(g_val, 0, 255, 0, 100)
    b_val = makerobo_pwm_map(b_val, 0, 255, 0, 100)

    p_R.ChangeDutyCycle(100-r_val)      # change duty cycle
    p_G.ChangeDutyCycle(100-g_val)      # change duty cycle
    p_B.ChangeDutyCycle(100-b_val)      # change duty cycle


def makerobo_loop():
    while True:
        for col in colors:
            makerobo_set_color(col)     # set color
            time.sleep(1)               # delay time 1s


def makerobo_destroy():
    p_G.stop()
    p_R.stop()
    p_B.stop()
    makerobo_off()      # close all led
    GPIO.cleanup()      # release sources


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        makerobo_setup(makerobo_pins)   # initial setting
        makerobo_loop()
    except KeyboardInterrupt:           # press the CTRL+C, release sources
        makerobo_destroy()
