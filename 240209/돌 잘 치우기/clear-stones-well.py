from itertools import combinations
from collections import deque
import copy
n, k, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
start_lst = []
for _ in range(k):
    r, c = map(int, input().split())
    r-=1;c-=1
    start_lst.append((r, c))
pos = []
for i in range(n):
    for j in range(n):
        if grid[i][j]:
            pos.append([i, j])
canGo_lst = list(combinations(pos, m))

dxs = [0,1,0,-1]
dys = [1,0,-1,0]
def in_range(x, y):
    return 0<=x<n and 0<=y<n
def bfs(sx, sy):
    q = deque([(sx, sy)])
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not visited[nx][ny] and tmp[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = True
mx = 0
for canGo in canGo_lst:
    tmp = copy.deepcopy(grid)
    for [x, y] in canGo:
        tmp[x][y] = 0
    visited = [
        [False]*n
        for _ in range(n)
    ]
    for sx, sy in start_lst:
        bfs(sx, sy)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                cnt += 1
    mx = max(mx, cnt)
print(mx)