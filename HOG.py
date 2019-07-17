import matplotlib.pyplot as plt

from skimage.feature import hog
from skimage import data, color, exposure

import cv2, numpy

original_image = cv2.imread('G:\\usped1\\train\\frames\\1\\1_1.jpg',0)
original_height, original_width = original_image.shape[:2]
factor = 20
resized_image = cv2.resize(original_image, (int(original_height*factor), int(original_width*factor)), interpolation=cv2.INTER_CUBIC )

cv2.imwrite('G:\\usped1\\train\\frames\\resized_image.jpg',resized_image)
f="G:\\usped1\\train\\frames\\resized_image.jpg"

imge = data.load(f, as_gray=True)
image = color.rgb2gray(imge)

fd, hog_image = hog(image, orientations=8, pixels_per_cell=(20, 20),
                    cells_per_block=(1, 1), visualize=True)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4), sharex=True, sharey=True)

ax1.axis('off')
ax1.imshow(image, cmap=plt.cm.gray)
ax1.set_title('Input image')
ax1.set_adjustable('box')

# Rescale histogram for better display
hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 0.02))

ax2.axis('off')
ax2.imshow(hog_image_rescaled, cmap=plt.cm.gray)
ax2.set_title('Histogram of Oriented Gradients')
ax1.set_adjustable('box')
plt.show()