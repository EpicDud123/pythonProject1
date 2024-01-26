import cv2

# Create a VideoCapture object
cap = cv2.VideoCapture(0)  # 0 for default camera, or specify the camera index if multiple cameras are available

# Check if the camera was successfully opened
if cap.isOpened():
    print("Yep, the camera works")
else:
    print("Failed to open the camera")

# Release the VideoCapture object
cap.release()