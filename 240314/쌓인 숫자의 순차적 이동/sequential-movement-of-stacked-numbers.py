import sys
input = sys.stdin.readline
n, m = map(int, input().split())
grid = [
    []*n
    for _ in range(n)
]
for i in range(n):
    lst = list(map(int, input().split()))
    for j in range(n):
        grid[i].append([lst[j]])
m_lst = list(map(int, input().split()))

dxs = [0,1,0,-1,1,1,-1,-1]
dys = [1,0,-1,0,1,-1,1,-1]

def in_range(x, y):
    return 0<=x<n and 0<=y<n

def find(num):
    for i in range(n):
        for j in range(n):
            if num in grid[i][j]:
                return i, j

for num in m_lst:
    x, y = find(num)
    mx = -1
    mx_nx, mx_ny = -1, -1
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and grid[nx][ny]:
            if mx < max(grid[nx][ny]):
                mx = max(grid[nx][ny])
                mx_nx = nx; mx_ny = ny
    if mx != -1:
        idx = grid[x][y].index(num)
        tmp = grid[x][y][idx:]
        grid[x][y] = grid[x][y][:idx]
        grid[mx_nx][mx_ny].extend(tmp)
    
for i in range(n):
    for j in range(n):
        if grid[i][j]:
            print(*grid[i][j][::-1])
        else:
            print('None')