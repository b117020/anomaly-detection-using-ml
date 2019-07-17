import cv2
import numpy as np
for i in range(13,17):

    cap = cv2.VideoCapture("G:\\usped2\\train\\normal\\videos\\%d.avi"%i)

    ret, frame1 = cap.read()
    prvs = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
    hsv = np.zeros_like(frame1)
    hsv[...,1] = 255
    frame=1
    k=0
    while(1):
        ret, frame2 = cap.read()

        if frame2 is None:
            break
        next = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)

        flow = cv2.calcOpticalFlowFarneback(prvs,next, None, 0.5, 3, 15, 3, 5, 1.2, 0)

        mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])
        hsv[...,0] = ang*180/np.pi/2
        hsv[...,2] = cv2.normalize(mag,None,0,255,cv2.NORM_MINMAX)
        rgb = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)

        cv2.imwrite('G:\\usped2\\train\\normal\\256 256 optical frames\\%d\\frame%d.jpg'%(i,frame),rgb)
        frame+=1


        prvs = next

