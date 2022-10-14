from email.mime import image
import cv2
from matplotlib import pyplot as plt

imageFile = 'jenny.jpg'
img_gray = cv2.imread(imageFile, cv2.IMREAD_GRAYSCALE)

plt.figure(figsize=(6,6)) # 크기를 (6 inch, 6 inch)로 설정
plt.subplots_adjust(left = 0, right = 1, bottom = 0, top = 1) # 영상출력 범위를 좌우를 [0,1] 위아래를 [0,1]로 조정 범위는 left < right, bottom < top 이어야 함.
plt.imshow(img_gray, cmap='gray') #img_gray 영상을 cmap = 'gray'로 그레이스케일로 화면에 표시
##plt.axis('tight')
plt.axis('off') # 축을 없앰
plt.savefig('jenny05.png') # 영상을 jenny05.png로 저장
plt.show()