import pyAES

def intToList(number):
    """Convert a 16-byte number into a 16-element list"""
    return [(number >> 120) & 0xff, (number >> 112) & 0xff,
            (number >> 104) & 0xff, (number >> 96)  & 0xff,
            (number >> 88)  & 0xff, (number >> 80)  & 0xff,
            (number >> 72)  & 0xff, (number >> 64)  & 0xff,
            (number >> 56)  & 0xff, (number >> 48)  & 0xff,
            (number >> 40)  & 0xff, (number >> 32)  & 0xff,
            (number >> 24)  & 0xff, (number >> 16)  & 0xff,
            (number >> 8)   & 0xff,  number & 0xff]

def intToText(hexNumber):
    """Convert a 16-byte number into a 16 char text string"""
    return "".join(chr(e) for e in intToList(hexNumber))

def checkTestVector1(mode, keySize, key, plaintext, ciphertext, iv = None):
    """Check test vectors for single block encryption and decryption"""
    success = True
    obj = pyAES.AES(mode)
    obj.setKey(keySize, key, iv)
    for i, (p, c) in enumerate(zip(plaintext, ciphertext)):
        p_text = intToText(p)
        c_text = intToList(c)
        code = "{0:3s}-{1:3s}".format(mode[5:], keySize[5:])
        try:
            assert obj.encrypt(p_text) == c_text
        except AssertionError:
            print(code, "encryption #{:d} failed".format(i))
            success = False
        try:
            assert obj.decrypt(c_text) == p_text
        except AssertionError:
            print(code, "decryption #{:d} failed".format(i))
            success = False
    if success:
        print(code, "encryption/decryption ok")
    return success

def checkTestVector2(mode, keySize, plaintext, key1, key2, iv1 = None, iv2 = None):
    obj1 = pyAES.AES(mode, "PKCS5Padding")
    obj1.setKey(keySize, key1, iv1)
    obj2 = pyAES.AES(mode, "PKCS5Padding")
    obj2.setKey(keySize, key2, iv2)
    ciphertext1 = obj1.encrypt(plaintext)
    ciphertext2 = obj2.encrypt(plaintext)
    plaintext1 = obj1.decrypt(ciphertext1)
    plaintext2 = obj2.decrypt(ciphertext2)
    code = "{0:3s}-{1:3s}".format(mode[5:], keySize[5:])
    try:
        assert plaintext1 == plaintext and plaintext2 == plaintext
    except AssertionError:
        print("Multi-block", code, "encryption/decryption failed")
        return False
    print("Multi-block", code, "encryption/decryption ok")
    return True

#===========================================================================

# Test vectors from NIST SP800-38A sections F.1.1 and F.1.2
def ECB_128_NOPAD():
    key = 0x2b7e151628aed2a6abf7158809cf4f3c
    plaintext =  [0x6bc1bee22e409f96e93d7e117393172a,
                  0xae2d8a571e03ac9c9eb76fac45af8e51,
                  0x30c81c46a35ce411e5fbc1191a0a52ef,
                  0xf69f2445df4f9b17ad2b417be66c3710]
    ciphertext = [0x3ad77bb40d7a3660a89ecaf32466ef97,
                  0xf5d3d58503b9699de785895a96fdbaaf,
                  0x43b1cd7f598ece23881b00e3ed030688,
                  0x7b0c785e27e8ad3f8223207104725dd4]
    return checkTestVector1("MODE_ECB", "SIZE_128", key, plaintext, ciphertext)

# Test vectors from NIST SP800-38A sections F.1.3 and F.1.4
def ECB_192_NOPAD():
    key = 0x8e73b0f7da0e6452c810f32b809079e562f8ead2522c6b7b
    plaintext =  [0x6bc1bee22e409f96e93d7e117393172a,
                  0xae2d8a571e03ac9c9eb76fac45af8e51,
                  0x30c81c46a35ce411e5fbc1191a0a52ef,
                  0xf69f2445df4f9b17ad2b417be66c3710]
    ciphertext = [0xbd334f1d6e45f25ff712a214571fa5cc,
	              0x974104846d0ad3ad7734ecb3ecee4eef,
                  0xef7afd2270e2e60adce0ba2face6444e,
                  0x9a4b41ba738d6c72fb16691603c18e0e]
    return checkTestVector1("MODE_ECB", "SIZE_192", key, plaintext, ciphertext)

# Test vectors from NIST SP800-38A sections F.1.5 and F.1.6
def ECB_256_NOPAD():
    key = 0x603deb1015ca71be2b73aef0857d77811f352c073b6108d72d9810a30914dff4
    plaintext =  [0x6bc1bee22e409f96e93d7e117393172a,
                  0xae2d8a571e03ac9c9eb76fac45af8e51,
                  0x30c81c46a35ce411e5fbc1191a0a52ef,
                  0xf69f2445df4f9b17ad2b417be66c3710]
    ciphertext = [0xf3eed1bdb5d2a03c064b5a7e3db181f8,
                  0x591ccb10d410ed26dc5ba74a31362870,
                  0xb6ed21b99ca6f4f9f153e7b1beafed1d,
                  0x23304b7a39f9f3ff067d8d8f9e24ecc7]
    return checkTestVector1("MODE_ECB", "SIZE_256", key, plaintext, ciphertext)

