S = input()

pos = [-1 for i in range(26)]

for i in range(0, len(S), 1) :
    if pos[ord(S[i])-97] == -1 :
        pos[ord(S[i])-97] = i

for i in range(0, 26, 1) :
    print(pos[i], end=" ")
