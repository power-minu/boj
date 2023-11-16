N = int(input())
intlist = list(map(int, input().split()))
v = int(input())
# for i in range(0, N, 1) : print(intlist[i])

res = 0

for i in range(0, N, 1) :
    if intlist[i]==v :
        res += 1

print(res)