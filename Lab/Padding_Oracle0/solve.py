import sys
sys.path.append('/home/curious/code')

from CTFLib.Crypto.Block_Cipher import padding_oracle_attack
from pwn import *

r = remote('35.201.230.193', 10004)

iv_cipher = bytes.fromhex(r.recvline().strip().split(b'= ')[1].decode())

def oracle(cipher):
    r.sendlineafter(b'> ', cipher.hex().encode())
    return b'CORRECT' in r.recvline()

plain = b''
for i in range(0, len(iv_cipher) - 16, 16):
    plain += padding_oracle_attack(iv_cipher[i: i + 16], iv_cipher[i + 16: i + 32], oracle)

print(plain)

r.close()