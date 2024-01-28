n = int(input())
dp = [-1]*46
def memoization(i):
    if dp[i] != -1:
        return dp[i]
    if i < 3:
        dp[i] = 1
    else:
        dp[i] = memoization(i-1) + memoization(i-2)
    return dp[i]

print(memoization(n))