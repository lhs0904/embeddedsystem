import cv2

imageFile = 'data/jenny.jpg'
img = cv2.imread(imageFile) # cv2.imread(imageFile, cv2.IMREAD_COLOR)
cv2.imwrite('jenny.bmp', img) #jenny.bmp로 저장
cv2.imwrite('jenny.png', img) #jenny.png로 저장
cv2.imwrite('jenny2.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 90]) #압축률 90의 JPEG 영상으로 저장, 압축률 범위는 0~100 , 기본값은 95
cv2.imwrite('jenny2.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 9]) #압축률 9의 PNG 영상으로 저장, 압축률 범위는 0~9, 기본값은 3