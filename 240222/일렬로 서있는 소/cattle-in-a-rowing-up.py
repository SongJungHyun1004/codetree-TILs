n = int(input())
pos = []
for _ in range(n):
    pos.append(int(input()))
pos = sorted(pos)
cows = []
cnt = 0
def choose(i):
    global cnt
    if i == 3:
        x, y, z = cows[0], cows[1], cows[2]
        if x < y < z and y-x <= z-y <= 2*(y-x):
            cnt += 1
        return
    for p in pos:
        if cows:
            if p not in cows:
                cows.append(p)
                choose(i+1)
                cows.pop()
        else:
            cows.append(p)
            choose(i+1)
            cows.pop()
choose(0)
print(cnt)