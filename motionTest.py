#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import sys
import time
import RPi.GPIO as io
import subprocess
 
io.setmode(io.BCM)
SHUTOFF_DELAY = 60  # seconds
PIR_PIN = 4         # Pin 7 on pi
 
def main():
    io.setup(PIR_PIN, io.IN)
    turned_off = False
    last_motion_time = time.time()
    
    while True:
        if not io.input(PIR_PIN):
            last_motion_time = time.time()
            sys.stdout.flush()
            if turned_off:
                turned_off = False
                turn_on()
        else:
            if not turned_off and time.time() > (last_motion_time + SHUTOFF_DELAY):
                turned_off = True
                turn_off()
        time.sleep(.1)
 
def turn_on():
    print('TURNING ON')
    subprocess.call('/home/pi/mirror/turnOnMonitor.sh', shell=True)
    subprocess.call('/home/pi/mirror/turnOnLights.sh', shell=True)
 
def turn_off():
    print('TURNING OFF')
    subprocess.call('/home/pi/mirror/turnOffMonitor.sh', shell=True)
    subprocess.call('/home/pi/mirror/turnOffLights.sh', shell=True)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        io.cleanup()
