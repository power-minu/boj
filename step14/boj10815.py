# 파이썬의 set 자료형
# unordered, unique elements, mutable
# in list의 시간 복잡도는 평균 O(n), in set의 시간 복잡도는 평균 O(n)
# 이는 set이 해시 테이블로 구현되어 있기 떼문이다. 데이터를 해시한 값을 인덱스로 설정.
# 어떤 값이 set에 있는지 확인할 때, 그 값을 해시 함수에 넣어서 인덱스를 얻어내고, 바로 접근 가능하다.

N = int(input())
Narr = set(map(int, input().split()))

M = int(input())
Marr = list(map(int, input().split()))

res = [0 for i in range(M)]

for i in range(0, M, 1) :
    if Marr[i] in Narr : res[i] = 1

for i in range(0, M, 1) :
    print(res[i], end=" ")