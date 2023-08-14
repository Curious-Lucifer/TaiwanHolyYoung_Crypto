from Crypto.Cipher import AES
import os, sys

from secret import flag

iv = os.urandom(16)
key = os.urandom(32)

def pad(msg):
    padding = 16 - (len(msg) % 16)
    return msg + bytes([padding]) * padding

def unpad(msg):
    padding = msg[-1]
    assert 1 <= padding <= 16
    assert msg.endswith(bytes([padding]) * padding)
    return msg[:-padding]

def encrypt(username, uid=b"1337"):
    aes = AES.new(key, AES.MODE_CBC, iv)
    cipher = aes.encrypt(pad(username) + pad(uid))
    return cipher

def decrypt(cipher):
    aes = AES.new(key, AES.MODE_CBC, iv)
    plain = aes.decrypt(cipher)
    return plain[:-16], unpad(plain[-16:])

def login():
    username = input("Username > ").encode()
    print(f"Token : {encrypt(username).hex()}")

def verify():
    token = bytes.fromhex(input("Token > "))
    username, uid = decrypt(token)

    print(f'Welcome {username.hex()} !')

    if uid == b"0":
        print(f"Flag : {flag}")

def main():
    while True:
        print("1. Login")
        print("2. Verify")
        print("3. Exit")
        choice = input("Choice > ")
        if choice == '1':
            login()
        elif choice == '2':
            verify()
        else:
            sys.exit()

try:
    main()
except:
    sys.exit()