import sys

T = int(sys.stdin.readline())
calls = 0

def recursion(s, l, r):
    global calls
    calls += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

for i in range(T):
    calls = 0
    S = sys.stdin.readline().strip()
    print(isPalindrome(S), end=" ")
    print(calls)