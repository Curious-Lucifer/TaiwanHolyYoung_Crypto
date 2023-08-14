import random, sys

from secret import flag

MASK = (1 << 32) - 1

def main():
    state = random.getrandbits(32)
    for _ in range(624):
        print(f"State : {state}")
        data = int(input("Data > "))
        state = (state + data + random.getrandbits(32)) & MASK
        if state == 0:
            print(f'Flag : {flag}')

try:
    main()
except:
    sys.exit()