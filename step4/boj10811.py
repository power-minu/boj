N, M = map(int, input().split())

basketnumber = [0 for i in range(N)]
for i in range(0, N, 1) : basketnumber[i] = i+1

for i in range(0, M, 1) :
    i, j = map(int, input().split())
    jo = j
    for count in range(i-1, (i-1+jo-1)//2+1, 1) :
        left = count
        right = j-1
        temp = basketnumber[right]
        basketnumber[right] = basketnumber[left]
        basketnumber[left] = temp
        j -= 1

for pr in range(0, N, 1) : print(basketnumber[pr], end=" ")