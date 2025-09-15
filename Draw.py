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

#Drawing a Circle 0,
cv.circle(img,(img.shape[1]//2, img.shape[0]//2),40,(0,0,255) , thickness= -1) 
cv.imshow('Circle',img) 

#Drawing a Line 
cv.line(img,(0,0) , (img.shape[1]//2, img.shape[0]//2), (255,255,255),thickness= 3) 
cv.imshow('Line',img)  

#writing Text 
cv.putText(img, 'Hello' ,(255,255), cv.FONT_HERSHEY_COMPLEX, 2.0, (0,255,0),2)  
cv.imshow('Text',img)


cv.waitKey(0) 