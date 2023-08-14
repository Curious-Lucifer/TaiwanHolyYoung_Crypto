from pwn import *
from tqdm import trange

r = remote('35.201.230.193', 10003)

for i in trange(100):
    cipher = bytes.fromhex(r.recvline().strip().split(b': ')[1].decode())
    old_plain_block = bytes.fromhex(r.recvline().strip().split(b': ')[1].decode())
    new_plain_block = bytes.fromhex(r.recvline().strip().split(b': ')[1].decode())

    new_cipher = cipher[:-32] + xor(cipher[-32: -16], old_plain_block, new_plain_block) + cipher[-16:]
    r.sendlineafter(b'> ', new_cipher.hex().encode())

r.interactive()