import sys

N, M = map(int, sys.stdin.readline().split())
words = dict()

for i in range(N):
    typedWord = sys.stdin.readline().strip()
    if len(typedWord) >= M:
        if typedWord in words:
            words[typedWord] += 1
        else:
            words[typedWord] = 1

output = sorted(words.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for i in output:
    print(i[0])