xlist = [0, 0, 0]
ylist = [0, 0, 0]

for i in range(0, 3, 1) :
    x, y = map(int, input().split())
    xlist[i] = x
    ylist[i] = y

newx = xlist[0]
if xlist[1] != xlist[0] and xlist[2] != xlist[1] :
    newx = xlist[1]
if xlist[0] == xlist[1] and xlist[2] != xlist[1] :
    newx = xlist[2]

newy = ylist[0]
if ylist[1] != ylist[0] and ylist[2] != ylist[1] :
    newy = ylist[1]
if ylist[0] == ylist[1] and ylist[2] != ylist[1] :
    newy = ylist[2]

print(newx, end=" ")
print(newy, end=" ")