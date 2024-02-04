n = int(input())
MOD = 10007
nums = [1,2,5]
dp = [1]+[0]*n
for i in range(1, n+1):
    for j in range(3):
        if i >= nums[j]:
            dp[i] = (dp[i] + dp[i-nums[j]])%MOD
print(dp[n])