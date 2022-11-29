# Python code to read image
import cv2
import os
print(os.getcwd())

image_filename = '2022 11 12 - Snippet Upper Laser @ Hopla -02358.jpg'
# image_filename = 'pic23-200x141.png'

# To read image from disk, we use
# cv2.imread function, in below method,
img = cv2.imread(image_filename, cv2.IMREAD_COLOR)

print (img.shape)
crop = img[50:180, 100:300]

b,g,r = (img[50, 50])
print (r)
print (g)
print (b)

# Creating GUI window to display an image on screen
# first Parameter is windows title (should be in string format)
# Second Parameter is image array
cv2.imshow("image", img)
cv2.imshow("crop", crop)

# To hold the window on screen, we use cv2.waitKey method
# Once it detected the close input, it will release the control
# To the next line
# First Parameter is for holding screen for specified milliseconds
# It should be positive integer. If 0 pass an parameter, then it will
# hold the screen until user close it.
cv2.waitKey(0)

# It is for removing/deleting created GUI window from screen
# and memory
cv2.destroyAllWindows()