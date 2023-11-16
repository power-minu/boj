S = input()

res = 1

for i in range(0, len(S)//2, 1) :
    if S[i] != S[len(S)-1-i] : res = 0

print(res)