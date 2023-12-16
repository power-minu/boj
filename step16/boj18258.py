import sys

N = int(sys.stdin.readline())

myqueue = []

def empty(queue):
    if tail < head:
        return 1
    else:
        return 0
head = 0
tail = -1

for i in range(N):
    cmd = sys.stdin.readline().split()

    if cmd[0] == 'push':
        myqueue.append(int(cmd[1]))
        tail += 1
    elif cmd[0] == 'pop':
        if empty(myqueue):
            print(-1)
        else:
            print(myqueue[head])
            # pop(myqueue[0])를 하면 앞에꺼 없애고 나머지 애들을
            # 앞으로 쫙 땡기는 것도 해서 오래 걸림. O(N-1)
            head += 1
    elif cmd[0] == 'size':
        print(tail-head+1)
    elif cmd[0] == 'empty':
        print(empty(myqueue))
    elif cmd[0] == 'front':
        if empty(myqueue):
            print(-1)
        else:
            print(myqueue[head])
    elif cmd[0] == 'back':
        if empty(myqueue):
            print(-1)
        else:
            print(myqueue[tail])