
#returning max number of char that can be hide into img
def MaxASCIIchar(img,thresold = 0.3):
	h , w , c = img.shape
	return int(h*w*thresold)
