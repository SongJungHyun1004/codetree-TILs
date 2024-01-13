n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
dxs = [0,-1,0,1]
dys = [1,0,-1,0]
def in_range(x, y):
    return 0<=x<n and 0<=y<n

def explode(col):
    x, y = -1, -1
    for i in range(n):
        if grid[i][col]:
            x, y = i, col
            break
    if x != -1:
        v = grid[x][y]
        grid[x][y] = 0
        for i in range(1, v):
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx * i, y + dy * i
                if in_range(nx, ny):
                    grid[nx][ny] = 0

def drop():
    for j in range(n):
        tmp = [0]*n
        k = 0
        for i in range(n-1, -1, -1):
            if grid[i][j]:
                tmp[k] = grid[i][j]
                k += 1
        for i, v in enumerate(tmp[::-1]):
            grid[i][j] = v

for _ in range(m):
    col = int(input())-1
    explode(col)
    drop()
    
for i in range(n):
    print(*grid[i])