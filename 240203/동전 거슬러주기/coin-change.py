import sys
INT_MAX = sys.maxsize
n, m = map(int, input().split())
coin = [0]+list(map(int, input().split()))
dp = [0]+[INT_MAX]*m

for i in range(1, m+1):
    for j in range(1, n+1):
        if i >= coin[j]:
            if dp[i-coin[j]] == INT_MAX:
                continue
            dp[i] = min(dp[i], dp[i-coin[j]]+1)

print(-1) if dp[m] == INT_MAX else print(dp[m])