import pprint
from mult import mult
from collections import deque

sBox = [[99,124,119,123,242,107,111,197,48,1,103,43,254,215,171,118],
        [202,130,201,125,250,89,71,240,173,212,162,175,156,164,114,192],
        [183,253,147,38,54,63,247,204,52,165,229,241,113,216,49,21],
        [4,199,35,195,24,150,5,154,7,18,128,226,235,39,178,117],
        [9,131,44,26,27,110,90,160,82,59,214,179,41,227,47,132],
        [83,209,0,237,32,252,177,91,106,203,190,57,74,76,88,207],
        [208,239,170,251,67,77,51,133,69,249,2,127,80,60,159,168],
        [81,163,64,143,146,157,56,245,188,182,218,33,16,255,243,210],
        [205,12,19,236,95,151,68,23,196,167,126,61,100,93,25,115],
        [96,129,79,220,34,42,144,136,70,238,184,20,222,94,11,219],
        [224,50,58,10,73,6,36,92,194,211,172,98,145,149,228,121],
        [231,200,55,109,141,213,78,169,108,86,244,234,101,122,174,8],
        [186,120,37,46,28,166,180,198,232,221,116,31,75,189,139,138],
        [112,62,181,102,72,3,246,14,97,53,87,185,134,193,29,158],
        [225,248,152,17,105,217,142,148,155,30,135,233,206,85,40,223],
        [140,161,137,13,191,230,66,104,65,153,45,15,176,84,187,22]]

def main():
	originalKey = '00000000000000010000001000000011000001000000010100000110000001110000100000001001000010100000101100001100000011010000111000001111'
	mat = generateMat(originalKey)
	#pprint.pprint(mat)
	for i in range(11):
		print i
		roundKeyMat = generateKey(mat, i)
		printHex(roundKeyMat)
	return

def printHex(mat):
	for r in mat:
		for c in r:
			print hex(int(c, 2)), '\t',
	print 

def generateMat(msg):
	mat = [[0 for col in range(4)] for row in range(4)]
	for i in range(len(mat)):
		for j in range(len(mat[i])):
			mat[i][j] = msg[8 * i + 32 * j : 8 * i + 32 * j + 8]
	return mat

def XOR(col1, col2):
	col = []
	for i in range(len(col1)):
		result = '{:08b}'.format(int(col1[i], 2) ^ int(col2[i], 2))
		col.append(result)
	return tuple(col)

def transform(col, i):
	# rotate
	#print 'col:', col
	d = deque(col)
	d.rotate(-1)
	rotated = list(d)
	#print 'rotated:', rotated
	# replace
	for idx, val in enumerate(rotated):
		sRow = int(val[0:4], 2)
		sCol = int(val[4:8], 2)
		rotated[idx] = intToBinaryStr(sBox[sRow][sCol])
	#print 'replaced:', rotated
    # compute round constant
	power = (i - 4) / 4
	r = 1
	if power != 0:
		for i in range(power):
			r = mult(r, 2)
	#print 'r:', r
    # XOR e and r
	rotated[0] = intToBinaryStr(int(rotated[0], 2) ^ r)            
	# print 'XOR:', rotated
	return rotated

def generateKey(key, ith):
	columns = zip(*key)
	for i in range(4, 44):
		#print i
		if i % 4 == 0:
			columns.append(XOR(columns[i - 4], transform(columns[i - 1], i)))
		else:
			columns.append(XOR(columns[i - 4], columns[i - 1]))
	return [columns[ith * 4 + j] for j in range(4)]

def mult(p1, p2):
    """Multiply two polynomials in GF(2^8)/x^8 + x^4 + x^3 + x + 1"""
    p = 0
    while p2:
        if p2 & 0x01:
            p ^= p1
        p1 <<= 1
        if p1 & 0x100:
            p1 ^= 0x1b
        p2 >>= 1
    return p & 0xff

def intToBinaryStr(intVal):
    return '{:08b}'.format(intVal)

if __name__ == '__main__':
	main()
