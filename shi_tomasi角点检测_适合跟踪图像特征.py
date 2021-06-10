# -*- coding: utf-8 -*-
# @Time : 2021/06/10 11:33
# @Author : yunshan
# @File : shi_tomasi角点检测_适合跟踪图像特征.py
import numpy as np

import cv2

image = cv2.imread(r"../picture_data/jiaodian1.png")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = np.float32(image_gray)

corners = cv2.goodFeaturesToTrack(gray,25,0.01,10)
corners = np.int0(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(image,(x,y),3,(0,0,255),-1)

cv2.imshow("result",image)
cv2.waitKey(0)
