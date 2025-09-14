import cv2 as cv 
import numpy as np 

img = cv.imread('Photos/cat.jpg') 
cv.imshow('cat',img)  

#Paint a image on a certain color 

img[100:100, 100:100] = 0,200,0  
cv.imshow('Neo Img',img) 





cv.waitKey(0) 