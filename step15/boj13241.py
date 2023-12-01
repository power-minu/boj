import sys

A, B = map(int, sys.stdin.readline().split())

def gcd(A, B):
    r = B % A
    if r == 0:
        return A
    return gcd(r, A)

gcd_res = gcd(A, B)
print(int(gcd_res * (A/gcd_res) * (B/gcd_res)))