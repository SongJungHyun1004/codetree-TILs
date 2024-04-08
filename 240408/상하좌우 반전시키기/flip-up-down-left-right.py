n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
dxs = [0,1,0,-1]
dys = [1,0,-1,0]
def in_range(x, y):
    return 0<=x<n and 0<=y<n

def click(x, y):
    grid[x][y] = 1-grid[x][y]
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny):
            grid[nx][ny] = 1-grid[nx][ny]

cnt = 0
for i in range(1, n):
    for j in range(n):
        if grid[i-1][j] == 0:
            click(i, j)
            cnt += 1

for j in range(n):
    if grid[n-1][j] == 0:
        print(-1)
        exit(0)
print(cnt)