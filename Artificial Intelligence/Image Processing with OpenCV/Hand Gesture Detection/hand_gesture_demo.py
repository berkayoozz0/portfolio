import mediapipe as mp
import cv2 as cv


capture = cv.VideoCapture(0)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.2, min_tracking_confidence=0.5)
mp_draw = mp.solutions.drawing_utils


def finger_count(landmarks):
    fingers = [4,8,12,16,20]
    count = 0

    if landmarks.landmark[5].x < landmarks.landmark[17].x: #hand right hand
        if landmarks.landmark[4].x > landmarks.landmark[3].x: #başparmak için x ekseni kontrolü
            count +=1
            if (landmarks.landmark[7].y > landmarks.landmark[6].y and
            landmarks.landmark[11].y > landmarks.landmark[10].y and
            landmarks.landmark[15].y > landmarks.landmark[14].y and
            landmarks.landmark[19].y > landmarks.landmark[18].y and
            landmarks.landmark[4].x > landmarks.landmark[3].x):
                count = 0
        else:
            for finger_tips in fingers:
                if landmarks.landmark[finger_tips].y < landmarks.landmark[finger_tips-1].y: #diğer parmaklar için y ekseni kontrolü
                    count +=1
        
    else: #hand = left hand
        if landmarks.landmark[4].x < landmarks.landmark[3].x: #başparmak için x ekseni kontrolü
            count +=1
        if (landmarks.landmark[7].y > landmarks.landmark[6].y and
            landmarks.landmark[11].y > landmarks.landmark[10].y and
            landmarks.landmark[15].y > landmarks.landmark[14].y and
            landmarks.landmark[19].y > landmarks.landmark[18].y and
            landmarks.landmark[4].x < landmarks.landmark[3].x):
                count = 0
        else:
            for finger_tips in fingers:
                if landmarks.landmark[finger_tips].y < landmarks.landmark[finger_tips-1].y: #diğer parmaklar için y ekseni kontrolü
                    count +=1

    return count



while True:
    ret,frame = capture.read()
    rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB) #mediapipe rgbde çalışır.
    result = hands.process(rgb)  #el tespiti
    if result.multi_hand_landmarks:
       for landmarks in result.multi_hand_landmarks:
           mp_draw.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)
           result_count = finger_count(landmarks)
           cv.putText(frame, f'Finger Count: {result_count}', (10, 50), cv.FONT_ITALIC, 1, (255,0,0), 2)

    cv.imshow("captured",frame)

    if cv.waitKey(20) == ord("q"):
        break   

capture.release()
cv.destroyAllWindows()