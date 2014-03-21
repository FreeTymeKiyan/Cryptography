# hack vigenre
import sys
sys.path.append('../lib')
sys.path.append('../CeaserCipher')
import BasicFunc
import HackCeaser
import VigenereDecrypt

def main():
    print 'vigenere encrypted message:'
    #msg = 'LGEMXKLOYZRKEWVYGKMOKKLOLVEBXKLOOFCKZVWYYKLOLKEBLYMZXEXOKGVSLVMDLTSXMZREBEKWBJWSHEXYXOTVHIICMIEXZVROPNSBEUWDHJIODFYDGVAVBWIKGUROPTMFBCMJTKMYGJXYUFPNEPKYPYIBXESYGVLKLXSXXSIPHIIIHLNEWXIIHLVCXCZOLRKKBEWDMYIZBKMPNCENOVVCTIMOLPSENMIOGTSEGKIBXUWYYRVDAVVYFLPKGJXRXBPSGXSXLKLORIIXHKLSGXGYFGEBXUXYPYEDLNESMZRQIZGKKUCYNRVOTSSEMKSWHMISGKSKKVECHWXRXXEVTOCMHEXKBEMXZNSXWVVCFFVOBEGBXUMLEVXRTECYNTEXIFWCBSPIBDEQBEIKGUXOKISBLKSPKVIJXPSEKJSEEZSPYVVWRJIVYRWKZLMNXFRVRKSLXIITXTXOWFYDHWLKGU'
    msg = 'yyccrcajetafxjusjlozlcaizmcyforztzipjcklszchmjbjvrlkcokammomfovqhtoslhbakzyamevbvryjgvxyvkwhzrjmvbkolwehtitwexslezsydjwzpyyvbqllrcirpwyvgcwedpvvbdohwrgkfxlqhewsyeesmdicpibuhwlgyhgvydiadbztqlrrcryvxsklkghijlhkspwaevlwnvsrktedmmvgxpwswkkeuxrlryvvivpxaqrlktnipsvuxcphthgbukeruifdiblsivkuwgmrillilhuwemfuecspzxsictfvqwalenzcvlyjrdstriwygcfnziqxapgpwmkejxmqunzjzzbpurwxypmoqretapvfktivlqlwewbuodkggeprivohzqedfxcobjedmmveyvcswuhowvryrgghikukjktlggxenvseaspfdvoriecibwfwerdsddppgnjhbwsvrhvvosehuzipgwemynjxedvammiazqzxmcfrsdpgnjuijmxatasdivwsoklsxwzzfslprfwyderqgxejdoigjlwfygmmqtmpwfeqscitkqiwdiwrtzvwatwrepllyfpaobljwvnahcuifrhvqmhnwryepmcpqdemmbuxammejtqzsqowsoaasopsucwyvoikkwlwmhyrwneatykmnvbipoxmlgcszuoebgusjldlsgxbjidyisfszlcgyoksprmfdklxripmxyvcpsipakgbkdolexbvvsxpqkeiypsndmzcjbvftsenzyvuowgidirrlqrlhmarmgamyqvxsczspwtwbtzsiyjhymdlkasxhdwgkhnjszninarkmlkzzsdggevceoezpemmfhlvpexgwfcxmxstrjamasofdcewhxlqhlzexiclcobtykweptamyrrpwyvcpwtdhscfcqojiwvomeqwlzaztpcpwjwjhiaqhafofpwcorcrsezealhlzcemxxkkgytmlitkncqazundefinedlsmkdfwpomqbzoslahzpaweqzinllillautiewsgvcainmotknvfnsxdsguhvikabkwdhrgfsvwwxmomgdilacgpjmvnmlvfjyhubxmskxmderecedhscfcqojiqxjpszmkes'
    print msg
    text = hackVigenere(msg)
    print 
    print 'hacked message:'
    print text
    return text

def getNthLetter(text, n):
    result = []
    idx = 0
    # get rid of spaces and non-english char
    for symbol in text.upper():
        if symbol in BasicFunc.LETTERS:
            if len(result) < n:
                result.append(symbol)
            else:
                result[idx % n] += symbol
            idx += 1
    return result

def hackVigenere(text):
    keyLength = BasicFunc.findCoincidence(text)
    sentences = getNthLetter(text, keyLength)
    # print sentences
    key = ''
    for s in sentences:
        curKeyInt = HackCeaser.hackCeaser(s)[0][0]
        key += BasicFunc.LETTERS[curKeyInt]
        # for i in range(5):
            # print BasicFunc.LETTERS[curKeyInt[i][0]],
    print 
    print 'possible key:'
    print key
    # decrypt vigenere with this key
    return VigenereDecrypt.decryptVigenere(text, key)

if __name__ == '__main__':
    main()
