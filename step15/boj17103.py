import sys

numrange = 1000001
numarr = [True] * numrange
primeset = set()

numarr[0] = numarr[1] = False
for i in range(2, numrange, 1):
    if numarr[i] == False:
        continue
    for j in range(2*i, numrange, i):
        numarr[j] = False

for i in range(numrange):
    if numarr[i] == True:
        primeset.add(i)

T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())
    count = 0
    for j in range(2, (N//2) + 1, 1):
        if j in primeset and N-j in primeset:
            count += 1
    print(count)