# find coincidence in a given text 
def findCoincidence(cipherText):
    maxC = 0
    maxD = 1
    for displacement in range(1, len(cipherText) / 2):
        coin = 0
        for i in range(len(cipherText) - displacement):
            if cipherText[i] == cipherText[i + displacement]:
                coin += 1
            print 'displacement:', displacement, '\tcoin:', coin
            if coin > maxC:
                maxC = coin
                maxD = displacement
    print 'max coincidence:', maxC, 'max displacement:', maxD
    return maxC
