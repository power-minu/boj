student = [0 for i in range(30)]

for i in range(0, 28, 1) :
    submit = int(input())
    student[submit-1] = 1

for j in range(0, 30, 1) :
    if student[j] == 0 :
        print(j+1)