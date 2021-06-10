import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread(r"../picture_data/frame.png")

colors = ('b', 'g', 'r')
for i,color in enumerate(colors):
    hist_tr = cv2.calcHist([image],[i],None,[256],[0,256])
    plt.plot(hist_tr,color = color)
    plt.xlim([0,255])
# hist 是一个256*1 的数组，每一个值代表了与次灰度值对应的像素点数目
plt.hist(image.ravel(),256,[0,256])
plt.show()
