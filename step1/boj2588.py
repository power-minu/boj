A = int(input())
B = int(input())

B_fin = B%10
B_mid = int((B%100)/10)
B_1st = int(B/100)

print(A*B_fin)
print(A*B_mid)
print(A*B_1st)
print(A*B)