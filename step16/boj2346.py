import sys
from collections import deque

N = int(sys.stdin.readline())
q = deque(enumerate(map(int, sys.stdin.readline().split())))
res = []

while q:
    idx, paper = q.popleft()
    res.append(idx+1)

    if paper > 0 :
        q.rotate(-paper+1)
    #     rotate : 덱을 시계방향으로 매개변수 값만큼 회전시킴
    elif paper < 0:
        q.rotate(-paper)

print(' '.join(map(str, res)))