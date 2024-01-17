import sys
input = sys.stdin.readline()

N = int(input)
res = 1

if N != 0:
    for i in range(1, N+1, 1):
        res = res * i

print(res)