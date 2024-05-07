MOD = 10**9+7
n = int(input())
dp = [0]*(n+1)
dp[1] = 9
if n == 1:
    print(dp[1])
    exit(0)
dp[2] = 17
for i in range(3, n+1):
    if i%2 == 1:
        dp[i] = dp[i-1]
    else:
        dp[i] = dp[i-2]*2%MOD
print(dp[n])