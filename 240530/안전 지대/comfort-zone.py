import sys
sys.setrecursionlimit(10**5)

dxs = [0,1,0,-1]
dys = [1,0,-1,0]

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
MAX_HEIGHT = 0
for i in range(n):
    for j in range(m):
        MAX_HEIGHT = max(MAX_HEIGHT, grid[i][j])

def in_range(x, y):
    return 0<=x<n and 0<=y<m

def dfs(x, y, h):
    visited[x][y] = True
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] > h:
            dfs(nx, ny, h)

ans, mx_zone = 1, 0
for k in range(1, MAX_HEIGHT+1):
    visited = [[False]*m for _ in range(n)]
    zone = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] > k and not visited[i][j]:
                dfs(i, j, k)
                zone += 1
    if zone > mx_zone:
        mx_zone = zone
        ans = k

print(ans, mx_zone)