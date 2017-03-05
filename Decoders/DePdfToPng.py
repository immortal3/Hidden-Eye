import numpy as np

def UnHidePdfintoPng(img,x,y):
	counterx = 0
	countery = 0
	h , w , c = img.shape
	data = []
	while counterx <= x:
		temp1 = (img[counterx][countery][0] & 0x03) << 6;
		temp2 = (img[counterx][countery][ 1]  & 0x03) << 4
		temp3 = (img[counterx][countery ][2]  & 0x03) << 2
		temp4 = (img[counterx][countery ][3]  & 0x03)
		data.append(temp1 | temp2 | temp3 | temp4)
		if counterx == x and countery == y:
			#print ('EOF Found')
			break
		if(countery == w - 1):
			countery = 0
			counterx += 1
		else:
			countery += 1
	data = np.int8(data)
	return data
