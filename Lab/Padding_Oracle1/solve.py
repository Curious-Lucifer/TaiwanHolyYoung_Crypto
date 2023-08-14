import sys
sys.path.append('/home/curious/code')

from CTFLib.Crypto.Block_Cipher import padding_oracle_attack
from pwn import *
from base64 import b64encode, b64decode

r = remote('35.201.230.193', 10005)

r.recvlines(2)

token_sig = b64decode(r.recvline().strip().split(b': ')[1].decode())
token, sig = token_sig[:-16], token_sig[-16:]
flag_enc = b64decode(r.recvline().strip().split(b': ')[1].decode())

r.recvlines(1)

def oracle(cipher):
    r.sendlineafter(b': ', b64encode(cipher))
    return b'Message Stored' in r.recvline()

pre_token = padding_oracle_attack(b'\x00' * 16, sig, oracle)
pre_token = xor(padding_oracle_attack(b'\x00' * 16, pre_token, oracle), token[-16:])
iv = xor(padding_oracle_attack(b'\x00' * 16, pre_token, oracle), token[:16])

flag_enc = iv + flag_enc
flag = b''
for i in range(0, len(flag_enc) - 16, 16):
    flag +=  padding_oracle_attack(flag_enc[i:i + 16], flag_enc[i + 16:i + 32], oracle)

print(flag)

r.close()
