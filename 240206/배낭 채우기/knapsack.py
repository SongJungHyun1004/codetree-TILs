n, m = map(int, input().split())
arr = []
for _ in range(n):
    w, v = map(int, input().split())
    arr.append((w, v))
dp = [
    [0]*(m+1)
    for _ in range(n)
]

for i in range(n):
    for j in range(1, m+1):
        weight = arr[i][0]
        value = arr[i][1]
        if j >= weight:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight]+value)
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n-1][m])