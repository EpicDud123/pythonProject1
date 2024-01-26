
from sklearn.metrics.pairwise import cosine_similarity
from PIL import Image
import numpy as np
import math
# import onnxruntime
import imutils
import cv2
import pickle
import os
import glob
from sklearn.metrics.pairwise import cosine_similarity
import winsound
modelpath = r"C:\Users\WinstonBai\Downloads\facenet.onnx"
# session = onnxruntime.InferenceSession(modelpath)
session = cv2.dnn.readNetFromONNX(modelpath)


def wow(image_path, session=session):
    image = Image.open(image_path).convert('RGB').resize((160, 160))  # loading the image and resizing
    image_array = np.array(image).astype("float32")  # converting the image to array
    image_array = (image_array - 127.5) / 128  # normalization
    image_array = np.expand_dims(image_array, 0)  # add the batch dimension in the beginning (1 image is just 1)
    image_array = np.moveaxis(image_array, -1,
                              1)  # move the color channel to be after the batch dimension (required by this particular onnx model)
    # input_name = session.get_inputs()[0].name
    
    # output_name = session.get_outputs()[0].name
    # result = session.run([output_name], {input_name: image_array})[0]
    session.setInput(image_array)
    result = session.forward()
    return result


if __name__ == "__main__":
    result=wow(r"C:\Users\WinstonBai\Downloads\goat.jpg")
    print(result)