# encryption of ceaser cipher
import types
import sys
sys.path.append('../lib/')
import BasicFunc

# command line
if len(sys.argv) != 3:
    print 'format: python', sys.argv[0], 'message key'
    sys.exit()
else:
    msg = sys.argv[1]
    key = int(sys.argv[2])

# A string to be encrypted
#msg = 'This is my message'
# The encryption key
#key = 13

msg = msg.upper() # convert to upper case
translated = ''

for symbol in msg:
		if symbol in BasicFunc.LETTERS:
				num = BasicFunc.LETTERS.find(symbol)
				num += key
				num %= len(BasicFunc.LETTERS)
				translated = translated + BasicFunc.LETTERS[num]
		else: 
				translated = translated + symbol
print translated
