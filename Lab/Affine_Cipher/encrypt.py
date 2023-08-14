import random

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ \"'#,?:@!.-"

def char2num(char):
    return alphabet.index(char)

def num2char(num):
    return alphabet[num]

def encrypt(plain, a, b):
    cipher = [(a * char2num(char) + b) % len(alphabet) for char in plain]
    return ''.join(num2char(num) for num in cipher)

plain = open('plain.txt').read()
a, b = random.randint(1, len(alphabet) - 1), random.randint(0, len(alphabet) - 1)
cipher = encrypt(plain, a, b)

print(cipher)