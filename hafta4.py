import cv2
import numpy as np
import matplotlip as plt

img=cv2.imread("histImg.jpg")
cv2.imshow("img",img)


cv2.waitKey(0)