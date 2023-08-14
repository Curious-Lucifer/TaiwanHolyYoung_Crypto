import sys
sys.path.append('/home/curious/code')

from CTFLib.Crypto.Classical_Cipher import simple_freq_analysis
from tqdm import trange
import hashlib

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ \"'#,?:@!.-"

cipher = open('cipher.txt').read()

def char2num(char):
    return alphabet.index(char)

def num2char(num):
    return alphabet[num]

def decrypt(cipher, a, b):
    a_inv = pow(a, -1, len(alphabet))
    plain = [(a_inv * (char2num(char) - b)) % len(alphabet) for char in cipher]
    return ''.join(num2char(num) for num in plain)

freq_list = []
key_list = []
for a in trange(1, len(alphabet)):
    for b in range(len(alphabet)):
        plain_test = decrypt(cipher, a, b)
        freq_list.append(simple_freq_analysis(plain_test))
        key_list.append((a, b))

a, b = key_list[freq_list.index(min(freq_list))]
plain = decrypt(cipher, a, b)

print(f'FLAG{{{hashlib.md5(plain.encode()).hexdigest()}}}')