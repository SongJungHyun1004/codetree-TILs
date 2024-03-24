n, m = map(int, input().split())
clothes = [(0, 0, 0)]
for _ in range(n):
    s, e, v = map(int, input().split())
    clothes.append((s, e, v))
dp = [
    [-1]*(n+1)
    for _ in range(m+1)
]

def in_range(s, e, day):
    return s <= day <= e

for j in range(1, n+1):
    s, e, v = clothes[j]
    if in_range(s, e, 1):
        dp[1][j] = 0

for i in range(2, m+1):
    for j in range(1, n+1):
        s, e, v = clothes[j]
        for k in range(1, n+1):
            _, _, pre_v = clothes[k]
            if dp[i-1][k] == -1 or not in_range(s, e, i):
                continue
            dp[i][j] = max(dp[i][j], dp[i-1][k]+abs(pre_v-v))

print(max(dp[m]))