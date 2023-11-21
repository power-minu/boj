a, b, c, d, e, f = map(int, input().split())

x = -999
y = 0
solved = False

while x <= 999 :
    y = -999
    while y <= 999 :
        if a*x + b*y == c and d*x + e*y == f : 
            solved = True
            break
        y += 1
    if solved == True : break
    x += 1

print(x, end=" ")
print(y)