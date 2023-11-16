T = int(input())

for i in range(0, T, 1) :
    a, b = map(int, input().split())
    print("Case #" + str(i+1) + ": " + str(a+b))