# -*- coding: utf-8 -*-
# @Time : 2021/06/11 11:47
# @Author : yunshan
# @File : ORB快速特征点提取和描述.py

import cv2

image = cv2.imread("../picture_data/jiaodian.png",0)
image1 = cv2.imread("../picture_data/jiaodian1.png",0)

# initiate SIFT detector
orb = cv2.ORB_create()

# find the keypoints and descriptors with SIFT
kp,des = orb.detectAndCompute(image,None)
kp1,des1 = orb.detectAndCompute(image1,None)

# creat BFMatch object
bf = cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck = True)




image2 = cv2.drawKeypoints(image,kp1,outImage=image,color=(0,255,0),flags=0)

cv2.imshow("Image2",image2)
cv2.waitKey()