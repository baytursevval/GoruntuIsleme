import cv2
import numpy as np

image=cv2.imread("Resources/histImg.jpg")
#cv2.imshow("image",image)

kernel1=np.ones((5,5), np.float32)/30
img=cv2.filter2D(src=image,ddepth=-1,kernel=kernel1)

#cv2.imshow("original",image)
#cv2.imshow("kernel blur", img)

img_blur=cv2.blur(image,(3,3))
#cv2.imshow("blur", img_blur)

img_boxFilter=cv2.boxFilter(image,-1, (3,3), normalize=False)
#cv2.imshow("boxFilter",img_boxFilter)

#doğrusal olmayan filtreler
img_median=cv2.imread("Resources/median2.jpg")
#img_median=cv2.imread("Resources/car.jpg")
median=cv2.medianBlur(img_median,5)
birlestirme=np.concatenate((img_median, median), axis=1)

cv2.imshow("img",birlestirme)


cv2.waitKey(0)
