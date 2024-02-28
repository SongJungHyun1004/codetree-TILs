from collections import deque
n, h, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
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

def bfs(sx, sy):
    visited = [
        [False]*n
        for _ in range(n)
    ]
    dist = [
        [0]*n
        for _ in range(n)
    ]
    q = deque([(sx, sy)])
    visited[sx][sy] = True
    mn_dist = -1
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] != 1:
                visited[nx][ny] = True
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
                if grid[nx][ny] == 3:
                    mn_dist = dist[nx][ny]
                    return mn_dist
    return mn_dist
    
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            ans[i][j] = bfs(i, j)
for i in range(n):
    print(*ans[i])