import cv2
import os
import numpy as np
image_folder = 'C:\\Users\\DELL\\Desktop\\UCSD_Anomaly_Dataset.v1p2\\UCSDped1\\Train\\Train034'
video_name = 'video34.avi'

images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 1, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()

cap = cv2.VideoCapture('video34.avi')

# params for ShiTomasi corner detection
feature_params = dict( maxCorners = 100,
                       qualityLevel = 0.3,
                       minDistance = 7,
                       blockSize = 7 )

# Parameters for lucas kanade optical flow
lk_params = dict( winSize  = (15,15),
                  maxLevel = 2,
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# Create some random colors
color = np.random.randint(0,255,(100,3))

# Take first frame and find corners in it
ret, old_frame = cap.read()
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
p0 = cv2.goodFeaturesToTrack(old_gray, mask = None, **feature_params)

# Create a mask image for drawing purposes
mask = np.zeros_like(old_frame)

while(cap.isOpened()):
    ret,frame = cap.read()
    if ret:
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # calculate optical flow
        p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)

    # Select good points
        good_new = p1[st==1]
        good_old = p0[st==1]

    # draw the tracks
        for i,(new,old) in enumerate(zip(good_new,good_old)):
            a,b = new.ravel()
            c,d = old.ravel()
            mask = cv2.line(mask, (a,b),(c,d), color[i].tolist(), 2)
            frame = cv2.circle(frame,(a,b),5,color[i].tolist(),-1)
        img = cv2.add(frame,mask)

        cv2.imshow('frame',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

    # Now update the previous frame and previous points
    old_gray = frame_gray.copy()
    p0 = good_new.reshape(-1,1,2)

cv2.destroyAllWindows()
cap.release()

flow = mex_OF(double(im1), double(im2))

scale = 16
mag = sqrt(flow(:,:, 1).^ 2 + flow(:,:, 2).^ 2)*scale + 128
mag = min(mag, 255)
flow = flow * scale + 128
flow = min(flow, 255)
flow = max(flow, 0)

[x, y, z] = size(flow)
flow_image = zeros(x, y, 3)
flow_image(:,:, 1: 2) = flow
flow_image(:,:, 3) = mag
imwrite(flow_image. / 255, sprintf('%s/%s/flow_image_%s', save_base, video, frames
{k}))