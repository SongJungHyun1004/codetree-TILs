import sys
INT_MAX = sys.maxsize
N_MAX = 1000000
n = int(input())
dp = [INT_MAX]*(N_MAX+1)
dp[0] = 1
dp[1] = 0
for i in range(2, N_MAX+1):
    if i%2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i%3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    if i != N_MAX:
        dp[i] = min(dp[i], min(dp[i-1], dp[i+1])+1)
print(dp[n])