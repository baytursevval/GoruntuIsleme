import cv2
import numpy as np
import matplotlib.pyplot as plt

#gauss noise örnek1
img=cv2.imread("Resources/gauss.jpg")
img=cv2.resize(img,(400,400))
#cv2.imshow("original",img)
def gaussian_noise(img):
    row,col,ch=img.shape
    mean=0
    var=0.05
    sigma=var**0.5
    gauss=np.random.normal(mean,sigma,(row,col,ch))
    gauss=gauss.reshape(row,col,ch)
    noisy=img+gauss
    return noisy

image=cv2.imread("Resources/gauss.jpg")
image=image/255
image=cv2.resize(image,(400,400))
noise_img=gaussian_noise(image)
#cv2.imshow("gaussian noise", noise_img)


#tuz&biber noise örnek1
def saltPepperNoise(image):
    row,col,ch=image.shape
    s_vs_p=0.5  #siyah beyaz eşit oranda
    amount=0.04 #nokta oranı
    noisy=np.copy(image) #orj resme zarar gelmemesi için kopyalama

    num_salt=int(np.ceil(amount*image.size*s_vs_p)) #beyaz nokta sayısı
    corrds=[np.random.randint(0,i-1,num_salt) for i in image.shape]
    noisy[corrds]=1

    num_pep=int(np.ceil(amount*image.size*s_vs_p))
    corrds=[np.random.randint(0,i-1,num_pep) for i in image.shape]
    noisy[corrds]=0 #siyah

    return noisy

img=cv2.imread("Resources/gauss.jpg")
img=img/255
img=cv2.resize(img,(400,400))
noise_img = saltPepperNoise(img)

cv2.imshow("Gaussian Noise",noise_img)


cv2.waitKey(0)
