import cv2
import numpy as np

image = cv2.imread(r"../picture_data/change.png")
image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(image_gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

counters, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

cnt = counters[0]

mask = np.zeros(image_gray,np.uint8)
counters = cv2.drawContours(mask,[cnt],0,255,-1)
pixel_points = np.transpose(np.nonzero(mask))

cv2.namedWindow("mask",cv2.WINDOW_NORMAL)
cv2.imshow("mask",counters)
cv2.waitKey()
cv2.destroyAllWindows()