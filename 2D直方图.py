import cv2
import numpy as np
from matplotlib import pyplot as plt

# 前面说的一维直方图只考虑了图像的一个特征：灰度值
# 二维直方图要考虑色调Hue(0-180)、饱和度Saturation(0-256)

image = cv2.imread(r'../picture_data/ROI_test.png')
hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)


# OpenCV 实现
opencv_hist2 = cv2.calcHist([hsv],[0,1],None,[180,256],[0,180,0,256])
cv2.imshow("HSV_hist",opencv_hist2)
cv2.waitKey()
cv2.destroyAllWindows()

# NumPy 实现
# h =hsv[0]
# s =hsv[1]
# numpy_hist2, xbins, ybins = np.histogram2d(h.ravel(),s.ravel(),[180,256],[[0,180],[0,256]])
#
#
# plt.imshow(numpy_hist2,interpolation='nearest')
# plt.xlabel("s")
# plt.ylabel('h')
# plt.show()