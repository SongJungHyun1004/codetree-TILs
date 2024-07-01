n, m = map(int, input().split())
grid = [[0]*m for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def in_range(x, y):
    return 0<=x<n and 0<=y<m

x, y, d = 0, 0, 0
num = 1
for _ in range(n*m):
    grid[x][y] = num
    nx, ny = x + dx[d], y + dy[d]
    if not in_range(nx, ny) or grid[nx][ny]:
        d = (d+1)%4
        nx, ny = x + dx[d], y + dy[d]
    x, y = nx, ny
    num += 1
for i in range(n):
    print(*grid[i])