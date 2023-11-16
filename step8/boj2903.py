N = int(input())

dots = 4

# for i in range(0, N, 1) :
#     dots += 2**i * 4
    # dots += 
    # 쫙있는거 길이 : 1 - 3 - 7 - 15
    # 1 - 1+2 - 3+4 - 7+8 - 15+16

straightlen = 0
straights = 0
straightsave = 0
twos = 0
res = 0

for i in range(0, N, 1) :
    dots += 2**i * 4
    straightlen += (2**i)
    straights = straightlen * ((straightlen//2) + 1)
    straightsave += straights
    twos += (straightlen//2) * (straightlen//2 + 1)
    res = dots + straightsave + twos
    # 더해지는 수 : 1, 2, 4, 8, 16, 32
    # 스트레이트의 개수 : 0, 1, 2, 4, 8, 16
    # 두개만있는거 개수 : 0, 0, 1, 3, 7, 15

# print(dots)
# print(straightlen)
# print(straightsave)
# print(twos)

print(res)