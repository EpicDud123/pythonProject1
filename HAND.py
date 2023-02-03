import cv2
import mediapipe as mp
import mouse
import pyautogui
pyautogui.FAILSAFE = False

from UTIL import *
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
SCREEN_WIDTH, SCREEN_HEIGHT=pyautogui.size()
last_right_hand_x = None
last_right_hand_y = None
VISIBILITY_THRESHOLD = 0.8
MOUSEHELPDOWN = False


# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    if keyboard.is_pressed("f"):
        break
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    right_hand_visible = False
    if results and results.multi_hand_landmarks:
        right_hand_index = 0
        try:
            for i in range(0,1):
                if results.multi_handedness[i].classification[0].label == "Right":
                    right_hand_index = i
        except: pass
        right_hand_x = results.multi_hand_landmarks[right_hand_index].landmark[8].x  # between 0 and 1
        right_hand_y = results.multi_hand_landmarks[right_hand_index].landmark[8].y  # between 0 and 1
        thumb_y = results.multi_hand_landmarks[right_hand_index].landmark[4].y
        thumb_x = results.multi_hand_landmarks[right_hand_index].landmark[4].x
        right_hand_visible = True
        if right_hand_visible:
            if last_right_hand_x is not None and last_right_hand_y is not None:
                mouse_x, mouse_y = mouse.get_position()
                new_mouse_x = mouse_x - (right_hand_x - last_right_hand_x) * SCREEN_WIDTH * 1.5
                new_mouse_y = mouse_y + (right_hand_y - last_right_hand_y) * SCREEN_HEIGHT * 1.5
                mouse.move(new_mouse_x, new_mouse_y, duration=0.001)
                if abs(right_hand_x - thumb_x)<0.03 and abs(right_hand_y - thumb_y)<0.03:
                    # if not MOUSEHELPDOWN:
                    pyautogui.mouseDown()
                    MOUSEHELPDOWN=True
                else:
                    # if MOUSEHELPDOWN:
                    pyautogui.mouseUp()
                    MOUSEHELPDOWN=False
                #if thumb_y<left_hand_y:
                    #mouse.click(button=mouse.RIGHT)

            last_right_hand_x = right_hand_x
            last_right_hand_y = right_hand_y
        else: # the hand is outside the screen
            last_right_hand_x = None
            last_right_hand_y = None
    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())
    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()
