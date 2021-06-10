# -*- coding: utf-8 -*-
# @Time : 2021/06/10 10:59
# @Author : yunshan
# @File : Harris角点检测.py
import numpy as np

import cv2

image = cv2.imread(r"../picture_data/jiaodian1.png")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = np.float32(image_gray)

# 第一种检测
# dst = cv2.cornerHarris(gray, 2, 3, 0.04)
# dst = cv2.dilate(dst, None)
# image[dst > 0.01*dst.max()] = [0,0,255]

# 亚像素级
dst = cv2.cornerHarris(gray, 2, 3, 0.04)
dst = cv2.dilate(dst, None)

ret, dst = cv2.threshold(dst, 0.01 * dst.max(), 255, 0)
dst = np.uint8(dst)

ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners = cv2.cornerSubPix(gray, np.float32(centroids), (5, 5), (-1, -1), criteria)
res = np.hstack((centroids, corners))
res = np.int0(res)

image[res[:, 1], res[:, 0]] = [0, 0, 255]
image[res[:, 3], res[:, 2]] = [0, 255, 0]


cv2.imshow("dst", image)
cv2.waitKey(0)
