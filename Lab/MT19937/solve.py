import sys
sys.path.append('/home/curious/code')

from CTFLib.Crypto.PRNG import MT19937_attack
from pwn import *
from tqdm import trange

r = remote('35.201.230.193', 10007)

rand_list = []

rand_list.append(int(r.recvline().strip().split(b': ')[1]))
for i in trange(623):
    r.sendlineafter(b'> ', str(-rand_list[-1]).encode())
    rand_list.append(int(r.recvline().strip().split(b': ')[1]))

new_rand = MT19937_attack(rand_list, 624)
ans = - (rand_list[-1] + new_rand)

r.sendlineafter(b'> ', str(ans).encode())

r.interactive()