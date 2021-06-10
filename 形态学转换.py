import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r"../picture_data/j.png")
# 设定平滑卷积核
kernel = np.ones((5, 5), np.uint8)
# 腐蚀
erosion = cv2.erode(img, kernel, iterations=3)

# 膨胀
dilation = cv2.dilate(img, kernel, iterations=1)

# 开运算（先腐蚀再膨胀）用来去除噪声
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# 闭运算（先膨胀在腐蚀）用来填充前景物体中的小洞，或者小黑点
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# 礼帽运算 原始图像与进行开运算之后得到的图像的差
# dst = tophat(src,element)= src - open(src,element)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

# 黑帽运算 进行闭运算之后得到的图像与原始图像的差
# dst = blackhat(src,element) =close(src,element) - src
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)


plt.subplot(1, 3, 1)
plt.imshow(img)
plt.title("Original")

plt.subplot(1, 3, 2)
plt.imshow(tophat)
plt.title("erosion")

plt.subplot(1, 3, 3)
plt.imshow(blackhat)
plt.title("closing")

plt.show()
