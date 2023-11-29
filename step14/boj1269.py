import sys

N, M = map(int, sys.stdin.readline().split())

A = set()
B = set()

A.update(sys.stdin.readline().split())
B.update(sys.stdin.readline().split())

print(len(A ^ B))