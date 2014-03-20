# decryption of ceasar cipher
import sys
sys.path.append('../lib')
import BasicFunc

def main():
    msg = 'ESTD TD L DLXAWP XPDDLRP'
    texts = hackCeaser(msg)
    for i in range(5):
        print 'key:%s' % BasicFunc.LETTERS[texts[i][0]], '\tresult:%s' % texts[i][1], 'freq:%.5f' % texts[i][2]
    return texts

def hackCeaser(msg):
    msg = msg.upper()
    result = []
    # exhausive search
    for key in range(1, 25):
        translated = ''
        for symbol in msg:
            if symbol in BasicFunc.LETTERS:
                num = BasicFunc.LETTERS.find(symbol) - key
                num %= len(BasicFunc.LETTERS)
                translated = translated + BasicFunc.LETTERS[num]
            else:
                translated = translated + symbol
        freq = BasicFunc.frequency(translated)
        result.append((key, translated, freq))
    result = sorted(result, key = lambda freq : freq[2], reverse = True)        
    return result


if __name__ == '__main__':
    main()
