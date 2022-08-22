## This codes is an introduction to image processing and different functions we will use during the class.
## There are different libraries that
## libraries
import numpy as np # library for mathematical ecuations
import cv2 as cv # image processing
import matplotlib.pyplot as plt # figures and graphs (shares some functionality wiht cv2)
import pandas as pd # Data analisis.
## there are different aplications we need for the course
# opening an image
# this function allows you to read an image remeber that unless the image is in the same folder as
# the source code it is necesary to use the full path of the image.
image = cv.imread('filename')
size = image.ndarray.shape() # gets the shape of the image, there are different options with pillow lib
x,y = size/2
v_newsize = [x,y]  # new dimensions for the fucntion
halfSize = cv.resize(image,v_newsize) # changes the size of the image (you can see this function for lab 01)}
## exampe using pillow
# from the pillow library we import the files contnaining the image functions.
from PIL import Image as im

# opening an image with pillow
image = im.open('filename')
# getting the image size
'''
in this case, we have parameters that wiht the values for the image
'''
print('width: ', image.width)
print('height:', image.height)

## Image resizing using nearest neighbor interpolation
def f_resize(image,size):
    '''
    this functions allows to resize any image considering any size based on the relationship between
    the images.
    NOTE: this function may not work it's to explain how a function like this would work testing required
    :param image: Original image
    :param size: Size of the desired output
    :return: single image with the new size given by parameter.
    '''
    # Get image dimensions
    s_dim = image.shape()
    # calculate the scaling factor
    v_factor = [size[0]/s_dim[0],size[1]/s_dim[1]]
    # create new image
    m_image = np.zeros(size)
    # cicle to fill the fill the new image
    for col in range(size[0]):
        # find the current position of the pixel
        colf = int(col/v_factor[0])
        for row in range (size[1]):
            rowf = int(row/v_factor[1])
            # get the value of the closest pixel to the image
            currPix = image[colf][rowf]
            # assing the same value to the new image.
            m_image[col][row] = currPix
    return m_image