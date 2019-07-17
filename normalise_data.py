import cv2 as cv
import numpy as np
path = r"C:\\Users\\DELL\\PycharmProjects\\anomaly_detection\\Avenue Dataset\\train_frames\\1\\1_1.jpg"
img = cv.imread(path, cv.IMREAD_COLOR)

norm = cv.normalize(img, None, alpha=0, beta=1, norm_type=cv.NORM_MINMAX, dtype=cv.CV_32F)
cv.imshow('dst_rt', norm)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imwrite("C:\\Users\\DELL\\PycharmProjects\\anomaly_detection\\Avenue Dataset\\1_2.jpg",norm)