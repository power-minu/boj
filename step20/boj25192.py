import sys

N = int(sys.stdin.readline())

members = set()
count = 0

for i in range(N):
    mystr = sys.stdin.readline().strip()
    if mystr == 'ENTER':
        members.clear()
    else:
        if mystr not in members:
            members.add(mystr)
            count += 1

print(count)