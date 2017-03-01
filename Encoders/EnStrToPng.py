import cv2
import random as rd


# Hiding string into png (2-bit into 1 pixel)
def HideStringIntoPng_2bit1pixel(img,DataArray,seed = 0):
    # saving points where data is hidden
    if(seed != 0):
        rd.seed(seed)
    DataHidenX = []
    DataHidenY = []
    DataHidenZ = []
    h , w, c = img.shape
    # hiding data into image
    for i in range(0,len(DataArray)):
        x = rd.randint(0,h -1)
        while x in DataHidenX:
            x = rd.randint(0,h -1)
        y = rd.randint(0,w - 1)
        while y in DataHidenY:
            y = rd.randint(0,w -1)
        DataHidenX.append(x)
        DataHidenY.append(y)
        z = rd.randint(0,c - 1)
        while z in DataHidenZ:
            z = rd.randint(0,c -1)
        DataHidenZ.append(z)
        img[x][y][z] |= 0x03
        img[x][y][z] &= (0xfc | DataArray[i])

    return DataHidenX,DataHidenY,DataHidenZ,img

# Hiding string into png (8-bit into 1 pixel)
def HideStringIntoPng_8bit1pixel(img,DataArray,seed = 0):
    # saving points where data is hidden
    DataHidenX = []
    DataHidenY = []
    if(seed != 0):
        rd.seed(seed)
    h , w, c = img.shape
    if c <= 3:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2BGRA)
    # hiding data into image
    counter = len(DataArray)
    i = 0
    while i < counter:
        x = rd.randint(0,h -1)
        while x in DataHidenX:
            x = rd.randint(0,h -1)
        y = rd.randint(0,w - 1)
        while y in DataHidenY:
            y = rd.randint(0,w -1)
        DataHidenX.append(x)
        DataHidenY.append(y)
        img[x][y][0] |= 0x03
        img[x][y][0] &= (0xfc | DataArray[i])
        img[x][y][1] |= 0x03
        img[x][y][1] &= (0xfc | DataArray[i + 1])
        img[x][y][2] |= 0x03
        img[x][y][2] &= (0xfc | DataArray[i + 2])
        img[x][y][3] |= 0x03
        img[x][y][3] &= (0xfc | DataArray[i + 3])
        i += 4

    return DataHidenX,DataHidenY,img
