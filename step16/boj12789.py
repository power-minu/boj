import sys

N = int(sys.stdin.readline())
stu_line = list(map(int, sys.stdin.readline().split()))
stu_line.reverse()
wait_line = []

cur = 1
complete = False

while 1:
    if len(stu_line) != 0 and stu_line[-1] == cur:
        stu_line.pop()
        cur += 1
    elif len(wait_line) != 0 and wait_line[-1] == cur:
        wait_line.pop()
        cur += 1
    else:
        if len(stu_line) == 0:
            break
        wait_line.append(stu_line[-1])
        stu_line.pop()

    if len(stu_line) == 0 and len(wait_line) == 0:
        complete = True
        break

if complete == True:
    print("Nice")
elif complete == False:
    print("Sad")