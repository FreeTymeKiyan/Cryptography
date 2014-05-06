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
    return '{:08b}'.format(p & 0xff)

def main():
	p1 = 7	
	p2 = 11
	print p1, p2
	print mult(p1, p2)
	return

if __name__ == '__main__':
	main()
