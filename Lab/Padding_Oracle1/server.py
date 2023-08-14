from Crypto.Cipher import AES
from base64 import b64encode,b64decode
import os
import sys

from secret import flag

iv = os.urandom(16)
key = os.urandom(32)

def pad(msg):
    padding = 16 - (len(msg) % 16)
    return msg + bytes([padding]) * padding

def unpad(msg):
    assert (len(msg) % 16) == 0
    padding = msg[-1]
    assert (1 <= padding <= 16) and msg.endswith(bytes([padding]) * padding)
    return msg[:-padding]

def encrypt(plain):
    aes_cbc = AES.new(key, AES.MODE_CBC, iv)
    return aes_cbc.encrypt(pad(plain))

def decrypt(cipher):
    assert (len(cipher) % 16) == 0
    aes_cbc = AES.new(key, AES.MODE_CBC, iv)
    plain = aes_cbc.decrypt(cipher)
    try:
        plain = unpad(plain)
        return 'Message Stored'
    except:
        return 'Error !'

def signature(msg):
    assert len(msg) > 16
    aes = AES.new(key, AES.MODE_ECB)
    return aes.encrypt(encrypt(msg)[-16:])

def main():
    print('Welcome Secure Store GPT')
    print('=' * 36)

    token = os.urandom(0x18)
    token_sig = b64encode(pad(token) + signature(token)).decode()
    print(f'Token : {token_sig}')
    FLAG_cipher = b64encode(encrypt(flag)).decode()
    print(f'Flag : {FLAG_cipher}')
    print('=' * 36)

    while True:
        cipher = b64decode(input('Cipher : ').encode())
        print(decrypt(cipher))

try:
    main()
except:
    sys.exit()