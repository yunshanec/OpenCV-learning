# -*- coding: utf-8 -*-
# @Time : 2021/06/10 09:48
# @Author : yunshan
# @File : 分水岭图像分割.py
import cv2
import numpy as np

image = cv2.imread(r'../picture_data/coins_fenkai.png')
image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# 二值化
ret,thresh = cv2.threshold(image_gray,0,255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# 形态学操作 去除噪声
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
mb = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel,iterations=2)

# 膨胀
sure_bg= cv2.dilate(mb,kernel,iterations=2)

# 获取距离变换获取确定的前景色
dist = cv2.distanceTransform(mb,cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist,dist.max()*0.6,255,cv2.THRESH_BINARY)
sure_fg = np.uint8(sure_fg)
# finding unknown region
unknown = cv2.subtract(sure_bg,sure_fg)

# make label
ret,markers1 = cv2.connectedComponents(sure_fg)
# Add one to all labels so that sure background is not 0,but 1
makers = markers1+1
# Now, make the region of unknown with zero
makers[unknown==255] = 0

# 使用JET 颜色地图表示
makers3 = cv2.watershed(image,makers)
image[makers == -1] = [255,0,0]

# 归一化的距离图像数组 骨骼图像
dist_output= cv2.normalize(dist,0,1.0,cv2.NORM_MINMAX)


cv2.imshow("result",image)
cv2.waitKey(0)
cv2.destroyAllWindows()