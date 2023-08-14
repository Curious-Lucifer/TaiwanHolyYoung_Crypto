from math import gcd
import random

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ \"'#,?:@!.-"
alphabet_length = len(alphabet)

def char2num(char):
    assert len(char) == 2
    return alphabet.index(char[0]) * alphabet_length + alphabet.index(char[1])

def num2char(num):
    return alphabet[num // alphabet_length] + alphabet[num % alphabet_length]

def encrypt(plain, a, b):
    assert (gcd(alphabet_length ** 2, a) == 1) and ((len(plain) % 2) == 0)
    cipher = [(a * char2num(plain[i: i + 2]) + b) % (alphabet_length ** 2) for i in range(0, len(plain), 2)]
    return ''.join(num2char(num) for num in cipher)

plain = open('plain.txt').read()
a, b = random.randint(1, alphabet_length ** 2 - 1), random.randint(0, alphabet_length ** 2 - 1)
cipher = encrypt(plain, a, b)

print(cipher)