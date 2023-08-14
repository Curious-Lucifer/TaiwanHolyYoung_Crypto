from Crypto.Cipher import AES
import sys, os

from secret import flag

iv = os.urandom(16)
key = os.urandom(32)

def encrypt(plain, key, iv):
    assert (len(plain) % 16) == 0
    aes = AES.new(key, AES.MODE_CBC, iv)
    return aes.encrypt(plain)

def decrypt(cipher, key, iv):
    assert (len(cipher) % 16) == 0
    aes = AES.new(key, AES.MODE_CBC, iv)
    return aes.decrypt(cipher)

def main():
    for i in range(100):
        plain = os.urandom(48)
        new_plain_block = os.urandom(16)

        print(f'Cipher : {encrypt(plain, key, iv).hex()}')
        print(f'Last Block Of Plain : {plain[-16:].hex()}')
        print(f'Last Block Of New Plain : {new_plain_block.hex()}')
        new_cipher = bytes.fromhex(input('New Cipher > '))
        assert len(new_cipher) == len(plain)
        if decrypt(new_cipher, key, iv)[-16:] != new_plain_block:
            print('Wrong!')
            sys.exit()
    print(f'Flag : {flag}')

try:
    main()
except:
    sys.exit()