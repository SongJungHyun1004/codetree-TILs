# 각 층의 보물의 개수 정보를 입력받습니다.
n = int(input())
a = [[0] * 4 for _ in range(1005)]
for i in range(1, n + 1):
    a[i][1], a[i][2], a[i][3] = map(int, input().split())

# 동적 프로그래밍을 사용하여 최대 점수를 계산합니다.
dp = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(1005)]
for j in range(1, 4):
    dp[1][j][j] = a[1][j]

for i in range(1, n):
    for j in range(1, 4):
        for k in range(1, 4):
            for l in range(1, 4):
                if k == l:
                    continue
                dp[i + 1][j][l] = max(dp[i + 1][j][l], dp[i][j][k] + a[i + 1][l])

# 최종적으로 가능한 최대 점수를 계산합니다.
ans = 0
for j in range(1, 4):
    for k in range(1, 4):
        if j == k:
            continue
        ans = max(ans, dp[n][j][k])

# 계산된 최대 점수를 출력합니다.
print(ans)