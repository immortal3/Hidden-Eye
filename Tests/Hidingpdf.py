import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from Encoders import EnPdfToPng
from Utils import DataChunk,PdfWriter
from Decoders import DePdfToPng
import cv2
import numpy as np
from PIL import Image

img = cv2.imread('Tests/big_photo.png')
dataArray = DataChunk.pdfTo2bit('Tests/testing3.pdf')
DataHidenX,DataHidenY,img = EnPdfToPng.HidePdfintoPng(img,dataArray)
print (img.shape)

#encoded_img = Image.fromarray(img)
#encoded_img.save('encoded.png','png')
cv2.imwrite('encoded.png',img)
#encoded_img = cv2.imread('encoded.png')
unhidden_data = DePdfToPng.UnHidePdfintoPng(img,DataHidenX,DataHidenY)

#print (type(unhidden_data[0]))
PdfWriter.writePDF('decoded.pdf',unhidden_data)

#print(dataArray)
