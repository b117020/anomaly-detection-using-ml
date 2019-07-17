import os
dirname = "C:\\Users\\DELL\\Desktop\\UCSD_Anomaly_Dataset.v1p2\\UCSDped1\\Train\\Train003"
for root, dirs, files in os.walk(dirname):
    for i,f in enumerate(files):
        absname = os.path.join(root, f)
        newname = os.path.join(root,"3_"+str(i)+".jpg")
        os.rename(absname, newname)