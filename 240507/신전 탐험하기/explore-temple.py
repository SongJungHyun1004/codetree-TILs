n = int(input())
grid = [[0, 0, 0]]
for _ in range(n):
    grid.append(list(map(int, input().split())))

dp = [[0, 0, 0] for _ in range(n+1)]
dp[1] = grid[1]

for i in range(2, n+1):
    for j in range(3):
        dp[i][j] = max(dp[i-1][(j+1)%3], dp[i-1][(j+2)%3])+grid[i][j]

print(max(dp[n]))