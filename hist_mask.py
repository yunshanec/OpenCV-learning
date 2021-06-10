import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread(r"../picture_data/ROI_test.png",0)

print(image.shape)

# creat a mask
mask = np.zeros(image.shape[:2],np.uint8)

mask[50:250,100:300] = 255
mask_img = cv2.bitwise_and(image,image,mask=mask)

hist_full = cv2.calcHist([image],[0],None,[256],[0,256])
hist_mask = cv2.calcHist([image],[0],mask,[256],[0,256])

plt.subplot(2,2,1)
plt.imshow(image,'gray')

plt.subplot(2,2,2)
plt.imshow(mask,"gray")

plt.subplot(2,2,3)
plt.imshow(mask_img,'gray')

plt.subplot(2,2,4)
plt.plot(hist_full)
plt.plot(hist_mask)
plt.xlim([0,256])

plt.show()







# cv2.namedWindow("Mask_image",cv2.WINDOW_NORMAL)
# cv2.imshow("Maks_image",mask_img)
# cv2.waitKey()
# cv2.destroyAllWindows()