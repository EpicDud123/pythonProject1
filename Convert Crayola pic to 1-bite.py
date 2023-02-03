

from UTIL import *
from PIL import Image

def  low_image_as_array(path):
    img=Image.open(path)
    img_array=np.array(img)
    return img_array

def one_bite_transformitive(img, save_path,size=(300, 169)):
    img = img.resize(size)
    img = img.convert("1")
    # img.show()
    img.save(save_path)

def consumption_rgb(img_array, size):
    R=img_array[:,:,0]
    G=img_array[:,:,1]
    B=img_array[:,:,2]
    R_img=Image.fromarray(R)
    G_img = Image.fromarray(G)
    B_img = Image.fromarray(B)
    one_bite_transformitive(R_img, "R.png", size)
    one_bite_transformitive(G_img, "G.png", size)
    one_bite_transformitive(B_img, "B.png", size)

img_array=low_image_as_array(r"C:\Users\WinstonBai\OneDrive\Pictures\Camera Roll\The_Chosen_One.jpg")
print(img_array.shape)

consumption_rgb(img_array, size=(300, 169))