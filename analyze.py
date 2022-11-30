# Python code to read image
import cv2
import json
from json import JSONEncoder
import numpy


# ### SETTINGS ###
snipsignsize = [300, 300]

# landscape
image_path = './images/'
image_filename = '2022 11 12 - Snippet Upper Laser @ Hopla -02358.jpg'
image_path_name = image_path + image_filename

#portrait
# image_path_name = './images/2022 11 12 - Snippet Upper Laser @ Hopla -02546.jpg'


# ### HELPERS ###
class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)
    
    
    
# ### MAIN ###

# To read image from disk, we use
# cv2.imread function, in below method,
img = cv2.imread(image_path_name, cv2.IMREAD_COLOR)
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

b,g,r = (crop[50, 50])
print (r)
print (g)
print (b)

encodedNumpyData = json.dumps(crop, cls=NumpyArrayEncoder)  # use dump() to write array into file
print("Printing JSON serialized NumPy array")
# print(encodedNumpyData)
# [print(i) for i in crop]

file1 = open('./dumps/' + image_filename + '.json', 'w')
file1.write(encodedNumpyData)
file1.close()


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
