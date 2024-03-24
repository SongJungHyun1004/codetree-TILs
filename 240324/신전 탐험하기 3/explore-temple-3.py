import sys
input = sys.stdin.readline

n, m = map(int, input().split())
temple = [[0]*m]
for _ in range(n):
    room = list(map(int, input().split()))
    temple.append(room)
dp = [
    [0]*m
    for _ in range(n+1)
]

for j in range(m):
    dp[1][j] = temple[1][j]

for i in range(2, n+1):
    for j in range(m):
        for k in range(m):
            if j != k:
                dp[i][j] = max(dp[i][j], dp[i-1][k]+temple[i][j])

print(max(dp[n]))