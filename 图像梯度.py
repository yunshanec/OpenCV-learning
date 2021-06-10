import cv2
import numpy as np
from matplotlib import pyplot as plt

# 梯度简单来说就是求导，OpenCV提供了三种不同的高通滤波器

# Scharr Sobel 是一阶求导
# Sobel 算子是高斯平滑与微分操作的结合体，抗噪声能力很好
# laplacian 算子是二阶求导


img = cv2.imread(r"../picture_data/dave.png", 0)

# cv2.CV_64F 输出图像的深度（数据类型），可以使用-1，与原图像保持一致 np.uint8
laplacian = cv2.Laplacian(img, cv2.CV_64F)

# 参数1,0 为只在x方向求一阶导数，最大可求二阶导数
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)

# 参数0,0 为只在y方向求一阶导数，最大可求二阶导数
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

plt.subplot(2,2,1)
plt.imshow(img,cmap='gray')
plt.title('Original')
plt.subplot(2,2,2)
plt.imshow(laplacian,cmap='gray')
plt.title('laplacian')
plt.subplot(2,2,3)
plt.imshow(sobel_x,cmap='gray')
plt.title('sobel_x')
plt.subplot(2,2,4)
plt.imshow(sobel_y,cmap='gray')
plt.title('sobel_y')

plt.show()
