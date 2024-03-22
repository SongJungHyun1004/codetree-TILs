from collections import deque
n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

dxs = [0,1,0,-1]
dys = [1,0,-1,0]
def in_range(x, y):
    return 0<=x<n and 0<=y<n

mx = 1
for i in range(n):
    for j in range(n):
        dp = [
            [0]*n
            for _ in range(n)
        ]
        dp[i][j] = 1
        x, y = i, j
        q = deque([(x, y)])
        while q:
            x, y = q.popleft()
            mx = max(mx, dp[x][y])
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if in_range(nx, ny) and grid[nx][ny] > grid[x][y]:
                    q.append((nx, ny))
                    dp[nx][ny] = max(dp[nx][ny], dp[x][y]+1)
print(mx)