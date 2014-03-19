import numpy
import math
# calculate frequency and dot product
# common frequency
#COMMON_FREQUENCY = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}
COMMON_FREQUENCY = {'A': 0.082, 'B': 0.015, 'C': 0.028, 'D': 0.043, 'E': 0.127, 'F': 0.022, 'G': 0.020, 'H': 0.061, 'I': 0.070, 'J': 0.002, 'K': 0.008, 'L': 0.040, 'M': 0.024, 'N': 0.067, 'O': 0.075, 'P': 0.019, 'Q': 0.001, 'R': 0.060, 'S': 0.063, 'T': 0.091, 'U': 0.028, 'V': 0.010, 'W': 0.023, 'X': 0.001, 'Y': 0.020, 'Z': 0.001}
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    print 'library module for hacking cipher'
    return 0

def magnitude(v):
    return math.sqrt(numpy.dot(v, v))

def normalize(v):
    vmag = magnitude(v)
    return [ v[i]/vmag for i in range(len(v)) ]

def frequency(text):
    # get letter count
    letterCount = getLetterCount(text)
    # get letter freq
    for key in letterCount.keys():
        count = letterCount[key]
        freq = float(count) / len(text)
        letterCount[key] = freq
    # do dot product with common freq
    result = numpy.dot(normalize(letterCount.values()), COMMON_FREQUENCY.values())
    return result

def getLetterCount(text):
    letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
    
    for letter in text.upper():
        if letter in LETTERS:
            letterCount[letter] += 1
    return letterCount

if __name__ == '__main__':
    main()
