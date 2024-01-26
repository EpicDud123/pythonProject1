# import the opencv library
import cv2
from FACF import *
# define a video capture object
vid = cv2.VideoCapture(0)
with open("facedb.pkl", "rb") as f:
    facedb = pickle.load(f)
while (True):

    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    # frame is numpy array with shape (480,640,3) in BGR channel order
    # frame[:,:,::-1] #change the BGR order to RGB
    detectface(frame)
    face_plants=sorted(glob.glob("goofyahhface*.jpg"))
    for face_plant in face_plants:
        result = stwangadanga(fip=face_plant, facedb=facedb, threseshold=0.65)
        print(result)




    # Display the resulting frame
    cv2.imshow('frame', frame)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()