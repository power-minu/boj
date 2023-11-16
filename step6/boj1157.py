S = input()

chrarray = [0 for i in range(26)]

for i in range(0, len(S), 1) :
    if ord(S[i]) >= 65 and ord(S[i]) <= 90 : chrarray[ord(S[i])-65] += 1
    elif ord(S[i]) >= 97 and ord(S[i]) <= 122 : chrarray[ord(S[i])-97] += 1

maxv = max(chrarray)
maxcount = 0
for i in range(0, 26, 1) : 
    if chrarray[i] == maxv : maxcount += 1

if maxcount > 1 : print("?")
else : 
    idx = chrarray.index(max(chrarray))
    print(chr(idx+65))