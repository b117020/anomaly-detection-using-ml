import cv2
import os
import numpy as np
for i in range(1,17):
    image_folder = 'G:\\usped2\\train\\normal\\256 256 frames\\%d\\' % i
    video_name = 'G:\\usped2\\train\\normal\\videos\\%d.avi' % i

    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, 0, 1, (width,height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()
