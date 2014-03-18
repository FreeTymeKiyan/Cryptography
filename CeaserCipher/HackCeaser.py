# decryption of ceasar cipher
import Frequency

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

msg = 'ESTD TD L DLXAWP XPDDLRP'

msg = msg.upper()
result = []
# exhausive search
for key in range(1, 25):
    translated = ''
    for symbol in msg:
        if symbol in LETTERS:
            num = LETTERS.find(symbol) + key
            num %= len(LETTERS)
            translated = translated + LETTERS[num]
        else:
            translated = translated + symbol
    freq = Frequency.frequency(translated)
    result.append((key, translated, freq))

result = sorted(result, key = lambda freq : freq[2], reverse = True)
for i in range(5):
    print 'key:%d' % result[i][0], '\tresult:%s' % result[i][1], 'freq:%.5f' % result[i][2]