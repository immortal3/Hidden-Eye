import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from Encoders import EnStrToPng
import cv2
from Utils import DataChunk
from Decoders import DeStrToPng
from Utils import MaxDataCalculator
import random
img = cv2.imread('Tests/White.png')
#dataString = '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890'
dataString = ''

for _ in range(0,2500):
	dataString += chr(random.randint(0,127))
#cv2.imshow('nothing',img)
numberofchar = MaxDataCalculator.MaxASCIIchar(img)
print (numberofchar)

dataArray = DataChunk.asciiTo2bit(dataString)
#print (dataArray)
DataHidenX,DataHidenY,img = EnStrToPng.HideStringIntoPng_8bit1pixel(img,dataArray)
cv2.imwrite('encoded.png',img)

'''
hiddendata = DeStrToPng.UnHideStringIntoPng_2bit1pixel(img,DataHidenX,DataHidenY,DataHidenZ)
for x in hiddendata:
	print (chr(x))
'''
hiddendata = DeStrToPng.UnHideStringIntoPng_8bit1pixel(img,DataHidenX,DataHidenY)
if hiddendata == dataString:
	print ('correct hiding')
else:
	print ('error')
