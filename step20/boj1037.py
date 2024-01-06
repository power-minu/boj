import sys

number_of_measure = int(sys.stdin.readline())

measures_input = list(map(int, sys.stdin.readline().split()))
measures = set()
for i in measures_input:
    measures.add(i)

if number_of_measure == 1:
    print(min(measures) ** 2)
else:
    print(max(measures) * min(measures))
