N = int(input())

for i in range(1, N+1, 1) :
    for j in range(N, i, -1) :
        print(" ", end="")
    for j in range(0, i, 1) :
        print("*", end="")
    print("")