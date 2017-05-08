#!/usr/bin/python
from PIL import Image
import os, sys

path = sys.argv[1]
dirs = os.listdir(path)

def resize():
    root, pardir = os.path.split(path)
    os.makedirs(os.path.join(root, pardir + '_256'), exist_ok=True)
    for i, item in enumerate(dirs):
        if os.path.isfile(os.path.join(path, item)):
            print('remaining:', len(dirs) - i)
            im = Image.open(os.path.join(path, item))
            imResize = im.resize((256,256), Image.ANTIALIAS)
            imResize.save(os.path.join(root, pardir + '_256', item), 'JPEG', quality=90)

resize()
