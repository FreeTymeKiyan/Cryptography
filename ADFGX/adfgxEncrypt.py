# encrypt of adgfx cipher
import sys
sys.path.append('../lib')
import BasicFunc
import pprint

row = 'ADFGX'
col = 'ADFGX'
grid = ['aflqv', 'wbgmr','sxchn', 'otydi', 'kpuze']
# pprint.pprint(grid)

def main():
    msg = 'a test message for the adfgx cipher'
    key = 'LUFT'
    text = encrypt(msg.upper(), key)
    print text
    return text

def translate(char):
    encrypted = ''
    for rowIdx, s in enumerate(grid):
        colIdx = s.upper().find(char)
        if colIdx != -1:
            encrypted = row[rowIdx] +  col[colIdx]
    # print encrypted
    return encrypted 

def encrypt(msg, key):
    translated = ''
    idx = 0
    d = {}
    for i in range(len(key)):
        d[key[i]] = ''
    for symbol in msg:
        # print symbol
        if symbol in BasicFunc.LETTERS:
            d[key[idx % len(key)]] += translate(symbol)
            idx += 1
    # sort
    #print d 
    d = sorted(d.iteritems(), key = lambda d : d[0])
    #print d
    for i in range(len(d)):
         translated += d[i][1]
    return translated

if __name__ == '__main__':
    main()
