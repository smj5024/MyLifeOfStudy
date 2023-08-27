# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# file name: DuleColorLED.py
# version: 1.0
# author: Neal Shen
# ------------------------------------------------------------------

import RPi.GPIO as GPIO
import time
colors = [0xff00, 0x00ff, 0x0ff0, 0xf00f]
makerobo_pins = (11, 12)                # pin
GPIO.setmode(GPIO.BOARD)                # pyshical interface for board
GPIO.setwarnings(False)                 # filter warnings
GPIO.setup(makerobo_pins, GPIO.OUT)     # set pin as out mode
GPIO.output(makerobo_pins, GPIO.LOW)    # set pin as low volat
p_R = GPIO.PWM(makerobo_pins[0], 2000)  # set frequency is 2kHz
p_G = GPIO.PWM(makerobo_pins[1], 2000)  # set frequency is 2kHz

# close LED
p_R.start(0)
p_G.start(0)


def makerobo_pwm_map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def makerobo_set_color(col):    # col == 0x1122
    r_val = col >> 8
    g_val = col & 0x00ff
    # 0-255 --> 0-100
    r_val = makerobo_pwm_map(r_val, 0, 255, 0, 100)
    g_val = makerobo_pwm_map(g_val, 0, 255, 0, 100)

    p_R.ChangeDutyCycle(r_val)    # change duty cycle
    p_G.ChangeDutyCycle(g_val)    # change duty cycle


def makerobo_loop():
    while True:
        for col in colors:
            makerobo_set_color(col)
            time.sleep(0.5)


def makerobo_destroy():
    p_G.stop()
    p_R.stop()
    GPIO.output(makerobo_pins, GPIO.LOW)
    GPIO.cleanup()      # release sources


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        makerobo_loop()
    except KeyboardInterrupt:   # press the CTRL+C, release sources
        makerobo_destroy()
