import sys

N = int(sys.stdin.readline())
cardinput = sys.stdin.readline().split()
cards = dict()

for i in range(N) :
    cards[cardinput[i]] = 0
for i in range(N) :
    cards[cardinput[i]] += 1

M = int(sys.stdin.readline())
req = sys.stdin.readline().split()

for i in range(M) :
    if req[i] in cards :
        print(cards[req[i]], end=' ')
    else :
        print(0, end=' ')