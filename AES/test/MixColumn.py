from mult import mult

multMat = [['00000010', '00000011', '00000001', '00000001'], 
		   ['00000001', '00000010', '00000011', '00000001'], 
		   ['00000001', '00000001', '00000010', '00000011'], 
		   ['00000011', '00000001', '00000001', '00000010']]

def main():
	mixColumn()

def mixColumn(mat):
	# multMat * mat
	result = multiplyMat(multMat, mat)
	return result

def multiplyMat(mat1, mat2):
	resultMat = [[], [], [], []]
	for i, row in enumerate(resultMat):
		for j in range(4):
			multMatCol1 = mat1[i]
			multMatCol2 = [item[j] for item in mat2]
			#print 'cols:', multMatCol1, multMatCol2
			result = 0	
			for a, b in zip(multMatCol1, multMatCol2):
				x = int(mult(int(a, 2), int(b, 2)), 2)
				result = result ^ x	
				#print 'x: ', x
			#print 'result:', result
			row.append(intToStr(result))
	print resultMat
	return resultMat

def intToStr(intVal):
	return '{:08b}'.format(intVal)

if __name__ == '__main__':
	multiplyMat(multMat, multMat)
