import sys

while 1:
    mystr = sys.stdin.readline().rstrip()
    mystack = []
    balance = True

    if mystr == ".":
        break

    for i in mystr:
        if i == '(' or i == '[':
            mystack.append(i)
        elif i == ')':
            if len(mystack) == 0 or mystack[-1] == '[':
                print("no")
                balance = False
                break
            else: mystack.pop()
        elif i == ']':
            if len(mystack) == 0 or mystack[-1] == '(':
                print("no")
                balance = False
                break
            else: mystack.pop()

    if balance == True:
        if not mystack:
            print("yes")
        else:
            print("no")