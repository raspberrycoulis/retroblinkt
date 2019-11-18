#!/usr/bin/env python

import time

import blinkt

blinkt.set_clear_on_exit()

REDS = [0, 0, 0, 0, 0, 16, 64, 255, 64, 16, 0, 0, 0, 0, 0, 0]

start_time = time.time()

while 'LARSON' in open('/home/pi/control.txt').read():
    delta = (time.time() - start_time) * 16
    offset = int(abs((delta % len(REDS)) - blinkt.NUM_PIXELS))

    for i in range(blinkt.NUM_PIXELS):
        blinkt.set_pixel(i, REDS[offset + i], 0, 0)

    blinkt.show()

    time.sleep(0.1)