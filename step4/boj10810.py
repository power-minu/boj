N, M = map(int, input().split())

basketlist = [0 for s in range(N)]

for count in range(0, M, 1) :
    i, j, k = map(int, input().split())
    for put in range(i, j+1, 1) :
        basketlist[put-1] = k

for p in range(0, N, 1) :
    print(basketlist[p], end=" ")