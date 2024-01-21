import sys

N = int(sys.stdin.readline())

dancing = set()
dancing.add('ChongChong')

for i in range(N):
    name1, name2 = sys.stdin.readline().split()
    if name1 in dancing:
        dancing.add(name2)
    elif name2 in dancing:
        dancing.add(name1)

print(len(dancing))