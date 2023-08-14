import sys
sys.path.append('/home/curious/code')

from CTFLib.Crypto.RSA import factor_online
from Crypto.Util.number import long_to_bytes

n, e = (153492655596332768779183, 65537)
c = 26221050060582353115054

[p, _, q, r] = factor_online(n)
phi = p * (p - 1) * (q - 1) * (r - 1)
d = pow(e, -1, phi)
m = pow(c, d, n)

print(long_to_bytes(m))