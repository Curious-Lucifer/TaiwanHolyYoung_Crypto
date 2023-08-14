import sys
sys.path.append('/home/curious/code')

from CTFLib.Crypto.PRNG import lcg_attack
from CTFLib.Crypto.Utils import generate_lcg
from pwn import *

r = remote('35.201.230.193', 10006)

state = [int(s) for s in r.recvline().strip().split(b': ')[1].split(b',')]
m, inc, N = lcg_attack(state)
s = generate_lcg(state[0], m, inc, N, len(state))

r.sendlineafter(b'> ', str(s).encode())

r.interactive()