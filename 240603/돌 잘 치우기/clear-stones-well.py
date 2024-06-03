from collections import deque
from itertools import combinations
import copy
n, k, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
rock_pos = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            rock_pos.append((i, j))
rmv_combi = list(combinations(rock_pos, m))

dxs = [0,1,0,-1]
dys = [1,0,-1,0]
def in_range(x, y):
    return 0<=x<n and 0<=y<n

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not visited[nx][ny] and tmp[nx][ny] == 0:
                visited[nx][ny] = True
                q.append((nx, ny))
                
start_points = []
for _ in range(k):
    r, c = map(int, input().split())
    r-=1;c-=1
    start_points.append((r, c))
mx = 0
for rmv_pos in rmv_combi:
    tmp = copy.deepcopy(grid)
    for x, y in rmv_pos:
        tmp[x][y] = 0
    visited = [[False]*n for _ in range(n)]
    for sx, sy in start_points:
        bfs(sx, sy)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                cnt += 1
    mx = max(mx, cnt)
print(mx)