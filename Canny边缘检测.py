import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r"../picture_data/dave.png")

# 噪声去除 （高斯滤波器 高斯核为5*5）
# 计算图像梯度 使用Sobel算子计算水平方向和竖直方向的一阶倒数
# 非极大值抑制
# 滞后阈值
edges = cv2.Canny(img,100,200)

images = [img,edges]
titles = ["Original","Canny"]

for i in range(2):
    plt.subplot(1,2,i+1)
    plt.imshow(images[i],"gray")
    plt.title(titles[i])

plt.show()
