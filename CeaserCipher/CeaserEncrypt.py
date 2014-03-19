# encryption of ceaser cipher
import sys
sys.path.append('../lib/')
import Frequency
import types

if len(sys.argv) != 3:
    print 'format: python', sys.argv[0], 'message key'
    sys.exit()
else:
    msg = sys.argv[1]
    key = int(sys.argv[2])


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# A string to be encrypted
#msg = 'This is my message'
# The encryption key
#key = 13

msg = msg.upper() # convert to upper case
translated = ''

for symbol in msg:
		if symbol in LETTERS:
				num = LETTERS.find(symbol)
				num += key
				num %= len(LETTERS)
				translated = translated + LETTERS[num]
		else: 
				translated = translated + symbol
print translated
