import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread(r"../picture_data/wiki.png", 0)

# Numpy matplotlib 实现
# # flatten() 将数组变成一维
# hist, bins = np.histogram(image.flatten(), 256, [0, 256])
#
# # 计算累积分布图
# cdf = hist.cumsum()
# cdf_normalized = cdf * hist.max() / cdf.max()
#
#
# # 直方图均衡化
# # 构建Numpy 掩模数组，cdf 为原数组，当数组元素为0时，掩盖
# cdf_mask = np.ma.masked_equal(cdf, 0)
# cdf_mask = (cdf_mask - cdf_mask.min()) * 255 / (cdf_mask.max() - cdf_mask.min())
# # 对被掩盖的元素赋值，此处赋值为0
# cdf1 = np.ma.filled(cdf_mask, 0).astype("uint8")
# # 均衡化后的图像image1
# equal_image = cdf1[image]
# hist1, bins1 = np.histogram(equal_image.flatten(), 256, [0, 256])
#
# # 计算累积分布图
# cdf1 = hist1.cumsum()
# cdf_equalization = cdf1 * hist1.max() / cdf1.max()
#
# # 计算累积分布图
# cdf_mask = cdf1 * hist.max() / cdf1.max()
#
#
# # 原图 累积分布图和直方图
# plt.plot(cdf_normalized, color="b")
# plt.hist(image.flatten(), 256, [0, 256], color="b")
#
# # 均衡化后图像的累计分布图和直方图
# plt.plot(cdf_equalization, color="r")
# plt.hist(equal_image.flatten(), 256, [0, 256], color="r")
#
#
# plt.xlim([0, 256])
# plt.legend(
#     ("cdf_normalized", "original_histogram", "cdf_equalization", "equalization_hist"),
#     loc="upper left",
# )
# plt.show()

# OpenCV 实现
# equ = cv2.equalizeHist(image)
# res = np.hstack((image,equ))
# cv2.imshow("After",res)
# cv2.waitKey()

# 自适应直方图均衡化 提升图像对比度的一种方法
clahe = cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
cl1 = clahe.apply(image)
cv2.imshow("After",cl1)
cv2.waitKey()
