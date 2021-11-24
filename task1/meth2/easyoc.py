import cv2
import numpy as np
import os
# from PIL import Image,display
import easyocr
from PIL import Image


def tx(r):
    for a,b,c in r:
        if c >=0.5:
            print(b)

def  get_image():
    path = 'D:\\Git work\\2nd project\\rep\\img'
    a = os.listdir(r'D:\\Git work\\2nd project\\rep\\img')
    for i in a:
        t = os.path.join(path,i)
        # b = gray(t)
        reader = easyocr.Reader(['en'])
        r = reader.readtext(t)
        tx(r)
        print()
        print()
get_image()