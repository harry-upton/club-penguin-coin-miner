# This script repeatedly prints the pixel coordinates of the mouse on the screen,
# to make it easier to specify the region the mining script should dig within.

from pynput.keyboard import Key, Controller as kc
from pynput.mouse import Button, Controller as mc
import time
import cv2

keyboard = kc()
mouse = mc()

def function_thing():
    while(True):
        print('The current pointer position is {0}'.format(mouse.position))

function_thing()

