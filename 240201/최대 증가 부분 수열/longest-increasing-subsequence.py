n = int(input())
a = list(map(int, input().split()))
dp = [0]*n
dp[0] = 1
for i in range(1, n):
    for j in range(i):
        if dp[j] == 0:
            continue
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))