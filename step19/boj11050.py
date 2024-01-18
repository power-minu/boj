import sys
input = sys.stdin.readline()

N, K = map(int, input.split())

divider = 1
if K != 0:
    for i in range(1, K+1, 1):
        divider = divider * i

res = 1

for i in range(0, K):
    res = res * (N-i)

print(int(res/divider))