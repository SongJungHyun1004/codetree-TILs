n, d = map(int, input().split())
pos = []
for _ in range(n):
    x, y = map(int, input().split())
    pos.append((x, y))
pos = sorted(pos, key=lambda x: x[1])
mn = float('inf')
j = 0
for i in range(n):
    while j < n and abs(pos[i][1]-pos[j][1]) < d:
        j += 1
    if j < n:
        mn = min(mn, abs(pos[i][0]-pos[j][0]))
print(mn)