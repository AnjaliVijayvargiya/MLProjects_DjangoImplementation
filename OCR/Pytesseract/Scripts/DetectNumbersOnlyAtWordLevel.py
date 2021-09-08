import cv2

import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img_path = "../images/2.png" 
img = cv2.imread(img_path)
if(img is not None):
    cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# text = pytesseract.image_to_string(img)
#print(text)

#Image: 2.png,2.jpg
#Detecting only numbers not words; word-level
conf = r'--oem 3 --psm 6 outputbase digits'
boxes = pytesseract.image_to_data(img, config=conf)

for x,b in enumerate(boxes.splitlines()):
    if x!=0:
        b = b.split()
        # print(b)
        if(len(b)==12):
            x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
            cv2.rectangle(img, (x,y), (w+x,h+y), (0,0,255),2)
            cv2.putText(img, b[11], (x, y),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),1)
cv2.imshow('Result',img)
cv2.waitKey(0)