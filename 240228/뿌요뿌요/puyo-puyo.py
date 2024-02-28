import sys
sys.setrecursionlimit(10**5)
n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [
    [False]*n
    for _ in range(n)
]
dxs = [0,1,0,-1]
dys = [1,0,-1,0]
def in_range(x, y):
    return 0<=x<n and 0<=y<n

def dfs(x, y, num):
    global size
    visited[x][y] = True
    size += 1
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] == num:
            dfs(nx, ny, num)
cnt = 0
mx = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            size = 0
            dfs(i, j, grid[i][j])
            if size >= 4:
                cnt += 1
            mx = max(mx, size)
print(cnt, mx)