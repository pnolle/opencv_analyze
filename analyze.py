# Python code to read image
import cv2

snipsignsize = [300, 300]

# landscape
image_filename = './images/2022 11 12 - Snippet Upper Laser @ Hopla -02358.jpg'

#portrait
# image_filename = './images/2022 11 12 - Snippet Upper Laser @ Hopla -02546.jpg'

# To read image from disk, we use
# cv2.imread function, in below method,
img = cv2.imread(image_filename, cv2.IMREAD_COLOR)
imgshape = img.shape

if imgshape[0] <= imgshape[1]:
    factor = snipsignsize[0]/imgshape[0]
else:
    factor = snipsignsize[1]/imgshape[1]
    
imgshape0 = int(imgshape[0]*factor)
imgshape1 = int(imgshape[1]*factor)
resized = cv2.resize(img, (imgshape1, imgshape0))
imgshape = resized.shape

start0 = 0
start1 = 0
end0 = snipsignsize[0]
end1 = snipsignsize[1]
if imgshape[0] < imgshape[1]:
    half = (imgshape[1]-imgshape[0])/2
    start1 = int(half)
    end1 = int(imgshape[1]-half)
elif imgshape[0] > imgshape[1]:
    half = (imgshape[0]-imgshape[1])/2
    start0 = int(half)
    end0 = int(imgshape[0]-half)

crop = resized[start0:end0, start1:end1]

b,g,r = (img[50, 50])
print (r)
print (g)
print (b)

# Creating GUI window to display an image on screen
# first Parameter is windows title (should be in string format)
# Second Parameter is image array
cv2.imshow("image", img)
cv2.imshow("resized", resized)
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
