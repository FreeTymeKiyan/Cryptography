# an implementation of AES

# a sample run of AES
def main():
	return

# takes string text as an input
# output the encrypted text
def aes(text):
	msg = ''
	addRoundKey()
	for i in range(10):
		byteSub()
		shiftRow()
		if i != 9:
			mixColumn()
		addRoundKey()				
	return msg

def byteSub():
	return 

def shiftRow():
	return

def mixColumn():
	return

def addRoundKey():
	return

if __name__ == '__main__':
	main()
