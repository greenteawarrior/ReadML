import cv2
import numpy as np

#emilywang
#march11, 2014
#opencvtutorials
#coreoperations

img = cv2.imread('messi5.jpg')
px = img[100, 100]
print px

### accessing and modifying pixel values

# accessing RED value
redval = img.item(10, 10, 2)
print redval #50

# modifying RED value
img.itemset((10, 10, 2), 100)
redvalagain = img.item(10, 10, 2)
print redvalagain #100


### accessing image properties

# shape of img
print img.shape 
# if an img is grayscale, the returned tuple
# contains only number of rows and cols

#total number of pixels
print img.size

#img datatype
print img.dtype #useful for debugging!!


### image ROI (region of interest)
#selecting the ball in the image and copying it to another region
# ball = img[280:340, 330:390] 
# img[273:333, 100:160] = ball


### splitting and merging image channels

# when you want to work separately on BGR channels of an image
# (splitting images to single planes)

# split method is less efficient than the numpy method
b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

# OR

# use numpy indexing!
b = img[:,:,0]

# ex. making all the red pixels zero
img[:,:,2] = 0