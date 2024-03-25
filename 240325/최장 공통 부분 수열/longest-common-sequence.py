import sys
input = sys.stdin.readline
a = list(input().rstrip())
b = list(input())
n = len(a)
m = len(b)
a = [""]+a
b = [""]+b
dp = [
    [0]*(m+1)
    for _ in range(n+1)
]

dp[1][1] = 1 if a[1] == b[1] else 0
for i in range(2, n+1):
    if a[i] == b[1]:
        dp[i][1] = 1
    else:
        dp[i][1] = dp[i-1][1]
for j in range(2, m+1):
    if a[1] == b[j]:
        dp[1][j] = 1
    else:
        dp[1][j] = dp[1][j-1]

for i in range(2, n+1):
    for j in range(2, m+1):
        if a[i] == b[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[n][m])