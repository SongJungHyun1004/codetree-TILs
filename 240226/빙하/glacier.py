from collections import deque
n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

dxs = [0,1,0,-1]
dys = [1,0,-1,0]
def in_range(x, y):
    return 0<=x<n and 0<=y<m

def bfs(x, y):
    visited = [
        [False]*m
        for _ in range(n)
    ]
    q = deque([(x, y)])
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not visited[nx][ny]:
                if grid[nx][ny]:
                    grid[nx][ny] = -1
                else:
                    visited[nx][ny] = True
                    q.append((nx, ny))
def melt():
    size = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == -1:
                grid[i][j] = 0
                size += 1
    return size
def is_done():
    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                return False
    return True
t = 0
while True:
    if is_done():
        break
    bfs(0, 0)
    size = melt()
    t += 1

print(t, size)