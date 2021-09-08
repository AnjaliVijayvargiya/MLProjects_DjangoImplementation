import cv2

import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img_path = "../images/2.png" 
img = cv2.imread(img_path)
if(img is not None):
    cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# text = pytesseract.image_to_string(img)
#print(text)

# #Image: 2.png,2.jpg
#Detecting only numbers not characters; character-level
hImg, wImg,_ = img.shape
conf = r'--oem 3 --psm 6 outputbase digits'
boxes = pytesseract.image_to_boxes(img,config=conf)
for b in boxes.splitlines():
    # print(b)
    b = b.split(' ')
    # print(b)
    x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv2.rectangle(img, (x,hImg-y), (w,hImg-h), (0,0,255),2)
    cv2.putText(img, b[0], (x, hImg-y+25),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),1)
cv2.imshow('Result',img)
cv2.waitKey(0)