S = input()

length = len(S)

i = 0
while i < len(S) :
    if i+1 < len(S) and S[i] == 'c' :
        if S[i+1] == '=' or S[i+1] == '-' : 
            length -= 1
            i += 1
    elif i+2 < len(S) and S[i] == 'd' and S[i+1] == 'z' and S[i+2] == '=' :
        length -= 2
        i += 2
    elif i+1 < len(S) and S[i] == 'd' and S[i+1] == '-' :
        length -= 1
        i += 1
    elif i+1 < len(S) and S[i] == 'l' and S[i+1] == 'j' :
        length -= 1
        i += 1
    elif i+1 < len(S) and S[i] == 'n' and S[i+1] == 'j' :
        length -= 1
        i += 1
    elif i+1 < len(S) and S[i] == 's' and S[i+1] == '=' :
        length -= 1
        i += 1
    elif i+1 < len(S) and S[i] == 'z' and S[i+1] == '=' :
        length -= 1
        i += 1
    i += 1

print(length)