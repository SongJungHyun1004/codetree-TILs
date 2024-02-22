n = int(input())
pos = []
for _ in range(n):
    pos.append(int(input()))
pos = sorted(pos)
selected = [False]*n
cnt = 0
def combi(idx, last):
    global cnt
    if idx == 3:
        xyz = []
        for i in range(n):
            if selected[i]:
                xyz.append(pos[i])
        x, y, z = xyz[0], xyz[1], xyz[2]
        if x < y < z and y-x <= z-y <= 2*(y-x):
            cnt += 1
        return
    for i in range(last, n):
        if not selected[i]:
            selected[i] = True
            combi(idx+1, i)
            selected[i] = False

combi(0, 0)
print(cnt)