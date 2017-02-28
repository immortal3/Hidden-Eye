
def HideStringIntoPng(img,X,Y,Z):
	data = []
	counter = 0

	while counter < len(X):
		temp1 = (img[X[counter]][Y[counter]][Z[counter]] & 0x03) << 6;
		temp2 = (img[X[counter + 1]][Y[counter + 1]][Z[counter + 1]]  & 0x03) << 4
		temp3 = (img[X[counter + 2]][Y[counter + 2]][Z[counter+ 2]]  & 0x03) << 2
		temp4 = (img[X[counter + 3]][Y[counter + 3]][Z[counter + 3]]  & 0x03)
		counter += 4
		data.append(temp1 | temp2 | temp3 | temp4)

	return data
