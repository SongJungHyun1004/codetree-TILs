n = int(input())
dp = [[[0 for _ in range(n+1)] for _ in range(n+1)] for _ in range(2*n+1)]
for i in range(1, 2*n+1):
    red, blue = map(int, input().split())
    for j in range(n+1):
        for k in range(n+1):
            if j > 0:
                dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-1][k] + red)
            if k > 0:
                dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k-1] + blue)
            dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k])
print(dp[2*n][n][n])