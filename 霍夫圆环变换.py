# -*- coding: utf-8 -*-
# @Time : 2021/06/10 09:17
# @Author : yun shan
# @File : 霍夫圆环变换.py
import cv2
import numpy as np

image_gray =cv2.imread(r'../bot_camera/1.bmp',0)

mean_image = cv2.medianBlur(image_gray,5)
c_image = cv2.cvtColor(mean_image,cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(image_gray,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    print((i[0],i[1]))
    # 画圆心
    cv2.circle(c_image, (i[0], i[1]), 1, (0, 255, 0), 3)
    #画圆
    cv2.circle(c_image,(i[0],i[1]),i[2],(0,0,255),2)


cv2.imshow("Detected Circles",c_image)
cv2.waitKey()
cv2.destroyAllWindows()