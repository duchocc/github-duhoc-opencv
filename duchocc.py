

import cv2
from cv2 import waitKey
import numpy


img = cv2.imread("IMG_4454.jpg")
blur_img = cv2.blur(img, (100, 100))


mask = numpy.zeros(img.shape, dtype=numpy.uint8)
mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
cv2.circle(mask, (1210, 2280), 280, 255, -1)
first_img = cv2.bitwise_and(blur_img, blur_img, mask=mask)

mask_inv = cv2.bitwise_not(mask)
second_img = cv2.bitwise_and(img, img, mask=mask_inv)

img = first_img + second_img


#cv2.imshow('duchocc', numpy.concatenate((first_img, second_img), axis = 1))
cv2.imshow('duchocc', img)
waitKey(0)

