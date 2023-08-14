from hashlib import md5

from secret import flag

def transform(msg):
    msg = bytearray(msg)
    for i in range(0, len(msg), 4):
        a = msg[i]
        b = msg[i + 1]
        c = msg[i + 2]
        d = msg[i + 3]
        msg[i + 2] = d
        msg[i + 1] = a
        msg[i + 3] = b
        msg[i] = c

    return bytes(msg)


flag += b'0' * (4 - (len(flag) % 4))
for i in range(0, len(flag), 4):
    print(transform(md5(flag[i: i + 4]).hexdigest().encode()).decode())
