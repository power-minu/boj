import sys

A1, B1 = map(int, sys.stdin.readline().split())
A2, B2 = map(int, sys.stdin.readline().split())

def gcd(A, B):
    r = B % A
    if r == 0:
        return A
    return gcd(r, A)

def lcm(A, B) :
    gcd_res = gcd(A, B)
    return int(gcd_res * (A/gcd_res) * (B/gcd_res))

lcm_of_denom = lcm(B1, B2)
res_A = int((lcm_of_denom/B1)*A1 + (lcm_of_denom/B2)*A2)
res_B = lcm_of_denom

temp = res_A
res_A = int(res_A / gcd(temp, res_B))
res_B = int(res_B / gcd(temp, res_B))

print(res_A, end=" ")
print(res_B)