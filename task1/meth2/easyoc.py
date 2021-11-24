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
            # just tried for better result
# def gray(g):
#     img = cv2.imread(g) 
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Gray Scale
#     # img = cv2.medianBlur(img, 5) #Remove Noice
#     img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
#     img = Image.fromarray(img)
#     # img.show()
#     return img
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