import sys

N = int(sys.stdin.readline())

if N == 1:
    print(1)
else:
    myList = [0] * (2 * N - 2)

    for i in range(N):
        myList[N - 2 + i] = N - i;

    head = N - 3

    while len(myList) > 1:
        myList.pop()
        if len(myList) == 1:
            break
        myList[head] = myList.pop()
        head -= 1

    print(myList[-1])
