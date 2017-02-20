

def asciiTo2bit(dataString):
	#dataString = 'bigger string lol lol'
	ascii_array = []
	#

	#converting string into ascii char array
	for x in string:
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
