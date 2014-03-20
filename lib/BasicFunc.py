import numpy
import math

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
COMMON_FREQUENCY = {'A': 0.082, 'B': 0.015, 'C': 0.028, 'D': 0.043, 'E': 0.127, 'F': 0.022, 'G': 0.020, 'H': 0.061, 'I': 0.070, 'J': 0.002, 'K': 0.008, 'L': 0.040, 'M': 0.024, 'N': 0.067, 'O': 0.075, 'P': 0.019, 'Q': 0.001, 'R':0.060, 'S': 0.063, 'T': 0.091, 'U': 0.028, 'V': 0.010, 'W': 0.023, 'X': 0.001, 'Y': 0.020, 'Z': 0.001}
def main():
    print 'library functions for hacking cipher'
    return None

def magnitude(v):
    return math.sqrt(numpy.dot(v, v))

def normalize(v):
    vmag = magnitude(v)
    return [ v[i] / vmag for i in range(len(v)) ]

def getLetterCount(text):
    letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
    for letter in text.upper():
        if letter in LETTERS:
            letterCount[letter] += 1
    return letterCount

def frequency(text):
    letterCount = getLetterCount(text)
    for key in letterCount.keys():
        count = letterCount[key]
        freq = float(count) / len(text)
        letterCount[key] = freq
    result = numpy.dot(normalize(letterCount.values()), COMMON_FREQUENCY.values())
    # result = numpy.dot(letterCount.values(), COMMON_FREQUENCY.values())
    return result

# find coincidence in a given text 
def findCoincidence(cipherText):
    maxC = 0
    maxD = 1
    for displacement in range(1, len(cipherText) / 2):
        coin = 0
        for i in range(len(cipherText) - displacement):
            if cipherText[i] == cipherText[i + displacement]:
                coin += 1
            if coin > maxC:
                maxC = coin
                maxD = displacement
        # print 'displacement:', displacement, '\tcoin:', coin
    # print 'max coincidence:', maxC, 'max displacement:', maxD
    return maxD

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
