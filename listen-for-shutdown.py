#!/usr/bin/env python
#
#Button on GPIO 24
#LED on GPIO 27

import RPi.GPIO as GPIO
import subprocess


GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.wait_for_edge(24, GPIO.FALLING)

GPIO.setup(27, GPIO.OUT, initial=GPIO.LOW)
GPIO.output(27, GPIO.LOW) # Turn off the led


subprocess.call(['shutdown', '-h', 'now'], shell=False)
