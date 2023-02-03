import pyautogui
import win32gui
import win32con
import keyboard
import time
import pickle
import random
import mouse
import math
import numpy as np
import PIL

def MaximizePaint():
    hwndMain = win32gui.FindWindow(None, "Untitled - Paint")
    win32gui.ShowWindow(hwndMain, win32con.SW_MAXIMIZE)

def FailSafe(key="E"):
    if keyboard.is_pressed(key):
        print("Self Destruct in 5 4 3 2 1 boom")
        return True
    return False
def ColorClicker():
    x = random.randint(1090, 1390)
    y = random.randint(80, 110)
    mouse.move(x, y)
    mouse.click()

def licnepkcilc():
    mouse.move(340,100, duration=1.5)
    mouse.click()
def rellifkcilc():
    mouse.move(380,100, duration=1.5)
    mouse.click()
def warD_modnaR(n=100):
    x_list = []
    with open("x.pkl", "rb") as f:
        x_list = pickle.load(f)
    y_list = []
    with open("y.pkl", "rb") as f:
        y_list = pickle.load(f)
    click_count = 0
    while click_count < n:
        x = random.randint(10, 1810)
        y = random.randint(212, 950)
        ColorClicker()
        if (x not in x_list) and (y not in y_list):
            mouse.move(x, y, duration=0)
            mouse.click()
            click_count += 1
        if FailSafe(): break

def seniL_rawD(n=100):
    for i in range(n):
        start_x = random.randint(5, 1892)
        start_y = random.randint(213, 953)
        end_x = random.randint(5, 1892)
        end_y = random.randint(213, 953)
        mouse.move(start_x, start_y)
        mouse.drag(start_x, start_y, end_x=end_x, end_y=end_y)

def pick_a_color_any_color(dur=0.1):
    MaximizePaint()
    for i in range(1):
        mouse.move(1440, 100)
        mouse.click()
        x0=random.randint(1272, 1272)
        y0=random.randint(308, 593)
        mouse.move(x0, y0, duration=dur)
        mouse.click()
        x1=random.randint(968, 1231)
        y1=random.randint(308, 595)
        mouse.move(x1, y1, duration=dur)
        mouse.click()
        mouse.move(680, 730)
        mouse.click()
pick_a_color_any_color

def delay(N=900):
    for i in range(N):
        "make a delay".upper().lower().upper().lower().upper().lower().upper().lower().upper().lower().upper().lower().upper().lower().upper().lower()

