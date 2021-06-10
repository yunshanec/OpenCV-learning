import cv2
import numpy as np, sys

# 图像金字塔---具有不同分辨率的原始图像的集合
# 可以使用图像金字塔进行图像融合

img = cv2.imread(r"../picture_data/dave.png")

# cv2.pyrDown() 从一个高分辨率大尺寸的图像向上构建一个金字塔（尺寸变小，分辨率降低）
lower_reso = cv2.pyrDown(img)

# cv2.pyrUp() 从一个低分辨率小尺寸的图像向下构建一个金字塔（尺寸变大，但分辨率不会增加）
heigher_reso = cv2.pyrUp(lower_reso)

cv2.imshow("lower_reso", lower_reso)
cv2.imshow("heigher_reso", heigher_reso)

cv2.waitKey()
