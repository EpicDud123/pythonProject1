
from PIL import Image
import numpy as np
import cv2
import pickle
import os
import glob
#from sklearn.metrics.pairwise import cosine_similarity
from numpy import dot
from numpy.linalg import norm
def cosine_sim(a, b):
    cos_sim = dot(a, b) / (norm(a) * norm(b))
    return cos_sim

prototxt = 'deploy.prototxt'
model = 'res10_300x300_ssd_iter_140000.caffemodel'
net = cv2.dnn.readNetFromCaffe(prototxt, model)
print(f"Successfully loaded CV2 DNN model: {model}")

# face detection
def detectface(image_file, cv2_dnn_net = net):
    file_pattern = "goofyahh*.jpg"
    # get a list of all files matching the pattern
    files_to_delete = glob.glob(file_pattern)
    # delete each file in the list
    for file in files_to_delete:
        os.remove(file)
        print(f"File '{file}' deleted successfully.")

    faceid = 0
    if type(image_file)==str:
        image = cv2.imread(image_file)
    else: #if the input is an image array, skip the image loading
        image=image_file
    # resize it to have a maximum width of 400 pixels
    (h, w) = image.shape[:2]
    print(w, h)
    new_width = 400
    image = cv2.resize(image, dsize=(int(new_width/w*h), new_width), interpolation=cv2.INTER_CUBIC)
    (h, w) = image.shape[:2]

    # cv2_imshow(image)
    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
    net.setInput(blob)
    detections = net.forward()
    outputpath=[]
    for i in range(0, detections.shape[2]):

        # extract the confidence (i.e., probability) associated with the prediction
        confidence = detections[0, 0, i, 2]

        # filter out weak detections by ensuring the `confidence` is
        # greater than the minimum confidence threshold
        if confidence > 0.5:
            # compute the (x, y)-coordinates of the bounding box for the object
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            # draw the bounding box of the face along with the associated probability
            text = "{:.2f}%".format(confidence * 100)
            y = startY - 10 if startY - 10 > 10 else startY + 10
            cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 1)
            cv2.putText(image, text, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
            facething = Image.fromarray(image[startY:endY, startX:endX][:, :, ::-1])
            facething.save(crop_path := f"goofyahhface{faceid}.jpg")
            outputpath.append(crop_path)
            faceid += 1
    if faceid > 0:
        print(f"Face detected: {faceid}")
    return outputpath


# facial recognition
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

def stwangadanga(fip: str, threseshold: float = 0.8, facedb: dict = {}, secret_option=True) -> bool:
    """
    Compare a face picture to the face db to see if it's a family member

    Args:
         fip: filepath of the input face picture
         threseshold: if the face similarity is above this threshold, it's a family member

    Returns:
        True=familymemeber, False=mostlikelyintruder
    """
    for face, embedding in facedb.items():
        epicwooo = wow(fip).ravel()
        similarity = cosine_sim(epicwooo, embedding).ravel()[0]
        if similarity > threseshold:
            print(f"similarity: {similarity}")
            return True
        else:
            print(f"similarity: {similarity}")
            #if secret_option==True:
                #winsound.PlaySound("mixkit-ambulance-siren-us-1642.wav", winsound.SND_ALIAS)
            #return False



def addition(identity_face_crop_path: str, identity_name: str, face_db_pickle_path: str):
    numpyarray = wow(identity_face_crop_path).ravel()
    with open(face_db_pickle_path, "rb") as f:
        facedb = pickle.load(f)
        facedb[identity_name]=numpyarray
    with open(face_db_pickle_path, "wb") as f:
        pickle.dump(facedb, f)
    print("we did it")


if __name__ == "__main__":
    with open("facedb.pkl", "rb") as f:
        facedb = pickle.load(f)
    detectface(r"C:\Users\WinstonBai\OneDrive\Pictures\Camera Roll\WIN_20230407_13_32_47_Pro.jpg")
    face_plants=sorted(glob.glob("goofyahhface*.jpg"))
    for face_plant in face_plants:
        result = stwangadanga(fip=face_plant, facedb=facedb)
        print(result)
    #addition(r"C:\Users\WinstonBai\PycharmProjects\pythonProject1\goofyahhface0.jpg", "Winstonisalive", r"C:\Users\WinstonBai\PycharmProjects\pythonProject1\facedb.pkl")