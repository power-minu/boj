import sys
input = sys.stdin.readline()

count = 0
N = int(input)
pos = [0] * (N) # idx는 x축, value는 y축

def promising(x):
    for i in range(x):
        if pos[x]==pos[i] or abs(pos[x]-pos[i])==abs(x-i):
            return False
    return True

def backtracking(col):
    global count
    if col == N:
        count += 1
        return
    for i in range(N):
        pos[col] = i
        if promising(col):
            backtracking(col+1)

backtracking(0)
print(count)