#!/usr/bin/env python3

from PIL import Image
import os

# get list of image files
dir = os.path.expanduser('~/supplier-data/images/')
list_image = os.listdir(dir)
list_image = [name for name in list_image if name.endswith('.tiff')]

# modify and save the images
for name in list_image:
  with Image.open(dir+name) as im:
    new_im = im.resize((600,400)).convert('RGB')
    new_name = os.path.splitext(name)[0]
    new_im.save(dir + new_name + '.jpeg')
    print("Converted and resized to {} successfully".format(dir+new_name+'.jpeg'))
