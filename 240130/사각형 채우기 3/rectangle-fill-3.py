n = int(input())
MOD = 1000000007
dp = [0]*1001
dp[0] = 1
dp[1] = 2
dp[2] = 7
for i in range(3, n+1):
    s = 0
    for j in range(3, i+1):
        s += dp[i-j]*2
    dp[i] = (dp[i-1]*2+dp[i-2]*3+s)%MOD
print(dp[n])