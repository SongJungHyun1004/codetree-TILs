import sys
INT_MAX = sys.maxsize
n = int(input())
coin = [2, 5]
dp = [0]+[INT_MAX]*n
for i in range(2, n+1):
    for j in range(2):
        if i >= coin[j]:
            dp[i] = min(dp[i], dp[i-coin[j]]+1)
if dp[n] == INT_MAX:
    print(-1)
else:
    print(dp[n])