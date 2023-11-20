import cv2
from PIL import Image

image_path = 'cat.jpeg'
fase_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
image = cv2.imread(image_path)
cat_fase = fase_cascade.detectMultiScale(image)


cat = Image.open(image_path)
glasses = Image.open('glasses.png')
cat = cat.convert("RGBA")
glasses = glasses.convert("RGBA")

for(x,y,w,h) in cat_fase:
   glasses = glasses.resize((w, int(h / 3)))
   cat.paste(glasses, (x, int(y+h/4)), glasses)
   cat.save("catZok.png")
   catZok = cv2.imread("catZok.png")
   cv2.imshow("Cat with glasses", catZok)


   cv2.waitKey()