# vigenere cipher
import sys
sys.path.append('../lib')
import BasicFunc

msg = 'this is a simple message'
key = 'crypto'
LETTERS = BasicFunc.LETTERS

msg = msg.upper()
key = key.upper()
keyIndex = 0
translated = ''
for symbol in msg:
    if symbol in LETTERS:
        num = LETTERS.find(symbol)
        if num != -1:
            num += LETTERS.find(key[keyIndex])
            num %= len(LETTERS)
        translated += LETTERS[num]
        keyIndex += 1
        if keyIndex == len(key):
            keyIndex = 0

    else:
        translated += symbol
print translated
