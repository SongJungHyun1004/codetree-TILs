n = int(input())
income = [0]+list(map(int, input().split()))
m = len(income)
dp = [-1]*(n+1)
dp[0] = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if dp[i-j] == -1:
            continue
        if i >= j:
            dp[i] = max(dp[i], dp[i-j]+income[j])
print(dp[n])