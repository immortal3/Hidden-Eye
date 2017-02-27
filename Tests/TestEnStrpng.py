import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from Encoders import EnStrToPng
import cv2
from Utils import DataChunk

img = cv2.imread('Tests/White.png')
dataString = 'My name is dip'
#cv2.imshow('nothing',img)
dataArray = DataChunk.asciiTo2bit(dataString)
DataHidenX,DataHidenY,DataHidenZ,img = EnStrToPng.HideStringIntoPng(img,dataArray)
cv2.imwrite('encoded.png',img)
