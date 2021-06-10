# -*- coding: utf-8 -*-
# @Time : 2021/06/10 13:24
# @Author : yunshan
# @File : 尺度不变特征变换SIFT算法.py
import numpy as np
from matplotlib import pyplot as plt

import cv2


def _sift(image,gray_image):
    sift = cv2.xfeatures2d.SIFT_create()
    kp, des = sift.detectAndCompute(gray_image, None)
    image1 = cv2.drawKeypoints(
        image_gray, kp, image, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
    )
    return image1


def _surf(image, gray_image):
    surf = cv2.xfeatures2d.SURF_create()
    kp,des = surf.detectAndCompute(gray_image, None)
    image1 = cv2.drawKeypoints(
        image_gray, kp, image, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
    )

    return image1


if __name__ == "__main__":
    image = cv2.imread(r"../picture_data/jiaodian1.png")
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    plt.subplot(1,2,1)
    plt.imshow(_sift(image,image_gray))
    plt.title("SIFT Image")

    plt.subplot(1,2,2)
    plt.imshow(_surf(image,image_gray))
    plt.title("SURF Image")

    plt.show()
