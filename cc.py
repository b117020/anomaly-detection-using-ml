from PIL import Image
im = Image.open('C:\\Users\\DELL\\PycharmProjects\\anomaly_detection\\Avenue Dataset\\1_2.jpg')
pix_val = list(im.getdata())  #pix_val is the list that contains all
#the pixel values which can be printed to see those values
print(pix_val)