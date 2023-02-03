import mouse

from UTIL import *


MaximizePaint()

time.sleep(2)
def DrawThingy(start, end):
    mouse.drag(start_x=start[0], start_y=start[1], end_x=end[0], end_y=end[1], duration=0)

x_list = []

for i in range(45):
    #DrawThingy(start=(1820, 970-i*40), end=(820, 970-i*40))
    x = int(1820-i*40)
    DrawThingy(start=(x, 950), end=(x, 212))
    x_list.append(x)
    if FailSafe(): break

y_list= []
for i in range(19):
    y=int(950-i*40)
    DrawThingy(start=(1820, y), end=(0, y))
    y_list.append(y)
    if FailSafe(): break
print(x_list)
with open("x.pkl", "wb")as f:
    pickle.dump(x_list, f)
print(y_list)
with open("y.pkl", "wb")as f:
    pickle.dump(y_list, f)


im1 = pyautogui.screenshot("buirhdgfyuewkfyerukt.png")
