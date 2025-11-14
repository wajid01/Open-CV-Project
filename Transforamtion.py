import cv2 as cv 
import numpy as np 


#Translation of an image

img = cv.imread('Photos/park.jpg') 
cv.imshow('park',img) 

def translated (img, x,y):  
    transMat = np.float32([[1,0,x],[0,1,y]]) 
    dimensions = (img.shape[1],img.shape[0]) 
    return cv.warpAffine(img,transMat,dimensions)  


translate = translated(img,100,200)
cv.imshow('translate',translate) 


#Rotation of an image 

def rotate(img,angle,rotationpoint=None): 

    (height,width) = img.shape[:2] 

    if rotationpoint is None: 
       rotationpoint= (width//2,height//2)
    
    rotationpoint = cv.getRotationMatrix2D(rotationpoint,angle,1.0) 
    dimensions = (height,width) 

    return cv.warpAffine(img,rotationpoint,dimensions)

rotated = rotate (img,45) 
cv.imshow('Rotaeded',rotated)

#Resizing 




cv. waitKey(0) 

  