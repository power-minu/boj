T = int(input())

# Q는 25, D는 10, N은 5, P는 1
for i in range(0, T, 1) :
    C = int(input())
    Q = 0
    D = 0
    N = 0
    P = 0
    cur = 0
    while cur < C :
        Q += 1
        cur += 25
    if cur == C :
        print(Q, end=" ")
        print(D, end=" ")
        print(N, end=" ")
        print(P)
        continue
    else :
        Q -= 1
        cur -= 25

    while cur < C :
        D += 1
        cur += 10
    if cur == C :
        print(Q, end=" ")
        print(D, end=" ")
        print(N, end=" ")
        print(P)
        continue
    else :
        D -= 1
        cur -= 10

    while cur < C :
        N += 1
        cur += 5
    if cur == C :
        print(Q, end=" ")
        print(D, end=" ")
        print(N, end=" ")
        print(P)
        continue
    else :
        N -= 1
        cur -= 5

    while cur < C :
        P += 1
        cur += 1

    print(Q, end=" ")
    print(D, end=" ")
    print(N, end=" ")
    print(P)