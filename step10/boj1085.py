x, y, w, h = map(int, input().split())

dist = 1001

if x < dist : dist = x
if h-y < dist : dist = h-y
if w-x < dist : dist = w-x
if y < dist : dist = y

print(dist)