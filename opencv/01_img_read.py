import cv2

imageFile = '/home/pi/embeddedsystem/opencv/data/jenny.jpg'
img = cv2.imread(imageFile)
img_gray = cv2.imread(imageFile, 0)
cv2.imshow('Jenny colour', img)
cv2.imshow('Jenny Gray', img_gray)

cv2.waitKey()
cv2.destroyAllWindows()