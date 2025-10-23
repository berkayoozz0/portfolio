import cv2 as cv

#face detection ten rengine bakmaz, edgelere bakarak o şeyin yüz olup olmadığını anlamaya çalışır.

img = cv.imread('photos/group.jpeg')
resized = cv.resize(img, (900,600), interpolation=cv.INTER_AREA)
gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
haar_cascade = cv.CascadeClassifier('haar.face.xml') #classifierımızı bir variable üzerinden çağırıyoruz

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10)
"""
minNeighbors parametresi, OpenCV'nin detectMultiScale fonksiyonunda yüz tespitinin doğruluğunu artırmak için kullanılır.
Bu parametre, bir yüz adayının geçerli bir yüz olarak kabul edilmesi için çevresinde kaç "komşu" dikdörtgenin bulunması gerektiğini belirtir.
"""
print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(resized, (x,y), (x+w,y+h),(0,255,0),thickness=2)

cv.imshow('Detected Faces',resized)
cv.waitKey(0)