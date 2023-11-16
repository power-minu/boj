S = input()

time = 0

for i in range(0, len(S), 1) :
    myinput = ord(S[i])
    if myinput>=65 and myinput<=67 : time += 3
    elif myinput>=68 and myinput<=70 : time += 4
    elif myinput>=71 and myinput<=73 : time += 5
    elif myinput>=74 and myinput<=76 : time += 6
    elif myinput>=77 and myinput<=79 : time += 7
    elif myinput>=80 and myinput<=83 : time += 8
    elif myinput>=84 and myinput<=86 : time += 9
    elif myinput>=87 and myinput<=90 : time += 10

print(time)