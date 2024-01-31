n = int(input())
matrix = [
    list(map(int, input().split()))
    for _ in range(n)
]
dp = [
    [0]*n
    for _ in range(n)
]

def initialize():
    dp[0][0] = matrix[0][0]
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], matrix[i][0])
    for j in range(1, n):
        dp[0][j] = max(dp[0][j-1], matrix[0][j])

initialize()
for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(min(dp[i-1][j], dp[i][j-1]), matrix[i][j])
print(dp[n-1][n-1])