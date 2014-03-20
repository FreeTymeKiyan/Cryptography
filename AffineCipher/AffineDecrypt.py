# decryption of affine cipher
import sys
sys.path.append('../lib')
import BasicFunc

LETTERS = BasicFunc.LETTERS
# give a and b, decrypt an affine cypher
def main():
    text = 'HXAE AE CP CRRAPO IAVXOB OTCMVJO'
    a = 3
    b = 2
    msg = decryptAffine(text, 3, 2)
    print msg
    return msg

def decryptAffine(text, a, b):
    translated = ''
    modInverse = BasicFunc.findModInverse(a, len(LETTERS))
    for symbol in text:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = (modInverse * (num - b)) % len(LETTERS)
            translated = translated + LETTERS[num]
        else:
            translated = translated + symbol
    return translated

if __name__ == '__main__':
    main()
