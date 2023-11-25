# sorted 함수 : 정렬된 list 반환. 함수에서 reverse 필드로 order 설정 가능.

n = int(input())

people = set()

for i in range(n) :
    name, inst = input().split()
    if inst == 'enter' : people.add(name)
    elif inst == 'leave' : people.remove(name)

myList = sorted(people, reverse=True)

for i in range(len(myList)) :
    print(myList[i])