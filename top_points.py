import cv2
import rrcvutils
import numpy as np


def find_circle_center(image_path):
    image = cv2.imread(image_path)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(
        image_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
    )
    kernel = np.ones((5, 5), np.uint8)
    # 膨胀
    erosion = cv2.dilate(thresh, kernel, iterations=5)
    # 腐蚀
    binary = cv2.erode(erosion, kernel, iterations=5)

    # 找轮廓
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    idx = rrcvutils.find_topk_area_contours_indices(contours)[0]

    # 画轮廓
    res = cv2.drawContours(image, contours, -1, (0, 0, 255), 3)

    cnt = contours[idx]

    # 最小外接圆
    (x, y), radius = cv2.minEnclosingCircle(cnt)
    center = (int(x), int(y))
    center1 = [int(x), int(y)]

    print("最小外接圆圆心： {}".format(center))
    radius = int(radius)
    img_min_circle = cv2.circle(image, center, radius, (255, 0, 0), 3)

    M = cv2.moments(cnt)
    # 轮廓中心
    cx = int(M["m10"] / M["m00"])
    cy = int(M["m01"] / M["m00"])

    rrcvutils.imshow(image, win_name="src")
    rrcvutils.imshow(image_gray, win_name="gray")
    rrcvutils.imshow(binary, win_name="bin", wait_key_ms=0)

    return [cx, cy]
    # return center1


if __name__ == "__main__":
    ls_points = []
    for i in range(1, 10):
        point = find_circle_center("../top_camera/{}.bmp".format(i))
        print("轮廓中心： {}".format(point))
        ls_points.append(point)

    print(ls_points)
