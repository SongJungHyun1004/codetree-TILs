import sys
INT_MIN = -sys.maxsize
n = int(input())
mx = 3 # 1칸씩 오르는 최대 횟수
coin = [0] + list(map(int, input().split()))
dp = [
    [INT_MIN]*(n+1)
    for _ in range(mx+1)
]

for i in range(mx+1):
    dp[i][0] = 0
    dp[i][1] = dp[i-1][0] + coin[1]
for j in range(2, n+1, 2):
    dp[0][j] = dp[0][j-2] + coin[j]

for i in range(1, mx+1):
    for j in range(2, n+1):
        if dp[i-1][j-1] == INT_MIN or dp[i][j-2] == INT_MIN :
            continue
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i][j-2]) + coin[j]
mx_coin = INT_MIN
for i in range(mx+1):
    mx_coin = max(mx_coin, dp[i][n])
print(mx_coin)