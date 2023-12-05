import sys

numarr = [0] * 1000001

for i in range(1000001):
    numarr[i] = i

numarr[1] = 0
for i in range(2, 1000001, 1):
    if numarr[i] == 0:
        continue
    for j in range(2*i, 1000001, i):
        numarr[j] = 0

M, N = map(int, sys.stdin.readline().split())

for i in range(M, N+1, 1):
    if numarr[i] != 0 : print(numarr[i])