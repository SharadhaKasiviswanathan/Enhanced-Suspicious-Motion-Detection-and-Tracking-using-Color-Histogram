import cv2
import numpy as np
import time
import os

faceDetector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# cam = cv2.VideoCapture('http://192.168.1.18/mjpeg/1')
cam = cv2.VideoCapture(0)
rec = cv2.face.LBPHFaceRecognizer_create()
# rec = cv2.createLBPHFaceRecognizer()

rec.read("recognizer\\trainningData.yml")
# rec.load("recognizer\\trainningData.yml")
i1d = 0
id = 0
# font = (cv2.FONT_HERSHEY_SIMPLEX, 5, 1, 0, 4)
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    id = 0
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetector.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        id, conf = rec.predict(gray[y:y + h, x:x + w])
        print('conf=', conf)
        if id == 3:
            i1d = "unknown"
            cv2.imwrite(filename='saved_img.jpg', img=img)
            os.system("python mail.py")

        elif id == 2 and (conf >= 48 and conf <=60):
            i1d = "Sharadha Shivakumar"

        elif id == 1 and (conf >= 38 and conf <=45):
            i1d = "Sharadha K"


        cv2.putText(img, str(i1d), (x, y + h), font, 1, (0, 255, 0), 3)

    cv2.imshow("face", img)
    if cv2.waitKey(1) == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
