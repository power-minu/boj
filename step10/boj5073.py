while 1 :
    sides = list(map(int, input().split()))

    shortsides = sum(sides)-max(sides)

    if sides[0] == 0 and sides[1] == 0 and sides[2] == 0 : break
    elif shortsides <= max(sides) : res = "Invalid"
    elif sides[0] == sides[1] and sides[0] == sides[2] : res = "Equilateral"
    elif sides[0] == sides[1] or sides[0] == sides[2] or sides[2] == sides[1] : res = "Isosceles"
    else : res = "Scalene"
    print(res)