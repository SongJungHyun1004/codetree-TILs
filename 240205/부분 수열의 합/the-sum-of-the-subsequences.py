import sys
INT_MAX = sys.maxsize
n, m = map(int, input().split())
a = list(map(int, input().split()))
dp = [0]+[INT_MAX]*m

for i in range(n):
    for j in range(m, -1, -1):
        if j >= a[i]:
            if dp[j-a[i]] == INT_MAX:
                continue
            dp[j] = min(dp[j], dp[j-a[i]]+1)
print('No') if dp[m] == INT_MAX else print('Yes')