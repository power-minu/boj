A, B, C = map(int, input().split())

if A==B and B==C :
    price = 10000 + A*1000
elif A==B or B==C :
    price = 1000 + B*100
elif A==C :
    price = 1000 + A*100
elif A>B and A>C :
    price = A*100
elif B>A and B>C :
    price = B*100
elif C>A and C>B :
    price = C*100

print(price)