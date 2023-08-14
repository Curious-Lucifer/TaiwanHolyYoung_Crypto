import hashlib, os, sys

from secret import flag

secret = os.urandom(50)

payload = b'user=anonymous&admin=0'
sig = hashlib.sha256(secret + payload).digest()
print(f'Token : {(payload + sig).hex()}')

try:
    new_token = bytes.fromhex(input('New Token > '))
    payload, sig = new_token[:-32], new_token[-32:]
    if sig != hashlib.sha256(secret + payload).digest():
        print("Error!")
        sys.exit()

    data = dict(map(lambda x: x.split(b"="), payload.split(b"&")))
    if (data[b'admin'] == b'1') and (data[b'user'] == b'admin'):
        print(f'Flag : {flag}')
    else:
        print('You are not admin QQ')
except:
    sys.exit()