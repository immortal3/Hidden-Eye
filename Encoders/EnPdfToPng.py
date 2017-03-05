import cv2
import random as rd

def HidePdfintoPng(img,DataArray,seed = 0):
    # saving points where data is hidden
    if(seed != 0):
        rd.seed(seed)
    h , w, c = img.shape
    if c <= 3:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2BGRA)
    # hiding data into image
    counter = len(DataArray)
    print (counter)
    i = 0
    x = 0
    y = 0
    while i < counter:
        #print (i)
        img[x][y][0] |= 0x03
        img[x][y][0] &= (0xfc | DataArray[i])
        img[x][y][1] |= 0x03
        img[x][y][1] &= (0xfc | DataArray[i + 1])
        img[x][y][2] |= 0x03
        img[x][y][2] &= (0xfc | DataArray[i + 2])
        img[x][y][3] |= 0x03
        img[x][y][3] &= (0xfc | DataArray[i + 3])
        i += 4
        if(x == h -1):
            break
        if(y == w -1):
            x += 1
            y = 0
        y += 1

    return x,y-1,img
