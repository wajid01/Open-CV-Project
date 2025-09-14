import cv2 as cv 
import numpy as np 

img = cv.imread('Photos/cat.jpg') 
cv.imshow('cat',img)  

#Paint a image on a certain color 

img[50:50, 50:50] = 0,200,0  
cv.imshow('Neo Img',img)  

#Drawing a Rectangle  

cv.rectangle (img,(0,0), (img.shape[1]//2, img.shape[0]//2) ,(0,0,255),thickness=-1) 
cv.imshow('Rectangle',img)    


cv.waitKey(0) 