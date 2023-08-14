from Crypto.Cipher import AES
import os, sys

from secret import flag

def pad(msg):
    pad = 16 - (len(msg) % 16)
    return msg + bytes([pad]) * pad

def unpad(msg):
    assert 1 <= msg[-1] <= 16
    assert msg.endswith(msg[-1:] * msg[-1])
    return msg[:-msg[-1]]

def main():
    iv = os.urandom(16)
    key = os.urandom(32)

    aes = AES.new(key, AES.MODE_CBC, iv)
    flag_cipher = aes.encrypt(pad(flag))
    print(f'Flag\' Cipher = {(iv + flag_cipher).hex()}')

    while True:
        cipher = bytes.fromhex(input('Cipher > ').strip())
        if (len(cipher) < 32) or ((len(cipher) % 16) != 0):
            sys.exit()
        iv, cipher = cipher[:16], cipher[16:]
        try:
            aes = AES.new(key, AES.MODE_CBC, iv)
            unpad(aes.decrypt(cipher))
            print('CORRECT!!!')
        except:
            print('ERROR!!!')

try:
    main()
except:
    sys.exit()