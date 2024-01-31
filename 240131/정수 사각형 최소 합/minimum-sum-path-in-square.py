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
    dp[0][n-1] = matrix[0][n-1]
    for j in range(n-2, -1, -1):
        dp[0][j] = dp[0][j+1] + matrix[0][j]
    for i in range(1, n):
        dp[i][n-1] = dp[i-1][n-1] + matrix[i][n-1]

initialize()

for i in range(1, n):
    for j in range(n-2, -1, -1):
        dp[i][j] = min(dp[i-1][j], dp[i][j+1])+matrix[i][j]
print(dp[n-1][0])