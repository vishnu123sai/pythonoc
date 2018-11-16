import numpy as np
import cv2
import matplotlib.pyplot as plt

img1=cv2.imread('image1.jpg',0)
img2=cv2.imread('image2.jpg',0)


sift=cv2.ORB()
dest1 = sift.detectAndCompute(img1,None)
dest2 = sift.detectAndCompute(img2,None)

bf=cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches=bf.knnMatch(dest1,dest2,k=2)

good = []

for m,n in matches :
    if m.distance < 0.75*n.distanc:
        good.append([m])

img3=cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,flags=2)

plot.imshow(img3)
plot.show()
