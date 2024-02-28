from collections import deque
from itertools import combinations
import copy
n, k = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())
r1-=1;c1-=1;r2-=1;c2-=1
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
                dist[nx][ny] = dist[x][y] + 1
pos = []
for i in range(n):
    for j in range(n):
        if grid[i][j]:
            pos.append((i, j))

lst = list(combinations(pos, k))
mn = float('inf')
for remove_lst in lst:
    tmp = copy.deepcopy(grid)
    visited = [
        [False]*n
        for _ in range(n)
    ]
    dist = [
        [0]*n
        for _ in range(n)
    ]
    for i, j in remove_lst:
        tmp[i][j] = 0
    bfs(r1, c1)
    if visited[r2][c2]:
        mn = min(mn, dist[r2][c2])
if mn == float('inf'):
    print(-1)
else:
    print(mn)