import sys
from collections import deque

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
C = list(map(int, sys.stdin.readline().split()))

queue = deque([])
for i in range(N):
    if A[i] == 0:
        queue.append(B[i])
if queue == []:
    print(*C)
    sys.exit()

for i in range(M):
    queue.appendleft(C[i])
    print(queue.pop(), end=" ")