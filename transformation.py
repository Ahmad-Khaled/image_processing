import numpy as np 
import cv2

image = cv2.imread('6.jpg', cv2.IMREAD_GRAYSCALE)
r = 150.0/image.shape[1]
dim = (150, int(image.shape[0]*r))
resized_image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Original resized Gray scale image", resized_image)


def translation(image, x, y):
    M = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    return shifted

shifted = translation(image, 0, 100) 
cv2.imshow("Shifted Down", shifted)
cv2.waitKey(0)


