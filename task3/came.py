# from re import I
import cv2
from datetime import datetime
from easyocr import Reader
import os

lis = []
l = []
dic = {
    'Name':'-',
    'Father Name':'-',
    'Gender':'-',
    'Country of Stay':'Pakistan',
    'Identity Number':'-',
    'Date of Birth':'-',
    'Date of Issue':'-',
    'Date of Expiry':'-'
    }
def proces():

    reader = Reader(['en'])
    if os.path.isfile('id.avi'):
        cap = cv2.VideoCapture('id.avi')
    else:
        return 'Streaming Not found record again'
    while True:
        ret,fram = cap.read()
        if ret == 0:
            break
        cv2.imshow('hey',fram)
        if cv2.waitKey(1)==ord('q'):
            break
        results = reader.readtext(fram)
        if '-' in dic.values():    
            for i in range(len(results)):
                if results[i][2] > 0.8:
                    if  results[i][1] == 'Name' and dic['Name'] == '-' and results[i+1][1] not in dic.keys():
                        dic[results[i][1]] = results[i+1][1]
                
                    if results[i][1] == 'Father Name' and dic['Father Name'] == '-' and results[i+1][1] not in dic.keys():
                        dic['Father Name'] = results[i+1][1]


                    if results[i][1] not in dic.keys() and dic['Identity Number'] == '-' and len(results[i][1].split('-'))==3 and len(results[i][1])==15:
                        dic['Identity Number'] = results[i][1]
                        
                    if results[i][1] not in dic.keys() and len(results[i][1].split('.'))==3 and len(results[i][1])==10 and len(lis)<3:
                        lis.append(results[i][1])
                
                        if len(lis)==3 and dic['Date of Birth'] == '-' and dic['Date of Issue'] == '-' and dic['Date of Expiry'] == '-':
                            lis.sort(key=lambda date: datetime.strptime(date, "%d.%m.%Y"))
                            dic['Date of Birth'],dic['Date of Issue'],dic['Date of Expiry'] = lis
                    
                    if dic['Gender'] == '-':        
                        if  results[i][1] == 'M':
                            dic['Gender'] = 'M'
                        elif results[i][1] == 'F':
                            dic['Gender'] = 'F'
                        else:
                            dic['Gender'] = 'Not Found'
        if len(l) == 0:
            face(fram)
        else:
            print('ok')
            break
        lis.clear() 
    # cap.release()
    return dic



def face(fram):
    face_c = cv2.CascadeClassifier('h.xml')
    f = cv2.cvtColor(fram,cv2.COLOR_BGR2GRAY)
    box,det = face_c.detectMultiScale2(f)
    print('box',box)
    print(det)
    if len(det) > 0 and det[0] >= 60:
        x = box[0][0]
        y = box[0][1]
        w = box[0][2]
        h = box[0][3]
        x = x-30
        y = y-30
        w = w+x+45
        h = h+y+30
        f = fram[y:h,x:w]
        cv2.imwrite(r'static/images/id.jpg',f)
        l.append('3')
        return 'ok'

        