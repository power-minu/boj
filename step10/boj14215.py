sides = list(map(int, input().split()))

shortsides = sum(sides) - max(sides)

while shortsides <= max(sides) :
    sides[sides.index(max(sides))] -= 1

print(sum(sides))