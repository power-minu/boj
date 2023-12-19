import sys
from collections import deque

N = int(sys.stdin.readline())

mydeque = deque()

# def empty(queue):
#     if tail < head:
#         return 1
#     else:
#         return 0
# head = 0
# tail = -1

for i in range(N):
    cmd = sys.stdin.readline().split()

    if cmd[0] == '1':
        mydeque.appendleft(int(cmd[1]))
    elif cmd[0] == '2':
        mydeque.append(int(cmd[1]))
    elif cmd[0] == '3':
        if len(mydeque) == 0:
            print(-1)
        else:
            print(mydeque.popleft())
    elif cmd[0] == '4':
        if len(mydeque) == 0:
            print(-1)
        else:
            print(mydeque.pop())
    elif cmd[0] == '5':
        print(len(mydeque))
    elif cmd[0] == '6':
        if len(mydeque) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == '7':
        if len(mydeque) == 0:
            print(-1)
        else:
            print(mydeque[0])
    elif cmd[0] == '8':
        if len(mydeque) == 0:
            print(-1)
        else:
            print(mydeque[-1])