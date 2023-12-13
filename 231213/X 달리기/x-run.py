x = int(input())
t = 0
dist = 0
v = 1
while dist != x:
    dist += v
    if x-dist >= (v+1)*(v+2)//2:
        v += 1
    elif x-dist >= v*(v+1)//2:
        pass
    else:
        v -= 1
    t += 1

print(t)