
############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import numpy as np 
import math 
from PIL import Image 
import matplotlib.pyplot as plt


############################################################
# Individual Functions
############################################################

def convolve_greyscale(image, kernel):
    # get a empty array with all zeros
    shape = np.shape(image)
    image_height = shape[0]
    image_width = shape[1]
    kernel_shape = np.shape(kernel)
    kernel_height = kernel_shape[0]
    kernel_width = kernel_shape[1]
    flip_kernel = np.flipud(np.fliplr(kernel))
    output = np.zeros(shape)
    kernel_h_half = kernel_height//2
    kernel_w_half = kernel_width//2
    
    for i in range(image_height):
        
        if i - kernel_h_half < 0:
            slices = image[0:i+kernel_h_half+1]
            diff_h = -(i-kernel_h_half)
            applied_kernel = flip_kernel[diff_h:]
        
        elif i+kernel_h_half+1 >image_height:
            slices = image[i-kernel_h_half: image_width]
            diff_h = i +kernel_h_half+1-image_height
            applied_kernel = flip_kernel[:kernel_height-diff_h]
            
        else:
            slices = image[i-kernel_h_half:i+kernel_h_half+1]
            applied_kernel = flip_kernel
            
        for j in range(image_width):
            if j - kernel_w_half < 0:
                final_slices = slices[:,0: j+ kernel_w_half + 1]
                diff_w =  -(j - kernel_w_half)
                final_kernel = applied_kernel[:,diff_w:]
            elif j + kernel_w_half + 1 > image_width:
                final_slices = slices[:,j-kernel_w_half : image_width]
                diff_w = j + kernel_w_half + 1 - image_width
                final_kernel = applied_kernel[:,:kernel_width - diff_w]
            else:
                final_slices = slices[:,j-kernel_w_half : j + kernel_w_half + 1]
                final_kernel = applied_kernel
            output[i][j] = np.sum(final_slices * final_kernel)
    return output
        
        
            
      
# import numpy as np
# image = np.array([
#           [0,  1,  2,  3,  4],
#           [ 5,  6,  7,  8,  9], 
#           [10, 11, 12, 13, 14], 
#           [15, 16, 17, 18, 19], 
#           [20, 21, 22, 23, 24]])
# kernel = np.array([
#           [1, 2, 3],
#           [0, 0, 0],
#           [-1, -2, -3]])
# print(convolve_greyscale(image, kernel))
#   [[  16.   34.   40.   46.   42.]
#   [  30.   60.   60.   60.   50.]
#   [  30.   60.   60.   60.   50.]
#   [  30.   60.   60.   60.   50.]
#   [ -46.  -94. -100. -106.  -92.]]



# image = np.array(Image.open('5.1.09.tiff'))
# plt.imshow(image, cmap='gray')
# plt.show()
# kernel = np.array([
#           [0, -1, 0],
#           [-1, 5, -1],
#           [0, -1, 0]])
# output = convolve_greyscale(image, kernel)
# plt.imshow(output, cmap='gray')
# plt.show()
# print(output)

def convolve_rgb(image, kernel):
    output = np.zeros(np.shape(image))
    red_image = image[:,:,0]
    green_image = image[:,:,1]
    blue_image = image[:,:,2]
    
    red_image_conv = convolve_greyscale(red_image, kernel)
    green_image_conv = convolve_greyscale(green_image, kernel)
    blue_image_conv = convolve_greyscale(blue_image, kernel)
    output[:,:,0] = red_image_conv
    output[:,:,1] = green_image_conv
    output[:,:,2] = blue_image_conv
    return output
    
    
    
# image = np.array(Image.open('4.1.07.tiff'))
# plt.imshow(image)
# plt.show()
# kernel = np.array([
#          [0.11111111, 0.11111111, 0.11111111],
#          [0.11111111, 0.11111111, 0.11111111],
#          [0.11111111, 0.11111111, 0.11111111]])
# output = convolve_rgb(image, kernel)
# plt.imshow(output.astype('uint8'))
# plt.show()
# print(np.round(output[0:3, 0:3, 0:3], 2))
 # [[[ 63.67  63.44  47.22]
 #   [ 95.56  94.89  70.89]
 #   [ 95.56  94.78  70.89]]
    
 #  [[ 95.67  95.22  70.67]
 #   [143.33 142.56 105.89]
 #   [143.22 142.33 106.  ]]
    
 #  [[ 96.33  96.11  70.22]
 #   [144.11 144.   105.11]
 #   [143.78 143.44 105.22]]]
    
    


def max_pooling(image, kernel, stride):
    shape = np.shape(image)
    image_height = shape[0]
    image_width = shape[1]
    kernel_shape = kernel
    kernel_height = kernel_shape[0]
    kernel_width = kernel_shape[1]
    stride_shape = stride
    stride_height= stride_shape[0]
    stride_width= stride_shape[1]
    output_height = int(1+(image_height-kernel_height)/stride_height)
    output_width = int(1+(image_width-kernel_width)/stride_width)    
    output = np.zeros((output_height,output_width))
    for i in range(output_height): 
        index = i*stride_height
        for s in range(output_width):
            index1  = s*stride_width
            slides = image[index:index+kernel_height, index1:index1+kernel_width]
            output[i][s] = np.max(slides)
    return output
            
# image = np.array(Image.open('5.1.09.tiff'))
# plt.imshow(image, cmap='gray')
# plt.show()
# kernel_size = (2, 2)
# stride = (2, 2)
# output = max_pooling(image, kernel_size, stride)
# plt.imshow(output, cmap='gray')
# plt.show()
# print(output)       
    


def average_pooling(image, kernel, stride):
    shape = np.shape(image)
    image_height = shape[0]
    image_width = shape[1]
    kernel_shape = kernel
    kernel_height = kernel_shape[0]
    kernel_width = kernel_shape[1]
    stride_shape = stride
    stride_height= stride_shape[0]
    stride_width= stride_shape[1]
    output_height = int(1+(image_height-kernel_height)/stride_height)
    output_width = int(1+(image_width-kernel_width)/stride_width)    
    output = np.zeros((output_height,output_width))
    
    for i in range(output_height): 
        index = i*stride_height
        for s in range(output_width):
            index1  = s*stride_width
            slides = image[index:index+kernel_height, index1:index1+kernel_width]
            output[i][s] = np.average(slides)
    return output


# image = np.array(Image.open('5.1.09.tiff'))
# plt.imshow(image, cmap='gray')
# plt.show()
# kernel_size = (2, 2)
# stride = (2, 2)
# output = average_pooling(image, kernel_size, stride)
# plt.imshow(output, cmap='gray')
# plt.show()
# print(output)       
def sigmoid_function(x):
    return 1/(1+math.exp(-x))

def sigmoid(x):
    my_sigmoid = np.vectorize(sigmoid_function)
    r = my_sigmoid(x)
    return r



































