from pwn import *

r = remote('35.201.230.193', 10002)

r.sendlineafter(b'> ', b'1')
r.sendlineafter(b'> ', b'Curious')

token = bytes.fromhex(r.recvline().strip().split(b': ')[1].decode())
new_token = xor(token[:16], b'1337' + b'\x0c' * 12, b'0' + b'\x0f' * 15) + token[16:]

r.sendlineafter(b'> ', b'2')
r.sendlineafter(b'> ', new_token.hex().encode())

r.interactive()