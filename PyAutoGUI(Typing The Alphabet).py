import time

time.sleep(5)
import pyautogui
x=0
while x<6000:
    pyautogui.typewrite('m ', interval=0.01)
    x+=1