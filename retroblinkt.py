#!/usr/bin/env python
import sys
from blinkt import set_clear_on_exit, set_all, set_pixel,show,set_brightness
from time import sleep

def nintendo():
    set_all(228,0,15)
    set_brightness(0.5)
    show()

def gb():
    set_all(155,188,15)
    set_brightness(0.5)
    show()

def psx():
    set_all(102,92.190)
    set_brightness(0.5)
    show()

def sega():
    set_all(23,86,155)
    set_brightness(0.5)
    show()

def unknown():
    set_all(255,255,0)
    set_brightness(0.5)
    show()

platform = sys.argv[1]

while 'SOLID' in open('/home/pi/control.txt').read():
    if platform == "nes":
        nintendo()
    elif platform == "snes":
        nintendo()
    elif platform == "megadrive":
        sega()
    elif platform == "psx":
        psx()
    elif platform == "mastersystem":
        sega()
    elif platform == "gb":
        gb()
    elif platform == "gba":
        gb()
    else:
        unknown()

set_all(0,0,0)
show()
