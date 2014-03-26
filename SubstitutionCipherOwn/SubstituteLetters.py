# substitute letters in a given msg
import sys
sys.path.append('../lib')
import BasicFunc

def main():
    msg = 'AAABBBCCC'
    letterMap = {'A':'E'}
    translated = substitueLetters(letterMap, msg)
    print translated
    return translated

def substitueLetters(mapping, msg):
    msg = msg.upper()
    for key in mapping.keys():
        msg = msg.replace(key, mapping[key])
    return msg

if __name__ == '__main__':
    main()
