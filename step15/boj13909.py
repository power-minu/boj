import sys

N = int(sys.stdin.readline())
count = 0
x = 1
while x*x <= N:
    x += 1
    count += 1
print(count)