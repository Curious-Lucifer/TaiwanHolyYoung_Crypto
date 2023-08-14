import sys
sys.path.append('/home/curious/code')

from CTFLib.Crypto.Classical_Cipher import *
from math import gcd
from tqdm import trange
import hashlib

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ \"'#,?:@!.-"
alphabet_length = len(alphabet)

cipher = open('cipher.txt').read()

def char2num(char):
    assert len(char) == 2
    return alphabet.index(char[0]) * alphabet_length + alphabet.index(char[1])

def num2char(num):
    return alphabet[num // alphabet_length] + alphabet[num % alphabet_length]

def decrypt(cipher, a, b):
    a_inv = pow(a, -1, alphabet_length ** 2)
    plain = [(a_inv * (char2num(cipher[i: i + 2]) - b)) % (alphabet_length ** 2) for i in range(0, len(cipher), 2)]
    return ''.join(num2char(num) for num in plain)

freq_list = []
key_list = []
for a in trange(1, alphabet_length ** 2):
    if gcd(a, alphabet_length ** 2) != 1:
        continue
    for b in range(alphabet_length ** 2):
        plain_test = decrypt(cipher, a, b)
        freq = simple_freq_analysis(plain_test)
        if (freq < 500):
            freq_list.append(freq)
            key_list.append((a, b))

a, b = key_list[freq_list.index(min(freq_list))]
plain = decrypt(cipher, a, b)

print(f'FLAG{{{hashlib.md5(plain.encode()).hexdigest()}}}')