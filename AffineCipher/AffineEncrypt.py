# this is an affine cipher example
import sys
sys.path.append('../lib')
from BasicFunc import LETTERS

def main():
    msg = 'this is an affine cipher example'
    msg = msg.upper()
    a = 3
    b = 2
    translated = ''

    for symbol in msg:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = (a * num + b) % len(LETTERS)
            translated = translated + LETTERS[num]
        else:
            translated = translated + symbol
    print translated

if __name__ == '__main__':
    main()
