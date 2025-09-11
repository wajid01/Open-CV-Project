import cv2 as cv 

#resizing images 

img = cv.imread('Photos/cat.jpg') 
cv.imshow('cat',img) 
cv.waitKey(0)  

def rescalerFrame(frame,scale = 0.75): 
    width = int(frame.shape[1] * scale)  
    height = int(frame.shape1[0] * scale) 
    dimensions = (width,height) 

    return cv.resize (frame,dimensions ,interpolation=cv.INTER_AREA)
cv.waitKey(0) 



