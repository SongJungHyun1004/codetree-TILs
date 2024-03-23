n = int(input())
abilities = [tuple(map(int, input().split())) for _ in range(n)]

# dp[i][j][k] = i번째 학생까지 고려했을 때, 축구팀에 j명, 야구팀에 k명이 할당된 상태에서의 능력치 합의 최대값
dp = [[[0 for _ in range(10)] for _ in range(12)] for _ in range(n+1)]

for i in range(1, n+1):
    s, b = abilities[i-1]
    for j in range(12):
        for k in range(10):
            # i번째 학생을 축구팀에 할당하는 경우
            if j > 0:
                dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-1][k] + s)
            # i번째 학생을 야구팀에 할당하는 경우
            if k > 0:
                dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k-1] + b)
            # i번째 학생을 할당하지 않는 경우
            dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k])

# 축구팀 11명, 야구팀 9명이 할당된 상태에서의 최대 능력치 합
print(dp[n][11][9])