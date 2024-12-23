import cv2
import mediapipe as mp
import pyautogui
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
index_y = 0
TF_ENABLE_ONEDNN_OPTS=0
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)
                if id == 8:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                    index_x = screen_width/frame_width*x
                    index_y = screen_height/frame_height*y

                if id == 4:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                    thumb_x = screen_width/frame_width*x
                    thumb_y = screen_height/frame_height*y
                    #--------------------------------------
                    #distance = ((index_x - thumb_x)**2 + (index_y - thumb_y)**2)**0.5

                     # Scroll up if the distance is larger than the threshold
                    #if distance > 100:    
                     #pyautogui.scroll(1)
                    # Scroll down if the distance is smaller than the threshold
                    #elif distance < 50:
                     #pyautogui.scroll(-1)
                    print('outside', abs(index_y - thumb_y))
                    if abs(index_y - thumb_y) < 20:
                        pyautogui.click()
                        #pyautogui.sleep()
                    elif abs(index_y - thumb_y) < 100:
                        pyautogui.moveTo(index_x, index_y)#,duration=0.1)
    cv2.imshow('Virtual Mouse', frame)
    cv2.waitKey(1)