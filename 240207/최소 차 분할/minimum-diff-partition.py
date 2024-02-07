n = int(input())
arr = [0]+list(map(int, input().split()))
s = sum(arr)
dp = [
    [False]*(s+1)
    for _ in range(n+1)
]
dp[0][0] = True
for i in range(1, n+1):
    for j in range(s+1):
        if j >= arr[i] and dp[i-1][j-arr[i]]:
            dp[i][j] = True
        elif dp[i-1][j]:
            dp[i][j] = True
mn = float('inf')
# 한 쪽 그룹합이 1<= i <= s-1 선택 가능
# 다른 쪽 그룹합은 s-i가 됨
for i in range(1, s):
    if dp[n][i]:
        mn = min(mn, abs(i-(s-i)))
print(mn)