import sys

def gcd(A, B):
    r = B % A
    if r == 0:
        return A
    return gcd(r, A)

N = int(sys.stdin.readline())
trees = [0] * N
gaps = [0] * (N-1)
gcd_of_gaps = 0

for i in range(N):
    trees[i] = int(sys.stdin.readline())
for i in range(N-1):
    gaps[i] = trees[i+1]-trees[i]
gcd_of_gaps = gcd(gaps[0], gaps[1])
for i in range(2, N-1, 1):
    gcd_of_gaps = gcd(gcd_of_gaps,gaps[i])

print(((max(trees)-min(trees)) // gcd_of_gaps) + 1 - N)