import cv2
import os
import numpy as np
from PIL import Image

#recognizer = cv2.createLBPHFaceRecognizer()
recognizer = cv2.face.LBPHFaceRecognizer_create()

path = 'dataSet'


def getImagesWithID(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    IDs = []
    for imagePath in imagePaths:
        UserImg = Image.open(imagePath).convert('L')
        UserNp = np.array(UserImg, 'uint8')
        ID = int(os.path.split(imagePath)[-1].split(".")[1])
        faces.append(UserNp)
        print(ID)
        IDs.append(ID)
        cv2.imshow("training", UserNp)
        cv2.waitKey(10)
    return IDs, faces


Ids, faces = getImagesWithID(path)
recognizer.train(faces, np.array(Ids))
recognizer.save('recognizer/trainningData.yml')
cv2.destroyAllWindows()
