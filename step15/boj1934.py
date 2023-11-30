import sys

T = int(sys.stdin.readline())

res = [0] * T

def gcd(A, B) :
    res = 1
    if A > B : small = B
    else: small = A
    for i in range(1, small+1, 1):
        if A % i == 0 and B % i == 0:
            res = i
    return res

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    gcd_res = gcd(A, B)
    res[i] = int(gcd_res * (A/gcd_res) * (B/gcd_res))

for i in range(T):
    print(res[i])