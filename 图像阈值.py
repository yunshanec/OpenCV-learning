import cv2
from matplotlib import pyplot as plt

img = cv2.imread("../picture_data/zaosheng.png", 0)

# # 应用5种不同的阈值方法
# ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# ret, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
# ret, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
# ret, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
# ret, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
# titles = ["Original", "BINARY", "BINARY_INV", "TRUNC", "TOZERO", "TOZERO_INV"]
# images = [img, th1, th2, th3, th4, th5]
# for i in range(6):
#     plt.subplot(2, 3, i + 1)
#     plt.imshow(images[i])
#     plt.title(titles[i])
# plt.show()

###########################################################################################
# # 自适应阈值
#
# # 固定阈值
# ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
#
# # 自适应阈值 阈值取自相邻区域的平均值
# # cv2.ADAPTIVE_THRESH_MEAN_C
# th2 = cv2.adaptiveThreshold(
#     img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 4
# )
# # 自适应阈值 阈值取自相邻区域的加权和，权重为一个高斯窗口
# # cv2.ADAPTIVE_THRESH_GAUSSIAN_C
# th3 = cv2.adaptiveThreshold(
#     img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 4
# )
#
# titles = ["Original", "Global(v = 127)", "Adaptive Mean", "Adaptive Gaussian"]
# images = [img, th1, th2, th3]
#
# for i in range(4):
#     plt.subplot(2, 2, i + 1)
#     # opencv 打开图片以BGR存储，matplotlib 是以RGB显示。所以需要进行一个通道的转换，才能正常显示。
#     plt.imshow(cv2.cvtColor(images[i],cv2.COLOR_BGR2RGB))
#     plt.title(titles[i])
#
# plt.show()

#################################################################################################
# Otsu's 二值化
# global threshold
# ret1, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# 自适应阈值（高斯自适应）
th1 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 4
)
# Otsu's threshold
ret2, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Otsu's threshold after Gaussian filtering
# (5,5)为高斯内核的大小，0 为标准差
blur = cv2.GaussianBlur(img, (3, 3), 0)
ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
images = [img, th1, th2, blur, th3]

# 可视化
images = [img, 0, th1, img, 0, th2, blur, 0, th3]
titles = ['Original', 'Histogram', 'Global(v=100)',
          'Original', 'Histogram', "Otsu's",
          'Gaussian filtered Image', 'Histogram', "Gaussian+Otsu's"]
for i in range(3):
    # 绘制原图
    plt.subplot(3, 3, i * 3 + 1)
    plt.imshow(images[i * 3], 'gray')
    plt.title(titles[i * 3], fontsize=8)
    # 绘制直方图plt.hist,ravel函数将数组降成一维
    plt.subplot(3, 3, i * 3 + 2)
    plt.hist(images[i * 3].ravel(), 256)
    plt.title(titles[i * 3 + 1], fontsize=8)
    # 绘制阈值图
    plt.subplot(3, 3, i * 3 + 3)
    plt.imshow(images[i * 3 + 2], 'gray')
    plt.title(titles[i * 3 + 2], fontsize=8)
plt.show()