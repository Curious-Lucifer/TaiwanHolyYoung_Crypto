import sys
sys.path.append('/home/curious/code')

from CTFLib.Crypto.RSA import factor_online
from Crypto.Util.number import long_to_bytes

n, e = (7962448770086475881, 65537)
c = 7104869032992491716

[p, q] = factor_online(n)
d = pow(e, -1, (p - 1) * (q - 1))
m = pow(c, d, n)

print(long_to_bytes(m))