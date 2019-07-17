from PIL import Image
for j in range(16,17):
    for i in range(0,1):
        img = Image.open('C:\\Users\\DELL\\Downloads\\dev.jpg') # image extension *.png,*.jpg
        new_width  = 3.5
        new_height = 4.5
        img = img.resize((new_width, new_height), Image.ANTIALIAS)
        img.save('C:\\Users\\DELL\\Downloads\\dev1.jpg')
