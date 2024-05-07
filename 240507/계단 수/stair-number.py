MOD = 10**9+7
n = int(input())
dp = [
    [0]*10
    for _ in range(n+1)
]
for i in range(1, 10):
    dp[1][i] = 1

for i in range(1, n+1):
    for j in range(10):
        if j < 9:
            dp[i][j] = (dp[i-1][j+1]+dp[i][j]) % MOD
        if j > 0:
            dp[i][j] = (dp[i-1][j-1]+dp[i][j]) % MOD

ans = 0
for j in range(10):
    ans = (ans + dp[n][j]) % MOD
print(ans)