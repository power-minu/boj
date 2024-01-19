import sys
input = sys.stdin.readline()

T = int(input)

for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    divider = 1
    if N != 0:
        for i in range(1, N + 1, 1):
            divider = divider * i

    res = 1

    for i in range(0, N):
        res = res * (M - i)

    print(int(res / divider))