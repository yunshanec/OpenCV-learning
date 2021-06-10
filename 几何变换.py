import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("../picture_data/test_1.png", 1)
rows, cols = img.shape[:2]

# 翻转图片
# 其中第二个参数  等于0：垂直翻转(沿x轴) 大于0：水平翻转（沿y轴） 小于0：水平垂直翻转
# dst = cv2.flip(img, 0)

# 平移图片
# 首先要定义平移矩阵
# x axis move 100, y axis move 50, need numpy float32
# M = np.float32([[1, 0, 100], [0, 1, 50]])
# dst = cv2.warpAffine(img, M, (rows, cols))

# 旋转图像
# 旋转中心，旋转角度（正数表示逆时针旋转），缩放比例（0.5表示缩小一半）
# M = cv2.getRotationMatrix2D((cols/2,rows/2),45,0.5)
# dst = cv2.warpAffine(img,M,(cols,rows))

# 仿射变换
# pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
# pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
# 构建仿射变换矩阵
# M = cv2.getAffineTransform(pts1, pts2)
# dst = cv2.warpAffine(img, M, (cols, rows))

# 透视变换
pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
# 构建透视变换矩阵
M = cv2.getPerspectiveTransform(pts1, pts2)
# 仿射
dst = cv2.warpPerspective(img, M, (rows,cols))


plt.subplot(121)
plt.imshow(img)
plt.title("Input")

plt.subplot(122)
plt.imshow(dst)
plt.title("Output")

plt.show()
