import os
import shutil
import glob

dir = "C:\\Users\\DELL\\Desktop\\UCSD_Anomaly_Dataset.v1p2\\train_1"
dst_dir = "C:\\Users\\DELL\\Desktop\\UCSD_Anomaly_Dataset.v1p2\\dev"
dst_dir1 = "C:\\Users\\DELL\\Desktop\\UCSD_Anomaly_Dataset.v1p2\\dev_val"
list = os.listdir(dir)
number_files = len(list)
item=1
for jpgfile in glob.iglob(os.path.join(dir, "*.jpg")):

    if item > 0.8*number_files :
        shutil.copy(jpgfile, dst_dir1)
    else :
        shutil.copy(jpgfile, dst_dir)
    item=item+1

