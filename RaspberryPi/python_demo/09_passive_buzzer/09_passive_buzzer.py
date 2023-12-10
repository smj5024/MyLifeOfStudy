# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# file name: passive_buzzer.py
# version: 1.0
# author: Neal Shen
# ------------------------------------------------------------------
import RPi.GPIO as GPIO
import time
makerobo_BuzzerPin = 11    # active buzzer pin
# song spectrum
Tone_CL = [0,131,147,165,175,196,211,248] # low c note frequence
Tone_CM = [0,262,294,330,350,393,441,495] # middle c note frequence
Tone_CH = [0,525,589,661,700,786,882,990] # high c note frequence
# the first song spectrum
makerobo_song_1 = [ \
    Tone_CM[3], Tone_CM[5], Tone_CM[6], Tone_CM[3], Tone_CM[2], Tone_CM[3], \
    Tone_CM[5], Tone_CM[6], Tone_CH[1], Tone_CM[6], Tone_CM[5], Tone_CM[1], \
    Tone_CM[3], Tone_CM[2], Tone_CM[2], Tone_CM[3], Tone_CM[5], Tone_CM[2], \
    Tone_CM[3], Tone_CM[3], Tone_CL[6], Tone_CL[6], Tone_CL[6], Tone_CM[1], \
    Tone_CM[2], Tone_CM[3], Tone_CM[2], Tone_CL[7], Tone_CL[6], Tone_CM[1], \
    Tone_CL[5] \
]
# the first song's beats
n=makerobo_beat_1 = [ \
    1,1,3,1,1,3,1,1,1,1,1,1,1,1,3,1,1,3,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,3 \
]
# the second song spectrum
makerobo_song_2 = [ \
    Tone_CM[1], Tone_CM[1], Tone_CM[1], Tone_CL[5], Tone_CM[3], Tone_CM[3], \
    Tone_CM[3], Tone_CM[1], Tone_CM[1], Tone_CM[3], Tone_CM[5], Tone_CM[5], \
    Tone_CM[4], Tone_CM[3], Tone_CM[2], Tone_CM[2], Tone_CM[3], Tone_CM[4], \
    Tone_CM[4], Tone_CM[3], Tone_CM[2], Tone_CM[3], Tone_CM[1], Tone_CM[1], \
    Tone_CM[3], Tone_CM[2], Tone_CM[2], Tone_CL[5], Tone_CL[7], Tone_CM[2], \
    Tone_CM[1] \
]
# the second song's beats
n=makerobo_beat_2 = [ \
    1,1,2,2,1,1,2,2,1,1,2,2,1,1,3,1,1,2,2,1,1,2,2,1,1,2,2,1,1,3,1,1,1,1,1,3 \
]


# gpio inilization
def makerobo_setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(makerobo_BuzzerPin, GPIO.OUT)
    global makerobo_Buzz # the varible is alterative as gpi.pwm
    makerobo_Buzz = GPIO.PWM(makerobo_BuzzerPin, 440) # set initial frequence is 440
    makerobo_Buzz.start(50) # set 50% work mode


# loop function
def makerobo_loop():
    while True:
        # play the first song
        for i in range(1, len(makerobo_song_1)):
            makerobo_Buzz.ChangeFrequency(makerobo_song_1[i]) # set song's note frequency
            time.sleep(makerobo_beat_1[i] * 0.5)
        time.sleep(1)
        # play the second song
        for i in range(1, len(makerobo_song_2)):
            makerobo_Buzz.ChangeFrequency(makerobo_song_2[i]) # set song's note frequency
            time.sleep(makerobo_beat_2[i] * 0.5)


# release source
def makerobo_destroy():
    makerobo_Buzz.stop() # close buzzer
    GPIO.output(makerobo_BuzzerPin, GPIO.HIGH)
    GPIO.cleanup()


if __name__ == '__main__':
    makerobo_setup()
    try:
        makerobo_loop()
    except KeyboardInterrupt:
        makerobo_destroy()