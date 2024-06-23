n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
def in_range(x, y):
    return 0<=x<n and 0<=y<n

def bomb(box, x, y):
    dxs = [0,1,0,-1]
    dys = [1,0,-1,0]
    size = box[x][y]
    for i in range(size):
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx*i, y + dy*i
            if in_range(nx, ny):
                box[nx][ny] = 0
    return box
    
def drop(box):
    tmp = [[0]*n for _ in range(n)]
    for j in range(n):
        k = n-1
        for i in range(n-1, -1, -1):
            if box[i][j]:
                tmp[k][j] = box[i][j]
                k -= 1
    return tmp

for _ in range(m):
    y = int(input())-1
    x = -1
    for i in range(n):
        if grid[i][y]:
            x = i
            break
    if x == -1:
        continue
    box = bomb(grid, x, y)
    grid = drop(box)

for i in range(n):
    print(*grid[i])