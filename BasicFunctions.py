import cv2 as cv 

img =  cv.imread('Photos/park.jpg') 
cv.imshow('Park',img) 

#converting to gray scale 

gray = cv.cvtColor (img, cv.COLOR_BGR2GRAY) 
cv.imshow('Gray img',gray) 

#Blur 

blur = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

#Edge Cascade 

canny = cv.Canny(blur,255,255) 
cv.imshow('canny', canny)  

#Dialating an image 

Dialating = cv.dilate(canny,(2,2),iterations=2) 
cv.imshow('Dialated Image',Dialating)

#Eroding  

Eroding = cv.erode(Dialating,(2,2), iterations=1) 
cv.imshow('Eroded',Eroding) 

#Resizing 
resize = cv.resize(img,(500,500))   #interplation is used by default in this function 
                                    #but we can used it for different reason making a 
                                    # image smaller then the aspect ratio we wil use 
                                    # cv. Interplation_Area , for making a image bigger 
                                    # then the aspect ratio we will use Interpolatin_Linear 
                                    # or for better result Interpolation_Cubic which is slow 
                                    # but the results are good in quality   
cv.imshow('Resize Image',resize)



#Croping 

Cropped = img[50:200, 200:400] 
cv.imshow('Cropped',Cropped)  

cv.waitKey(0) 