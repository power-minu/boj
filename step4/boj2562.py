# maxv = 0

# idx = 1

# for i in range(0, 9, 1) :
#     inputv = int(input())
#     if inputv > maxv :
#         maxv = inputv
#         idx = i+1

# print(maxv)
# print(idx)

mylist = []

for i in range(0, 9, 1) :
    mylist.append(0)
    mylist[i] = int(input())

print(max(mylist))
print(mylist.index(max(mylist))+1)