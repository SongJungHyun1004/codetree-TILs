import sys
INT_MAX = sys.maxsize
n, a, b, c, d = map(int, input().split())
dp = [0]+[INT_MAX]*n
for i in range(1, n+1):
    if i >= a:
        dp[i] = min(dp[i], dp[i-a]+b)
    if i >= c:
        dp[i] = min(dp[i], dp[i-c]+d)
print(dp[n])