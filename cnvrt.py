import glob
import os
import wand
import numpy as np
from wand.image import Image 

path = '/convert/'
files = [f for f in glob.glob("**/*.pdf", recursive=True)]
for f in files:
	array = np.asarray(files)
	print(array)

for lists in range(len(array)):
	pdf = Image(filename=array[lists], resolution=200)
	pdfImage = pdf.convert("jpeg")
	i = 1
	for img in pdfImage.sequence:
	    page = Image(image=img)
	    page.save(filename=array[lists] + "-" + str(i) + ".jpg")
	    i += 1