import sys
import math

T = int(sys.stdin.readline())

def prime(input):
    if input == 1 or input == 0:
        return False
    for i in range(2, int(math.sqrt(input)+1), 1):
        if input % i == 0: return False
    return True

for i in range(T):
    n = int(sys.stdin.readline())
    found = False
    checkno = n
    while 1:
        if prime(checkno) == True:
            print(checkno)
            break
        checkno += 1