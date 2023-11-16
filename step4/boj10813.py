N, M = map(int, input().split())

basketlist = [0 for i in range(N)]

for i in range(0, N, 1) :
    basketlist[i] = i+1

for count in range(0, M, 1) :
    i, j = map(int, input().split())
    temp = basketlist[j-1]
    basketlist[j-1] = basketlist[i-1]
    basketlist[i-1] = temp

for i in range(0, N, 1) :
    print(basketlist[i], end=" ")