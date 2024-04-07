import copy
from collections import deque
m, n = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(m)
]
visited = [[False]*n for _ in range(m)]
isColor = [
    list(map(int, input().split()))
    for _ in range(m)
]
color = deque([])
for i in range(m):
    for j in range(n):
        if isColor[i][j]:
            color.append((i, j))

dxs = [0,1,0,-1]
dys = [1,0,-1,0]
def in_range(x, y):
    return 0<=x<m and 0<=y<n

def bfs(sx, sy, mid):
    q = deque([(sx, sy)])
    visited[sx][sy] = True
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not visited[nx][ny] and abs(grid[nx][ny]-grid[x][y]) <= mid:
                visited[nx][ny] = True
                q.append((nx, ny))


def isPossible(mid):
    for i in range(m):
        for j in range(n):
            visited[i][j] = False
    tmp = copy.deepcopy(color)
    while len(tmp) > 1:
        x, y = tmp.popleft()
        bfs(x, y, mid)
        for i, j in color:
            if not visited[i][j]:
                return False
    return True

def binary_search():
    left = 0
    right = 10**9
    d = right
    while left <= right:
        mid = (left+right)//2
        if isPossible(mid):
            right = mid - 1
            d = min(d, mid)
        else:
            left = mid + 1
    return d

print(binary_search())