A, B = map(int, input().split())
C = int(input())

spendH = int(C/60)
spendM = int(C%60)

# print("spendH = " + str(spendH))
# print("spendM = " + str(spendM))

if B+spendM >= 60 :
    A = A + spendH + 1
    B = B + spendM - 60
    if A > 23 :
        A = A - 24
else :
    A = A + spendH
    B = B + spendM
    if A > 23 :
        A = A - 24

print(str(A) + " " + str(B))