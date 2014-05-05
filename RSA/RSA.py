# an implementation of decoding RSA msg
# author:	Yang Liu
# date:		2014-05-05

def main():
	RSA()
	return

def RSA():
	e = 5
	n = 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000020900000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000973
	p = long(pow(10, 110)) + 7
	q = long(pow(10, 111)) + 139
	msg = 47386274600715627711741231320889953635052682912275895170705519441900467437234068120729231868997125356903089949357565563350604020398667889098417715800228490969143071606844546349141649145365269219264564662542369533624712494
	# calculate d as mod inverse of e mod(p-1)(q-1)
	d = findModInverse(e, (p - 1) * (q - 1))
	m = pow(msg, d, n)
	convert2Letters(m)
	return

def convert2Letters(m):
	# add zero in front
	msg = str(m)
	mod = len(msg) % 3
	if mod != 0:
		msg = ('0' * (3 - mod)) + msg
		print msg
	i = 0
	while i < len(msg):
		print chr(int(msg[i:i+3])),
		i = i + 3

def gcd(a, b):
	while a != 0:
		a, b = b % a, a
	return b

def findModInverse(a, m):
    # returns the modular inverse of a % m, which is
	# the number x such that a * x % m = 1
	if gcd(a, m) != 1:
		return None
	u1, u2, u3 = 1, 0 ,a
	v1, v2, v3 = 0, 1, m
	while v3 != 0:
		q = u3 // v3
		v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
	return u1 % m

if __name__ == '__main__':
	main()
