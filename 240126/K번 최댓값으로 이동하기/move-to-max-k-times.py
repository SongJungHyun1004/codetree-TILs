from collections import deque
n, k = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
r, c = map(int, input().split())
r-=1; c-=1

dxs = [1,0,0,-1]
dys = [0,1,-1,0]

def in_range(x, y):
    return 0<=x<n and 0<=y<n

def bfs(sx, sy, v):
    global mx, next_x, next_y
    q = deque([(sx, sy)])
    visited[sx][sy] = True
    next_x, next_y = sx, sy
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] < v:
                visited[nx][ny] = True
                q.append((nx, ny))
                if mx <= grid[nx][ny]:
                    mx = grid[nx][ny]
                    next_x, next_y = nx, ny
pre_x, pre_y = r, c
for _ in range(k):
    mx = 0
    visited = [
        [False]*n
        for _ in range(n)
    ]
    bfs(pre_x, pre_y, grid[pre_x][pre_y])
    if next_x == pre_x and next_y == pre_y:
        break
    pre_x, pre_y = next_x, next_y
print(next_x+1, next_y+1)