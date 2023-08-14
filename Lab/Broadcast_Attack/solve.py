import sys
sys.path.append('/home/curious/code')

from CTFLib.Crypto.Utils import crt
from Crypto.Util.number import long_to_bytes
from gmpy2 import iroot

n_list = []
c_list = []
with open('chal.txt') as f:
    for i in range(11):
        n = int(f.readline().strip().split('= ')[1].split(', ')[0])
        c = int(f.readline().strip().split('= ')[1])
        n_list.append(n)
        c_list.append(c)

c = crt(c_list, n_list)
print(long_to_bytes(int(iroot(c, 11)[0])))