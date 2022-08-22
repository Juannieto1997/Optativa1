## This section will show some transformmations using histograms
'''
the functions of this code might not work they are made to explain the concepts
'''
# import libraries
import cv2 as cv
import numpy as np
# reading an image
fileName = 'ImageName'
image = cv.imread(fileName)

## getting the histogram
def f_hist(image):
    v_shape = image.shape()
    s_max = 256
    s_min = 0
    #initialize empy histogram
    v_xax = range(s_min,s_max)
    v_hist = np.zeros_like(v_xax)
    for col in range(v_shape[0]):
        for row in range(v_shape[1]):
            s_pix = image[col][row]
            v_hist[s_pix] += 1
    return [v_xax,v_hist]
## histogram equalization
def f_Sx(v_Px):
    '''
    calculate cumulative probability
    :param v_Px: probability for each intensity
    :return: v_Sx - cumulative probablity
    '''
    v_Sx = np.zeros_like(v_Px)
    # fill the cumulative probality
    for idx in range(len(v_Sx)):
        # note that in the first iteration, v_Sx[idx-1] = 0 therefore its not necesary to validate a special condition
        v_Sx[idx] = v_Sx[idx-1] + v_Px[idx]
    return v_Sx


def f_histeq (image):
    '''
    function for histogram equalization
    :param image: image sample to be equalized
    :return: original axis and new values
    '''
    # calculate histogram
    [v_ax,v_hist] = f_hist(image)
    s_tot = np.sum(v_hist) # total number of samples in the image
    v_Px = np.dot(v_hist,1/s_tot) # probablity of each intensity
    v_Sx = f_Sx(v_Px) # cumulative probablity
    v_val = int(np.dot(v_Sx,v_ax[-1])) # new values of the image
    return [v_ax,v_val]

## histogram matching
# TODO: create a function for histogram matching using the previous functions.

## Validations
# TODO: validate and correct functions.