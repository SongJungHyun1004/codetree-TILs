n, m, r, c = map(int, input().split())
r-=1;c-=1
grid = [[0]*n for _ in range(n)]
grid[r][c] = 1
dxs = [0,1,0,-1]
dys = [1,0,-1,0]

def in_range(x, y):
    return 0<=x<n and 0<=y<n

def bomb(box, dist):
    tmp = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if box[i][j]:
                for dx, dy in zip(dxs, dys):
                    nx, ny = i + dx*dist, j + dy*dist
                    if in_range(nx, ny) and not box[nx][ny]:
                        tmp[nx][ny] = 1
    for i in range(n):
        for j in range(n):
            if tmp[i][j]:
                box[i][j] = 1
    return box

for t in range(1, m+1):
    grid = bomb(grid, 2**(t-1))

cnt = 0
for i in range(n):
    cnt += sum(grid[i])
print(cnt)