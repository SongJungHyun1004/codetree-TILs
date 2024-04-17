from sortedcontainers import SortedSet
n, d = map(int, input().split())
pos = []
for _ in range(n):
    x, y = map(int, input().split())
    pos.append((x, y))
pos = sorted(pos)
mn = float('inf')
y_set = SortedSet()
j = 0
for i in range(n):
    y_set.add(pos[i][1])
    while y_set and y_set[-1] - y_set[0] >= d:
        min_y = y_set[0]
        max_y = y_set[-1]
        if max_y - min_y >= d:
            mn = min(mn, pos[i][0]-pos[j][0])
            y_set.discard(pos[j][1])
            j += 1
print(mn) if mn != float('inf') else print(-1)