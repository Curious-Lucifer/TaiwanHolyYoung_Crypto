from Crypto.Util.number import getPrime, bytes_to_long
import os

from secret import flag

p, q = getPrime(1024), getPrime(1024)
n = p * q
d = getPrime(500)
e = pow(d, -1, (p - 1) * (q - 1))

flag += b'\x00' + os.urandom(n.bit_length() // 8 - len(flag) - 1)
c = pow(bytes_to_long(flag), e, n)

print(f'{n, e = }')
print(f'{c = }')