import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("Resources/histImg.jpg")
#cv2.imshow("img",img)

hist,bins=np.histogram(img.flatten(),256,[0,256])
cdf=hist.cumsum()
cdf_normalized=cdf*float(hist.max())/cdf.max()
plt.plot(cdf_normalized, color='b')
plt.hist(img.flatten(),256,[0,256],color='r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'),loc='upper left')
plt.show()


#img2=cv2.imread("Resources/hist2.jpg")
#equ=cv2.equalizeHist(img2)
#res=np.hstack((img,equ))
#cv2.imwrite("res.png",res)


cv2.waitKey(0)
