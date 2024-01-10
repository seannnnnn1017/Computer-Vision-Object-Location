import matplotlib.pyplot as plt
import skimage.segmentation as seg
import skimage.filters as filters
import skimage.draw as draw
import skimage.color as color
from skimage import io
import numpy as np
from skimage.segmentation import mark_boundaries
from PIL import Image
import glob
import os
from skimage import img_as_ubyte

def implot(image, nrows=1, ncols=1, cmap='gray'):
    fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=(14, 14))
    ax.imshow(image, cmap='gray')
    ax.axis('off')
    return fig, ax
    
images = glob.glob('pics' + '/*.jpg')
x=1
os.makedirs('labels', exist_ok=True)
for i in images:
    image = io.imread(i)
    image_felzenszwalb = seg.felzenszwalb(image, scale=1000) 
    segmented_img = mark_boundaries(image, image_felzenszwalb)

    # Convert data type to uint8
    segmented_img_uint8 = img_as_ubyte(segmented_img)

    # 使用相對路徑保存輸出
    io.imsave('labels/' + os.path.basename(i)[:-4] + '_segmented.png', segmented_img_uint8)
    print(f'{x}/{len(images)+1}')
    x+=1
    # Optional: Show the segmented image
    implot(segmented_img)