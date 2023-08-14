import sys
sys.path.append('/home/curious/code')

from CTFLib.Crypto.PRNG import *
from pwn import *
from tqdm import trange

r = remote('35.201.230.193', 10008)

r.recvline()

def get_random():
    r.sendlineafter(b'> ', b'-1')
    return int(r.recvline().strip().split(b'is ')[1].decode()) - 0x80000000

randlist = [get_random() for _ in trange(624 * 2)]

state = [MT19937_rand2state(randlist[0] << 1)]
for i in range(624):
    s_test = MT19937_rand2state(randlist[i + 1] << 1)
    s_xor = MT19937_rand2state(randlist[i + 397] << 1)
    s_new = MT19937_rand2state(randlist[i + 624] << 1)

    if (bin((s_test >> 1) ^ s_xor)[2:].rjust(32, '0')[11] != bin(s_new)[2:].rjust(32, '0')[11]):
        state.append(MT19937_rand2state((randlist[i + 1] << 1) | 1))
    else:
        state.append(s_test)

state, next_state0 = state[:-1] ,state[-1]
MT19937_gen_next_state(state)
state[0] = next_state0

MT19937_gen_next_state(state)

for i in range(100):
    r.sendlineafter(b'> ', str((MT19937_state2rand(state[i]) >> 1) + 0x80000000).encode())
    r.recvline()

r.interactive()