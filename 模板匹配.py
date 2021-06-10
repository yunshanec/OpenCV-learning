import cv2
import numpy as np


def match_template(image, template, method_num):
    """

    :param image: RGB image
    :param template: Template image
    :param method_num: one of six methods
    :return: 匹配后的图像
    """
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    w, h = template_gray.shape[::-1]
    # All the 6 methods for comparison in a list
    methods = [
        "cv2.TM_CCOEFF",
        "cv2.TM_CCOEFF_NORMED",
        "cv2.TM_CCORR",
        "cv2.TM_CCORR_NORMED",
        "cv2.TM_SQDIFF",
        "cv2.TM_SQDIFF_NORMED",
    ]
    # for meth in methods:
    # exec 语句用来执行储存在字符串或文件中的 Python 语句。
    # 例如,我们可以在运行时生成一个包含 Python 代码的字符串,
    # 然后使用 exec 语句执行这些语句。

    # Apply template Matching
    res = cv2.matchTemplate(image_gray, template_gray, method_num)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    # 使用不同的比较方法,对结果的解释不同
    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if methods[int(method_num) - 1] in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc

    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(image, top_left, bottom_right, 255, 2)
    cv2.imshow("method: {}".format(methods[int(method_num) - 1]), image)
    cv2.waitKey(0)


# 多对象的模板匹配
def multiple_objects(img_bgr, template, threshold):
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_RGB2GRAY)
    w, h = template_gray.shape[::-1]
    res = cv2.matchTemplate(img_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_bgr, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 1)
    # cv2.imwrite('res.png',img_rgb)
    cv2.imshow("result", img_bgr)
    cv2.waitKey(0)


if __name__ == "__main__":
    img = cv2.imread(r"../picture_data/girl.jpg")
    template = cv2.imread(r"../picture_data/girl_head.jpg")
    match_template(img, template, 3)
