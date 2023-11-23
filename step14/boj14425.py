N, M = map(int, input().split())

S = set()
Marr = ['a' for i in range(M)]
res = 0

for i in range(N) :
    S.add(input())

for i in range(M) :
    Marr[i] = input()

for i in range(M) :
    if Marr[i] in S : res += 1

print(res)