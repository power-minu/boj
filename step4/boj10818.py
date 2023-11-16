N = int(input())

mylist = list(map(int, input().split()))

# minelement = mylist[0]
# maxelement = mylist[0]

minelement = min(mylist)
maxelement = max(mylist)

# for i in range(1, N, 1) :
#     if mylist[i] > maxelement : maxelement = mylist[i]
#     elif mylist[i] < minelement : minelement = mylist[i]

print(str(minelement) + " " + str(maxelement))