import sys
INT_MIN = -sys.maxsize
INT_MAX = sys.maxsize
n = int(input())
a = [INT_MAX] + list(map(int, input().split()))
dp = [0]+[INT_MIN]*n
for i in range(1, n+1):
    for j in range(i):
        if a[i] < a[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))