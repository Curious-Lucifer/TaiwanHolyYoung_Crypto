import sys
sys.path.append('/home/curious/code')

from CTFLib.Crypto.Hash import length_extension_attack
from pwn import *


r = remote('35.201.230.193', 10009)

token = bytes.fromhex(r.recvline().strip().split(b': ')[1].decode())
payload, sig = token[:-32], token[-32:]

new_sig, new_payload = length_extension_attack(sig, payload, b'&user=admin&admin=1', 50)
new_token = new_payload + new_sig

r.sendlineafter(b'> ', new_token.hex().encode())

r.interactive()