from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
time = [[0]*n for _ in range(n)]

dxs = [0,1,0,-1]
dys = [1,0,-1,0]

def in_range(x, y):
    return 0<=x<n and 0<=y<n

def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] == 1:
                visited[nx][ny] = True
                time[nx][ny] = time[x][y]+1
                q.append((nx, ny))

q = deque()
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            visited[i][j] = True
            q.append((i, j))
bfs()
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            if grid[i][j]:
                time[i][j] = -2
            else:
                time[i][j] = -1
for i in range(n):
    print(*time[i])