import cv2
import numpy as np

#emilywang
#opencv tutorials
#olin readml
#march 12, 2014

### image addition
x = np.uint8([250])
y = np.uint8([10])

# OpenCV addition vs numpy addition
print cv2.add(x,y) # 250+10 = 260 => 255
print x+y # 250+10 = 260 % 256 = 4


### image blending
# giving different weights to images so it feels like
# they've been blended together

# g(x) = (1-a)*f0(x) + a*f1(x)
# dst = a*img1 = b*img2 + gamma

# example where a = .7, b = .3, gamma = 0
# a + b = 1

img1 = cv2.imread('firefox-logo-300x300.png') 
img2 = cv2.imread('New-Chrome-Icon-300x300.png')

dst = cv2.addWeighted(img1,0.5,img2,0.5,0)

cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()


### bitwise operations
# to be continued!