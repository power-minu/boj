A, B = input().split()

sg_A = list(A)
sg_A.reverse()

sg_B = list(B)
sg_B.reverse()

sg_valueA = int(sg_A[0])*100 + int(sg_A[1])*10 + int(sg_A[2])
sg_valueB = int(sg_B[0])*100 + int(sg_B[1])*10 + int(sg_B[2])

res = 0

if sg_valueA > sg_valueB : res = sg_valueA
elif sg_valueA < sg_valueB : res = sg_valueB

print(res)

# print(sg_A[0]) #char임

# print(int(sg_A[0]) * 100) #int로 됨