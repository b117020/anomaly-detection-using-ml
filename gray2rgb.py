

import cv2
import numpy as np
img = cv2.imread('C:\\Users\\DELL\\Desktop\\UCSD_Anomaly_Dataset.v1p2\\test_1\\1_2.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img2 = np.zeros_like(img)
img2[:,:,0] = gray
img2[:,:,1] = gray
img2[:,:,2] = gray

print(len(gray.shape))