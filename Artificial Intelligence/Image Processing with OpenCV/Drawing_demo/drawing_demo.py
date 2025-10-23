import cv2 as cv
import numpy as np

blank = np.zeros((300,300,3), dtype='uint8')
drawing = False

def mouse_info(event, x, y, flag, any):
    global drawing,blank
    
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        blank[y:y+5, x:x+5] = (255,0,0)

    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            blank[y:y+5, x:x+5] = (255,0,0)
        
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False

cv.namedWindow("blank")
cv.setMouseCallback('blank',mouse_info)
while True:
    cv.imshow('blank',blank)
    key = cv.waitKey(1) & 0xFF

    if key == ord('q'):
        break
    elif key == ord('s'):
        cv.imwrite('painted blank.png',blank)
        print('Görüntünüz kaydedildi.')
    elif key == ord('e'):
        blank = np.zeros((300,300,3), dtype='uint8')
    
cv.destroyAllWindows()