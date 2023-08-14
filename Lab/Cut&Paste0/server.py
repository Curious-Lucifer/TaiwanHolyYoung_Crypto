from Crypto.Cipher import AES
import sys, os, random

from secret import flag

key = os.urandom(32)

def pad(msg):
    padding = 16 - (len(msg) % 16)
    return msg + bytes([padding]) * padding

def unpad(msg):
    padding = msg[-1]
    assert 1 <= padding <= 16
    assert msg.endswith(bytes([padding]) * padding)
    return msg[:-padding]

def encrypt(plain):
    aes = AES.new(key, AES.MODE_ECB)
    return aes.encrypt(pad(plain))

def decrypt(cipher):
    aes = AES.new(key, AES.MODE_ECB)
    return unpad(aes.decrypt(cipher))

def gen_token(userdata):
    user_str = ''
    for k in userdata:
        user_str += f'{k}={userdata[k]}&'
    return encrypt(user_str[:-1].encode()).hex()

def menu():
    print("1. Buy A Juice")
    print("2. Buy A Phone")
    print("3. Buy A Computer")
    print("4. Buy A Flag")
    print("5. Exit")
    choice = int(input('Choice > '))
    assert 1 <= choice <= 4
    return choice

def buy(choice):
    price = [50, 50000, 50000000, 50000000000]
    token = bytes.fromhex(input('Token > '))
    userdata = dict(map(lambda x: x.split('='), decrypt(token).decode().split('&')))
    if int(userdata['money']) < price[choice - 1]:
        print('You are so poor !')
        return
    userdata['money'] = int(userdata['money']) - price[choice - 1]
    if choice == 1:
        print("Nice drink !")
    elif choice == 2:
        print("Cool phone !")
    elif choice == 3:
        print("Great to play game !")
    else:
        print(f'Flag : {flag}')
    print(f'Token : {gen_token(userdata)}')

def register():
    username = input('Username > ').strip()
    userdata = {'username': username, 'money': 100, 'id': random.randint(10000000, 99999999)}
    print(f'Token : {gen_token(userdata)}')


while True:
    try:
        register()
        buy(menu())
    except:
        sys.exit()
