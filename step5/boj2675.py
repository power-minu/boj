T = int(input())

for i in range(0, T, 1) :
    R, S = input().split()
    for j in range(0, len(S), 1) :
        for k in range(0, int(R), 1) :
            print(S[j], end="")
    print()