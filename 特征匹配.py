# -*- coding: utf-8 -*-
# @Time : 2021/06/10 14:32
# @Author : yunshan
# @File : 特征匹配.py
import cv2

image1 = cv2.imread(r"../picture_data/icon.png")
image1_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

image2 = cv2.imread(r"../picture_data/icon _1.png")
image2_gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)


sift = cv2.xfeatures2d.SIFT_create()
kp1,des1 = sift.detectAndCompute(image1_gray,None)
kp2,des2 = sift.detectAndCompute(image2_gray,None)

# BFMatcher with default params
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2,k = 2)
good =[]
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])
image3 = cv2.drawMatchesKnn(image1,kp1,image2,kp2,good[:10],image2,flags=2)

cv2.imshow("Result",image3)
cv2.waitKey(0)


