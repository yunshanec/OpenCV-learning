import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r"../bot_camera/1.bmp",0)
ret2, thresh = cv2.threshold(img,50,255,cv2.THRESH_BINARY_INV)
# 噪声去除 （高斯滤波器 高斯核为5*5）
# 计算图像梯度 使用Sobel算子计算水平方向和竖直方向的一阶倒数
# 非极大值抑制
# 滞后阈值

edges = cv2.Canny(thresh,100,200)

images = [img,edges]
titles = ["Original","Canny"]

cv2.namedWindow("Bin",cv2.WINDOW_NORMAL)
cv2.imshow("Bin",edges)
cv2.waitKey(0)

#

