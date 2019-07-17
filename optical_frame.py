import cv2


for i in range(1,35):
    vidcap = cv2.VideoCapture('G:\\optical_flow_videos\\%d.avi'% i)
    success,image = vidcap.read()
    count = 0
    success = True
    while success:
        cv2.imwrite("G:\opticalflow_frames\\%d\\%d_%d.jpg" %(i,i,count), image)     # save frame as JPEG file
        success,image = vidcap.read()

        count += 1