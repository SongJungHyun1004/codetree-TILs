n, m = map(int, input().split())
vilage = [
    list(map(int, input().split()))
    for _ in range(n)
]
mx_k = 0
mx_safe = 0
ans = 1
for i in range(n):
    for j in range(m):
        mx_k = max(mx_k, vilage[i][j])
dxs = [0,1,0,-1]
dys = [1,0,-1,0]
def in_range(x, y):
    return 0<=x<n and 0<=y<m

def dfs(x, y, k):
    visited[x][y] = True
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and not visited[nx][ny] and k < vilage[nx][ny]:
            dfs(nx, ny, k)

for k in range(1, mx_k+1):
    visited = [
        [False]*m
        for _ in range(n)
    ]
    safeArea = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and k < vilage[i][j]:
                dfs(i, j, k)
                safeArea += 1
    if safeArea > mx_safe:
        mx_safe = safeArea
        ans = k
print(ans, mx_safe)