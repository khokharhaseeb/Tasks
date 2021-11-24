import pytesseract
import os
from PIL import Image
# os.sys.path.append(r'Control Panel\Programs\Programs and Features\Tesseract-OCR')
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
a = os.listdir(r'D:\\Git work\\2nd project\\rep\\img')
path = 'D:\\Git work\\2nd project\\rep\\img'
for i in a:
    t = os.path.join(path,i)
    extractedInfo = pytesseract.image_to_string(Image.open(t))
    print(extractedInfo)