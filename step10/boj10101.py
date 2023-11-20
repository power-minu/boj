degree = [0 for i in range(3)]

res = ""

for i in range(3) :
    degree[i] = int(input())

if sum(degree) != 180 : res = "Error"
elif degree[0] == degree[1] and degree[0] == degree[2] : res = "Equilateral"
elif degree[0] == degree[1] or degree[0] == degree[2] or degree[2] == degree[1] : res = "Isosceles"
else : res = "Scalene"

print(res)