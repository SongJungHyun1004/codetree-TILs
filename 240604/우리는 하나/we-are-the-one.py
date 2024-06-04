from collections import deque

n, k, u, d = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [[False]*n for _ in range(n)]
dxs = [0,1,0,-1]
dys = [1,0,-1,0]
def in_range(x, y):
    return 0<=x<n and 0<=y<n

def bfs(x, y):
    global sizes
    q = deque([(x, y)])
    visited[x][y] = True
    cnt = 0
    while q:
        x, y = q.popleft()
        cnt += 1
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not visited[nx][ny] and u <= abs(grid[x][y]-grid[nx][ny]) <= d:
                visited[nx][ny] = True
                q.append((nx, ny))
    sizes.append(cnt)

sizes = []
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
sizes.sort(reverse=True)
print(sum(sizes[:k]))