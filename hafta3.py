import cv2
import numpy as np
import matplotlip as plt

img=cv2.imread("Resources/car.jpg")
#cv2.imshow("img",img)

#print(img.shape)
#print(img.size)
#print(img.dtype)

#MATRISLE GORUNTU OLUSTURMA
#zero=black
img2=np.zeros((300,300,3),np.uint8)
#print(img)
#img[100:250]=255,0,0
#ÇİZGİ OLUŞTURMA
cv2.line(img2,(0,0),(200,200),(0,255,0),3)
#cv2.imshow("image",img2)

#İKİLİ GÖRÜNTÜ
height=512
width=512
img3=np.random.randint(255,size=(height,width,1),dtype=np.uint8)
#cv2.imshow("binary",img3)

#VEKTORLERDE INDEKSLEME
v=[1,4,7,9,11]
print(v)
value=v[0]
#print(value)

t=np.transpose(v)
#print(t)

value=v[1:3] #1den baslayıp 3.elemana kadar. 3 dahil değil
value=v[2:] #2den baslayıp son elemana kadar
value=v[1::3] #1den baslayıp 1er artarak 3.elemana kadar
value=v[::-2]
#print(value)

#MATRISLERDE INDEKSLEME
A=[[1,4,7],  #iç içe liste
   [8,9,11],
   [-1,-5, 2],
   [0,10,20]]

print("A",A)
print("A[1]",A[1])
print("A[2][2]",A[2][2])
print("A[0][-1]",A[0][-1]) #ilk satırın son elemanı

#NUMPY İLE MATRİS OLUSTURMA
a=np.array([[1,4,7],
            [8,9,11],
             [-1,-5, 2],
            [0,10,20]])

print(type(a))
print("a=",a)
print("a[1]",a[1])
print("a[2][2]",a[2][2])
print("a[0][-1]",a[0][-1])

print("********")
C = np.array([[1, 4, 2], [3, 5, 7], [99, 66, 79]])
print(C[:,2])
print(C[1,:])




cv2.waitKey(0)
