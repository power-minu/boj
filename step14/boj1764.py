import sys

N, M = map(int, sys.stdin.readline().split())

Nset = set()
Mset = set()
res_set = set()

for i in range(N) :
    Nset.add(sys.stdin.readline().strip())

for i in range(M) :
    Mset.add(sys.stdin.readline().strip())

if len(Mset) >= len(Nset) :
    for i in Mset :
        if i in Nset : res_set.add(i)
elif len(Nset) > len(Mset) :
    for i in Nset :
        if i in Mset : res_set.add(i)

res = sorted(res_set)

print(len(res))
for i in range(len(res)) :
    print(res[i])