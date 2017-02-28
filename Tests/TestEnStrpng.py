import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from Encoders import EnStrToPng
import cv2
from Utils import DataChunk
from Decoders import DeStrToPng
img = cv2.imread('Tests/White.png')
dataString = 'my name is dip'
#cv2.imshow('nothing',img)
dataArray = DataChunk.asciiTo2bit(dataString)
print (dataArray)
DataHidenX,DataHidenY,DataHidenZ,img = EnStrToPng.HideStringIntoPng(img,dataArray)
cv2.imwrite('encoded.png',img)
hiddendata = DeStrToPng.HideStringIntoPng(img,DataHidenX,DataHidenY,DataHidenZ)
for x in hiddendata:
	print (chr(x))
