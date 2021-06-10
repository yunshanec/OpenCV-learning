# -*- coding: utf-8 -*-
# @Time : 2021/06/10 08:42
# @Author : yunshanec
# @File : 霍夫直线检测.py
import cv2
import numpy as np


def hough_lines(edges):
    """

    :param edges: 二值化图像
    :return: 显示检测后并划线的的图像
    """
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 10)
    for rho, theta in lines[0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))

        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv2.imshow("Hough", image)
    cv2.waitKey(0)


def hough_lines_P(edge, min_Line_Length, max_Line_Gap):
    lines = cv2.HoughLinesP(edge, 1, np.pi / 180, 100, min_Line_Length, max_Line_Gap)
    for x1, y1, x2, y2 in lines[0]:
        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

    cv2.imshow("Hough", image)
    cv2.waitKey(0)


if __name__ == "__main__":
    image = cv2.imread(r"../picture_data/dave.png")
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(image_gray, 50, 150, apertureSize=3)
    hough_lines_P(edges, 100, 10)
