n, m = map(int, input().split())
arr = [(0,0)]
for _ in range(n):
    w, v = map(int, input().split())
    arr.append((w, v))
dp = [
    [0]*(m+1)
    for _ in range(n+1)
]

for i in range(1, n+1):
    for j in range(1, m+1):
        weight = arr[i][0]
        value = arr[i][1]
        if j >= weight:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight]+value)
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n][m])