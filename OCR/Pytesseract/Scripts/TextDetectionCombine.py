import cv2

import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img_path = "../images/1.png" 
img = cv2.imread(img_path)
if(img is not None):
    cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# text = pytesseract.image_to_string(img)
#print(text)

# -------------------------------------------------------1---------------------------------------------------------- #
#Image: 1.png,2.png,2.jpg
#Detecting Characters
hImg, wImg,_ = img.shape
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    # print(b)
    b = b.split(' ')
    # print(b)
    x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv2.rectangle(img, (x,hImg-y), (w,hImg-h), (0,0,255),2)
    cv2.putText(img, b[0], (x, hImg-y+25),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),1)
cv2.imshow('Result',img)
cv2.waitKey(0)
# -------------------------------------------------------1---------------------------------------------------------- #

# -------------------------------------------------------2---------------------------------------------------------- #
#Image: 1.png,2.png,2.jpg,3.jpg
# #Detecting Words
# boxes = pytesseract.image_to_data(img)

# for x,b in enumerate(boxes.splitlines()):
#     if x!=0:
#         b = b.split()
#         # print(b)
#         if(len(b)==12):
#             x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
#             cv2.rectangle(img, (x,y), (w+x,h+y), (0,0,255),2)
#             cv2.putText(img, b[11], (x, y),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),1)
# cv2.imshow('Result',img)
# cv2.waitKey(0)
# -------------------------------------------------------2---------------------------------------------------------- #

# -------------------------------------------------------3---------------------------------------------------------- #
# #Image: 2.png,2.jpg
# #Detecting only numbers not characters; character-level
# hImg, wImg,_ = img.shape
# conf = r'--oem 3 --psm 6 outputbase digits'
# boxes = pytesseract.image_to_boxes(img,config=conf)
# for b in boxes.splitlines():
#     # print(b)
#     b = b.split(' ')
#     # print(b)
#     x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
#     cv2.rectangle(img, (x,hImg-y), (w,hImg-h), (0,0,255),2)
#     cv2.putText(img, b[0], (x, hImg-y+25),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),1)
# cv2.imshow('Result',img)
# cv2.waitKey(0)
# -------------------------------------------------------3---------------------------------------------------------- #

# -------------------------------------------------------4---------------------------------------------------------- #
#Image: 2.png,2.jpg
# #Detecting only numbers not words; word-level
# conf = r'--oem 3 --psm 6 outputbase digits'
# boxes = pytesseract.image_to_data(img, config=conf)

# for x,b in enumerate(boxes.splitlines()):
#     if x!=0:
#         b = b.split()
#         # print(b)
#         if(len(b)==12):
#             x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
#             cv2.rectangle(img, (x,y), (w+x,h+y), (0,0,255),2)
#             cv2.putText(img, b[11], (x, y),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),1)
# cv2.imshow('Result',img)
# cv2.waitKey(0)
# -------------------------------------------------------4---------------------------------------------------------- #

# -------------------------------------------------------5---------------------------------------------------------- #
#Image: 1.png,2.jpg,3.jpg
# #detect lines by hocr file
# hocr = pytesseract.image_to_pdf_or_hocr(img_path, extension='hocr')
# #print(hocr)
# pytesseract.pytesseract.run_tesseract(img_path, 'output',lang=None, config="hocr",extension='hocr')

# from bs4 import BeautifulSoup

# HTMLFile = open("output.hocr", "r")
  
# # Reading the file
# index = HTMLFile.read()
  
# # Creating a BeautifulSoup object and specifying the parser
# soup = BeautifulSoup(index,features="html.parser")
# hImg, wImg,_ = img.shape
# list_a = []
# for tag in soup.find_all('span', attrs={'class' : 'ocr_line'}):
#     output = tag['title']
#     out1 = tag.text
#     out2 = out1.replace('\n',' ')
   
#     if(out2!="   "):
#         b = output.split()
#         # print(b)
#         if(len(b)==14):
#             b4_edit = b[4]
#             # print(b4_edit[:-1])
#             x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b4_edit[:-1])
#             cv2.rectangle(img, (x,y), (w,h), (0,0,255),2)
#             cv2.putText(img, out2, (x, y),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),1)
# cv2.imshow('Result',img)
# cv2.waitKey(0)
# -------------------------------------------------------5---------------------------------------------------------- #
