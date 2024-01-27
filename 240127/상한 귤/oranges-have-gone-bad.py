from collections import deque
n, k = map(int, input().split())
box = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [
    [False]*n
    for _ in range(n)
]
time = [
    [-1]*n
    for _ in range(n)
]
dxs = [0,1,0,-1]
dys = [1,0,-1,0]
def in_range(x, y):
    return 0<=x<n and 0<=y<n

def bfs(start_lst):
    q = deque(start_lst)
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not visited[nx][ny] and box[nx][ny]:
                visited[nx][ny] = True
                time[nx][ny] = time[x][y] + 1
                q.append((nx, ny))
start_lst = []
for i in range(n):
    for j in range(n):
        if box[i][j] == 2:
            start_lst.append((i, j))
            visited[i][j] = True
            time[i][j] = 0
bfs(start_lst)
for i in range(n):
    for j in range(n):
        if not visited[i][j] and box[i][j]:
            time[i][j] = -2
for i in range(n):
    print(*time[i])