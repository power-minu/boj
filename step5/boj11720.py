N = int(input())

S = input()
res = 0

for i in range(0, N, 1) :
    res += int(S[i])

print(res)