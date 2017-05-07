#!/usr/bin/python
from PIL import Image, ImageOps
import os, sys

path = sys.argv[1]
dirs = os.listdir(path)

def invert_colors():
    root, pardir = os.path.split(path)
    os.makedirs(os.path.join(root, pardir + '_inverted'), exist_ok=True)
    for i, item in enumerate(dirs):
        if os.path.isfile(os.path.join(path, item)):
            print('remaining:', len(dirs) - i)
            im = Image.open(os.path.join(path, item))
            im_name, ext = os.path.splitext(item)
            inverted_image = ImageOps.invert(im)
            inverted_image.save(os.path.join(root, pardir + '_inverted', im_name + '.jpg'), 'JPEG', quality=90)

invert_colors()
