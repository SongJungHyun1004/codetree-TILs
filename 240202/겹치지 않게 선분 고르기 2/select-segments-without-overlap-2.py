n = int(input())
lst = [(0, 0)]
for _ in range(n):
    x1, x2 = map(int, input().split())
    lst.append((x1, x2))
dp = [0]+[-1]*n
for i in range(1, n+1):
    for j in range(i):
        if lst[i][0] > lst[j][1]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))