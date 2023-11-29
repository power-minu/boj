import sys

S = sys.stdin.readline().strip()
res_set = set()

for length in range(len(S)):
    for start in range(0, len(S)-length, 1):
        end = start+length+1
        to_add = S[start:end]
        res_set.add(to_add)

print(len(res_set))