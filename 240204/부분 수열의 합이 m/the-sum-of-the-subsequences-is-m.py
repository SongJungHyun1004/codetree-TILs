import sys
n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))
INT_MAX = sys.maxsize
dp = [0] + [INT_MAX]*m
for i in range(1, n+1):
    for j in range(m, -1, -1):
        if j >= a[i]:
            if dp[j-a[i]] == INT_MAX:
                continue
            dp[j] = min(dp[j], dp[j-a[i]]+1)
print(-1) if dp[m] == INT_MAX else print(dp[m])