

#convert pdf into 2bits array/list
def pdfTo2bit(PDFFilePath):
	byte_array_2bit = []
	with open(PDFFilePath,'rb') as f:
		while True:
			byte_array = f.read(1)
			if not byte_array:
				break
			for x in byte_array:
				byte_array_2bit.append(x >> 6)
				byte_array_2bit.append((x >>4) & 0x03)
				byte_array_2bit.append((x >>2) & 0x03)
				byte_array_2bit.append(x & 0x03)
	return byte_array_2bit

def asciiTo2bit(dataString):
	#dataString = 'bigger string lol lol'
	ascii_array = []
	#

	#converting string into ascii char array
	for x in dataString:
		ascii_array.append(ord(x))

	#print (ascii_array)

	ascii_array_2bit = []

	#converting 8-bit ascii into 4 * 2-bit ascii
	for x in ascii_array:
		ascii_array_2bit.append(x >> 6)
		ascii_array_2bit.append((x >>4) & 0x03)
		ascii_array_2bit.append((x >>2) & 0x03)
		ascii_array_2bit.append(x & 0x03)


	#print (ascii_array_2bit)

	return ascii_array_2bit
