import cv2
import time
import numpy as np

car_classifier = cv2.CascadeClassifier('Haarcascade/haarcascade_car.xml')

cap = cv2.VideoCapture('images/car.avi')

while cap.isOpened():

ret , frame = CAP.read()
 
gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)

cars = car_classifier.detectMultiScale(gray,1.3,3)

for(x , y , w , h) in cars:
cv2.rectangle(frame , (x,y) , (x+w, y+h) , (0 , 255 , 255) , 2)
cv2.imshow('Cars' , frame)

if cv2.waitKey(1) == 13:
break

cap.release()
cv2.destroyAllWindow()

