import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0)

def tb(x):
    pass


#cv.namedWindow("Trackbar")
#cv.createTrackbar("threshold1","Trackbar",0,300,tb)
#cv.createTrackbar("threshold2","Trackbar",0,300,tb)


while True:
    ret,frame = capture.read()
    cv.imshow("captured",frame)
    #threshold1 = cv.getTrackbarPos("threshold1","Trackbar")
    #threshold2 = cv.getTrackbarPos("threshold2","Trackbar")
    blurred = cv.GaussianBlur(frame,(3,3),cv.BORDER_DEFAULT)
    gray = cv.cvtColor(blurred,cv.COLOR_BGR2GRAY)
    high_thresh, threshold = cv.threshold(gray, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    low_thresh = 0.5*high_thresh
    canny_edge = cv.Canny(blurred,low_thresh,high_thresh)
    contours, hierarchy = cv.findContours(canny_edge, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    contour_image = np.zeros_like(frame)
    cv.drawContours(contour_image,contours,-1,(255,255,255),thickness=1)
    circles = cv.HoughCircles(gray,cv.HOUGH_GRADIENT,dp=1,minDist=50,param1=high_thresh,param2=30,minRadius=10,maxRadius=100)
    if circles is not None:
        circles = np.uint16(np.around(circles))  #Çember koordinatlarını tam sayıya çevir
        for i in circles[0, :]:
            center = (i[0], i[1])  # Çemberin merkezi
            radius = i[2]  # Çemberin yarıçapı
            center_of_image = (frame.shape[1]//2,frame.shape[0]//2)
            cv.circle(frame, center, radius, (255, 0, 0), 2)
            cv.line(frame, center, center_of_image, (255,0,0), 2)
        
    cv.imshow("contoured_image",contour_image)
    cv.imshow("captured_canny",canny_edge)
    cv.imshow("circles_detected", frame)
        

    if cv.waitKey(20) == (ord('q') or ord('Q')):
        break

capture.release()
cv.destroyAllWindows()