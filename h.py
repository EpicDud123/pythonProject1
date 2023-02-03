from os.path import join
import sys
def write():
        print('Creating a new file')
        path = "/content/drive/MyDrive/Python🐍sssssssss/sonic.wav"
        name = input('Enter a name for your file: ')+'.txt'  # Name of text file coerced with +.txt

        try:
            file = open(join(path, name),'w')   # Trying to create a new file or open one
            file.close()

        except:
            print('Something went wrong! Cannot tell what?')
            sys.exit(0)

write()