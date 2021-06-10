import cv2
import numpy as np

frame = cv2.imread("../picture_data/frame.png", 1)
# 转换到HSV
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
# 设定蓝色阈值
lower_blue = np.array([100, 43, 46])
upper_blue = np.array([124, 255, 255])

# 根据阈值构建掩模 mask
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# 对原图和掩模进行位运算
res = cv2.bitwise_and(frame, frame, mask=mask)

# Otsu's threshold after Gaussian filtering
# (5,5)为高斯内核的大小，0 为标准差
gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
ret3, th3 = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# 开运算 去除噪声
kernel = np.ones((8, 8), np.uint8)
opening = cv2.morphologyEx(th3, cv2.MORPH_OPEN, kernel=kernel)
# 画最小外切圆
contours, hierarchy = cv2.findContours(opening, 1, 2)
cnt = contours[0]
(x, y), radius = cv2.minEnclosingCircle(cnt)
center = (int(x), int(y))
radius = int(radius)
img = cv2.circle(frame, center, radius, (0, 255, 0), 2)

cv2.imshow("original", frame)
# cv2.imshow("hsv",hsv)
# cv2.imshow("hsv and mask",res)
# cv2.imshow("Otsu threshold",th3)
# cv2.imshow("Opening",opening)
# cv2.imshow("contours",img)


cv2.waitKey()
cv2.destroyAllWindows()
