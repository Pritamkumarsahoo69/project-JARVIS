import cv2
import mediapipe as mp
import pyautogui  
import time

# Initialize MediaPipe Hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Initialize MediaPipe Drawing module
mp_drawing = mp.solutions.drawing_utils

# Initialize the webcam feed
cap = cv2.VideoCapture(0)

prev_y = None

while True:
    # Read each frame from the webcam
    ret, frame = cap.read()

    # Flip the frame horizontally
    frame = cv2.flip(frame, 1)

    # Convert the BGR image to RGB
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe Hands
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Get the coordinates of the index finger tip
            x = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x
            y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y

            if prev_y is not None:
                # Scroll up if the current y-coordinate is less than the previous y-coordinate
                if y < prev_y:
                    pyautogui.scroll(100)
                    time.sleep(1)
                # Scroll down if the current y-coordinate is greater than the previous y-coordinate
                elif y > prev_y:
                    pyautogui.scroll(-100)
                    time.sleep(1)

            prev_y = y

            # Draw hand landmarks
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Display the frame
    cv2.imshow('Frame', frame)

    # Exit loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close OpenCV window
cap.release()
cv2.destroyAllWindows()
