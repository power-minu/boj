N = int(input())

res = 0

def verify_str(mystr) :
    defret = True
    emerge = [False for i in range(26)]
    emerge_and_disappear = [False for i in range(26)]
    for i in range(0, len(mystr), 1) :
        emerge[ord(mystr[i])-97] = True
        if i >= 1 and emerge[ord(mystr[i-1])-97] == True and mystr[i-1] != mystr[i] :
            emerge_and_disappear[ord(mystr[i-1])-97] = True
        if emerge_and_disappear[ord(mystr[i])-97] == True :
            defret = False
    return defret
        

for i in range(0, N, 1) :
    mystr = input()
    if verify_str(mystr) == True : res += 1

print(res)