from Crypto.Util.number import getPrime
import sys

from secret import flag

def main():
    N = getPrime(128)
    seed, m, inc = (getPrime(64) for _ in range(3))

    s = seed
    state = []
    for _ in range(0x10):
        state.append(s)
        s = (m * s + inc) % N

    state = ",".join(map(str, state))
    print(f"State : {state}")
    if s != int(input("Next State > ")):
        print("Wrong Answer!")
        sys.exit()

    print(f'Flag : {flag}')


try:
    main()
except:
    sys.exit()