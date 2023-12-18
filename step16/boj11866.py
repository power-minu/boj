import sys

N, K = map(int, sys.stdin.readline().split())

point = -1
size = N

people = [i+1 for i in range(N)]
exist = [True] * N
res = []

while size > 0:
    inc = 0
    while 1:
        point += 1
        if point > N - 1:
            point -= N
        if exist[point] == True:
            inc += 1
        if inc == K:
            break
    exist[point] = False
    res.append(people[point])
    size -= 1

print('<', end="")
for i in range(len(res)-1):
    print(res[i], end=", ")
print(res[len(res)-1], end=">")