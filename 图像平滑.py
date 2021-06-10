import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"../picture_data/wenli.png", 1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 2D卷积
# kernel = np.ones((5,5), np.float32)/25
# dst = cv2.filter2D(img,3,kernel)

# 图像模糊（平均）
# 用卷积框覆盖区域所有像素的平均值来代替中心元素
blur = cv2.blur(img, (5, 5))
boxFilter = cv2.boxFilter(img, -1, (5, 5))

# 高斯模糊 （高斯核的宽和高必须是奇数,标准差自己设定）
gaussianBlur = cv2.GaussianBlur(img, (5, 5), 0)

# 中值模糊 （用与卷积框对应像素的中值代替中心像素的值）
# 该滤波器常用于除椒盐噪声，卷积核的大小也是奇数
medianBlur = cv2.medianBlur(img, 5)

# 双边滤波 （在保持边界清晰的情况下有效的去除噪声）
# 9个领域直径，两个75分别是空间高斯函数标准差，灰度值相似的高斯函数标准差
bilateral_blur = cv2.bilateralFilter(img, 9, 75, 75)


plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title("Original")

plt.subplot(1, 2, 2)
plt.imshow(bilateral_blur)
plt.title("bilateral_blur")

plt.show()
