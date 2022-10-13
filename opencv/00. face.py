import cv2

face_detector = cv2.CascadeClassifier("/usr/local/lib/python3.9/dist-packages/cv2/data/haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)
_, img = cap.read()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_detector.detectMultiScale(gray, 1.1, 5)

cv2.imwrite("face_gray.jpg", gray) # save gray
cv2.imwrite("face_origin.jpg", img) # save origin

print(faces)

for face in faces:
	x, y, w, h = face
	#촬영한 이미지, 좌표1, 좌표2, 네모 테두리 색상, 네모 테두리 두께
	cv2.rectangle(img, (x,y), (x+w, y+h), (255, 255, 255), 5)
	
cv2.imwrite("image.jpg", img)
