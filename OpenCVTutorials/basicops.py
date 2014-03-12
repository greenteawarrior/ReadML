import cv2
import numpy as np

#emilywang
#march11, 2014
#opencvtutorials
#coreoperations

img = cv2.imread('messi5.jpg')
px = img[100, 100]
print px

# accessing RED value
redval = img.item(10, 10, 2)
print redval #50

# modifying RED value
img.itemset((10, 10, 2), 100)
redvalagain = img.item(10, 10, 2)
print redvalagain #100

# shape of img
print img.shape 
# if an img is grayscale, the returned tuple
# contains only number of rows and cols

#total number of pixels
print img.size

#img datatype
print img.dtype #useful for debugging!!


### image ROI (region of interest)
