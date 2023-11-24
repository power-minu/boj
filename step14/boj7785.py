n = int(input())

people = set()

for i in range(n) :
    name, inst = input().split()
    if inst == 'enter' : people.add(name)
    elif inst == 'leave' : people.remove(name)

myList = sorted(people, reverse=True)

for i in range(len(myList)) :
    print(myList[i])