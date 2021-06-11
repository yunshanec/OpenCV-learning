# -*- coding: utf-8 -*-
# @Time : 2021/06/10 18:30
# @Author : yunshan
# @File : findH.py

import cv2

# 轮廓可以简单地认为成将连续的点连在一起的曲线，具有相同的颜色或者灰度

# 为了更加准确，要是有二值化图像。
# 在寻找轮廓之前，要进行阈值化处理或者Canny边界检测
# 在OpenCV 中，查找轮廓就像在黑色背景中查找白色物体。所以查找的物体要是白色，背景是黑色

img = cv2.imread("../picture_data/coins.png")
tezheng={}

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret2, thresh = cv2.threshold(imgray, 125, 255, cv2.THRESH_BINARY)

#找轮廓
contours,hierarchy = cv2.findContours(
    thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE
)

# 绘制轮廓
draw_img = img.copy()
res = cv2.drawContours(draw_img, contours, -1, (0, 255, 0), 2)

cnt = contours[0]
M = cv2.moments(cnt)

# 轮廓中心
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
tezheng["重心"] = (cx, cy)

# 轮廓面积
area = cv2.contourArea(cnt)
tezheng["面积"] = area


# 轮廓周长
# True确认轮廓是否闭合
perimeter = cv2.arcLength(cnt, True)
tezheng["周长"] = perimeter

# # 轮廓近似???? 准确度参数用在哪了？
# epsilon = 0.1*cv2.arcLength(cnt,True)
# approx = cv2.approxPolyDP(cnt, epsilon,True)


print(tezheng)

cv2.namedWindow("Drawing", cv2.WINDOW_NORMAL)
cv2.imshow("Drawing", thresh)
cv2.waitKey(0)

cv2.destroyAllWindows()

