import cv2
import numpy as np
from matplotlib import pyplot as plt
from pathlib import Path

output_images = Path('output_images')

def show_image(img_path,name):
  img = cv2.imread(img_path)
  img_cvt=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  plt.figure(figsize=(16,16))
  plt.imshow(img_cvt)
  plt.show()
  plt.savefig("/home/hossein/github/yolact/content/output_images/{}.png".format(name))

# Iterate through all of the output images and display them
for i, img_path in enumerate(output_images.iterdir()):
  print(img_path)
  show_image(str(img_path),str(i))