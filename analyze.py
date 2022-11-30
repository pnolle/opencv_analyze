# Python code to read image
import cv2
import json
from json import JSONEncoder
import numpy
import base64
import zlib


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

# b,g,r = (crop[50, 50])
# print (r)
# print (g)
# print (b)

# previous_pixel = crop[0][0]
# eq_pix_cnt = 0
# pix_cnt = 0
# for i in range(len(crop)):
#     for j in range(len(crop[i])):
#         pix_cnt += 1
#         if (numpy.array_equal(previous_pixel, crop[i][j])):
#             eq_pix_cnt += 1
#             print('equal pixel %d/%d found' %(eq_pix_cnt, pix_cnt))
#             # print('equal pixel %d/%d found' %(eq_pix_cnt) %(pix_cnt)) #, crop[i][j])
#         previous_pixel = crop[i][j]
#         # print('j',j, crop[i][j])

encodedNumpyData = json.dumps(crop, cls=NumpyArrayEncoder).replace(" ", "")  # use dump() to write array into file
print('json len', len(encodedNumpyData))

bNumpyData = bytes(encodedNumpyData, 'utf-8')
b64NumpyData = base64.b64encode(bNumpyData)
zlibNumpyData = zlib.compress(b64NumpyData)
print('zlib len', len(zlibNumpyData))

# compressed = 'eJwdktkNgDAMQxfqR+5j/8V4QUJQUttx3Nrzl0+f+uunPPpm+Tf3Z/tKX1DM5bXP+wUFA777bCob4HMRfUk14QwfDYPrrA5gcuQB49lQQxdZpdr+1oN2bEA3pW5Nf8NGOFsR19NBszyX7G2raQpkVUEBdbTLuwSRlcDCYiW7GeBaRYJrgImrM3lmI/WsIxFXNd+aszXoRXuZ1PnZRdwKJeqYYYKq6y1++PXOYdgM0TlZcymCOdKqR7HYmYPiRslDr2Sn6C0Wgw+a6MakM2VnBk6HwU6uWqDRz+p6wtKTCg2WsfdKJwfJlHNaFT4+Q7PGfR9hyWK3p3464nhFwpOd7kdvjmz1jpWcxmbG/FJUXdMZgrpzs+jxC11twrBo3TaNgvsf8oqIYwT4r9XkPnNC1XcP7qD5cW7UHSJZ3my5qba+ozncl5kz8gGEEYOQ'
# data = zlib.decompress(base64.b64decode(compressed))

file1 = open('./dumps/' + image_filename + '.b64.zlib', 'wb')
# file1.write(encodedNumpyData)
file1.write(zlibNumpyData)
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
