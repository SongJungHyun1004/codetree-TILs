import sys
INT_MIN = -sys.maxsize
n, m = map(int, input().split())
coin = list(map(int, input().split()))
dp = [0]+[INT_MIN]*m
for i in range(1, m+1):
    for j in range(n):
        if i >= coin[j]:
            dp[i] = max(dp[i], dp[i-coin[j]]+1)
print(-1) if dp[m] == INT_MIN else print(dp[m])