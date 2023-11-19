N = int(input())

xlist = [0 for i in range(N)]
ylist = [0 for i in range(N)]

for i in range(0, N, 1) :
    xlist[i], ylist[i] = map(int, input().split())

print((max(xlist)-min(xlist)) * (max(ylist)-min(ylist)))