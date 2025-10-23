import cv2 as cv
import mediapipe as mp
import math
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

capture = cv.VideoCapture(0)
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, 1, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.2, min_tracking_confidence=0.5)
mp_draw = mp.solutions.drawing_utils



def calculate_distance(landmark1,landmark2):
    x1,y1 = landmark1.x, landmark1.y
    x2,y2 = landmark2.x, landmark2.y
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def get_finger_distance(landmarks):
    finger1 = landmarks.landmark[8]
    finger2 = landmarks.landmark[4]
    distance = calculate_distance(finger1,finger2)
    return min(distance*10,1)

while True:
    ret, frame = capture.read()
    rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    result = hands.process(rgb)
    if result.multi_hand_landmarks:
        for landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)
            finger_distance = get_finger_distance(landmarks)
            volume.SetMasterVolumeLevelScalar(finger_distance, None)
            cv.putText(frame, f'Volume Level: {finger_distance*100}', (10, 50), cv.FONT_ITALIC, 1, (255,0,0), 2)

    cv.imshow("captured",frame)
    if cv.waitKey(20) == ord("q"):
        break

capture.release()
cv.destroyAllWindows()
