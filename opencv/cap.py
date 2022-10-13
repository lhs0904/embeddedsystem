import cv2

cap = cv2.VideoCapture(0) # /dev/video0 지정
_, img = cap.read()

#print(img)

cv2.imwrite("cap.jpg", img) #cap.jpg save
