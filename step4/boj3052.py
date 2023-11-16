remainder = [0 for i in range(42)]

for i in range(0, 10, 1) :
    dividend = int(input())
    remainder[dividend % 42] += 1

res = 0

for i in range(0, 42, 1) :
    if remainder[i] != 0 : res += 1

print(res)