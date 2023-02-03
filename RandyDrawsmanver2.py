import pyautogui
import random
import mouse
from UTIL import *
def dg_45Randmwalk(steps=1000, ss=4, dur=0.001):
    MaximizePaint()
    x=start_x=906
    y=start_y=595
    mouse.move(x, y)
    for i in range(steps):
        if x>=1886:
            mouse.move(start_x, start_y)
        if y>=954 or y<=213:
            mouse.move(start_x, start_y)

        if FailSafe():
            break
        a=x+ss
        b=x-ss
        c=y+ss
        d=y-ss
        x2=random.choice([a,b])
        y2=random.choice([c,d])
        mouse.drag(x, y, end_x=x2, end_y=y2, duration=dur, absolute=True)
        x = x2
        y = y2
dg_45Randmwalk(ss=30, dur=0.001, steps=1)