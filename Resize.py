import cv2 as cv 
import numpy as np 

#resizing images 

img = cv.imread('Photos/cat.jpg') 
cv.imshow('cat',img) 
cv.waitKey(0)  

def rescalerFrame(frame,scale = 0.75): 
   
    width = int(frame.shape[1] * scale)  
    height = int(frame.shape[0] * scale) 
    dimensions = (width,height) 

    return cv.resize (frame,dimensions ,interpolation=cv.INTER_AREA)
cv.waitKey(0) 


resize_images = rescalerFrame(img) 
cv.imshow('image',resize_images) 


# Resizing Videos Files 
capture = cv.VideoCapture('Videos/dog.mp4')

while True: 
 
 isTrue, frame = capture.read()   
 #We can multiply the frame by scale to adjust the video size in this example scale = .2(20%)
 frame_resized = rescalerFrame(frame ,scale=.2)
 
 cv.imshow('Video', frame)  
 cv.imshow('video Resized',frame_resized) 

 if cv.waitKey(20) & 0xFF==ord('d'): 
  break 

capture.release() 
cv.destroyAllWindows() 
  


