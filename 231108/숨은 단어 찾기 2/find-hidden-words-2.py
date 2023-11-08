dxs = [0,1,1,1,0,-1,-1,-1]
dys = [1,1,0,-1,-1,-1,0,1]
def in_range(x, y):
    return 0<=x<n and 0<=y<m

n, m = map(int, input().split())
grid = [
    list(input())
    for _ in range(n)
]
cnt = 0
for x in range(n):
    for y in range(m):
        if grid[x][y] == 'L':
            for dx, dy in zip(dxs, dys):
                nx, ny = x+dx, y+dy
                nnx, nny = nx+dx, ny+dy
                if in_range(nx, ny) and in_range(nnx, nny) and grid[nx][ny] == 'E' and grid[nnx][nny] == 'E':
                    cnt += 1
print(cnt)