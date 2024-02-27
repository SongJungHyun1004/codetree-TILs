n, m = map(int, input().split())
grid = [
    [0]*m
    for _ in range(n)
]
visited = [
    [False]*m
    for _ in range(n)
]
dx = [0,1,0,-1]
dy = [1,0,-1,0]
d = [0,1,2,3]
def in_range(x, y):
    return 0<=x<n and 0<=y<m

d = 0
x, y = 0, 0
grid[x][y] = 1
visited[x][y] = True
for i in range(2, n*m+1):
    nx, ny = x + dx[d], y + dy[d]
    if in_range(nx, ny) and not visited[nx][ny]:
        x, y = nx, ny
    else:
        d = (d+1)%4
        x, y = x + dx[d], y + dy[d]
    grid[x][y] = i
    visited[x][y] = True
for i in range(n):
    print(*grid[i])