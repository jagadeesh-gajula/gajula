from PIL import Image
import os


li = os.listdir()
for i in li:
	if i.endswith('jpeg'):
		im = Image.open(i)
		im.save(i.split('.')[0]+'.png')