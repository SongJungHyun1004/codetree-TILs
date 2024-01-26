from collections import deque
n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [
    [False]*m
    for _ in range(n)
]
dxs = [0,1,0,-1]
dys = [1,0,-1,0]

def in_range(x, y):
    return 0<=x<n and 0<=y<m

def bfs(start):
    q = deque([start])
    while q:
        x, y = q.popleft()
        visited[x][y] = True
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny]:
                q.append((nx, ny))

bfs((0, 0))
print(1) if visited[n-1][m-1] else print(0)