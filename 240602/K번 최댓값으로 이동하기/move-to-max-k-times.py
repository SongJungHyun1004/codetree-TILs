from collections import deque

n, k = map(int, input().split())
grid = [[0]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    grid[i][1:] = list(map(int, input().split()))
r, c = map(int, input().split())

dxs = [0,1,0,-1]
dys = [1,0,-1,0]

def in_range(x, y):
    return 0<x<=n and 0<y<=n

def bfs(x, y):
    visited = [[False]*(n+1) for _ in range(n+1)]
    q = deque([(x, y, grid[x][y])])
    visited[x][y] = True
    mx_val = 0
    mx_x, mx_y = -1, -1
    while q:
        x, y, val = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] < val:
                visited[nx][ny] = True
                if mx_val < grid[nx][ny]:
                    mx_val = grid[nx][ny]
                    mx_x, mx_y = nx, ny
                elif mx_val == grid[nx][ny]:
                    if nx < mx_x:
                        mx_x, mx_y = nx, ny
                    elif nx == mx_x and ny < mx_y:
                        mx_y = ny
                q.append((nx, ny, val))

    return mx_x, mx_y

for _ in range(k):
    nr, nc = bfs(r, c)
    if (nr, nc) == (-1, -1):
        print(r, c)
        exit(0)
    r, c = nr, nc
print(r, c)