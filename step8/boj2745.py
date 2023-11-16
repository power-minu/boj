N, myB = input().split()

B=int(myB)

res = 0

for i in range(0, len(N), 1) :
    if ord(N[i]) <= 57 and ord(N[i]) >= 48 : res += (ord(N[i])-48) * (B**(len(N)-1-i))
    elif ord(N[i]) <= 90 and ord(N[i]) >= 65 :
        res += (ord(N[i])-55) * (B**(len(N)-1-i))

print(res)