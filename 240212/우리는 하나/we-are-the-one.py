from collections import deque
from itertools import combinations
n, k, u, d = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
dxs = [0,1,0,-1]
dys = [1,0,-1,0]
def in_range(x, y):
    return 0<=x<n and 0<=y<n
    
def bfs(sx, sy):
    global cnt
    q = deque([(sx, sy)])
    visited[sx][sy] = True
    cnt += 1
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not visited[nx][ny] and u <= abs(grid[x][y]-grid[nx][ny]) <= d:
                q.append((nx, ny))
                visited[nx][ny] = True
                cnt += 1
mx = 0
lst = []
for i in range(n):
    for j in range(n):
        lst.append((i, j))

pos_lsts = list(combinations(lst, k))
for pos_lst in pos_lsts:
    visited = [
        [False]*n
        for _ in range(n)
    ]
    cnt = 0
    for x, y in pos_lst:
        bfs(x, y)
    mx = max(mx, cnt)
print(mx)