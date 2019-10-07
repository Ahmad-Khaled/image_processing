import numpy as np 
import cv2

'''
performing various geometrical transformations of 2D images
'''

image = cv2.imread('6.jpg', cv2.IMREAD_GRAYSCALE)
r = 150.0/image.shape[1]
dim = (150, int(image.shape[0]*r))
resized_image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Original resized Gray scale image", resized_image)


def translation(image, x, y):
    M = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    return shifted

def rotation(image, angle, center = None, scale = 1.0):
    (h, w) = image.shape[:2]
    center = (w//2, h//2)
    M = cv2.getRotationMatrix2D(center, 45, 1.0) # Soecifying the rotation and it is normally the center of the image
    rotated_image = cv2.warpAffine(image, M, (w, h))
    return rotated_image

shifted = translation(image, 0, 100) 
cv2.imshow("Shifted Down", shifted)
cv2.waitKey(0)
shifted = translation(image, 0, 100) 
cv2.imshow("Shifted Down", shifted)
cv2.waitKey(0)


