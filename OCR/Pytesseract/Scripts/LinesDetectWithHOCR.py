import cv2

import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img_path = "../images/3.jpg" 
img = cv2.imread(img_path)
if(img is not None):
    cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# text = pytesseract.image_to_string(img)
#print(text)

#Image: 1.png,2.jpg,3.jpg
#detect lines by hocr file
hocr = pytesseract.image_to_pdf_or_hocr(img_path, extension='hocr')
#print(hocr)
pytesseract.pytesseract.run_tesseract(img_path, 'output',lang=None, config="hocr",extension='hocr')

from bs4 import BeautifulSoup

HTMLFile = open("output.hocr", "r")
  
# Reading the file
index = HTMLFile.read()
  
# Creating a BeautifulSoup object and specifying the parser
soup = BeautifulSoup(index,features="html.parser")
hImg, wImg,_ = img.shape
list_a = []
for tag in soup.find_all('span', attrs={'class' : 'ocr_line'}):
    output = tag['title']
    out1 = tag.text
    out2 = out1.replace('\n',' ')
   
    if(out2!="   "):
        b = output.split()
        # print(b)
        if(len(b)==14):
            b4_edit = b[4]
            # print(b4_edit[:-1])
            x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b4_edit[:-1])
            cv2.rectangle(img, (x,y), (w,h), (0,0,255),2)
            cv2.putText(img, out2, (x, y),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),1)
cv2.imshow('Result',img)
cv2.waitKey(0)