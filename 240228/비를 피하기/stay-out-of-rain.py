from collections import deque
n, h, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [
    [False]*n
    for _ in range(n)
]
dist = [
    [0]*n
    for _ in range(n)
]
ans = [
    [0]*n
    for _ in range(n)
]
dxs = [0,1,0,-1]
dys = [1,0,-1,0]
def in_range(x, y):
    return 0<=x<n and 0<=y<n

def push(nx, ny, new_dist):
    q.append((nx, ny))
    visited[nx][ny] = True
    dist[nx][ny] = new_dist

def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] != 1:
                push(nx, ny, dist[x][y]+1)
q = deque()
three_pos = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 3:
            three_pos.append((i, j))
for i, j in three_pos:
    push(i, j, 0)

bfs()
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            if not visited[i][j]:
                ans[i][j] = -1
            else:
                ans[i][j] = dist[i][j]
for i in range(n):
    print(*ans[i])