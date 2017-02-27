import cv2
import random as rd
# Hide to string png
def HideStringIntoPng(img,DataArray):
    # saving points where data is hidden
    DataHidenX = []
    DataHidenY = []
    DataHidenZ = []
    h , w, c = img.shape
    # hiding data into image
    for i in range(0,len(DataArray)):
        x = rd.randint(0,h -1)
        y = rd.randint(0,w - 1)
        DataHidenX.append(x)
        DataHidenY.append(y)
        z = rd.randint(0,c - 1)
        DataHidenZ.append(z)
        img[x][y][z] &= (0xfc | DataArray[i])

    return DataHidenX,DataHidenY,DataHidenZ,img
