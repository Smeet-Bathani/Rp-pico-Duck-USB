# ducky_script.py (MicroPython code for Pico)

import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

def type_string(text):
    layout.write(text)

def press_keys(*keys):
    keyboard.press(*keys)
    keyboard.release_all()

def ducky_script():
    time.sleep(5)  # Wait for the laptop to recognize the Pico
    press_keys(Keycode.GUI, Keycode.R) # Windows + R
    time.sleep(0.5)
    type_string("notepad\n") # Opens notepad
    time.sleep(1)
    type_string("Hello, world! This is the Pico Duck speaking.\n")
    time.sleep(1)
    type_string("Performing automated task...\n")
    time.sleep(1)
    press_keys(Keycode.GUI, Keycode.L) # Locks the computer.
    time.sleep(1)

ducky_script()
