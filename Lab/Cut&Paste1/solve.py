from pwn import *

'''
username=Curious
sss&username=adm
0000000000000000
in&money=1000000
ssssss&money=100
&id=????????
'''

r = remote('35.201.230.193', 10001)

r.sendlineafter(b'> ', b'Curioussss&username=adm0000000000000000in&money=1000000ssssss')

token = bytes.fromhex(r.recvline().strip().split(b': ')[1].decode())
new_token = token[:32] + token[48: 64] + token[32: 48] + token[80:]

r.sendlineafter(b'> ', b'4')
r.sendlineafter(b'> ', new_token.hex().encode())

r.interactive()