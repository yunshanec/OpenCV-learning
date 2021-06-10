# # 用于来做图像分割，或者在图像中寻找我们感兴趣的区域
#
# import cv2
# import numpy as np
#
# # roi 需要查找区域
# roi = cv2.imread(r"../picture_data/girl_head.jpg")
# hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
#
# # 查找目标区域
# target = cv2.imread(r"../picture_data/girl.jpg")
# hsvt = cv2.cvtColor(target, cv2.COLOR_BGR2HSV)
#
# # 目标直方图
# M = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
# # 待搜索直方图
# I = cv2.calcHist([hsvt], [0, 1], None, [180, 256], [0, 180, 0, 256])
#
# # 计算反向投影R
# R = M / I
# h, s, v = cv2.split(hsvt)
# B = R[h.ravel(), s.ravel()]
# B = np.minimum(B, 1)
# B = B.reshape(hsvt.shape[:2])
#
# # 卷积
# disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
# B = cv2.filter2D(B, -1, disc)
# B = np.uint8(B)
# cv2.normalize(B, B, 0, 255, cv2.NORM_MINMAX)
# cv2.imshow("B", B)
#
# # 二值化
# ret, thresh = cv2.threshold(B, 50, 255, 0)
# cv2.imshow("thresh", thresh)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
##################################################################
import cv2
import numpy as np

# ROI区域
roi = cv2.imread(r"../picture_data/girl_head.jpg")
hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
# 目标搜索区域
target = cv2.imread(r"../picture_data/girl.jpg")
hsvt = cv2.cvtColor(target, cv2.COLOR_BGR2HSV)
# calculating object histogram
roihist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
# normalize histogram and apply backprojection
# 归一化：原始图像，结果图像，映射到结果图像中的最小值，最大值，归一化类型
# cv2.NORM_MINMAX 对数组的所有值进行转化，使它们线性映射到最小值和最大值之间
# 归一化之后的直方图便于显示，归一化之后就成了 0 到 255 之间的数了。
cv2.normalize(roihist, roihist, 0, 255, cv2.NORM_MINMAX)
dst = cv2.calcBackProject([hsvt], [0, 1], roihist, [0, 180, 0, 256], 1)
# Now convolute with circular disc
# 此处卷积可以把分散的点连在一起
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
dst = cv2.filter2D(dst, -1, disc)
# threshold and binary AND
ret, thresh = cv2.threshold(dst, 50, 255, 0)
# 别忘了是三通道图像，因此这里使用 merge 变成 3 通道
thresh = cv2.merge((thresh, thresh, thresh))
# 按位操作
res = cv2.bitwise_and(target, thresh)
res = np.hstack((target, thresh, res))
cv2.imwrite("res.jpg", res)
# 显示图像
cv2.imshow("1", res)
cv2.waitKey(0)
