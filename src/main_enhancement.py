import numpy as np
#import cv2
#import numpy as np;
import matplotlib.pylab as plt;
import scipy.ndimage
import sys
import os
from image_enhance import image_enhance


#if(len(sys.argv)<2):
print('loading sample image');
base=os.path.basename(sys.argv[1])
img_name = os.path.splitext(base)
img_name = str(img_name[0] + img_name[1])
print(img_name)
img = scipy.ndimage.imread('./images/' + img_name);
#elif(len(sys.argv) >= 2):
#    base=os.path.basename(sys.argv[1])
#    img_name = os.path.splitext(base)
#    img_name = str(img_name)
#    img = scipy.ndimage.imread(sys.argv[1]);

if(len(img.shape)>2):
    # img = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
    img = np.dot(img[...,:3], [0.299, 0.587, 0.114]);

rows,cols = np.shape(img);
aspect_ratio = np.double(rows)/np.double(cols);

new_rows = 350;             # randomly selected number
new_cols = new_rows/aspect_ratio;

#img = cv2.resize(img,(new_rows,new_cols));
img = scipy.misc.imresize(img,(np.int(new_rows),np.int(new_cols)));

enhanced_img = image_enhance(img);    

if(1):
    print('saving the image')
    scipy.misc.imsave('./enhanced/' + img_name,enhanced_img);
else:
    plt.imshow(enhanced_img,cmap = 'Greys_r');
