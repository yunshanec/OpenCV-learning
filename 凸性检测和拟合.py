import cv2
import numpy as np

image = cv2.imread(r"../picture_data/change.png")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# 找轮廓
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# 在原图上绘制轮廓
draw_img = image.copy()
res = cv2.drawContours(image, contours, -1, (0, 255, 0), 2)


cnt = contours[0]

# 检测曲线是不是为凸的，返回True/False
k = cv2.isContourConvex(cnt)
print(k)

# 边界矩形有两种
# 直边界矩形
x, y, w, h = cv2.boundingRect(cnt)
img_bounding_Rectangle = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)


# 旋转的边界矩形(最小外接矩形)
# 返回Box2D结构，其中包含矩形左上角角点的坐标（x,y）,矩形的宽和高（w,h）以及旋转角度。
points = cv2.minAreaRect(cnt)
print(points)
# 绘制矩形需要四个角点，可以通过cv2.boxPoints()获得
box = cv2.boxPoints(points)
box = np.int0(box)
img_minRectangle = cv2.drawContours(image, [box], 0, (0, 0, 255), 2)

# 最小外接圆
(x, y), radius = cv2.minEnclosingCircle(cnt)
center = (int(x), int(y))
radius = int(radius)
img_min_circle = cv2.circle(image, center, radius, (255, 255, 0), 2)

# 椭圆拟合
ellipse = cv2.fitEllipse(cnt)
img_ellipse = cv2.ellipse(image, ellipse, (0, 255, 255), 2)

# 直线拟合
rows, cols = image.shape[:2]
[vx, vy, x, y] = cv2.fitLine(cnt, cv2.DIST_L2, 0, 0.01, 0.01)
lefty = int((-x * vy / vx) + y)
righty = int(((cols - x) * vy / vx) + y)
img_line = cv2.line(image, (cols - 1, righty), (0, lefty), (0, 255, 0), 2)


cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.imshow("image", image)
cv2.waitKey()
cv2.destroyAllWindows()
