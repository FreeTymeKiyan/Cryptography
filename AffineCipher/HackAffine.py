# this is a hack affine cipher program
# try all combination of a and b
# a should prime to len(LETTERS)
# b can be 0~25
import sys
sys.path.append('../lib')
import AffineDecrypt
import BasicFunc

def main():
    if len(sys.argv) != 2:
        print 'USAGE: python', sys.argv[0], 'message'
        sys.exit()
    #text = 'HXAE AE CP CRRAPO IAVXOB OTCMVJO'
    text = sys.argv[1]
    msg = hackAffine(text)
    return msg

def hackAffine(text):
    result = []
    for a in range(25):
        if a == 0 or BasicFunc.gcd(a, len(BasicFunc.LETTERS)) != 1:
            continue
        for b in range(25):
            key = (a, b)
            translated = AffineDecrypt.decryptAffine(text, a, b)
            freq = BasicFunc.frequency(translated)
            result.append((key, translated, freq))
    result = sorted(result, key = lambda freq : freq[2], reverse = True)
    for i in range(5):
        print 'keys:', result[i][0], '\tresult:%s' % result[i][1], '\tfreq:%.5f' % result[i][2]

if __name__ == '__main__':
    main()
