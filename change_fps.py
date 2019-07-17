import cv2
import math

for i in range(12,13):

    count = 0
    pathOut = r'G:\\avenue\\train_of_videos\\30 frames each\\%d\\'%i
    vidcap = cv2.VideoCapture(r"C:\\Users\\DELL\\PycharmProjects\\anomaly_detection\\Avenue Dataset\\training_videos\\%d.avi"%i);
    x=1
    success = True
    while success and x<=200:
        success, image = vidcap.read()
        print('read a new frame:', success)
        if count % 1 == 0:
            cv2.imwrite(pathOut + '%d.jpg' % x, image)
            x+=1
        count += 1


