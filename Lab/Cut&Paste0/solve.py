from pwn import *

'''
username=Curious
0000000000000000
ssssss&money=100
&id=????????
'''

r = remote('35.201.230.193', 10000)

r.sendlineafter(b'> ', b'Curious0000000000000000ssssss')

token = bytes.fromhex(r.recvline().strip().split(b': ')[1].decode())
new_token = token[:16] + token[32: 48] + token[16: 32] + token[48:]

r.sendlineafter(b'> ', b'4')
r.sendlineafter(b'> ', new_token.hex().encode())

r.interactive()