n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
dp = [
    [0]*m
    for _ in range(n)
]
dp[0][0] = 1

for i in range(1, n):
    for j in range(1, m):
        for k in range(i):
            for l in range(j):
                if dp[k][l] == 0:
                    continue
                if grid[i][j] > grid[k][l]:
                    dp[i][j] = max(dp[i][j], dp[k][l]+1)
mx = float('-inf')
for i in range(n):
    for j in range(m):
        mx = max(mx, dp[i][j])
print(mx)