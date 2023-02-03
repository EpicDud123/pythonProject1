import pyautogui
import random
import mouse

from UTIL import *
#MaximizePaint()
time.sleep(3)
x_list=[]
with open("x.pkl", "rb") as f:
    x_list = pickle.load(f)
y_list=[]
with open("y.pkl", "rb") as f:
    y_list = pickle.load(f)
for i in range(250):
    x=random.randint(0, 1890)
    y=random.randint(270, 840)
    if (x not in x_list) and (y not in y_list):
        mouse.move(x, y, duration=0)
        mouse.click()
    if FailSafe(): break