# Test vectors from NIST SP800-38A sections F.2.1 and F.2.2
def CBC_128_NOPAD():
    key = 0x2b7e151628aed2a6abf7158809cf4f3c
    iv = 0x000102030405060708090a0b0c0d0e0f
    plaintext =  [0x6bc1bee22e409f96e93d7e117393172a,
                  0xae2d8a571e03ac9c9eb76fac45af8e51,
                  0x30c81c46a35ce411e5fbc1191a0a52ef,
                  0xf69f2445df4f9b17ad2b417be66c3710]
    ciphertext = [0x7649abac8119b246cee98e9b12e9197d,
                  0x5086cb9b507219ee95db113a917678b2,
                  0x73bed6b8e3c1743b7116e69e22229516,
                  0x3ff1caa1681fac09120eca307586e1a7]
    return checkTestVector1("MODE_CBC", "SIZE_128", key, plaintext, ciphertext, iv)

# Test vectors from NIST SP800-38A sections F.2.3 and F.2.4
def CBC_192_NOPAD():
    key = 0x8e73b0f7da0e6452c810f32b809079e562f8ead2522c6b7b
    iv = 0x000102030405060708090a0b0c0d0e0f
    plaintext =  [0x6bc1bee22e409f96e93d7e117393172a,
                  0xae2d8a571e03ac9c9eb76fac45af8e51,
                  0x30c81c46a35ce411e5fbc1191a0a52ef,
                  0xf69f2445df4f9b17ad2b417be66c3710]
    ciphertext = [0x4f021db243bc633d7178183a9fa071e8,
                  0xb4d9ada9ad7dedf4e5e738763f69145a,
                  0x571b242012fb7ae07fa9baac3df102e0,
                  0x08b0e27988598881d920a9e64f5615cd]
    return checkTestVector1("MODE_CBC", "SIZE_192", key, plaintext, ciphertext, iv)

# Test vectors from NIST SP800-38A sections F.2.5 and F.2.6
def CBC_256_NOPAD():
    key = 0x603deb1015ca71be2b73aef0857d77811f352c073b6108d72d9810a30914dff4
    iv = 0x000102030405060708090a0b0c0d0e0f
    plaintext=  [0x6bc1bee22e409f96e93d7e117393172a,
                 0xae2d8a571e03ac9c9eb76fac45af8e51,
                 0x30c81c46a35ce411e5fbc1191a0a52ef,
                 0xf69f2445df4f9b17ad2b417be66c3710]
    ciphertext = [0xf58c4c04d6e5f1ba779eabfb5f7bfbd6,
                  0x9cfc4e967edb808d679f777bc6702c7d,
                  0x39f23369a9d9bacfa530e26304231461,
                  0xb2eb05e2c39be9fcda6c19078c6a9d1b]
    return checkTestVector1("MODE_CBC", "SIZE_256", key, plaintext, ciphertext, iv)

#===========================================================================

# Two multi-block encryptions in ECB mode with 128-bit key
def ECB_128_PKCS5():
    plaintext = "The quick brown fox jumps over the lazy dog"
    key1 = 0x000102030405060708090a0b0c0d0e0f
    key2 = 0xffeeddccbbaa99887766554433221100
    return checkTestVector2("MODE_ECB", "SIZE_128", plaintext, key1, key2)

# Two multi-block encryptions in ECB mode with 192-bit key
def ECB_192_PKCS5():
    plaintext = "The quick brown fox jumps over the lazy dog"
    key1 = 0x000102030405060708090a0b0c0d0e0f1011121314151617
    key2 = 0x1716151413121110ffeeddccbbaa99887766554433221100
    return checkTestVector2("MODE_ECB", "SIZE_192", plaintext, key1, key2)

# Two multi-block encryptions in ECB mode with 256-bit key
def ECB_256_PKCS5():
    plaintext = "The quick brown fox jumps over the lazy dog"
    key1 = 0x000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f
    key2 = 0x1f1e1d1c1b1a19181716151413121110ffeeddccbbaa99887766554433221100
    return checkTestVector2("MODE_ECB", "SIZE_256", plaintext, key1, key2)

# Two multi-block encryptions in CBC mode with 128-bit key
def CBC_128_PKCS5():
    plaintext = "The quick brown fox jumps over the lazy dog"
    key1 = 0x000102030405060708090a0b0c0d0e0f
    key2 = 0xffeeddccbbaa99887766554433221100
    iv1 = 0x0123cdef456789ab0123cdef456789ab
    iv2 = 0xab0123cdef456789ab0123cdef456789
    return checkTestVector2("MODE_CBC", "SIZE_128", plaintext, key1, key2, iv1, iv2)

# Two multi-block encryptions in CBC mode with 192-bit key
def CBC_192_PKCS5():
    plaintext = "The quick brown fox jumps over the lazy dog"
    key1 = 0x000102030405060708090a0b0c0d0e0f1011121314151617
    key2 = 0x1716151413121110ffeeddccbbaa99887766554433221100
    iv1 = 0x0123cdef456789ab0123cdef456789ab
    iv2 = 0xab0123cdef456789ab0123cdef456789
    return checkTestVector2("MODE_CBC", "SIZE_192", plaintext, key1, key2, iv1, iv2)

# Two multi-block encryptions in CBC mode with 256-bit key
def CBC_256_PKCS5():
    plaintext = "The quick brown fox jumps over the lazy dog"
    key1 = 0x000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f
    key2 = 0x1f1e1d1c1b1a19181716151413121110ffeeddccbbaa99887766554433221100
    iv1 = 0x0123cdef456789ab0123cdef456789ab
    iv2 = 0xab0123cdef456789ab0123cdef456789
    return checkTestVector2("MODE_CBC", "SIZE_256", plaintext, key1, key2, iv1, iv2)

def main():
    # Perform vector tests
    testSuccess = True
    for pad in ["NOPAD", "PKCS5"]:
        for mode in ["ECB", "CBC"]:
            for size in ["128", "192", "256"]:
                testVector = mode + "_" + size + "_" + pad + "()"
                testSuccess = testSuccess & eval(testVector)
    if testSuccess:
        print("All tests passed!")

if __name__ == '__main__':
    main()
