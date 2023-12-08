import sys

N = int(sys.stdin.readline())

mystack = []

for i in range(N):
    cmd = sys.stdin.readline().strip()
    if len(cmd) > 2 :
        mystack.append(int(cmd[2:]))
    elif cmd == '2':
        if len(mystack) == 0:
            print(-1)
        else: print(mystack.pop())
    elif cmd == '3':
        print(len(mystack))
    elif cmd == '4':
        if len(mystack) == 0:
            print(1)
        else: print(0)
    elif cmd == '5':
        if len(mystack) == 0:
            print(-1)
        else: print(mystack[-1])