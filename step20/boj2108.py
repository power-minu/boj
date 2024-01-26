import sys

N = int(sys.stdin.readline())

mylist = []
mydict = dict()
total = 0

for i in range(N):
    myinput = int(sys.stdin.readline())
    total += myinput
    mylist.append(myinput)
    if myinput not in mydict:
        mydict[myinput] = 1
    elif myinput in mydict:
        mydict[myinput] += 1

mylist = sorted(mylist)

modelist = []
mode = max(mydict, key=mydict.get)
mxfreq = max(mydict.values())
for i in mydict.items():
    if i[1] == mxfreq:
        modelist.append(i[0])
modelist = sorted(modelist)
if len(modelist) >= 2:
    mode = modelist[1]

print(round(total/N))
print(mylist[int(N/2)])
print(mode)
print(max(mylist)-min(mylist))