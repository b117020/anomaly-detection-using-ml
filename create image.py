from PIL import Image
for i in range(1,37):
    img = Image.new('RGB', (238, 158), color=(0, 0, 0))
    img.save('G:\\dense_opt_test\\%d\\frame0.jpg'%i)