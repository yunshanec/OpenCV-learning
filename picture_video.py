import cv2


# 图片基础操作
def picture():
    # 读取图片
    img = cv2.imread("../picture_data/test.png", -1)
    # 隨意調整窗口的大小
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    # 显示图片
    cv2.imshow("image", img)

    # 保存圖片
    keyword = cv2.waitKey(0)
    if keyword == 27 :
        # 釋放窗口
        cv2.destroyAllWindows()

    elif keyword == ord("s") :
        cv2.imwrite("result.png", img)
        cv2.destroyAllWindows()


# 视频基础操作
def video() :
    capture = cv2.VideoCapture(0)
    while True :
        # 获取一帧照片
        ret, frame = capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("BGR2GRAY", gray)
        if cv2.waitKey(1) == ord("q") :
            break


if __name__ == "__main__" :
    picture()
    #video()
