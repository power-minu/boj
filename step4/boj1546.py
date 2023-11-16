import statistics

N = int(input())

score = list(map(float, input().split()))
maxscore = max(score)

for i in range(0, N, 1) :
    score[i] = score[i]/maxscore*100

print(statistics.mean(score))