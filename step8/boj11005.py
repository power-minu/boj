N, B = map(int, input().split())

digit = 0

while 1 :
    if N < B**digit : break
    digit += 1

i = digit
res = 0

# print(digit)
# B^자릿수 * 계수. 계수를 일단 구함

for i in range(1, digit+1, 1) :
    coef = 0
    while 1 :
        if B**(digit-i) * coef > N : break
        coef += 1
    coef -= 1
    N -= B**(digit-i) * coef
    # print(coef, end=" ")
    # print()
    if coef > 9 :
        print(chr(coef+55), end="")
    else : print(coef, end="")