import os
for j in range(35,37):
    dirname = "G:\\dense_opt_test\\%d"%j
    for root, dirs, files in os.walk(dirname):
        for i,f in enumerate(files):
            absname = os.path.join(root, f)
            newname = os.path.join(root,str(j)+"_"+str(i)+".jpg")
            os.rename(absname, newname)

