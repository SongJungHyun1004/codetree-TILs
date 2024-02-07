n, m = map(int, input().split())
arr = []
for _ in range(n):
    w, v = map(int, input().split())
    arr.append((w, v))
dp = [-1]*(m+1)
dp[0] = 0
for i in range(1, m+1):
    for j in range(n):
        weight = arr[j][0]
        value = arr[j][1]
        if dp[i-weight] == -1:
            continue
        if i >= weight:
            dp[i] = max(dp[i], dp[i-1], dp[i-weight]+value)
print(dp[m])