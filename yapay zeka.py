

import cv2
from cvzone.HandTrackingModule import HandDetector


detector=HandDetector()
img=cv2.imread('i5.jpg')

hands,img=detector.findHands(img)
cv2.imshow('Resim',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

