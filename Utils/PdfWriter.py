# writing pdf using given data
def writePDF(filename,Data):
	with open('decoded.pdf','wb') as f:
	    for x in Data:
	        f.write(x)
