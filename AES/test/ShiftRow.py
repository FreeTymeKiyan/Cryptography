from collections import deque
import pprint

def main():
	msg1 = '01100110011001100110011001100110011001100110011001100110011001100110011001100110011001100110011001100110011001100110011001100110' 
	msg2 = '11001100110011001100110011001100110011001100110011001100110011001100110011001100110011001100110011001100110011001100110011001100'
	n = 16
	msg = msg1[n:] + msg2[:n]
	print msg
	mat = generateMat(msg)
	shiftRow(mat)
	return

def generateMat(msg):
	mat = [[0 for col in range(4)] for row in range(4)]
	for i in range(len(mat)):
		for j in range(len(mat[i])):
			mat[i][j] = msg[8 * i + 32 * j : 8 * i + 32 * j + 8]
	pprint.pprint(mat)
	return mat

def shiftRow(mat):
	shiftRow = [[], [], [], []]
	for i in range(len(mat)):
		d = deque(mat[i])
		d.rotate(-i)
		shiftRow[i] = list(d)
	pprint.pprint(shiftRow)
	return mat

if __name__ == '__main__':
	main()
