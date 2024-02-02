n = int(input())
lst = [(0,0,0)]
for _ in range(n):
    s, e, p = map(int, input().split())
    lst.append((s,e,p))
dp = [0]*(n+1)

for i in range(1, n+1):
    for j in range(i):
        if lst[i][0] > lst[j][1]:
            dp[i] = max(dp[i], dp[j]+lst[i][2])
print(max(dp))