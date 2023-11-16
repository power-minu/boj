N = int(input())

for i in range(0, N, 1) :
    blnkcnt = N-i-1
    for k in range(0, blnkcnt, 1) :
        print(" ", end="")
    starcnt = 2*i+1
    for j in range(0, starcnt, 1) :
        print("*", end="")
    print()

for i in range(0, N-1, 1) :
    blnkcnt = i+1
    for k in range(0, blnkcnt, 1) :
        print(" ", end="")
    starcnt = 2*(N-2-i)+1
    for j in range(0, starcnt, 1) :
        print("*", end="")
    print()