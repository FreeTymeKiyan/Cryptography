# test write file functions
def main():
	writeFile()
	return

def writeFile():
	f = open('aesYangLiuout.txt', 'w')
	f.write('This is a test\n')
	return

if __name__ == '__main__':
	main()
