import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0)

while True:
    bool, frame = capture.read()
    if not bool:
        break

    # Görüntüyü HSV renk uzayına çevir
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # HSV renk uzayı için tüm aralığı kapsayan maske
    lower_boundary = np.array([0, 50, 50])  # Tüm renkler için başlangıç (H=0)
    upper_boundary = np.array([179, 255, 255])  # Tüm renkler için bitiş (H=179)

    # Renk maskesini oluştur
    mask = cv.inRange(hsv, lower_boundary, upper_boundary)

    # Maskeyi orijinal görüntüye uygula
    masked_frame = cv.bitwise_and(frame, frame, mask=mask)

    # Konturları bul
    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    # Her bir konturu çiz
    for contour in contours:
        if cv.contourArea(contour) > 500:  # Sadece büyük nesneleri algıla
            x, y, w, h = cv.boundingRect(contour)
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Yeşil çerçeve

    # Görüntüyü göster
    cv.imshow("Original", frame)
    cv.imshow("Masked", masked_frame)

    # Çıkış için 'q' tuşuna basın
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

# Kaynakları serbest bırak
capture.release()
cv.destroyAllWindows()
