# decrypt vigenere cipher
import sys
sys.path.append('../lib')
import BasicFunc

def main():
    msg = ''
    key = ''
    msg = decryptVigenre(msg, key)
    print msg
    return msg

def decryptVigenere(msg, key):
    idx = 0
    translated = ''
    for symbol in msg.upper():
        if symbol in BasicFunc.LETTERS:
            num = BasicFunc.LETTERS.find(symbol)
            num -= BasicFunc.LETTERS.find(key[idx % len(key)])
            word = BasicFunc.LETTERS[num % len(BasicFunc.LETTERS)]
            translated += word
            idx += 1
    # print translated
    return translated

if __name__ == '__main__':
    main()
