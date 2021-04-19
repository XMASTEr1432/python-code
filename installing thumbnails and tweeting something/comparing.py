import cv2
import os
import numpy as np

img_rgb = cv2.imread('super-mario-bros.jpg') #image where we want to find goomba
template = cv2.imread('goomba.png') #look for goomba
w, h = template.shape[:-1]

res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
threshold = .8
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):  # Switch collumns and rows
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

try:
    cv2.imwrite('result.png', img_rgb)
except:
    cv2.imwrite('result1.png', img_rgb)
    
