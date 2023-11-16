N, X = map(int, input().split())

A = list(map(int, input().split()))

if len(A) != N :
    quit()
else :
    for i in range(0, N, 1) :
        if A[i] < X : print(str(A[i]), end=" ")