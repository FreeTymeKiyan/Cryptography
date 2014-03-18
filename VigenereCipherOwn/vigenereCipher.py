import itertools

def getNthSubkeysLetters(n, keyLength, message):
    # Returns every Nth letter for each keyLength set of letters in text.
    # E.g. getNthSubkeysLetters(1, 3, 'ABCABCABC') returns 'AAA'
    #      getNthSubkeysLetters(2, 3, 'ABCABCABC') returns 'BBB'
    #      getNthSubkeysLetters(3, 3, 'ABCABCABC') returns 'CCC'
    #      getNthSubkeysLetters(1, 5, 'ABCDEFGHI') returns 'AF'
    
    # Use a regular expression to remove non-letters from the message.
    message = NONLETTERS_PATTERN.sub('', message)
    
    i = n - 1
    letters = []
    while i < len(message):
        letters.append(message[i])
        i += keyLength
    return ''.join(letters)

def attemptHackWithKeyLength(ciphertext, mostLikelyKeyLength):
    ciphertextUp = ciphertext.upper()
    
    allFreqScores = []
    for nth in range(1, mostLikelyKeyLength + 1):
        nthLetters = getNthSubkeysLetters(nth, mostLikelyKeyLength, ciphertextUp)

        freqScores = []
        for possibleKey in LETTERS:
            decryptedText = vigenereCipher.decryptMessage(possibleKey, nthLetters)
            keyAndFreqMatchTuple = (possibleKey, freqAnalysis.englishFreqMatchScore(decryptedText))
                freqScores.append(keyAndFreqMatchTuple)
            # Sort by match score
        freqScores.sort(key=getItemAtIndexOne, reverse=True)
    
        allFreqScores.append(freqScores[:NUM_MOST_FREQ_LETTERS])

    if not SILENT_MODE:
        for i in range(len(allFreqScores)):
            # use i + 1 so the first letter is not called the "0th" letter
            print 'Possible letters for letter %s of the key: ' % (i + 1),
            for freqScore in allFreqScores[i]:
                print '%s ' % freqScore[0],
            print()# print a newline

    # Try every combination of the most likely letters for each position
    # in the key.
    for indexes in itertools.product(range(NUM_MOST_FREQ_LETTERS), repeat=mostLikelyKeyLength):
        # Create a possible key from the letters in allFreqScores
        possibleKey = ''
        for i in range(mostLikelyKeyLength):
            possibleKey += allFreqScores[i][indexes[i]][0]
    
        if not SILENT_MODE:
            print('Attempting with key: %s' % (possibleKey))
    
        decryptedText = vigenereCipher.decryptMessage(possibleKey, ciphertextUp)
    
        if detectEnglish.isEnglish(decryptedText):
            # Set the hacked ciphertext to the original casing.
            origCase = []
            for i in range(len(ciphertext)):
                if ciphertext[i].isupper():
                    origCase.append(decryptedText[i].upper())
                else:
                    origCase.append(decryptedText[i].lower())
            decryptedText = ''.join(origCase)
        
            # Check with user to see if the key has been found.
            print('Possible encryption hack with key %s:' % (possibleKey))
            print(decryptedText[:200]) # only show first 200 characters
            print()
            print('Enter D for done, or just press Enter to continue hacking:')
            response = input('> ')
        
            if response.strip().upper().startswith('D'):
                return decryptedText

    # No English-looking decryption found, so return None.
    return None


cipherText = """LGEMXKLOYZRKEWVYGKMOKKLOLVEBXKLOOFCKZVWYYKLOLKEBLYMZXEXOKGVSLVMDLTSXMZREBEKWBJWSHEXYXOTVHIICMIEXZVROPNSBEUWDHJIODFYDGVAVBWIKGUROPTMFBCMJTKMYGJXYUFPNEPKYPYIBXESYGVLKLXSXXSIPHIIIHLNEWXIIHLVCXCZOLRKKBEWDMYIZBKMPNCENOVVCTIMOLPSENMIOGTSEGKIBXUWYYRVDAVVYFLPKGJXRXBPSGXSXLKLORIIXHKLSGXGYFGEBXUXYPYEDLNESMZRQIZGKKUCYNRVOTSSEMKSWHMISGKSKKVECHWXRXXEVTOCMHEXKBEMXZNSXWVVCFFVOBEGBXUMLEVXRTECYNTEXIFWCBSPIBDEQBEIKGUXOKISBLKSPKVIJXPSEKJSEEZSPYVVWRJIVYRWKZLMNXFRVRKSLXIITXTXOWFYDHWLKGU"""
# shift and check coincidences
maxC = 0
maxD = 1
for displacement in range(1, len(cipherText) / 2):
		coin = 0
		for i in range(len(cipherText) - displacement):
				if cipherText[i] == cipherText[i + displacement]:
						coin += 1
		print 'displacement:', displacement,'\tcoin:', coin
		if coin > maxC:
				maxC = coin
				maxD = displacement
print 'max coincidence:', maxC, 'max displacement:', maxD

# use maxD as key length
hackedMessage = attemptHackWithKeyLength(ciphertext, maxD)
if hackedMessage != None:
    print(hackedMessage)
else:
    print('Failed to hack encryption.')
