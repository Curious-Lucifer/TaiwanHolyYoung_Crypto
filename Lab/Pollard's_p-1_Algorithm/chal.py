from Crypto.Util.number import bytes_to_long, getPrime, isPrime
from Crypto.Random.random import randrange

from secret import flag

def genkey(nbits):
    while True:
        p = 2
        while p.bit_length() < nbits:
            p *= getPrime(randrange(2, 12))
        if isPrime(p + 1):
            return p + 1

p = genkey(512)
q = getPrime(512)
n = p * q
e = 65537

c = pow(bytes_to_long(flag), e, n)

print(f'{n, e = }')
print(f'{c = }')
