import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0)

def tb(x):
    pass

cv.namedWindow("Trackbars")
cv.createTrackbar("Lower H", "Trackbars", 30, 179, tb)
cv.createTrackbar("Lower S", "Trackbars", 50, 255, tb)
cv.createTrackbar("Lower V", "Trackbars", 70, 200, tb)
cv.createTrackbar("Upper H", "Trackbars", 130, 179, tb)
cv.createTrackbar("Upper S", "Trackbars", 255, 255, tb)
cv.createTrackbar("Upper V", "Trackbars", 200, 255, tb)

while True:
    bool,frame = capture.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    if bool == False:
        break
    lower_h = cv.getTrackbarPos("Lower H","Trackbars")
    lower_s = cv.getTrackbarPos("Lower S","Trackbars")
    lower_v = cv.getTrackbarPos("Lower V","Trackbars")
    upper_h = cv.getTrackbarPos("Upper H","Trackbars")
    upper_s = cv.getTrackbarPos("Upper S","Trackbars")
    upper_v = cv.getTrackbarPos("Upper V","Trackbars")
    
    lower_boundary = np.array([lower_h,lower_s,lower_v])
    upper_boundary = np.array([upper_h,upper_s,upper_v])
    mask = cv.inRange(hsv,lower_boundary,upper_boundary)
    contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    centers = []
    for contour in contours:
         if cv.contourArea(contour) > 800:
            M = cv.moments(contour)
            if M["m00"] == 0: 
                continue
            elif M["m00"] != 0:
                x = int(M["m10"] / M["m00"]) #1 olan xler/toplam alan
                y = int(M["m01"] / M["m00"]) #1 olan yler/toplam alan.
                centers.append((x, y))
                cv.circle(frame, (x, y), 5, (255, 0, 0), -1)
    if len(centers) >= 2:                    #2 noktadan fazlaysa işlem yap
        p1, p2 = centers[:2]
        distance = int(np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2))
        if distance < 100:
            line_color = (0, 255, 0)
        elif distance < 200:
            line_color = (0, 255, 255) 
        else:
            line_color = (0, 0, 255) 
        cv.line(frame, p1, p2, line_color, 2)
    cv.imshow("captured",frame)
    if cv.waitKey(20) & 0xFF in [ord("q"), ord("Q")]:
        break

capture.release()
cv.destroyAllWindows()