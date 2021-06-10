# 傅里叶变换常被用于分析不同滤波器的频率特性
# 可以使用2D离散傅里叶变换（DFT）分析图像的频域特性

import cv2
import numpy as np
from matplotlib import pyplot as plt

image_gray = cv2.imread(r"../picture_data/girl.jpg", 0)

# Numpy实现
"""
# 快速傅里叶变换FFT

# 做频率变换
f = np.fft.fft2(image_gray)
# 转换像素做幅度谱
fshift = np.fft.fftshift(f)
# 取绝对值：将复数变换成实数取对数的目的为了将数据变化到0-255
magnitude_spectrum = 20*np.log(np.abs(fshift))

# 构建振幅普HPF（高通滤波器）
rows,clos = image_gray.shape
crow,cclos = rows/2,clos/2

fshift[int(crow-30):int(crow+30),int(cclos-30):int(cclos+30)] = 0
f_ishift = np.fft.ifftshift(fshift)
image_back = np.fft.ifft2(f_ishift)
image_back = np.abs(image_back)

plt.subplot(1,4,1)
plt.imshow(image_gray,'gray')
plt.title("Input_image")

plt.subplot(1,4,2)
plt.imshow(magnitude_spectrum)
plt.title('Magnitude Spectrum')

plt.subplot(1,4,3)
plt.imshow(image_back,'gray')
plt.title("Image after HPF")

plt.subplot(1,4,4)
plt.imshow(image_back)
plt.title("Result in JET")

plt.show()

"""

# Opencv实现
dft = cv2.dft(np.float32(image_gray), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

# magnitude_spectrum = 20 * np.log(np.abs(dft_shift))

rows, cols = image_gray.shape
crow, ccol = int(rows / 2), int(cols / 2)
# create a mask first, center square is 1, remaining all zeros
mask = np.zeros((rows, cols, 2), np.uint8)
mask[crow - 30 : crow + 30, ccol - 30 : ccol + 30] = 1
# apply mask and inverse DFT
fshift = dft_shift * mask
f_ishift = np.fft.ifftshift(fshift)
image_back = cv2.idft(f_ishift)
image_back = cv2.magnitude(image_back[:, :, 0], image_back[:, :, 1])


plt.subplot(1, 4, 1)
plt.imshow(image_gray, "gray")
plt.title("Input_image")
#
# plt.subplot(1, 4, 2)
# plt.imshow(magnitude_spectrum)
# plt.title("Magnitude Spectrum")

plt.subplot(1, 4, 3)
plt.imshow(image_back, "gray")
plt.title("Image after HPF")

plt.subplot(1, 4, 4)
plt.imshow(image_back)
plt.title("Result in JET")

plt.show()

