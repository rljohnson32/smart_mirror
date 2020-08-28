#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function

import RPi.GPIO as GPIO
import time

# Pin Number
PIN = 4

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN, GPIO.IN)#, pull_up_down=GPIO.PUD_UP)

    while True:
        pin_status = GPIO.input(PIN)
	if pin_status == 0:
        	print('MOTION DETECTED')
	else:
		print('SCANING...')
        time.sleep(0.1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
