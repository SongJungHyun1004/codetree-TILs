from collections import deque
n = int(input())
grid = [
    list(input())
    for _ in range(n)
]
arr = []
for i in range(n):
    for j in range(n):
        v = grid[i][j]
        if v == 'S':
            start = (i, j)
        elif v == 'E':
            end = (i, j)
        elif v.isdigit():
            arr.append((int(v), (i, j)))
arr = sorted(arr)
dxs = [0,1,0,-1]
dys = [1,0,-1,0]
def in_range(x, y):
    return 0<=x<n and 0<=y<n

def bfs(frm):
    visited = [
        [False]*n
        for _ in range(n)
    ]
    dist = [
        [0]*n
        for _ in range(n)
    ]
    q = deque([frm])
    visited[frm[0]][frm[1]] = True
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not visited[nx][ny]:
                visited[nx][ny] = True
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
    return dist

mn_move = float('inf')
def simulation(coin):
    global mn_move
    move = 0
    dist = bfs(start)
    move += dist[coin[0][1][0]][coin[0][1][1]]
    dist = bfs(coin[0][1])
    move += dist[coin[1][1][0]][coin[1][1][1]]
    dist = bfs(coin[1][1])
    move += dist[coin[2][1][0]][coin[2][1][1]]
    dist = bfs(coin[2][1])
    move += dist[end[0]][end[1]]
    mn_move = min(mn_move, move)

coin = []
selected = [False]*len(arr)
def combi(idx, last):
    if idx == 3:
        simulation(coin)
        return
    for i in range(last, len(arr)):
        if not selected[i]:
            coin.append(arr[i])
            selected[i] = True
            combi(idx+1, i)
            coin.pop()
            selected[i] = False
combi(0, 0)

print(mn_move) if not float('inf') else print(-1)