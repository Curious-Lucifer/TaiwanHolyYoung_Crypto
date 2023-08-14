from hashlib import md5
from tqdm import trange

def untransform(msg):
    msg = bytearray(msg)
    for i in range(0, len(msg), 4):
        d = msg[i + 2]
        a = msg[i + 1]
        b = msg[i + 3]
        c = msg[i]
        msg[i] = a
        msg[i + 1] = b
        msg[i + 2] = c
        msg[i + 3] = d

    return bytes(msg)

cipher_list = [untransform(cipher.encode()) for cipher in open('chal.txt').read().strip().split('\n')]
plain_list = [b''] * len(cipher_list)

count = len(cipher_list)
for i in trange(128):
    for j in range(128):
        for k in range(128):
            for l in range(128):
                test = md5(bytes([i, j, k, l])).hexdigest().encode()
                if test in cipher_list:
                    idx = cipher_list.index(test)
                    plain_list[idx] = bytes([i, j, k, l])
                    cipher_list[idx] = b''
                    count -= 1
                if count == 0:
                    break
            if count == 0:
                break
        if count == 0:
            break
    if count == 0:
        break

print(b''.join(plain_list))