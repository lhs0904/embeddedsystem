import cv2
from matplotlib import pyplot as plt

path = '/home/pi/embeddedsystem/opencv/data/'
imgBGR1 = cv2.imread(path + 'jenny.jpg')
imgBGR2 = cv2.imread(path + 'apple.jpg')
imgBGR3 = cv2.imread(path + 'banana.jpg')
imgBGR4 = cv2.imread(path + 'orange.jpg')

#컬러 변환: cvtColor() 함수로 BGR 채널에서 RGB 채널의 영상으로 변환
imgRGB1 = cv2.cvtColor(imgBGR1, cv2.COLOR_BGR2RGB)
imgRGB2 = cv2.cvtColor(imgBGR2, cv2.COLOR_BGR2RGB)
imgRGB3 = cv2.cvtColor(imgBGR3, cv2.COLOR_BGR2RGB)
imgRGB4 = cv2.cvtColor(imgBGR4, cv2.COLOR_BGR2RGB)

#fig.canvas.set_window_title()은 Figure 객체 fig를 이용하여 윈도우 타이틀을 'Sample Pictures'로 설정
#2X2 서브플롯을 figsize (10, 10) 크기로 ax에 생성
fig, ax = plt.subplots(2, 2, figsize = (10, 10), sharey = True)
#fig.canvas.set_window_title('Sample Pictures')

#영상의 배치는 [0][0], [0][1], [1][0], [1][1]로 설정
ax[0][0].axis('off') #axis('off')로 좌표축 없앰
ax[0][0].imshow(imgRGB1, aspect = 'auto') #imshow()에서 aspect = 'auto'로 설정하여 영상출력

ax[0][1].axis('off')
ax[0][1].imshow(imgRGB2, aspect = 'auto')

ax[1][0].axis('off')
ax[1][0].imshow(imgRGB3, aspect = 'auto')

ax[1][1].axis('off')
ax[1][1].imshow(imgRGB4, aspect = 'auto')

plt.subplots_adjust(left = 0, bottom=0, right = 1, top=1, wspace=0.05, hspace=0.05)
plt.savefig('/home/pi/embeddedsystem/opencv/data/img_06.png', bbox_inches = 'tight')
plt.show()